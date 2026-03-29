#Generation der Tabelle BeziehungenZuschreibungen.csv, die Trefferzahlen zwischen Beziehungen und Zuschreibungen anzeigt

import pickle, pandas

global KORPUS

def main():
    global KORPUS
    beziehungen = {}
    with open ("./Kerndaten/"+KORPUS+"_BeziehungenStatsDict", "rb") as infile:
        beziehungen=pickle.load(infile)
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
        df.at['Gesamt', bez] = beziehungen[bez][0]
        for zus in beziehungen[bez][1]:
            df.at[zus, bez] = int(beziehungen[bez][1][zus][0])
    df['Gesamt'] = df.sum(axis=1, numeric_only=True)
    csv = df.to_csv()
    outfile = open("./Ausgabetabellen/"+KORPUS+"_BeziehungenZuschreibungen.csv", "w", encoding='UTF-8', newline='')
    outfile.write(csv)
    outfile.close()

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    main()