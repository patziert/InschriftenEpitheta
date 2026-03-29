#Generation der fünften Evaluationstabelle bezüglich der Dependency Analysis

import pandas, re, csv, pickle, random

global KORPUS
global SUCHTABELLE

def gather(size):
    global KORPUS
    global SUCHTABELLE
    df = pandas.read_csv('./Kerntabellen/'+KORPUS+'_adjsearch.csv', low_memory=False)
    df2 = pandas.read_csv('./Kerntabellen/'+KORPUS+'_participlesearch.csv', low_memory=False)
    beziehungen = {}
    with open ("./Kerndaten/"+KORPUS+"_BeziehungenStatsDict", "rb") as infile:
        beziehungen=pickle.load(infile)
    rowlist = []
    pos = ''
    pos2 = ''
    with open ("./Kerndaten/"+KORPUS+"_AdjPositions", "rb") as infile:
        pos=pickle.load(infile)
    with open ("./Kerndaten/"+KORPUS+"_ParticiplePositions", "rb") as infile:
        pos2=pickle.load(infile)
    pos.extend(pos2)
    ids = df['ID'].tolist()
    ids2 =df2['ID'].tolist()
    ids.extend(ids2)
    for id in ids:
        for p in pos:
            if p[0][0] == id:
                for i in p:
                    token = ""
                    for b in beziehungen:
                        for t in beziehungen[b][2]:
                            if t[0] == id:
                                token = t[3]
                    textfile = open('./'+KORPUS+'/'+id+'/'+id+'_raw', "rb")
                    text = pickle.load(textfile)
                    rowlist.append({'ID' : id, 'Text' : text, 'Zuschreibung' : i[2], 'Token' : token})
    samples = []
    for i in range(size):
        rnd = random.randint(0, len(rowlist))
        samples.append(rowlist[rnd])
    return samples

def main():
    global KORPUS
    KORPUS = 'Korpus_Sepulcrales'
    samples = gather(65)
    KORPUS = 'Korpus_Varia'
    samples2 = gather(35)
    for s in samples2:
        samples.append(s)
    with open('./Evaluationstabellen/evaltab5.csv', "w", encoding="utf-8", newline='') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames=['ID','Text', 'Zuschreibung', 'Token'], quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in samples:
            writer.writerow(row)
    outcsv.close()

if __name__ == "__main__":
    main()