#Generation der dritten Evaluationstabelle bezüglich der Lemmatisierung der Beziehungswörter

import pandas, re, csv, pickle, random, io
from Hilfsskripte import searchcombine4

def main():
    dfA = pandas.read_csv('./EDCS-Tabellen/searchresultSepulcralesReduziert.csv', low_memory=False)
    dfB = pandas.read_csv('./EDCS-Tabellen/searchresultWeitere.csv', low_memory=False)
    df = pandas.read_csv(io.StringIO(searchcombine4.combine(dfA, dfB)), low_memory=False)
    texts = df[['ID','Text']].values.tolist()
    outputtexts = []
    beziehungen = {"mat(er|ri|rum|re)" : [], "pat(er|ri|rum|re)" : [], "frat(er|ri|rum|re)" : [], "soror" : [], "noverca" : [], "privign" : [],
                "amita" : [], "marterta": [], "nurr" : [], "filia": [], "fili(us|i|o|um)" : [], "nepo(s|ti|te|tum)" : [], "avia" : [], "av(us|i|o|um)" : [],
                "avuncul" : [], "patru(us|i|o|um)" : [], "gener(\s|i\s|o\s|um\s)" : [], "nur(us|ui|um|u)\s": [], "uxor" : [],
                "marit(us|i|o|um)" : [], "marita" : [], "coniu(n?)(x|gi)" : [], "concubina" :[], "contubernal(|i|e)" : [], 
                "paren(s|ti|te|tum)": [], "socer" : [], "coniugi(um|i|o|a|orum|is)" : [], "conubi" : [], "matrimoni" : []}
    beziehungsLemmata = ["mater", "pater", "frater",  "soror" ,"noverca", "privignus", "amita", "matertera", "nurrus", "filia", "filius", "nepos",
                    "avia", "avus", "avunculus", "patruus", "gener", "nurus", "uxor", "maritus", "marita", "coniux", "concubina", "contubernalis",
                    "parens", "socer", "coniugium", "conubium", "matrimonium"]
    for t in texts:
        try:
            textfile = open('./Korpus_Sepulcrales/'+t[0]+'/'+t[0]+'_raw', "rb")
        except:
            textfile = open('./Korpus_Varia/'+t[0]+'/'+t[0]+'_raw', "rb")
        text = pickle.load(textfile)
        for i, b in enumerate(beziehungen):
            try:
                with open ("./Korpus_Sepulcrales/"+t[0]+"/"+t[0]+"_words", "rb") as infile:
                    words = pickle.load(infile)
                    for w in words:
                        if re.search(b, w.string):
                            beziehungen[b].append({"ID" : t[0], "Lemma (RegEx)" : beziehungsLemmata[i], "Regulärer Ausdruck" : b,"Text": text, "Lemma (Latincy)": w.lemma})
            except:
                with open ("./Korpus_Varia/"+t[0]+"/"+t[0]+"_words", "rb") as infile:
                    words = pickle.load(infile)
                    for w in words:
                        if re.search(b, w.string):
                            beziehungen[b].append({"ID" : t[0], "Lemma (RegEx)" : beziehungsLemmata[i], "Regulärer Ausdruck" : b,"Text": text, "Lemma (Latincy)": w.lemma})
    rows = []
    for b in beziehungen:
        length = 10
        if(len(beziehungen[b]))<10:
            length = len(beziehungen[b])
        if (length>0):
            for i in range(length):
                rnd = random.randint(0, len(beziehungen[b])-1)
                rows.append(beziehungen[b][rnd])
    with open('./Evaluationstabellen/evaltab3.csv', "w", encoding="utf-8", newline='') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames=['ID', 'Lemma (RegEx)', 'Regulärer Ausdruck', 'Text', 'Lemma (Latincy)'], quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    outcsv.close()

if __name__ == "__main__":
    main()