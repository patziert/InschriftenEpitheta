#Generation der Tabelle BeziehungenZuschreibungen.csv, die Trefferzahlen zwischen Beziehungen und Zuschreibungen für Rom anzeigt

import pickle, pandas

global KORPUS
global SUCHTABELLE

def main():
    global KORPUS
    global SUCHTABELLE
    beziehungen = pandas.read_excel('./Kerntabellen/'+KORPUS+"_BeziehungsListen.xlsx", sheet_name=None)
    sframe = pandas.read_csv('./EDCS-Tabellen/'+SUCHTABELLE+'.csv', low_memory=False)
    sframe.index = sframe['ID'].to_list()
    colnames = []
    rownames = []
    for bez in beziehungen:
        colnames.append(bez)
    rownames = ['incomparabilis', 'pius', 'dulcis', 'carus', 'pudens', 'impudens',
                    'castus', 'rarus', 'felix', 'clarus', 'fortis', 'honestus', 'sollicitus', 'securus', 'anxius', 'beatus',
                    'laetus', 'fidus', 'placidus', 'clemens', 'integer', 'prudens', 'amabilis', 'probus', 'frugi', 'pulcher',
                    'lepidus', 'bonus', 'sapiens', 'dignus', 'suavis', 'simplex',
                    'iucundus', 'sanctus', 'moderatus', 'amans', 'probatus', 'merens', 'adfectus', 'natus', 'desertus',
                    'studiosus', 'miser', 'mellitus', 'tristis', 'modestus', 'simplex', 'iucundus', 'innocens', 
                    'indulgentus', 'fidelis', 'moderatus', 'amo', 'probo', 'doleo', 'mereo', 'afficio', 'nascor', 'desero', 'obsequor', 'pudens', 
                    'sapiens', 'sanctus', 'praesto', 'mero']
    rownames.append("Gesamt")
    df = pandas.DataFrame(0, index=rownames, columns=colnames)
    for bez in beziehungen:
        bcount = 0
        for name in rownames:
            if name != 'Gesamt':
                zcount = 0
                for i, row in beziehungen[bez].iterrows():
                    if row.loc['Zuschreibung']==name:
                        id = row.loc['ID']
                        prov = str(sframe.loc[id]['Provinz'])
                        if prov == 'Roma':
                            zcount+=1
                            bcount+=1
                df.at[name, bez] = zcount
        df.at['Gesamt', bez] = bcount
    df['Gesamt'] = df.sum(axis=1, numeric_only=True)
    csv = df.to_csv()
    outfile = open("./Ausgabetabellen/"+KORPUS+"_BeziehungenZuschreibungenRom.csv", "w", encoding='UTF-8', newline='')
    outfile.write(csv)
    outfile.close()

if __name__ == "__main__":
    KORPUS = "Korpus_Sepulcrales"
    SUCHTABELLE = "searchresultSepulcralesReduziert"
    main()