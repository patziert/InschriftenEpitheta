#Zählt Gesamtmengen der jeweiligen Geschlechter unter den Funden

import pandas
global KORPUS

def main():
    global KORPUS
    sheets = pandas.read_excel('./Kerntabellen/'+KORPUS+'_ZuschreibungsListen.xlsx', sheet_name=None)
    mcount = 0
    fcount = 0
    ncount = 0
    for sheet in sheets:
        for i, row in sheets[sheet].iterrows():
            if row.loc['Geschlecht'] == '[masculine]':
                mcount+=1
            if row.loc['Geschlecht'] == '[feminine]':
                fcount+=1
            if row.loc['Geschlecht'] == '[neuter]':
                ncount+=1
    print('Gesamtzahl männlich: '+str(mcount))
    print('Gesamtzahl weiblich: '+str(fcount))
    print('Gesamtzahl neutral: '+str(ncount))

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    main()