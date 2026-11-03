// WCAG relative luminance for the text/background token pairs used in v0.2.
const luminance=h=>h.match(/../g).map(x=>parseInt(x,16)/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4).reduce((a,x,i)=>a+x*[.2126,.7152,.0722][i],0);
const pairs=[['e9edf2','101317'],['a4afbb','20262e'],['96bbeb','191e24'],['dfb46e','191e24'],['8fc8aa','191e24'],['e6a0a0','191e24'],['d9e9fc','2a435e'],['4c5a67','ebeff1'],['243341','f6dfaa'],['a4afbb','1e2a36']];
for(const [fg,bg] of pairs){const a=luminance(fg),b=luminance(bg),ratio=(Math.max(a,b)+.05)/(Math.min(a,b)+.05);if(ratio<4.5)throw Error(`${fg}/${bg}: ${ratio}`);console.log(`${fg}/${bg}: ${ratio.toFixed(2)}:1`);}
