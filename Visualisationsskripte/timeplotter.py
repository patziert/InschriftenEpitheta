import matplotlib, pandas
import matplotlib.pyplot as plt

sframe = pandas.read_csv('/EDCS-Tabellen/searchresult.csv', low_memory=False)
sframe.index = sframe['ID'].to_list()
sheets = pandas.read_excel('./Kerntabellen/ZuschreibungsListen.xlsx', sheet_name=None)
catsm = {'0': 0, '50' : 0, '100' : 0, '150' : 0, '200' : 0, '250' :0}
catsf = {'0': 0, '50' : 0, '100' : 0, '150' : 0, '200' : 0, '250' :0}
catsm2 = {'0': 0, '50' : 0, '100' : 0, '150' : 0, '200' : 0, '250' :0}
catsf2 = {'0': 0, '50' : 0, '100' : 0, '150' : 0, '200' : 0, '250' :0}
undatiertm = 0
undatiertf = 0
for i, row in sheets['pius'].iterrows():
    try:
        von = sframe.loc[row.loc['ID']]['Datum von']
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
                    catsm2[d]+=1
                if row.loc['Geschlecht'] == '[feminine]' or row.loc['Geschlecht'] == 'feminine':
                    catsf2[d]+=1
    except:
        if row.loc['Geschlecht'] == '[masculine]' or row.loc['Geschlecht'] == 'masculine':
                undatiertm+=1
        if row.loc['Geschlecht'] == '[feminine]' or row.loc['Geschlecht'] == 'feminine':
                undatiertf+=1
catsmlist = []
catsflist = []
catsmlist2 = []
catsflist2 = []
for e in catsm:
    catsmlist.append(catsm[e])
    catsflist.append(catsf[e])
    catsmlist2.append(catsm2[e])
    catsflist2.append(catsf2[e])
periode = ['0-49', '50-99', '100-149', '150-199', '200-249', 'ab 250']
df = pandas.DataFrame ({
    'Männer' : catsmlist,
    'Frauen' : catsflist,
    'Periode' : periode
})
df2 = df = pandas.DataFrame ({
    'Männer' : catsmlist2,
    'Frauen' : catsflist2,
    'Periode' : periode
})
#df.plot(x='Periode', y=['Männer', 'Frauen'], kind = 'bar', color=['blue', 'red'])
df2.plot(x='Periode', y=['Männer', 'Frauen'], kind = 'bar', color=['blue', 'red'])
#plt.title("Zuschreibung \"pius\" nach Überschneidung der Datierungsperiode")
plt.title("Zuschreibung \"pius\" nach Median der Datierungsperiode")
plt.show()
