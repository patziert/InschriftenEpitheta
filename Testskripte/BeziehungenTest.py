import cltk
from cltk import NLP

cltk_nlp = NLP(language="lat")

beziehungen = "mater pater frater soror noverca privignus amita matertera nurrus filius filia nepos avia avus avunculus"
beziehungen = beziehungen+" patruus gener nurus uxor maritus marita coniux coniunx concubina contubernalis parens"
beziehungen = beziehungen+" parentes socer coniugium conubium matrimonium natus nata natorum"

cltk_doc = cltk_nlp.analyze(beziehungen)
words = cltk_doc.words
tokens = cltk_doc.tokens
#with open ("./Testdaten/testBoutput.txt", "w", encoding="UTF-8") as outfile:
#    for word, token in zip(words, tokens):
#        outfile.write(token+"\n")
#        outfile.write(str(word))
#        outfile.write("\n")
#    outfile.close()
print(tokens)
