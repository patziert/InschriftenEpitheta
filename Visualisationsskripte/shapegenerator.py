#Erschafft Shapefiles zur Verwendung mit einem Geoinformationssystem aus den Trefferinschriften

import shapefile, pandas

global KORPUS
global SUCHTABELLE

def main():
    global KORPUS
    global SUCHTABELLE
    sframe = pandas.read_csv('./EDCS-Tabellen/'+SUCHTABELLE+'.csv', low_memory=False)
    sframe.index = sframe['ID'].to_list()
    sheets = pandas.read_excel('./Kerntabellen/'+KORPUS+'_BeziehungsListen.xlsx', sheet_name=None)
    dflist = []
    for s in sheets:
        sheets[s]['Beziehung'] = s
        dflist.append(sheets[s])
    bframe = pandas.concat(dflist, ignore_index=True)
    sdata = {'Breite' : [], 'Länge' : [], 'Datum von' : [], 'Datum bis' : []}
    todelete = []
    for i, row in bframe.iterrows():
        try:
            for d in sdata:
                #sframe.loc[row.loc['ID']]['Datum von'] = sframe.loc[row.loc['ID']]['Datum von'].replace(';', '')
                bis = sframe.loc[row.loc['ID']]['Datum bis']
                bis = bis.replace(';', '')
                sframe.at[row.loc['ID'], 'Datum bis'] = bis
                sdata[d].append(sframe.loc[row.loc['ID'], d])
        except:
            todelete.append(int(i))
            continue
    for t in todelete:
        bframe.drop(t, axis=0, inplace=True)
    print(len(bframe))
    for sd in sdata:
        bframe[sd] = sdata[sd]
    bframe = bframe.reset_index(drop=True)
    shape = shapefile.Writer("./Visualisierungen/"+KORPUS+"_emoinscr")
    shape.field("EDCS_ID", "C")
    shape.field("Text", "C", size=255)
    shape.field("Zuschreibung", "C")
    shape.field("Beziehung", "C")
    shape.field("Geschlecht", "C")
    shape.field("Datum von", "N")
    shape.field("Datum bis", "N")
    for index, row in bframe.iterrows():
        if not pandas.isnull(row.loc['Breite']):
            shape.point(row.loc['Länge'], row.loc['Breite'])
            shape.record(row.loc['ID'], row.loc['Inschrift'], row.loc['Zuschreibung'], row.loc['Beziehung'], 
                        row.loc['Geschlecht'])
    shape.close()
    print(bframe)

if __name__ == "__main__":
    KORPUS = "Korpus_Sepulcrales"
    SUCHTABELLE ="searchresultSepulcralesReduziert"
    main()
        
