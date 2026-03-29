#Genriert Tabelle mit Zuschreibungszahlen für coniunx nach Geschlecht getrennt

import pandas
global KORPUS

def main():
    global KORPUS
    sheets = pandas.read_excel('./Kerntabellen/'+KORPUS+'_BeziehungsListen.xlsx', sheet_name=None)
    blist = sheets['coniunx']
    condic = {}
    for i, row in blist.iterrows():
        if row.loc['Zuschreibung'] not in condic:
            condic[row.loc['Zuschreibung']] = {'[masculine]' : 0, '[feminine]' : 0, '[neuter]' : 0}
        condic[row.loc['Zuschreibung']][row.loc['Geschlecht']] +=1
    df = pandas.DataFrame(condic)
    df.to_csv('./Ausgabetabellen/'+KORPUS+'_coniunxG.csv', index = True, quoting = 1)

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    main()