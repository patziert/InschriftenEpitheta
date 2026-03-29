import cltk, re
from cltk import NLP
from cltk.alphabet import lat

cltk_nlp = NLP(language="lat")

inschrift = "D(is) M(anibus) s(acrum) / Delius Felicissimus / av(u)nculus dulcis(s)imus / vixit an(n)is LVI m(ense) I d(iebus) XVI"
text = str(inschrift)
print(text)
##text = re.sub(r'[^\w\s]', '', text)
text = re.sub(r' / ', ' ', text)
text = re.sub(r' // ', '. ', text)
text = re.sub(r'⟦', '', text)
text = re.sub(r'⟧', '', text)
text = lat.accept_editorial(text)
text = lat.drop_latin_punctuation(text)
text = lat.normalize_lat(text, drop_accents=True, drop_macrons=True, ligature_replacement=True)
print(text)
cltk_doc = cltk_nlp.analyze(text)
print(cltk_doc.normalized_text)
print(cltk_doc.lemmata)
print(cltk_doc.words[5])