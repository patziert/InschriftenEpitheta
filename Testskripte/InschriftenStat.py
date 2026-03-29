import re, pickle, cltk
zhitlist = []
with open ("/Testdaten/test4output.txt", "r", encoding="UTF-8") as lfile:
    zhitlist =lfile.read().split('\n')
    zhitlist =zhitlist[:-1]
wordsdic = {}
depsdic = {}
for z in zhitlist:
    with open("./inscraccs_test/"+z+"/"+z+"_words", "rb") as wfile:
        words = pickle.load(wfile)
        wordsdic[z] = words
    with open("./inscraccs_test/"+z+"/"+z+"_deps", "rb") as dfile:
        deps = pickle.load(dfile)
        depsdic[z] = deps
print(wordsdic["EDCS-85200198"][5].dependency_relation)
print(depsdic["EDCS-85200198"][5])