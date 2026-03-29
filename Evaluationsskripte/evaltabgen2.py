#Generation der zweiten Evaluationstabelle bezüglich der Lemmatisierung der Zuschreibungen

import pandas, re, csv, pickle, random, io
from Hilfsskripte import searchcombine4

def main():
    dfA = pandas.read_csv('./EDCS-Tabellen/searchresultSepulcralesReduziert.csv', low_memory=False)
    dfB = pandas.read_csv('./EDCS-Tabellen/searchresultWeitere.csv', low_memory=False)
    df = pandas.read_csv(io.StringIO(searchcombine4.combine(dfA, dfB)), low_memory=False)
    texts = df[['ID','Text']].values.tolist()
    outputtexts = []
    zuschreibungen = {"incomparabil" : [], "pi(us|a|um)" : [], "pientissim":[] , "obsequen": [],"dulcis" : [], "car" : [],"carissim" : [], 
                    "puden" : [], "cast(us|a|um)" : [], "rar(us|is|a|um|orum|arum)" : [], "felix" : [], "clar(us|a|um|i|o)" : [], "fortis" : [], 
                    "honest" : [], "modest": [], "moderat": [], "sollicit" : [], "secur" : [], "anxi" : [], "studios" : [], "beat(us|a|um|i|o)" : [],
                    "laet" : [], "fid(us|a|um)" : [], "placid" : [], "clemen" : [], "integ(er|ra|rum)" : [], "pruden(s|t)" : [], "amabil" : [],
                    "amat" : [], "aman" : [], "prob(us|a|um|i|o)" : [], "frugi" : [], "pulch(er|ra|rum)" : [], "lepid" : [],
                    "dolen(s|t)" : [], "optim(us|a|um|i|o)" : [], "mer(ens|itus|enti|erentissima)" : [], "sapien" : [],
                    "mellit" : [], "trist(i|e)" : [], "dign" : [], "adfect" : [], "suav" : [], "nat(us|a|um|i|o)" : [],
                    "miser" : [], "simpl(ex|ic)" : [], "desert" : [], "iucund" : [], "sanct" : [], "probat" : [], "innocen" : [],
                    "innocentissim" : [], "praestantissim" : [], "indulgentissim" : [], "dignissim" : [], "fidel" : [], "fidelissim" : [], "praestan" : []}
    zuschreibungenLemmata = ["incomparabilis", "pius", "pientissimus", "obsequentissimus","dulcis", "carus", "carissimus", 
                    "pudens", "castus", "rarus", "felix", "clarus", "fortis", 
                    "honestus", "modestus", "moderatus", "sollicitus", "securus", "anxius", "studiosus", "beatus",
                    "laetus", "fidus", "placidus", "clemens", "integer", "prudens", "amabilis",
                    "amo", "amans", "probus", "frugi", "pulcher", "lepidus",
                    "doleo", "optimus", "merens", "sapiens",
                    "mellitus", "tristis", "dignus", "adfectus", "suavis", "natus",
                    "miser", "simplex", "desero", "iucundus", "sanctus", "probo", "innocens", "innocentissimus",
                    "praestantissimus", "indulgentissimus", "dignissimus", "fidelis", "fidelissimus", "praesto"]
    doubletten = {"mereo" : "mer(ens|itus|enti|erentissima)", "nascor" : "nat(us|a|um|i|o)", "mero" : "mer(ens|itus|enti|erentissima)"}
    for t in texts:
        try:
            textfile = open('./Korpus_Sepulcrales/'+t[0]+'/'+t[0]+'_raw', "rb")
        except:
            textfile = open('./Korpus_Varia/'+t[0]+'/'+t[0]+'_raw', "rb")
        text = pickle.load(textfile)
        for i, z in enumerate(zuschreibungen):
            try:
                with open ("./Korpus_Sepulcrales/"+t[0]+"/"+t[0]+"_words", "rb") as infile:
                    words = pickle.load(infile)
                    for w in words:
                        if re.search(z, w.string):
                            zuschreibungen[z].append({"ID" : t[0], "Lemma (RegEx)" : zuschreibungenLemmata[i], "Regulärer Ausdruck" : z,"Text": text, "Lemma (Latincy)": w.lemma})
                            continue
                        for d in doubletten:
                            if re.search(d, w.string):
                                index = list(zuschreibungen).index(doubletten[d])
                                zuschreibungen[doubletten[d]].append({"ID" : t[0], "Lemma (RegEx)" : zuschreibungenLemmata[index], "Regulärer Ausdruck" : d,"Text": text, "Lemma (Latincy)": w.lemma})
                                continue
            except:
                with open ("./Korpus_Varia/"+t[0]+"/"+t[0]+"_words", "rb") as infile2:
                    words = pickle.load(infile2)
                    for w in words:
                        if re.search(z, w.string):
                            zuschreibungen[z].append({"ID" : t[0], "Lemma (RegEx)" : zuschreibungenLemmata[i], "Regulärer Ausdruck" : z,"Text": text, "Lemma (Latincy)": w.lemma})
                            continue
                        for d in doubletten:
                            if re.search(d, w.string):
                                index = list(zuschreibungen).index(doubletten[d])
                                zuschreibungen[doubletten[d]].append({"ID" : t[0], "Lemma (RegEx)" : zuschreibungenLemmata[index], "Regulärer Ausdruck" : d,"Text": text, "Lemma (Latincy)": w.lemma})
                                continue

    rows = []
    for z in zuschreibungen:
        length = 10
        if(len(zuschreibungen[z]))<10:
            length = len(zuschreibungen[z])
        if (length>0):
            for i in range(length):
                rnd = random.randint(0, len(zuschreibungen[z])-1)
                rows.append(zuschreibungen[z][rnd])
    with open('./Evaluationstabellen/evaltab2.csv', "w", encoding="utf-8", newline='') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames=['ID', 'Lemma (RegEx)', 'Regulärer Ausdruck', 'Text', 'Lemma (Latincy)'], quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    outcsv.close()

if __name__ == "__main__":
    main()