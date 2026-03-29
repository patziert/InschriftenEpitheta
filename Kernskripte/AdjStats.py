#Suche nach adjektivischen Zuschreibungen und Zwischenspeicherung derer Position in den Inschriften 
#und morphologischer Schlüsseinformationen


import glob, re, pickle

global KORPUS

def main():
    #Initialisierung der Zuschreibungen
    global KORPUS
    dlist = glob.glob("./"+KORPUS+"/*")
    zfinds = []
    zcount = {}
    zuschreibungen = ['incomparabilis', 'pius', 'dulcis', 'carus', 'pudens', 'impudens',
                    'castus', 'rarus', 'felix', 'clarus', 'fortis', 'honestus', 'sollicitus', 'securus', 'anxius', 'beatus',
                    'laetus', 'fidus', 'placidus', 'clemens', 'integer', 'prudens', 'amabilis', 'probus', 'frugi', 'pulcher',
                    'lepidus', 'bonus', 'sapiens', 'dignus', 'suavis', 'simplex',
                    'iucundus', 'sanctus', 'moderatus', 'amans', 'probatus', 'merens', 'adfectus', 'natus', 'desertus',
                    'studiosus', 'miser', 'mellitus', 'tristis', 'modestus', 'simplex', 'iucundus', 'innocens', 
                    'indulgentus', 'fidelis']
    superlative = {'pientissimus' : 'pius', 'carissimus' : 'carus', 'optimus' : 'bonus', 'innocentissimus' : 'innocens',
                   'fidelissimus' : 'fidelis', 'dignissimus' : 'dignus', 'dulcissimus' : 'dulcis', 'rarissimus' : 'rarus',
                   'fortissimus' : 'fortis', 'clementissimus' : 'clemens', 'amantissimus' : 'amans', 
                   'simplicissimus' : 'simplex', 'sanctissimus' : 'sanctus'}
    for zs in zuschreibungen:
        zcount[zs]=0
    positionslist = []
    #Iteration aller Inschriften im Korpus
    for d in dlist:
        id = re.sub(r'./'+KORPUS+r'\\', "", d)
        hasz = False
        positions = []
        with open (d+"/"+id+"_lemmata", "rb") as infile:
            lemmata = pickle.load(infile)
            with open (d+"/"+id+"_words", "rb") as infile2:
                words = pickle.load(infile2)
                #Iteration aller Token in der jeweiligen Inschrift
                for i, (l, w) in enumerate(zip(lemmata, words)):
                    xpos = ""
                    upos = ""
                    pos = ""
                    #Extraktion von Position, POS-Tag und Geschlecht des jewiligen Tokens
                    try:
                        xpos = str(w.xpos)
                        upos = str(w.upos)
                        pos = str(w.pos)
                        gender = str(w.features['Gender'])
                    except:
                        continue
                    #Prüfe auf Superlativ, tausche gegebenenfalls Lemma aus
                    for s in superlative:
                        if l==s:
                            l=superlative[s]
                    #Prüfe ob Zuschreibung gefunden wurde und ob diese ein Adjektiv ist
                    for z in zuschreibungen:
                        if l==z:
                            if xpos == 'adjective' or upos == 'ADJ' or pos == 'adjective':
                                if xpos != 'adjective': print (l+" !xpos "+id)
                                if upos != 'ADJ': print (l+" !upos "+id)
                                if pos != 'adjective': print (l+" !pos "+id)
                                hasz = True #Die Inschrift enthält mindestens eine Zuschreibung
                                zcount[z]+=1 #Erhöhe Fundzahl für Zuschreibung
                                positions.append([id, i, l, gender]) #Notiere ID, Position im Text, Lemma und Geschlecht der Zuschreibung
        #Wenn Inschrift mindestens eine Zuschreibung hat, notiere Liste aller Funde in der Inschrift in Positionsliste und ID in zfinds
        if hasz:
            zfinds.append(id)
            positionslist.append(positions)
    #Speichere Liste aller IDs mit Funden
    with open ("./Kerndaten/"+KORPUS+"_adjOutput.txt", "w", encoding="UTF-8") as outfile:
        for i in zfinds:
            outfile.write(i+"\n")
    #Speichere Positionsliste
    with open ("./Kerndaten/"+KORPUS+"_adjPositions", "wb") as outfile:
        pickle.dump(positionslist, outfile)
    print(zcount)

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    main()