#Generation der Tabelle BieziehungsListen.xslx, die alle Inschriften nach Beziehungstyp verzeichnet

import pickle, pandas

global KORPUS
global SUCHTABELLE

def main():
    global KORPUS
    global SUCHTABELLE
    impframe = pandas.read_csv('./EDCS-Tabellen/'+SUCHTABELLE+'.csv', low_memory=False)
    impframe.index = impframe['ID'].to_list()
    dframes = {}
    beziehungen = {}
    with open ("./Kerndaten/"+KORPUS+"_BeziehungenStatsDict", "rb") as infile:
        beziehungen=pickle.load(infile)
    superlative = {'pientissimus' : 'pius', 'obsequentissimus' :'obsequor', 'carissimus' : 'carus', 'innocentissimus' : 'innocens', 'praestantissimus' : 'praesto', 'dignissimus' : 'dignus', 'fidelissimus' : 'fidelis', "mero" : "mereo"}
    for bsearch in beziehungen:
        framedict = {"ID" : [], "Zuschreibung" : [], "Geschlecht" : [], "Inschrift" : [], "Token" : []}
        for t in beziehungen[bsearch][2]:
                if t[0] in impframe.index:
                    framedict["ID"].append(t[0])
                    framedict["Geschlecht"].append(t[1])
                    if t[2] in superlative:
                        framedict["Zuschreibung"].append(superlative[t[2]])
                    else:
                        framedict["Zuschreibung"].append(t[2])
                    framedict['Inschrift'].append(impframe.loc[t[0], 'Text'])
                    framedict['Token'].append(t[3])
        df = pandas.DataFrame(framedict)
        dframes[bsearch] = df
    with pandas.ExcelWriter("./Kerntabellen/"+KORPUS+"_BeziehungsListen.xlsx") as writer:
        for d in dframes:
            dframes[d].to_excel(writer, sheet_name=d, index=False)

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    SUCHTABELLE ="searchresult"
    main()