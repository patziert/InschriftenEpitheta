import pandas, pickle

sheets = pandas.read_excel('./Kerntabellen/ZuschreibungsListen.xlsx', sheet_name=None)
zlist = sheets["pius"]
for i, row in zlist.iterrows():
    id=row.loc["ID"]
    with open ("./inscraccs_test/"+id+"/"+id+"_words", "rb") as infile:
        words=pickle.load(infile)
        for word in words:
            if word.lemma == "carus":
                print(word)