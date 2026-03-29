#Generiert Tabelle zur Ausgabe der Superlativanteile

import pandas, re, pickle, csv

global KORPUS

def main():
    global KORPUS
    superlative = {'pius' : 'pientissimus', 'carus' : 'carissimus', 'bonus' : 'optimus', 'innocens' : 'innocentissimus',
                   'fidelis' : 'fidelissimus', 'dignus' : 'dignissimus', 'dulcis' : 'dulcissimus', 'rarus' : 'rarissimus',
                   'fortis' : 'fortissimus', 'clemens' : 'clementissimus', 'amans' : 'amantissimus', 
                   'simplex' : 'simplicissimus', 'sanctus' : 'sanctissimus', 'obsequor' : 'obsequentissimus', 
                   'praesto' : 'praestantissimus'}
    sheets = pandas.read_excel('./Kerntabellen/'+KORPUS+'_ZuschreibungsListen.xlsx', sheet_name=None)
    pos = ''
    pos2 = ''
    with open ("./Kerndaten/"+KORPUS+"_AdjPositions", "rb") as infile:
        pos=pickle.load(infile)
    with open ("./Kerndaten/"+KORPUS+"_ParticiplePositions", "rb") as infile:
        pos2=pickle.load(infile)
    pos.extend(pos2)
    rowlist = []
    for sheet in sheets:
        if sheet in superlative:
            zcount = 0
            scount = 0
            for i, row in sheets[sheet].iterrows():
                zcount+=1
                id = row.loc['ID']
                token = ""
                for p in pos:
                    if p[0][0] == id:
                        for i in p:
                            if i[2] == sheet:
                                with open ("./"+KORPUS+"/"+id+"/"+id+"_tokens", "rb") as tfile:
                                    tokens = pickle.load(tfile)
                                    token = tokens[i[1]]
                                break
                if re.search("(issim)|(optim)", token):
                    scount+=1
            rowlist.append({"Zuschreibung" : sheet, "Superlative" : scount, "Gesamtzahl": zcount})
    with open('./Ausgabetabellen/'+KORPUS+'_superlative.csv', "w", encoding="utf-8", newline='') as outcsv:
        writer = csv.DictWriter(outcsv, fieldnames=['Zuschreibung','Superlative', 'Gesamtzahl'], quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for row in rowlist:
            writer.writerow(row)
    outcsv.close()



if __name__ == "__main__":
    KORPUS = "Korpus_Sepulcrales"
    main()