"use strict";
const $ = selector => document.querySelector(selector);
const token = $('meta[name="fold-token"]').content;
let active = null;
let subjects = [];
let editing = null;
let busy = false;
let noticeTimer;
const escape = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const dateLabel = value => value ? new Intl.DateTimeFormat("it-IT", {dateStyle:"medium"}).format(new Date(value.length === 10 ? value + "T12:00:00" : value)) : "—";
const paymentLabels = {paid:"Pagamento dichiarato", unpaid:"Dichiarata da pagare", unknown:"Pagamento non verificato"};
function display(value) {
  if (value && typeof value === "object" && value.currency) return new Intl.NumberFormat("it-IT", {style:"currency",currency:value.currency}).format(Number(value.amount));
  return value ?? "";
}
function inputValue(value) { return value && typeof value === "object" ? value.amount.replace(".", ",") : String(value ?? ""); }
function notify(text, error=false) {
  clearTimeout(noticeTimer); $("#notice").textContent = text; $("#notice").classList.toggle("error", error); $("#notice").hidden = false;
  noticeTimer = setTimeout(() => $("#notice").hidden = true, error ? 12000 : 6000);
}
async function api(path, options={}) {
  const response = await fetch(path, {...options, headers:{"X-Fold-Token":token,...options.headers}});
  const payload = await response.json();
  if (!response.ok) throw new Error(payload.error || "Operazione non completata.");
  return payload;
}
async function refreshList() {
  subjects = (await api("/api/subjects")).subjects;
  $("#count").textContent = subjects.length;
  $("#documents").innerHTML = subjects.length ? subjects.map(subject => `<button class="document ${active?.id===subject.id?"active":""}" data-subject="${subject.id}" aria-current="${active?.id===subject.id?"page":"false"}"><strong>${escape(subject.title)}</strong><small>Acquisita il ${escape(dateLabel(subject.created_at))}</small></button>`).join("") : '<p class="sidebar-empty">Le bollette che aggiungi appariranno qui.</p>';
}
async function openSubject(id) {
  if (busy) return;
  try { active = await api(`/api/subjects/${id}`); render(); await refreshList(); }
  catch (error) { notify(error.message, true); }
}
function render() {
  const fields = Object.entries(active.field_definitions).map(([predicate, definition]) => {
    const current = active.current[predicate];
    const candidates = active.assertions.filter(a => a.predicate===predicate && a.origin==="document");
    const ambiguous = !current && candidates.length;
    const state = current ? current.origin==="document" ? "Letto dal PDF" : current.origin==="human_confirmation" ? "Confermato da te" : "Corretto da te" : ambiguous ? "Più valori possibili" : "Non individuato";
    const value = current ? definition.kind==="date" ? dateLabel(current.value) : display(current.value) : ambiguous ? "Da chiarire" : "Dato non disponibile";
    let evidence = "Non è stata trovata una corrispondenza esplicita. Il dato potrebbe essere presente nel PDF.";
    if (ambiguous) evidence = "Sono presenti alternative: " + [...new Set(candidates.map(a=>display(a.value)))].join(" · ");
    if (current?.origin==="document") evidence = `<span>Pagina ${current.page} · testo estratto</span><blockquote>“${escape(current.excerpt)}”</blockquote>`;
    else if (current) evidence = `<span>Il valore corrente proviene dal tuo intervento</span><blockquote>${escape(current.received?.note)}</blockquote>`;
    else evidence = escape(evidence);
    return `<article class="field"><div class="field-top"><span class="field-label">${escape(definition.label)}</span><span class="field-state ${current?"":"missing"}">${state}</span></div><div class="field-value ${current?"":"empty"}">${escape(value)}</div><div class="evidence">${evidence}</div><div class="field-footer"><button class="text-button" data-edit="${predicate}">${current?"Verifica o correggi":"Chiarisci il dato"}</button>${current?.source_id?`<a href="/api/sources/${current.source_id}" target="_blank" rel="noopener">Scarica la fonte ↗</a>`:'<span>Storico conservato</span>'}</div></article>`;
  }).join("");
  const history = [...active.assertions].reverse().map(a => {
    const name = active.field_definitions[a.predicate]?.label || "Pagamento";
    const label = a.predicate === "payment_status" ? paymentLabels[a.value] : display(a.value);
    const detail = a.origin === "document" ? `Lettura dal PDF, pagina ${a.page}. ${a.excerpt}` : `${a.origin === "human_confirmation"?"Conferma":"Intervento"} di ${a.actor}: ${a.received?.note || ""}`;
    return `<div class="event"><strong>${escape(name)} · ${escape(label)}${a.selected?" · corrente":""}</strong><p>${escape(detail)}</p><time>${escape(dateLabel(a.created_at))}</time></div>`;
  }).join("");
  const source = active.sources[0];
  const title = active.current.document_number?.value || active.title;
  const payment = active.current.payment_status;
  $("#main").innerHTML = `<p class="breadcrumb">Il tuo spazio / Bollette elettriche</p><div class="page-heading"><div><h1>${escape(title)}</h1><p class="muted">${escape(source.filename)} · aggiunta il ${escape(dateLabel(source.created_at))}</p></div><span class="tag">${source.is_demo?"ESEMPIO FITTIZIO":"DOCUMENTO LOCALE"}</span></div>${!active.text_available?'<div class="warning">Originale conservato. Non è stato trovato testo leggibile: potrebbe essere una scansione. Questa versione non esegue OCR; puoi consultare l’originale e aggiungere una correzione esplicita.</div>':""}<section class="situation ${active.situation.tone}"><div class="eyebrow">LA SITUAZIONE · ${escape(dateLabel(active.situation.reference_date))}</div><h2>${escape(active.situation.label)}</h2><p>${escape(active.situation.reason)}</p></section><div class="section-heading"><h2>I dati e le loro evidenze</h2><p>Le letture automatiche rimangono ispezionabili.</p></div><section class="fields">${fields}</section><section class="panel payment-grid"><div class="payment-copy"><h2>Il pagamento è un’informazione distinta</h2><p class="muted">${payment?escape(paymentLabels[payment.value]):"Nessuna dichiarazione di pagamento disponibile."} Una modalità di pagamento stampata sul PDF non ne attesta l’esecuzione.</p>${payment?`<p class="muted">La tua dichiarazione: “${escape(payment.received?.note)}”</p>`:""}</div><div class="payment-controls"><button class="button outline small" data-payment="paid">Dichiara il pagamento</button><button class="button quiet small" data-payment="unknown">Chiarisci lo stato</button></div></section><details class="history"><summary>Cronologia e letture originali · ${active.assertions.length} registrazioni</summary><div class="timeline">${history||'<p class="muted">Nessun dato interpretato. L’originale rimane disponibile.</p>'}</div></details><div class="source-info"><a href="/api/sources/${source.id}" target="_blank" rel="noopener">Scarica il PDF originale ↗</a> · ${source.receptions} acquisizione/i<br>Impronta dell’originale: <code>${source.sha256}</code></div>`;
}
async function importDocument(file=null) {
  if (busy) return;
  if (file && file.size>10*1024*1024) return notify("Il limite è 10 MB per documento.",true);
  busy=true; $("#upload").disabled=true; const demo=$("#demo"); if(demo) demo.disabled=true;
  notify("Conservo e leggo il documento…");
  try {
    const result = file ? await api("/api/import", {method:"POST",headers:{"Content-Type":"application/pdf","X-Filename":encodeURIComponent(file.name)},body:file}) : await api("/api/demo",{method:"POST"});
    active=result.subject; render(); await refreshList();
    notify(result.duplicate ? "Documento già presente: ho registrato il nuovo ingresso senza duplicarlo." : "Originale conservato. Puoi consultare i dati e le evidenze.");
  } catch(error) { notify(error.message,true); }
  finally { busy=false; $("#upload").disabled=false; const demo=$("#demo"); if(demo) demo.disabled=false; $("#file").value=""; }
}
function showEditor(predicate, payment=null) {
  editing={predicate, revision:active.revision, subject:active.id, payment};
  const isPayment=predicate==="payment_status";
  $("#editor-title").textContent=isPayment?"La tua dichiarazione sul pagamento":active.field_definitions[predicate].label;
  $("#editor-description").textContent=isPayment?"Indica solo ciò che sai su questa bolletta. La dichiarazione rimane attribuita a te.":"Confronta il valore con l’originale. La correzione non modifica ciò che il documento riporta.";
  const candidates=active.assertions.filter(a=>a.predicate===predicate && a.origin==="document");
  const options=isPayment?'<option value="paid">Dichiaro di aver pagato</option><option value="unpaid">Dichiaro di dover ancora pagare</option><option value="unknown">Il pagamento non è verificato</option>':`<option value="">Inserisci una correzione</option>${candidates.map(a=>`<option value="${a.id}">${escape(display(a.value))} · pagina ${a.page}</option>`).join("")}`;
  $("#alternatives-title").textContent=isPayment?"Che cosa dichiari":"Valori letti nel documento";
  $("#alternatives").innerHTML=options; $("#alternatives-label").hidden=!isPayment&&!candidates.length;
  $("#edit-value").parentElement.hidden=isPayment; $("#edit-value").required=!isPayment;
  $("#edit-value").type=!isPayment && active.field_definitions[predicate].kind==="date"?"date":"text";
  $("#edit-value").value=inputValue(active.current[predicate]?.value);
  if(isPayment) $("#alternatives").value=payment;
  else if(active.current[predicate]?.origin==="document") $("#alternatives").value=active.current[predicate].id;
  $("#edit-note").value=""; $("#edit-error").textContent=""; $("#editor").showModal();
}
$("#alternatives").addEventListener("change",()=>{
  if(editing.predicate!=="payment_status") {const candidate=active.assertions.find(a=>a.id===$("#alternatives").value);if(candidate)$("#edit-value").value=inputValue(candidate.value);}
});
$("#edit-value").addEventListener("input",()=>{$("#alternatives").value="";});
$("#edit-form").addEventListener("submit",async event=>{
  event.preventDefault(); $("#save").disabled=true; $("#edit-error").textContent="";
  try {
    const payment=editing.predicate==="payment_status";
    const payload={predicate:editing.predicate,revision:editing.revision,value:payment?$("#alternatives").value:$("#edit-value").value,note:$("#edit-note").value};
    if(!payment && $("#alternatives").value) payload.selected_id=$("#alternatives").value;
    active=await api(`/api/subjects/${editing.subject}/revise`,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(payload)});
    $("#editor").close();render();await refreshList();notify("Intervento salvato. La versione precedente rimane nella cronologia.");
  } catch(error){$("#edit-error").textContent=error.message;}
  finally{$("#save").disabled=false;}
});
$("#cancel").addEventListener("click",()=>$("#editor").close());
$("#upload").addEventListener("click",()=>$("#file").click());
$("#file").addEventListener("change",()=>{if($("#file").files[0])importDocument($("#file").files[0]);});
document.addEventListener("click",event=>{
  const target=event.target.closest("button"); if(!target)return;
  if(target.id==="demo")importDocument();
  if(target.id==="empty-upload")$("#file").click();
  if(target.dataset.subject)openSubject(target.dataset.subject);
  if(target.dataset.edit)showEditor(target.dataset.edit);
  if(target.dataset.payment)showEditor("payment_status",target.dataset.payment);
});
refreshList().then(()=>{if(subjects.length)openSubject(subjects[0].id);}).catch(error=>notify(error.message,true));
