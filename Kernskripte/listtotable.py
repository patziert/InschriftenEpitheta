#Konventiert Fundlisten aus AdjStats.py und PPAStats.py in Tabellen

import pandas

global SUCHTABELLE
global TYPE
global KORPUS

def main():
    global SUCHTABELLE
    global TYPE
    global KORPUS
    #Laden der Input-Dateien
    ids = []
    with open ("./Kerndaten/"+KORPUS+"_"+TYPE+"Output.txt", "r", encoding="UTF-8") as infile:
        content=infile.read()
        ids=content.splitlines()
    df = pandas.read_csv('./EDCS-Tabellen/'+SUCHTABELLE+'.csv', low_memory=False)
    selection =[]
    #Such in EDCS-Tabellen nach den Inschriften mit Funden
    for row in df.itertuples():
        for id in ids:
            if id==row.ID:
                print(row)
                selection.append(row)
    #Schreibe Fundtabelle
    ndf = pandas.DataFrame(selection)#.set_index('Index')
    csv = ndf.to_csv()
    outfile = open("./Kerntabellen/"+KORPUS+"_"+TYPE+"search.csv", "w", encoding='utf-8', newline='')
    outfile.write(csv)
    outfile.close()

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    TYPE = "adj"
    SUCHTABELLE = "searchresult.csv"
    main()