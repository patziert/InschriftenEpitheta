#Zählt Gesamtmengen der jeweiligen Geschlechter unter den Funden für das Beziehungswort coniunx

import pandas

global KORPUS

def main():
    global KORPUS
    sheets = pandas.read_excel('./Kerntabellen/'+KORPUS+'_BeziehungsListen.xlsx', sheet_name=None)
    mcount = 0
    fcount = 0
    ncount = 0
    for i, row in sheets['coniunx'].iterrows():
        if row.loc['Geschlecht'] == '[masculine]':
            mcount+=1
        if row.loc['Geschlecht'] == '[feminine]':
            fcount+=1
        if row.loc['Geschlecht'] == '[neuter]':
            ncount+=1
    print('coniunx männlich: '+str(mcount))
    print('coniunx weiblich: '+str(fcount))
    print('coniunx neutral: '+str(ncount))

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    main()