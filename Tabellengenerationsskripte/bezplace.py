#Generiert Tabelle mit den Beziehungstypen für pius nach Provinz

import pandas

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
        catsdic[sheet] = {'Hispania citerior': 0, 'Roma': 0, 'Venetia et Histria / Regio X': 0, 'Apulia et Calabria / Regio II': 0, 'Transpadana / Regio XI': 0, 'Lusitania': 0, 'Latium et Campania / Regio I': 0, 'Umbria / Regio VI': 0, 'Samnium / Regio IV': 0, 'Gallia Narbonensis': 0, 'Dalmatia': 0, 'Aquitani(c)a': 0, 'Lugudunensis': 0, 'Germania superior': 0, 'Moesia superior': 0, 'Dacia': 0, 'Bruttium et Lucania / Regio III': 0, 'Noricum': 0, 'Picenum / Regio V': 0, 'Aemilia / Regio VIII': 0, 'Numidia': 0, 'Mauretania Caesariensis': 0, 'Raetia': 0, 'Moesia inferior': 0, 'Pannonia inferior': 0, 'Baetica': 0, 'Sicilia': 0, 'Sardinia': 0, 'Liguria / Regio IX': 0, 'Pannonia superior': 0, 'Germania inferior': 0, 'Alpes Maritimae': 0, 'Britannia': 0, 'Mauretania Tingitana': 0, 'Etruria / Regio VII': 0, 'Africa proconsularis': 0, 'Macedonia': 0, 'Alpes Cottiae': 0, 'Cappadocia': 0, 'Provincia incerta': 0, 'Corsica': 0, 'Asia': 0, 'Arabia': 0, 'Thracia': 0, 'Italia': 0, 'Belgica | Germania superior': 0, 'Palaestina': 0, 'Galatia': 0, 'Barbaricum': 0, 'Alpes Poeninae': 0, 'Belgica': 0, 'Achaia': 0, 'Pontus et Bithynia': 0, 'Aegyptus': 0, 'Syria': 0, 'Alpes Graiae': 0, 'Lycia et Pamphylia': 0, 'Regnum Bospori': 0, 'Cyprus': 0, 'Cilicia': 0}
        for i, row in sheets[sheet].iterrows():
            if row.loc['Zuschreibung'] == 'pius':
                cats = str(sframe.loc[row.loc['ID']]['Provinz'])
                catsdic[sheet][cats]+=1
    df = pandas.DataFrame(catsdic).T
    df.to_csv('./Ausgabetabellen/'+KORPUS+'_piusbez.csv', index=True, quoting=1)

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    SUCHTABELLE ="searchresult"
    main()