import re
from cltk.alphabet import lat

Inscription = '] Aeb[uti(?) 3] / [3] hic [situs(?) est<br><b>Inschriftengattung / Personenstatus:</b>&nbsp;tituli sepulcrales;&nbsp;&nbsp;tria nomina;&nbsp;&nbsp;viri<br><b>Material:</b> lapis</p><p><b>Publikation:</b>       <a href=\"bilder.php?s_language=de&bild=$AE_2012_00655.jpg;$AE_2005_00692.jpg\"\n target="_blank">CAG-02A-02B, p 177,55 = AE 2005, 00692 = AE 2012, 00655 = Gallia-2005-285</a> \n<br><b>Datierung:</b> &nbsp;<b>a:&nbsp;</b> 151&nbsp;<b>bis</b> 250;&nbsp;&nbsp;&nbsp;<b>b:&nbsp;</b> 151&nbsp;<b>bis</b> 250&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>EDCS-ID:</b> EDCS-67400270<br> <b>Provinz:</b> Corsica&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Ort:</b> <script language=\"JavaScript\"><!--document.writeln("<a href=\"javascript:Neues_Fenster(\'osm-map.php?ort=Aleria&latitude=42.1135718&longitude=9.5144732&provinz=Corsica\')\">Aleria</a>");\n-->\n</script>\n<noscript>n   <a href=\"osm-map.php?ort=\'Aleria\'&latitude=\'42.1135718\'&longitude=\'9.5144732\'&provinz=\'Corsica\'\" target=\"_blank\">Aleria</a>\n</noscript>\n<br>'
dattempb = re.search(r"(?:bis</b> )(.*?)(:?\s*&nbsp;)", Inscription).group(1)
dattemp = re.search(r"(?:Datierung:</b> &nbsp;<b>)(.*?)(:?\s*&nbsp;)", Inscription).group(1)
gattung = re.search(r"(?:Inschriftengattung / Personenstatus\:</b>?\s*)(.*?)(:?(<br>|<p>|<br/>))", Inscription).group(1)
print(gattung)

InscriptionB = 'D(is) M(anibus) / M(arcus) Iulius Sabinianus miles / ex clas(se) praetoria{e} Misene(n)si{s} / |(centuria) Antoni Prisci vixit annis XXX / militavit annis VIII natio(ne) Bes(s)us'
InscriptionB = lat.accept_editorial(InscriptionB)
print(InscriptionB)

#EDCS-15900537
text = '⟦D(is) [M(anibus)]⟧ / ⟦[Sa]turni[n]u[s]⟧ / ⟦[3 vi]x(it)⟧ / ⟦a(nnos) X[3]⟧ / ⟦h(ic) [s(itus) e(st)]⟧'
text = re.sub(r' / ', ' ', text)
text = re.sub(r' // ', '. ', text)
text = re.sub(r'⟦', '', text)
text = re.sub(r'⟧', '', text)
print(text)