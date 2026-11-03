# FMT / vijf ontwerpvoorbeelden

- Doel: vijf herkenbare UI-voorbeelden voor de GitHub-profielpagina; geen gewijzigde apps.
- Eén witte bovenbalk, origineel toolicoon, vaste naam, Arial en scherpe geometrie.
- Palet: #ffffff, #111111, #c51d17, neutrale grijzen #f7f7f7/#e5e5e5/#d2d2d2/#595959. Originele iconen behouden eigen #E10600/#0A0A0A. Geen beige.
- Formaat: ieder beeld 1600 × 1000. Header 118 px hoog, footer op 940 px.
- Elk beeld heeft label ONTWERPVOORBEELD plus vermelding dat de bestaande tool nog niet is aangepast.

## Bronnen en inhoud

Bestaande toolindelingen op github.com/erwinblom, zoals door Chief beoordeeld. Originele SVG-iconen uit Desktop/FMT-Dock-iconen-2026-11-03/iconen. Teksten en functies zijn alleen statische weergaven. Video gebruikt een abstract interviewvlak, geen verzonnen portret. Geen appcode of werkdocumenten gewijzigd.

## Bewerken

Voer `python3 generate.py` uit. De originele iconen zijn meegeleverd in `assets/`. De vijf SVG-bestanden zijn volledig bewerkbaar en bevatten de iconen inline; de eindbeelden hebben geen externe afhankelijkheden. Voor PNG-export: `npm install` en `npm run render` (Node.js en Python 3 nodig).
