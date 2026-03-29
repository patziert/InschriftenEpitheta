import pandas, csv, re, cltk, spacy, pickle
from cltk import NLP
from cltk.lemmatize.lat import LatinBackoffLemmatizer
from cltk.lemmatize.backoff import (UnigramLemmatizer, RegexpLemmatizer, DictLemmatizer)
from cltk.tokenizers.lat.lat import LatinWordTokenizer
from cltk.alphabet import lat, processes
from cltk.alphabet.processes import LatinNormalizeProcess, NormalizeProcess
from cltk.utils import CLTK_DATA_DIR
from cltk.dependency.processes import LatinSpacyProcess, LatinStanzaProcess
from cltk.core.data_types import Doc, Language, Process
from cltk.alphabet.lat import normalize_lat
from cltk.utils.feature_extraction import cltk_doc_to_features_table

lemmatizer = LatinBackoffLemmatizer()
cltk_nlp = NLP(language="lat")
df = pandas.read_csv('./EDCS-Tabellen/searchresult.csv')
texts = df['Text'].tolist()
ctexts = [] 
zuschreibungen = "incomparabili pientissimae pietas pius obsequentissimae obsequens dulcissimo dulcis carissima"
zuschreibungen = zuschreibungen+" pudens impudens castitas casta rarissima felix clarissima luctus lucti fortis"
zuschreibungen = zuschreibungen+" honestus modestus moderatus sollicitus securus anxius studiosus beatus laetus"
zuschreibungen = zuschreibungen+" fidus placidus clemens integer prudens amabilis amatus amantus amans"
zuschreibungen = zuschreibungen+" probus probitas probatus frugi pulchra lepidus laetitia gaudens virtus"
zuschreibungen = zuschreibungen+" fructusque recte fatum acerbum acerbo fato dolor in maeroribus fletu lacrima"
zuschreibungen = zuschreibungen+" dolens flevit honor honos honoratum optimus optima merens meritus bene merenti merentissima"
zuschreibungen = zuschreibungen+" sapiens forma exemplum desiderius desiderium sine querella studio parili mellitissimo"
zuschreibungen = zuschreibungen+" incomparabilis concordia tristia digna adfectus suavis natus nata misera amoena"
zuschreibungen = zuschreibungen+" simplex deserta iucundus iuncundissimus sanctus sanctissimus"
beziehungen = "mater pater frater soror noverca privignus amita matertera nurrus filius filia nepos avia avus avunculus"
beziehungen = beziehungen+" patruus gener nurus uxor maritus marita coniux coniunx concubina contubernalis parens"
beziehungen = beziehungen+" parentis socer coniugium conubium matrimonium natus nata natorum"
print(texts[30])
for text in texts:
    text = str(text)
    ##text = re.sub(r'[^\w\s]', '', text)
    text = lat.accept_editorial(text)
    text = lat.drop_latin_punctuation(text)
    text = lat.normalize_lat(text, drop_accents=True, drop_macrons=True, jv_replacement=True, ligature_replacement=True)
    ctexts.append(text)
print (ctexts[30])
unilem = UnigramLemmatizer (lemmatizer.train_sents, source="CLTK Sentence Training Data", verbose=lemmatizer.VERBOSE)
reglem = RegexpLemmatizer (lemmatizer.latin_sub_patterns, source="CLTK Latin Regex Patterns", verbose=lemmatizer.VERBOSE)
dlem = DictLemmatizer (lemmatizer.LATIN_MODEL, source="Latin Model", verbose=lemmatizer.VERBOSE)
cltk_doc = cltk_nlp.analyze(ctexts[30])
cltk_doc2 = cltk_nlp.analyze(zuschreibungen)
cltk_doc3 = cltk_nlp.analyze(beziehungen)
print(cltk_doc.lemmata)
print(type(cltk_doc.lemmata[0]))
print(cltk_doc2.lemmata)
print(cltk_doc3.lemmata)
print(lemmatizer.lemmatize(cltk_doc2.tokens))
print(lemmatizer.lemmatize(cltk_doc3.tokens))
lwt=LatinWordTokenizer()
tokens = lwt.tokenize(text=beziehungen)
print(lemmatizer.lemmatize(tokens))
bdoc = Doc(language="lat", raw=beziehungen)
#lstp = LatinStanzaProcess()
#bdoc = lstp.run(input_doc=bdoc)
#print(bdoc.lemmata)
#print(bdoc.pos)
#lsp = LatinSpacyProcess()
#bdoc = lsp.run(input_doc=bdoc)
#print(bdoc.lemmata)
#print(bdoc.pos)
cltk_doc_rec = ""
with open("cltktest", "wb") as outfile:
    pickle.dump(cltk_doc, outfile)
#with open("cltktest2", "wb") as outfile:
#    pickle.dump(cltk_doc2, outfile)
#with open("cltktest", "rb") as infile:
#    cltk_doc_rec = pickle.load(infile)
#print(cltk_doc.lemmata)
#print(cltk_doc_rec.lemmata)
#print(cltk_doc==cltk_doc_rec)
vnames, ftable = cltk_doc_to_features_table(cltk_doc)
print(ftable)
print(cltk_doc2.lemmata)
ancestors = []
for token in cltk_doc.spacy_doc:
    ancs= []
    for ancestor in token.ancestors:
        anaccs= {}
        anaccs["text"] = ancestor.text
        anaccs["i"] = ancestor.i
        anaccs["orth"] = ancestor.orth
        anaccs["idx"] = ancestor.idx
        anaccs["pos"] = ancestor.pos_
        anaccs["dep"] = ancestor.dep_
        anaccs["lemma"] =ancestor.lemma_
        ancs.append(anaccs)
    ancestors.append(ancs)
print(ancestors[4])
with open ("./Testdaten/ancestorstest", "wb") as outfile:
    pickle.dump(ancestors, outfile)