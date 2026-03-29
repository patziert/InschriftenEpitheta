#Generation der ersten Evaluationstabelle zur allgemein Evaluation

import pandas, random, pickle, csv

def main():
    impframeA = pandas.read_csv('./EDCS-Tabellen/searchresultSepulcralesReduziert.csv', low_memory=False)
    impframeB = pandas.read_csv('./EDCS-Tabellen/searchresultWeitere.csv', low_memory=False)
    index = impframeA['ID'].to_list()
    impframeA.index = index
    beziehungen = {}
    samplelist = []
    with open ("./Kerndaten/Korpus_Sepulcrales_BeziehungenStatsDict", "rb") as infile:
        beziehungen=pickle.load(infile)
    for i in range(130):
        rnd = random.randint(0, len(index))
        row = impframeA.loc[index[rnd]]
        textfile = open('./Korpus_Sepulcrales/'+index[rnd]+'/'+index[rnd]+'_raw', "rb")
        text = pickle.load(textfile)
        rowdict = {'ID' : index[rnd], 'Text' : text}
        for b in beziehungen:
            for t in beziehungen[b][2]:
                if t[0]==index[rnd]:
                    rowdict["Zuschreibung"] = t[2]
        samplelist.append(rowdict)
    index = impframeB['ID'].to_list()
    impframeB.index = index
    with open ("./Kerndaten/Korpus_Varia_BeziehungenStatsDict", "rb") as infile:
        beziehungen=pickle.load(infile)
    for i in range(70):
        rnd = random.randint(0, len(index))
        row = impframeB.loc[index[rnd]]
        textfile = open('./Korpus_Varia/'+index[rnd]+'/'+index[rnd]+'_raw', "rb")
        text = pickle.load(textfile)
        rowdict = {'ID' : index[rnd], 'Text' : text}
        for b in beziehungen:
            for t in beziehungen[b][2]:
                if t[0]==index[rnd]:
                    rowdict["Zuschreibung"] = t[2]
        samplelist.append(rowdict)
    with open('./Evaluationstabellen/evaltab.csv', "w", encoding="utf-8", newline='') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames=['ID','Text', 'Zuschreibung'], quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in samplelist:
            writer.writerow(row)
    outcsv.close()

if __name__ == "__main__":
    main()