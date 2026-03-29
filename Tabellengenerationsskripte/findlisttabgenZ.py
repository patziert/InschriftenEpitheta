#Generation der Tabelle ZuschreibungsListen.xslx, die alle Inschriften nach Beziehungstyp verzeichnet

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
        zlist = []
    for b in beziehungen:
        for z in beziehungen[b][1]:
            if z not in zlist:
                zlist.append(z)
    for z in zlist:
        framedict = {"ID" : [], "Zuschreibung" : [], "Geschlecht" : [], "Inschrift" : []}
        for b in beziehungen:
            for t in beziehungen[b][2]:
                if t[2]==z:
                    framedict["ID"].append(t[0])
                    framedict["Geschlecht"].append(t[1])
                    framedict["Zuschreibung"].append(t[2])
                    framedict['Inschrift'].append(impframe.loc[t[0], 'Text'])
        df = pandas.DataFrame(framedict)
        dframes[z] = df
    with pandas.ExcelWriter("./Kerntabellen/"+KORPUS+"_ZuschreibungsListen.xlsx") as writer:
        for d in dframes:
            dframes[d].to_excel(writer, sheet_name=d, index=False)

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    SUCHTABELLE ="searchresult"
    main()