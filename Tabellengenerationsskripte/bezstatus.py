#Generiert Tabelle zu pius nach Beziehungstyp und Statusgruppe

import pandas, re

global KORPUS
global SUCHTABELLE

def main():
    global KORPUS
    global SUCHTABELLE
    sframe = pandas.read_csv('./EDCS-Tabellen/'+SUCHTABELLE+'.csv', low_memory=False)
    sframe.index = sframe['ID'].to_list()
    sheets = pandas.read_excel('./Kerntabellen/'+KORPUS+'_BeziehungsListen.xlsx', sheet_name=None)
    catsdic = {}
    for sheet in sheets:
        catsdic[sheet] = {'milites' : 0, 'liberti/libertae' : 0, 'servi/servae' : 0, 'sacerdotes pagani' : 0, "ordo decurionum" : 0,
        "ordo equester" : 0, 'ordo senatorius' : 0}
        for i, row in sheets[sheet].iterrows():
            if row.loc['Zuschreibung'] == 'pius':
                cats = str(sframe.loc[row.loc['ID']]['Personenstatus / Inschriftengattung'])
                cats = re.split(";\s\s", cats)
                for c in cats:
                    if c in catsdic[sheet]:
                        catsdic[sheet][c]+=1
    df = pandas.DataFrame(catsdic).T
    df.to_csv('./Ausgabetabellen/'+KORPUS+'_piusbezstatus.csv', index=True, quoting=1)

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    SUCHTABELLE ="searchresult"
    main()