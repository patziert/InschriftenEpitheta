#Generiert Tabellen zur Entwicklung der Zuschreibungen über 50-Jahre-Schritte nach Geschlechtern getrennt und zur Entwicklung des Geschlechterverhältnisses

import pandas
global KORPUS
global SUCHTABELLE

def main():
    global KORPUS
    global SUCHTABELLE
    sframe = pandas.read_csv('./EDCS-Tabellen/'+SUCHTABELLE+'.csv', low_memory=False)
    sframe.index = sframe['ID'].to_list()
    sheets = pandas.read_excel('./Kerntabellen/'+KORPUS+'_ZuschreibungsListen.xlsx', sheet_name=None)
    catsm = {'0': 0, '50' : 0, '100' : 0, '150' : 0, '200' : 0, '250' :0}
    catsf = {'0': 0, '50' : 0, '100' : 0, '150' : 0, '200' : 0, '250' :0}
    catsm2 = {'0': 0, '50' : 0, '100' : 0, '150' : 0, '200' : 0, '250' :0}
    catsf2 = {'0': 0, '50' : 0, '100' : 0, '150' : 0, '200' : 0, '250' :0}
    undatiertm = 0
    undatiertf = 0
    catsmdic = {}
    catsfdic = {}
    catsvdic = {}
    for sheet in sheets:
        catsmdic[sheet] = {'0': 0, '50' : 0, '100' : 0, '150' : 0, '200' : 0, '250' :0, 'undatiert' : 0}
        catsfdic[sheet] = {'0': 0, '50' : 0, '100' : 0, '150' : 0, '200' : 0, '250' :0, 'undatiert' : 0}
        catsvdic[sheet] = {'0': 0, '50' : 0, '100' : 0, '150' : 0, '200' : 0, '250' :0, 'undatiert' : 0}
        for i, row in sheets[sheet].iterrows():
            try:
                von = int(sframe.loc[row.loc['ID']]['Datum von'])
                bis = sframe.loc[row.loc['ID']]['Datum bis']
                bis = int(bis.replace(';', ''))
                median = von+bis/2
                for d in catsm:
                    if von<=int(d)+49 and bis >=int(d):
                        if row.loc['Geschlecht'] == '[masculine]' or row.loc['Geschlecht'] == 'masculine':
                            catsm[d]+=1
                        if row.loc['Geschlecht'] == '[feminine]' or row.loc['Geschlecht'] == 'feminine':
                            catsf[d]+=1
                    if median<int(d)+50 and median>=int(d):
                        if row.loc['Geschlecht'] == '[masculine]' or row.loc['Geschlecht'] == 'masculine':
                            catsmdic[sheet][d]+=1
                            catsm2[d]+=1
                        if row.loc['Geschlecht'] == '[feminine]' or row.loc['Geschlecht'] == 'feminine':
                            catsfdic[sheet][d]+=1
                            catsf2[d]+=1
            except:
                if row.loc['Geschlecht'] == '[masculine]' or row.loc['Geschlecht'] == 'masculine':
                        undatiertm+=1
                        catsmdic[sheet]['undatiert']+=1
                if row.loc['Geschlecht'] == '[feminine]' or row.loc['Geschlecht'] == 'feminine':
                        undatiertf+=1
                        catsfdic[sheet]['undatiert']+=1
        for v in catsvdic[sheet]:
            try:
                catsvdic[sheet][v] = catsfdic[sheet][v]/catsmdic[sheet][v]
                catsvdic[sheet][v] = format(catsvdic[sheet][v], ".2f")
            except:
                catsvdic[sheet][v] = 'NaN'
    dfm = pandas.DataFrame(catsmdic).T
    dff = pandas.DataFrame(catsfdic).T
    dfv = pandas.DataFrame(catsvdic).T
    dfm.to_csv('./Ausgabetabellen/'+KORPUS+'dfm.csv', index=True, quoting=1)
    dff.to_csv('./Ausgabetabellen/'+KORPUS+'dff.csv', index=True, quoting=1)
    dfv.to_csv('./Ausgabetabellen/'+KORPUS+'dfv.csv', index=True, quoting=1)
    print('Männlich Überlappung: '+str(catsm))
    print('Weiblich Überlappung: '+str(catsf))
    print('Männlich Mittelwert: '+str(catsm2))
    print('Weiblich Mittelwert: '+str(catsf2))
    print('Männlich Undatiert: '+str(undatiertm))
    print('Weiblich Undatiert: '+str(undatiertf))
    
if __name__ == "__main__":
    KORPUS = "Korpus_Varia"
    SUCHTABELLE ="searchresultWeitere"
    main()