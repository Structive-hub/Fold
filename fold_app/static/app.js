"use strict";
const $ = selector => document.querySelector(selector);
const token = $('meta[name="fold-token"]').content;
let active = null;
let subjects = [];
let editing = null;
let busy = false;
let opening = false;
let noticeTimer;
let listPosition = {scroll:0, focus:null};
let selected = null;
const defaults = {q:"", filter:"all", sort:"recent"};
let view = {...defaults};
try {view = {...defaults,...JSON.parse(sessionStorage.getItem("fold-bills-view")||"{}")};} catch (_) {}
const escape = value => String(value ?? "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const dateLabel = value => value ? new Intl.DateTimeFormat("it-IT", {dateStyle:"medium"}).format(new Date(value.length===10?value+"T12:00:00":value)) : "Non disponibile";
const paymentLabels = {paid:"Pagamento dichiarato", unpaid:"Da pagare secondo la tua dichiarazione", unknown:"Pagamento non verificato"};
function display(value) {
  if(value && typeof value==="object" && value.currency) return new Intl.NumberFormat("it-IT",{style:"currency",currency:value.currency}).format(Number(value.amount));
  return value ?? "";
}
function inputValue(value) {return value&&typeof value==="object"?value.amount.replace(".",","):String(value??"");}
function notify(text,error=false) {
  clearTimeout(noticeTimer);$("#notice").textContent=text;$("#notice").classList.toggle("error",error);$("#notice").hidden=false;
  noticeTimer=setTimeout(()=>$("#notice").hidden=true,error?12000:6000);
}
async function api(path,options={}) {
  const response=await fetch(path,{...options,headers:{"X-Fold-Token":token,...options.headers}});
  const payload=await response.json();if(!response.ok)throw new Error(payload.error||"Operazione non completata.");return payload;
}
function titleOf(doc) {return doc.current.document_number?.value||doc.title;}
function missingFields(doc) {return Object.keys(doc.field_definitions).filter(key=>!doc.current[key]);}
function dataLabel(doc) {
  const missing=missingFields(doc).length;
  if(missing)return `${missing} ${missing===1?"dato da chiarire":"dati da chiarire"}`;
  const verified=Object.keys(doc.field_definitions).filter(key=>doc.current[key].origin.startsWith("human_")).length;
  return verified===4?"Dati verificati da te":verified?`${verified} di 4 dati verificati da te`:"Dati letti dal PDF";
}
function soon(doc) {
  const due=doc.current.due_date?.value;
  if(!due)return false;
  const days=(Date.parse(due+"T12:00:00Z")-Date.parse(doc.situation.reference_date+"T12:00:00Z"))/86400000;
  return days>=0&&days<=30;
}
function matches(doc) {
  const text=[titleOf(doc),doc.title,doc.current.pod?.value,display(doc.current.amount_due?.value),doc.current.amount_due?.value?.amount,doc.current.due_date?.value].join(" ").toLocaleLowerCase("it");
  const words=view.q.trim().toLocaleLowerCase("it").split(/\s+/).filter(Boolean);
  if(!words.every(word=>text.includes(word)))return false;
  const payment=doc.current.payment_status?.value||"unknown";
  if(view.filter==="review")return missingFields(doc).length>0;
  if(view.filter==="soon")return soon(doc);
  if(view.filter==="overdue")return Boolean(doc.current.due_date?.value&&doc.current.due_date.value<doc.situation.reference_date);
  if(view.filter==="paid"||view.filter==="unpaid")return payment===view.filter;
  return true;
}
function orderedDocuments() {
  return subjects.filter(matches).sort((a,b)=>{
    let order=0;
    if(view.sort==="due")order=(a.current.due_date?.value||"9999").localeCompare(b.current.due_date?.value||"9999");
    else if(view.sort==="amount")order=Number(b.current.amount_due?.value?.amount??-1)-Number(a.current.amount_due?.value?.amount??-1);
    else if(view.sort==="number")order=String(titleOf(a)).localeCompare(String(titleOf(b)),"it",{numeric:true});
    else order=b.created_at.localeCompare(a.created_at);
    return order||a.id.localeCompare(b.id);
  });
}
function persistView() {try {sessionStorage.setItem("fold-bills-view",JSON.stringify(view));} catch (_) {}}
async function refreshList() {
  const list=(await api("/api/subjects")).subjects.filter(doc=>doc.kind==="electricity_bill");
  // Use the existing detail API: no inferred metadata or new backend contract.
  const loaded=[];
  for(let i=0;i<list.length;i+=4)loaded.push(...await Promise.all(list.slice(i,i+4).map(doc=>api(`/api/subjects/${doc.id}`))));
  subjects=loaded;
  $("#archive-count").textContent=subjects.length;
}
function options(items,current) {return items.map(([value,label])=>`<option value="${value}" ${value===current?"selected":""}>${label}</option>`).join("");}
function renderList(restore=false) {
  active=null;persistView();
  $("#main").innerHTML=`<p class="breadcrumb">Archivio / Bollette elettriche</p><div class="page-heading"><div><h1>Bollette elettriche</h1><p class="muted">Confronta importi, scadenze e situazione dei documenti archiviati.</p></div></div>
    <div class="list-controls"><label class="search-label">Cerca una bolletta<input id="search" type="search" value="${escape(view.q)}" placeholder="Numero, nome del file, POD o importo" autocomplete="off"></label><label>Mostra<select id="filter" aria-label="Mostra">${options([["all","Tutte le bollette"],["review","Dati da chiarire"],["soon","Scadenza entro 30 giorni"],["overdue","Scadenza superata"],["paid","Pagamento dichiarato"],["unpaid","Dichiarata ancora da pagare"]],view.filter)}</select></label><label>Ordina per<select id="sort" aria-label="Ordina per">${options([["recent","Ultime acquisite"],["due","Scadenza più vicina"],["amount","Importo decrescente"],["number","Numero / documento"]],view.sort)}</select></label></div>
    <div class="result-bar"><p id="result-count" role="status" aria-live="polite"></p><button class="text-button" id="reset">Azzera ricerca e filtro</button></div><div id="results"></div><p class="list-note">La scadenza superata non dimostra un mancato pagamento. “Dati da chiarire” indica campi mancanti o con alternative; le letture complete non richiedono una conferma obbligatoria.</p>`;
  renderResults();
  if(restore)requestAnimationFrame(()=>{const focus=document.getElementById(listPosition.focus)||$("#result-count");focus.setAttribute("tabindex",focus.tabIndex<0?"-1":String(focus.tabIndex));focus.focus({preventScroll:true});window.scrollTo(0,listPosition.scroll);});
  else window.scrollTo(0,0);
}
function renderResults() {
  const docs=orderedDocuments();
  $("#result-count").textContent=`${docs.length} di ${subjects.length} bollette`;
  if(!docs.length) {
    $("#results").innerHTML=`<section class="empty-state"><h2>${subjects.length?"Nessuna bolletta corrisponde":"Il tuo archivio è vuoto"}</h2><p>${subjects.length?"Prova un altro termine o azzera la ricerca e il filtro. I documenti rimangono nell’archivio.":"Aggiungi una bolletta elettrica PDF con testo. L’originale e i dati letti saranno consultabili qui."}</p>${!subjects.length?'<button class="button primary" id="empty-upload">Aggiungi una bolletta PDF</button><p class="hint">Fino a 10 MB e 50 pagine. Le scansioni vengono conservate, ma non viene eseguito OCR.</p>':""}</section>`;return;
  }
  $("#results").innerHTML=`<div class="column-head" aria-hidden="true"><span>Documento</span><span>Importo</span><span>Scadenza</span><span>Situazione e dati</span></div><section class="bill-list" aria-label="Bollette archiviate">${docs.map(doc=>{
    const missing=missingFields(doc).length;
    const amount=doc.current.amount_due?.value;
    const due=doc.current.due_date?.value;
    return `<article class="bill-row ${selected===doc.id?"selected":""}"><div class="bill-identity"><button class="doc-link" id="open-${doc.id}" data-subject="${doc.id}">${escape(titleOf(doc))}</button><p>${escape(doc.title)}</p><small>${doc.current.pod?`POD ${escape(doc.current.pod.value)}`:"POD da chiarire"} · acquisita il ${escape(dateLabel(doc.created_at))}${doc.sources.some(source=>source.is_demo)?" · Esempio fittizio archiviato":""}</small></div><div class="bill-amount"><span class="cell-label">Importo</span><strong>${amount?escape(display(amount)):"Da chiarire"}</strong></div><div class="bill-due"><span class="cell-label">Scadenza</span><strong>${due?escape(dateLabel(due)):"Da chiarire"}</strong></div><div class="bill-state"><span class="situation-label ${doc.situation.tone=== "attention"?"attention":""}">${escape(doc.situation.label)}</span><span class="data-state ${missing?"attention":""}">${escape(dataLabel(doc))}</span></div></article>`;
  }).join("")}</section>`;
}
function rememberList() {
  listPosition={scroll:window.scrollY,focus:document.activeElement?.id};
  history.replaceState({foldList:true,view:{...view},position:listPosition,selected},"",location.pathname);
}
function enterDetail(doc) {
  if(!active){rememberList();history.pushState({foldDetail:true,id:doc.id,view:{...view},position:listPosition},"",`#bolletta-${doc.id}`);}
  else history.replaceState({foldDetail:true,id:doc.id,view:{...view},position:listPosition},"",`#bolletta-${doc.id}`);
  active=doc;selected=doc.id;render();window.scrollTo(0,0);$("#main").focus({preventScroll:true});
}
async function openSubject(id) {
  if(busy||opening)return;opening=true;
  try {enterDetail(await api(`/api/subjects/${id}`));}catch(error){notify(error.message,true);}finally{opening=false;}
}
function render() {
  const fields=Object.entries(active.field_definitions).map(([predicate,definition])=>{
    const current=active.current[predicate];
    const candidates=active.assertions.filter(a=>a.predicate===predicate&&a.origin==="document");
    const ambiguous=!current&&candidates.length;
    const state=current?current.origin==="document"?"Letto dal PDF":current.origin==="human_confirmation"?"Confermato da te":"Corretto da te":ambiguous?"Più valori possibili":"Non individuato";
    const value=current?definition.kind==="date"?dateLabel(current.value):display(current.value):ambiguous?"Da chiarire":"Non disponibile";
    let evidence="Non è stata trovata una corrispondenza esplicita. Il dato potrebbe essere presente nel PDF.";
    if(ambiguous)evidence="Alternative lette: "+[...new Set(candidates.map(a=>definition.kind==="date"?dateLabel(a.value):display(a.value)))].join(" · ");
    let proof=escape(evidence);
    if(current?.origin==="document")proof=`<p>Pagina ${current.page} · testo estratto</p><blockquote>${escape(current.excerpt)}</blockquote>`;
    else if(current)proof=`<p>Il valore corrente proviene dal tuo intervento.</p><blockquote>${escape(current.received?.note)}</blockquote><p>Le letture del PDF restano nella cronologia.</p>`;
    return `<article class="field" aria-label="${escape(definition.label)}"><div class="field-heading"><div><h3>${escape(definition.label)}</h3><strong class="field-value">${escape(value)}</strong></div><span class="field-state ${!current?"attention":""}">${state}</span></div><div class="field-actions"><button class="text-button" data-edit="${predicate}">${current?"Verifica o correggi":"Chiarisci il dato"}</button><details class="evidence"><summary>Mostra ${current?.origin==="document"||!current?"evidenza":"origine del dato"}</summary><div class="proof">${proof}${current?.source_id?`<a href="/api/sources/${current.source_id}" target="_blank" rel="noopener">Scarica la fonte PDF ↗</a>`:""}</div></details></div></article>`;
  }).join("");
  const historyItems=[...active.assertions].reverse().map(a=>{
    const definition=active.field_definitions[a.predicate];
    const label=a.predicate==="payment_status"?paymentLabels[a.value]:definition?.kind==="date"?dateLabel(a.value):display(a.value);
    const detail=a.origin==="document"?`Lettura dal PDF, pagina ${a.page}. ${a.excerpt}`:`${a.origin==="human_confirmation"?"Conferma":"Intervento"} di ${a.actor}: ${a.received?.note||""}`;
    return `<li class="event"><strong>${escape(definition?.label||"Pagamento")} · ${escape(label)}${a.selected?" · corrente":""}</strong><p>${escape(detail)}</p><time>${escape(dateLabel(a.created_at))}</time></li>`;
  }).join("");
  const source=active.sources[0];
  const payment=active.current.payment_status;
  $("#main").innerHTML=`<button class="text-button back" id="back-list">← Torna alle bollette</button><p class="breadcrumb">Archivio / Bollette elettriche / Dettaglio</p><div class="page-heading"><div><h1>${escape(titleOf(active))}</h1><p class="muted">${escape(source.filename)} · acquisita il ${escape(dateLabel(source.created_at))}${source.is_demo?" · Esempio fittizio archiviato":""}</p></div><a class="button outline" href="/api/sources/${source.id}" target="_blank" rel="noopener">Scarica PDF originale ↗</a></div>
    ${!active.text_available?'<div class="warning">Originale conservato. Nessun testo leggibile individuato: questa versione non esegue OCR. Puoi consultare il PDF e correggere i singoli dati.</div>':""}
    <section class="document-summary" aria-label="Sintesi della bolletta"><div><span>Totale da pagare</span><strong>${escape(active.current.amount_due?display(active.current.amount_due.value):"Da chiarire")}</strong></div><div><span>Scadenza</span><strong>${escape(active.current.due_date?dateLabel(active.current.due_date.value):"Da chiarire")}</strong></div></section>
    <section class="situation ${active.situation.tone=== "attention"?"attention":""}"><p class="eyebrow">SITUAZIONE AL ${escape(dateLabel(active.situation.reference_date))}</p><h2>${escape(active.situation.label)}</h2><p>${escape(active.situation.reason)}</p></section>
    <div class="detail-layout"><section class="fields-section"><h2>Dati e provenienza</h2><p class="muted">Verifica il dato che ti serve. La conferma di tutte le letture non è obbligatoria.</p><div class="fields">${fields}</div></section><aside class="payment-panel"><h2>Pagamento</h2><p>${payment?escape(paymentLabels[payment.value]):"Nessuna dichiarazione disponibile."}</p><p class="muted">La modalità stampata sul PDF non attesta l’esecuzione. Una tua dichiarazione non è una verifica bancaria.</p>${payment?`<blockquote>${escape(payment.received?.note)}</blockquote>`:""}<div class="payment-controls"><button class="button outline" data-payment="paid">Dichiara il pagamento</button><button class="text-button" data-payment="unknown">Chiarisci lo stato</button></div></aside></div>
    <details class="history"><summary>Cronologia e letture originali · ${active.assertions.length} registrazioni</summary><ol class="timeline">${historyItems||'<li>Nessun dato interpretato. Originale conservato.</li>'}</ol></details><details class="source-info"><summary>Informazioni sull’originale</summary><p>${source.receptions} acquisizione/i · Impronta SHA-256</p><code>${escape(source.sha256)}</code></details>`;
}
document.addEventListener("input",event=>{if(event.target.id==="search"){view.q=event.target.value;persistView();renderResults();}});
document.addEventListener("change",event=>{if(event.target.id==="filter"||event.target.id==="sort"){view[event.target.id]=event.target.value;persistView();renderResults();}});
document.addEventListener("click",event=>{
  const target=event.target.closest("button");if(!target)return;
  if(target.id==="reset"){view={...defaults};renderList();$("#search").focus();}
  if(target.id==="back-list"){if(history.state?.foldDetail)history.back();else returnToList();}
});
async function returnToList() {
  if(busy||opening)return;
  try {await refreshList();renderList(true);}catch(error){notify(error.message,true);}
}
window.addEventListener("popstate",async()=>{
  const state=history.state;
  if(state?.view)view={...defaults,...state.view};
  if(state?.position)listPosition=state.position;
  if(state?.foldDetail){try {active=await api(`/api/subjects/${state.id}`);selected=active.id;render();window.scrollTo(0,0);}catch(error){notify(error.message,true);}}
  else await returnToList();
});

async function importDocument(file=null) {
  if (busy) return;
  if (file && file.size>10*1024*1024) return notify("Il limite è 10 MB per documento.",true);
  busy=true; $("#upload").disabled=true; const demo=$("#demo"); if(demo) demo.disabled=true;
  notify("Conservo e leggo il documento…");
  try {
    const result = file ? await api("/api/import", {method:"POST",headers:{"Content-Type":"application/pdf","X-Filename":encodeURIComponent(file.name)},body:file}) : await api("/api/demo",{method:"POST"});
    enterDetail(result.subject); await refreshList();
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
  if(target.id==="empty-upload")$("#file").click();
  if(target.dataset.subject)openSubject(target.dataset.subject);
  if(target.dataset.edit)showEditor(target.dataset.edit);
  if(target.dataset.payment)showEditor("payment_status",target.dataset.payment);
});
(async()=>{
  await refreshList();
  renderList();
  const id=location.hash.match(/^#bolletta-([a-f0-9]{32})$/)?.[1];
  if(id)await openSubject(id);
  else history.replaceState({foldList:true,view:{...view},position:listPosition},"",location.pathname);
})().catch(error=>{
  $("#main").innerHTML='<section class="empty-state"><h1>Archivio non disponibile</h1><p>Ricarica la pagina per riprovare. I documenti non sono stati modificati.</p></section>';
  notify(error.message,true);
});
