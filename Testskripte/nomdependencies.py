import pandas, pickle

def getSentence(words):
    sentence=""
    for word in words:
        sentence+=word.string+" "
    return sentence

df = pandas.read_csv('./Testdaten/nomsearch.csv', low_memory=False)
ids =df['ID'].tolist()
beziehungen = {'mater' : 0, 'pater' : 0, 'frater' : 0, 'soror' : 0, 'noverca' : 0, 'privignus' : 0, 'amita' :0, 
               'matertera' : 0, 'nurrus' : 0, 'filius' : 0, 'filia' : 0, 'avia' : 0, 'auus' : 0, 'avunculus' :0, 
               'patruus' : 0, 'gener' : 0, 'nurus' : 0, 'uxor' : 0, 'maritus' : 0, 'coniux' : 0, 'coniunx' :0, 
               'concubinus' : 0, 'contubernalis' : 0, 'parens' : 0, 'socer' : 0, 'conubium' : 0, 'matrimonium' :0}
pos = []
ecount = 0
with open ("./Testdaten/testNomPositions", "rb") as infile:
    pos=pickle.load(infile)
    print(pos)
for id, p in zip(ids, pos):
    words = []
    for l, (o) in enumerate (p):
        with open ("./inscraccs_test/"+p[l][0]+"/"+p[l][0]+"_words", "rb") as infile:
            words=pickle.load(infile)
        with open ("./inscraccs_test/"+p[l][0]+"/"+p[l][0]+"_ancestors", "rb") as infile:
            ancs=pickle.load(infile)
            find = False
            efind = False
            enttemp = ""
            for a in ancs[p[l][1]]:
                for b in beziehungen:
                    if a['lemma']==b:
                        beziehungen[b]+=1
                        print(p)
                        print(getSentence(words))
                        print(ancs[p[l][1]])
                        find = True
                if find == False and efind == False:
                    with open ("./inscraccs_test/"+p[l][0]+"/"+p[l][0]+"_ents", "rb") as entfile:
                        ents=pickle.load(entfile)
                        try:
                            for e in ents:
                                if (e[0]==a['text'] or e[0]==a['lemma']) and e[3] == 'PERSON':
                                    print(p)
                                    print(getSentence(words))
                                    print(ancs[p[l][1]])
                                    print(e[0])
                                    ecount+=1
                                    efind=True
                                    break
                        except:
                            pass
                if find:
                    break

print(beziehungen)
print(ecount)