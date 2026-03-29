import cltk
from cltk import NLP

cltk_nlp = NLP(language="lat")

zuschreibungen = "incomparabili pientissimae pietas pius obsequentissimae obsequens dulcissimo dulcis carissima"
zuschreibungen = zuschreibungen+" pudens impudens castitas casta rarissima felix clarissima luctus lucti fortis"
zuschreibungen = zuschreibungen+" honestus modestus moderatus sollicitus securus anxius studiosus beatus laetus"
zuschreibungen = zuschreibungen+" fidus placidus clemens integer prudens amabilis amatus amantus amans"
zuschreibungen = zuschreibungen+" probus probitas probatus frugi pulchra lepidus laetitia gaudens virtus"
zuschreibungen = zuschreibungen+" fructusque recte fatum acerbum acerbo fato dolor in maeroribus fletu lacrima"
zuschreibungen = zuschreibungen+" dolens flevit honor honos honoratum optimus optima merens meritus bene merenti merentissima"
zuschreibungen = zuschreibungen+" sapiens forma exemplum desiderius desiderium sine querella studio parili mellitissimo"
zuschreibungen = zuschreibungen+" incomparabilis concordia tristia digna adfectus suavis natus nata misera amoena"
zuschreibungen = zuschreibungen+" simplex deserta iucundus iuncundissimus sanctus sanctissimus tristis amantissima"
zuschreibungen = zuschreibungen+" innocentissimus praestantissimus praestans innocentis dignissimus fidelissimus piissimus indulgentissimus fidelibus bene merenti"

cltk_doc = cltk_nlp.analyze(zuschreibungen)
words = cltk_doc.words
tokens = cltk_doc.tokens
with open ("./Testdaten/testZoutput.txt", "w", encoding="UTF-8") as outfile:
    for word, token in zip(words, tokens):
        outfile.write(token+"\n")
        outfile.write(str(word))
        outfile.write("\n")
    outfile.close()
