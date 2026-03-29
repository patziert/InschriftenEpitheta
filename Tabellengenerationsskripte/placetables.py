#Generiert Tabellen der Zuschreibungen nach Orten, sowie zum Anteilsverhältnis der Zuschreibungen im Vergleich zu Rom

import pandas, re

global KORPUS
global SUCHTABELLE

def main():
    global KORPUS
    global SUCHTABELLE
    sframe = pandas.read_csv('./EDCS-Tabellen/'+SUCHTABELLE+'.csv', low_memory=False)
    sframe.index = sframe['ID'].to_list()
    sheets = pandas.read_excel('./Kerntabellen/'+KORPUS+'_ZuschreibungsListen.xlsx', sheet_name=None)
    catsdic = {}
    basedic = {}
    #for sheet in sheets:
    #    for i, row in sheets[sheet].iterrows():
    #        basedic[str(sframe.loc[row.loc['ID']]['Provinz'])] = 0
    #    catsdic[sheet] = basedic
    #print(basedic)
    for sheet in sheets:
        catsdic[sheet] = {'Hispania citerior': 0, 'Roma': 0, 'Venetia et Histria / Regio X': 0, 'Apulia et Calabria / Regio II': 0, 'Transpadana / Regio XI': 0, 'Lusitania': 0, 'Latium et Campania / Regio I': 0, 'Umbria / Regio VI': 0, 'Samnium / Regio IV': 0, 'Gallia Narbonensis': 0, 'Dalmatia': 0, 'Aquitani(c)a': 0, 'Lugudunensis': 0, 'Germania superior': 0, 'Moesia superior': 0, 'Dacia': 0, 'Bruttium et Lucania / Regio III': 0, 'Noricum': 0, 'Picenum / Regio V': 0, 'Aemilia / Regio VIII': 0, 'Numidia': 0, 'Mauretania Caesariensis': 0, 'Raetia': 0, 'Moesia inferior': 0, 'Pannonia inferior': 0, 'Baetica': 0, 'Sicilia': 0, 'Sardinia': 0, 'Liguria / Regio IX': 0, 'Pannonia superior': 0, 'Germania inferior': 0, 'Alpes Maritimae': 0, 'Britannia': 0, 'Mauretania Tingitana': 0, 'Etruria / Regio VII': 0, 'Africa proconsularis': 0, 'Macedonia': 0, 'Alpes Cottiae': 0, 'Cappadocia': 0, 'Provincia incerta': 0, 'Corsica': 0, 'Asia': 0, 'Arabia': 0, 'Thracia': 0, 'Italia': 0, 'Belgica | Germania superior': 0, 'Palaestina': 0, 'Galatia': 0, 'Barbaricum': 0, 'Alpes Poeninae': 0, 'Belgica': 0, 'Achaia': 0, 'Pontus et Bithynia': 0, 'Aegyptus': 0, 'Syria': 0, 'Alpes Graiae': 0, 'Lycia et Pamphylia': 0, 'Regnum Bospori': 0, 'Cyprus': 0, 'Cilicia': 0}
    catsdic['Gesamt'] = {'Hispania citerior': 0, 'Roma': 0, 'Venetia et Histria / Regio X': 0, 'Apulia et Calabria / Regio II': 0, 'Transpadana / Regio XI': 0, 'Lusitania': 0, 'Latium et Campania / Regio I': 0, 'Umbria / Regio VI': 0, 'Samnium / Regio IV': 0, 'Gallia Narbonensis': 0, 'Dalmatia': 0, 'Aquitani(c)a': 0, 'Lugudunensis': 0, 'Germania superior': 0, 'Moesia superior': 0, 'Dacia': 0, 'Bruttium et Lucania / Regio III': 0, 'Noricum': 0, 'Picenum / Regio V': 0, 'Aemilia / Regio VIII': 0, 'Numidia': 0, 'Mauretania Caesariensis': 0, 'Raetia': 0, 'Moesia inferior': 0, 'Pannonia inferior': 0, 'Baetica': 0, 'Sicilia': 0, 'Sardinia': 0, 'Liguria / Regio IX': 0, 'Pannonia superior': 0, 'Germania inferior': 0, 'Alpes Maritimae': 0, 'Britannia': 0, 'Mauretania Tingitana': 0, 'Etruria / Regio VII': 0, 'Africa proconsularis': 0, 'Macedonia': 0, 'Alpes Cottiae': 0, 'Cappadocia': 0, 'Provincia incerta': 0, 'Corsica': 0, 'Asia': 0, 'Arabia': 0, 'Thracia': 0, 'Italia': 0, 'Belgica | Germania superior': 0, 'Palaestina': 0, 'Galatia': 0, 'Barbaricum': 0, 'Alpes Poeninae': 0, 'Belgica': 0, 'Achaia': 0, 'Pontus et Bithynia': 0, 'Aegyptus': 0, 'Syria': 0, 'Alpes Graiae': 0, 'Lycia et Pamphylia': 0, 'Regnum Bospori': 0, 'Cyprus': 0, 'Cilicia': 0}
    for sheet in sheets:
        for i, row in sheets[sheet].iterrows():
            cats = str(sframe.loc[row.loc['ID']]['Provinz'])
            catsdic[sheet][cats]+=1
            catsdic['Gesamt'][cats]+=1
    quotadic = {}
    for sheet in catsdic:
        quotadic[sheet] = dict(catsdic[sheet])
    for sheet in catsdic:
        for place in quotadic[sheet]:
            try:
                quotadic[sheet][place] = quotadic[sheet][place]/quotadic['Gesamt'][place]
            except:
                continue
    for sheet in quotadic:
        for place in quotadic[sheet]:
            if not place == 'Roma':
                try:
                    quotadic[sheet][place] = format(quotadic[sheet][place]/quotadic[sheet]['Roma'], ".2f")
                except:
                    quotadic[sheet][place] = None
        try:
            quotadic[sheet]['Roma'] = format(quotadic[sheet]['Roma']/quotadic[sheet]['Roma'], ".2f")
        except:
            quotadic[sheet]['Roma'] = None
    df = pandas.DataFrame(catsdic).T
    df2 = pandas.DataFrame(quotadic).T
    df.to_csv('./Ausgabetabellen/'+KORPUS+'_provinzen.csv', index=True, quoting=1)
    df2.to_csv('./Ausgabetabellen/'+KORPUS+'_provquotas.csv', index=True, quoting=1)

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    SUCHTABELLE ="searchresult"
    main()