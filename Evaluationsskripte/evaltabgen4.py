#Generation der vierten Evaluationstabelle bezüglich der Named Entity Regognition

import pandas, re, csv, pickle, random, io
from Hilfsskripte import searchcombine4

def main():
    dfA = pandas.read_csv('./EDCS-Tabellen/searchresultSepulcralesReduziert.csv', low_memory=False)
    dfB = pandas.read_csv('./EDCS-Tabellen/searchresultWeitere.csv', low_memory=False)
    df = pandas.read_csv(io.StringIO(searchcombine4.combine(dfA, dfB)), low_memory=False)
    texts = df[['ID','Text']].values.tolist()
    rowlist = []
    for t in texts:
        try:
            textfile = open('./Korpus_Sepulcrales/'+t[0]+'/'+t[0]+'_raw', "rb")
        except:
            textfile = open('./Korpus_Varia/'+t[0]+'/'+t[0]+'_raw', "rb")
        text = pickle.load(textfile)
        try:
            with open ("./Korpus_Sepulcrales/"+t[0]+"/"+t[0]+"_ents", "rb") as infile:
                enttext = ""
                ents=pickle.load(infile)
                for e in ents:
                    enttext += e[0]+" "+e[3]+"; "
                rowlist.append({'ID' : t[0], 'Text' : text, 'Named Entities' : enttext})
        except:
            with open ("./Korpus_Varia/"+t[0]+"/"+t[0]+"_ents", "rb") as infile:
                enttext = ""
                ents=pickle.load(infile)
                for e in ents:
                    enttext += e[0]+" "+e[3]+"; "
                rowlist.append({'ID' : t[0], 'Text' : text, 'Named Entities' : enttext})
    samples = []
    for i in range(100):
        rnd = random.randint(0, len(rowlist))
        samples.append(rowlist[rnd])
    with open('./Evaluationstabellen/evaltab4.csv', "w", encoding="utf-8", newline='') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames=['ID','Text', 'Named Entities'], quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in samples:
            writer.writerow(row)
    outcsv.close()

if __name__ == "__main__":
    main()