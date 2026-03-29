import cltk, pickle
from cltk import NLP

cltk_nlp = NLP(language="lat")
with open ("./inscraccs_test/EDCS-04201487/EDCS-04201487_pos", "rb") as infile:
    pos = pickle.load(infile)
    print(pos)
with open ("./inscraccs_test/EDCS-19800615/EDCS-19800615_raw", "rb") as infile:
    raw = pickle.load(infile)
    print(raw)
    cltk_doc = cltk_nlp.analyze(raw)
    print(cltk_doc.pos)
    print(cltk_doc.normalized_text)
with open ("./inscraccs_test/EDCS-19800615/EDCS-19800615_lemmata", "rb") as infile:
    lemmata = pickle.load(infile)
    print(lemmata)