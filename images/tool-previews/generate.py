from pathlib import Path
from html import escape
import re
OUT=Path(__file__).parent
ICONS=OUT/'assets'
RED='#c51d17';BLACK='#111111';GRAY='#f7f7f7';LINE='#d2d2d2';MUTED='#595959';WHITE='#ffffff'
parts=[]
def rect(x,y,w,h,fill=WHITE,stroke=None,sw=1):
 parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+'/>')
def text(x,y,s,size=22,weight=400,fill=BLACK,anchor='start'):
 parts.append(f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>')
def line(x,y,x2,y2,c=LINE,sw=1):parts.append(f'<path d="M{x} {y}H{x2}" stroke="{c}" stroke-width="{sw}"/>' if y==y2 else f'<path d="M{x} {y}L{x2} {y2}" stroke="{c}" stroke-width="{sw}"/>')
def button(x,y,w,s,primary=False):
 rect(x,y,w,46,RED if primary else WHITE,RED if primary else BLACK)
 text(x+w/2,y+29,s,17,600,WHITE if primary else BLACK,'middle')
def icon(key,x,y,size=68):
 src=(ICONS/f'fmt-{key}.svg').read_text()
 inner=src[src.index('>')+1:src.rindex('</svg>')]
 parts.append(f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 1024 1024">{inner}</svg>')
def begin(name,key,desc):
 global parts
 parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">',f'<title>{escape(name)} — FMT ontwerpvoorbeeld</title>']
 rect(0,0,1600,1000,WHITE);rect(0,0,1600,6,RED)
 icon(key,40,28,76);text(132,63,name.upper(),28,700);text(133,87,'FAST MOVING TARGETS',12,700,MUTED)
 text(1552,65,'ONTWERPVOORBEELD',18,700,MUTED,'end');line(40,118,1560,118,BLACK,2)
 text(48,158,desc,19,400,MUTED)
 line(40,940,1560,940,BLACK);text(48,974,'FMT / GEREEDSCHAP OM ZELF VERDER TE BOUWEN',12,700,MUTED)
 text(1552,974,'Visuele richting · De bestaande tool is nog niet aangepast',12,400,MUTED,'end')
def finish(key):
 parts.append('</svg>');(OUT/f'{key}.svg').write_text('\n'.join(parts))
# Werkplaats
begin('Werkplaats','werkplaats','Je eigen plek voor ideeën, teksten en projecten.')
text(48,238,'JE WERK.',58,700);text(48,302,'JE GEREEDSCHAP.',58,700)
text(1010,235,'Verzamelen, maken en terugvinden.',24,600);text(1010,272,'Je bestanden blijven onder jouw controle.',19,400,MUTED)
button(48,334,184,'Nieuw beginnen',True);button(248,334,184,'Verder werken')
line(48,420,1552,420,BLACK);text(48,454,'INFORMATIE',15,700,MUTED)
labels=[('VERZAMELEN','Bewaar links, citaten en notities.'),('SCHRIJVEN','Schrijf en lees je documenten.'),('ZOEKEN','Vind je bronnen en werk terug.'),('PROJECTEN','Beheer je ideeën en projecten.'),('DOEN','Houd taken en deadlines bij.'),('CONTACTEN','Bewaar contacten en gesprekken.')]
for i,(name,desc) in enumerate(labels):
 col=i%3;row=i//3;x=48+col*512;y=474+row*224
 rect(x,y,480,178,BLACK);text(x+24,y+49,f'0{i+1}',16,700,'#aaaaaa');text(x+24,y+92,name,28,700,WHITE);text(x+24,y+129,desc,18,400,WHITE);text(x+452,y+153,'→',24,400,WHITE,'end')
text(48,685,'ORGANISATIE',15,700,MUTED)
finish('werkplaats')
# Tools voor Teksten
begin('Tools voor Teksten','tools-voor-teksten','Jouw informatie. In bruikbare bestanden. Onder jouw controle.')
rect(48,198,294,696,GRAY);text(68,234,'JOUW BESTANDEN',16,700);text(68,274,'Voorbeeldbestanden',21,700);text(68,303,'5 van 5 geselecteerd',16,400,MUTED);button(68,325,250,'Kies een map')
files=['Interview.docx','Beleidsnotitie.pdf','Informatiepagina.html','Voorstel.txt','Voorstel-herzien.txt']
for i,f in enumerate(files):
 y=425+i*73;rect(68,y-17,16,16,RED);text(70,y-3,'✓',12,700,WHITE);text(98,y,f,17);text(98,y+25,['38 kB','66 kB','5 kB','4 kB','5 kB'][i],13,400,MUTED)
text(382,234,'WAT WIL JE DOEN?',30,700);rect(382,264,1170,105,WHITE,BLACK);text(408,306,'Sleep een map of bestand hierheen',23,700);text(408,338,'Kies daarna wat je ermee wilt doen.',17,400,MUTED);button(1324,292,204,'Kies map of bestand')
rect(382,401,1170,127,WHITE,BLACK);rect(382,401,6,127,RED);text(408,445,'Naar Markdown',29,700);text(408,480,'Van Word, PDF, HTML of tekst naar een .md-bestand.',20);text(408,508,'DOCX  /  PDF  /  HTML  /  TXT  →  MD',13,700,MUTED);text(1522,471,'→',30,400,BLACK,'end')
items=[('Persoonsgegevens afschermen','Herken persoonsgegevens. Controleer wat je afschermt.'),('Metadata controleren','Bekijk verborgen gegevens en maak een schone tekstkopie.'),('Documenten samenvoegen','Maak één Markdown-bestand van meerdere documenten.'),('Versies vergelijken','Bekijk wat er is veranderd.')]
for i,(n,d) in enumerate(items):
 x=382+(i%2)*597;y=552+(i//2)*148
 rect(x,y,573,124,WHITE,LINE);text(x+24,y+44,n,23,700);text(x+24,y+80,d,16,400,MUTED);text(x+542,y+106,'→',24,400,BLACK,'end')
text(382,886,'JOUW BESTANDEN BLIJVEN VAN JOU.',14,700,MUTED)
finish('tools-voor-teksten')
# Kladblok
begin('Kladblok','kladblok','Eén plek voor even. Plak of schrijf maar.')
text(250,238,'TITEL VAN JE KLAD',16,700,MUTED);rect(250,260,1100,62,WHITE,BLACK);text(270,301,'Mijn ideeën',26,600)
text(250,375,'JE TEKST',16,700,MUTED);rect(250,397,1100,328,WHITE,BLACK)
text(274,444,'Eerste idee: meer tijd voor maken.',25);text(274,486,'Tweede idee: samen leren.',25)
button(250,757,220,'Markdown (.md)  ⌄');button(486,757,230,'Download bestand',True);button(732,757,190,'Kopieer alles');button(938,757,94,'Wis')
text(250,850,'Je klad blijft in deze browser op deze computer.',18,400,MUTED);text(250,880,'Download belangrijke tekst ook als bestand.',18,400,MUTED)
finish('kladblok')
# Video
begin('Video Editor','video','Importeer, monteer en ondertitel je interview.')
button(1340,198,212,'Exporteer video',True);text(324,230,'Strawberry',30,700);text(324,263,'Opening · teasers',18,400,MUTED)
rect(48,198,240,696,GRAY);text(68,234,'MONTAGE',16,700)
scenes=[('Opening · teasers','00:14 · 1 fragment'),('Waarom een browser','00:32 · 3 fragmenten'),('Voor wie Strawberry is','00:53 · 2 fragmenten'),('Een collega die je volgt','00:53 · 1 fragment'),('Beginnen en samenwerken','01:05 · 2 fragmenten'),('De Europese keuze','00:23 · 1 fragment')]
for i,(n,d) in enumerate(scenes):
 y=267+i*85
 if i==0:rect(48,y-16,240,78,'#e5e5e5');rect(48,y-16,4,78,RED)
 text(68,y+8,f'{i+1:02}',14,700,MUTED);text(100,y+8,n,14,600);text(100,y+34,d,13,400,MUTED)
rect(324,292,912,514,GRAY,LINE)
# Deliberate abstract video placeholder: no invented portrait.
rect(356,351,350,245,'#e5e5e5');rect(381,376,300,195,BLACK);parts.append('<path d="M500 430L500 519L567 474Z" fill="#ffffff"/>');text(531,616,'INTERVIEWFRAGMENT',13,700,MUTED,'middle')
rect(737,350,4,260,RED);text(770,441,'6',108,700,RED);text(770,489,'maanden met Fritz',31,700);text(770,533,'Een agent die je',27,700);text(770,567,'leert kennen',27,700)
rect(356,670,848,66,WHITE,BLACK);text(780,711,'Ik werk nu ongeveer zes maanden met Fritz samen.',23,400,BLACK,'middle')
line(356,768,1204,768,LINE,3);rect(356,763,30,10,RED);text(324,844,'00:00 / 10:11',16,400,MUTED);button(972,826,264,'Knip aanpassen')
rect(1270,278,282,616,GRAY);text(1294,322,'CONTROLE',16,700);text(1294,371,'Controle afgerond',23,700);text(1294,405,'Audio en overgangen',17,400,MUTED);text(1294,431,'gecontroleerd.',17,400,MUTED);button(1294,475,234,'AI-voorstellen');button(1294,539,234,'Alle controles')
finish('video')
# Screenshot Editor
begin('Screenshot Editor','screenshot','Een beeld. Jouw woorden. Klaar om te delen.')
rect(48,198,350,696,GRAY);text(72,237,'1. KIES JE INHOUD',17,700);button(72,259,302,'Laad afbeelding');button(72,320,302,'Maak screenshot');text(72,414,'2. MAAK HET PASSEND',17,700)
text(72,450,'Formaat',15,600,MUTED);button(72,466,302,'Breed · 1920 × 1080  ⌄');text(72,549,'Achtergrond',15,600,MUTED);button(72,565,302,'Rood  ⌄');text(72,653,'Uitsnede / zoom',15,600,MUTED);line(76,679,368,679,LINE,5);rect(150,671,15,16,RED)
text(72,748,'3. BEWAAR JE BEELD',17,700);button(72,774,144,'Bewaar PNG',True);button(232,774,142,'Kopieer beeld')
text(442,229,'JOUW BEELD',16,700);text(1552,229,'1920 × 1080',14,400,MUTED,'end');button(1394,132,158,'Eigen stijl')
rect(442,259,1110,624,'#e5e5e5');rect(474,291,1046,560,RED)
text(506,333,'STUDIO VOORBEELD',14,700,WHITE);rect(560,378,874,360,WHITE,BLACK,2);rect(584,402,826,62,BLACK);text(610,442,'Een idee dat je wilt bewaren',29,700,WHITE)
rect(584,488,236,218,RED);text(854,536,'Maak het zelf.',36,700);text(854,583,'Begin klein. Probeer.',24);text(854,622,'Pas aan.',24)
text(506,803,'Een klein idee, helder in beeld.',18,600,WHITE)
finish('screenshot')
(OUT/'ontwerpcontract.md').write_text('''# FMT / vijf ontwerpvoorbeelden\n\n- Doel: vijf herkenbare UI-voorbeelden voor de GitHub-profielpagina; geen gewijzigde apps.\n- Eén witte bovenbalk, origineel toolicoon, vaste naam, Arial en scherpe geometrie.\n- Palet: #ffffff, #111111, #c51d17, neutrale grijzen #f7f7f7/#e5e5e5/#d2d2d2/#595959. Originele iconen behouden eigen #E10600/#0A0A0A. Geen beige.\n- Formaat: ieder beeld 1600 × 1000. Header 118 px hoog, footer op 940 px.\n- Elk beeld heeft label ONTWERPVOORBEELD plus vermelding dat de bestaande tool nog niet is aangepast.\n\n## Bronnen en inhoud\n\nBestaande toolindelingen op github.com/erwinblom, zoals door Chief beoordeeld. Originele SVG-iconen uit Desktop/FMT-Dock-iconen-2026-11-03/iconen. Teksten en functies zijn alleen statische weergaven. Video gebruikt een abstract interviewvlak, geen verzonnen portret. Geen appcode of werkdocumenten gewijzigd.\n\n## Bewerken\n\nVoer `python3 generate.py` uit. De originele iconen zijn meegeleverd in `assets/`. De vijf SVG-bestanden zijn volledig bewerkbaar en bevatten de iconen inline; de eindbeelden hebben geen externe afhankelijkheden. Voor PNG-export: `npm install` en `npm run render` (Node.js en Python 3 nodig).\n''')
print('Gegenereerd: '+', '.join(p.name for p in OUT.glob('*.svg')))
