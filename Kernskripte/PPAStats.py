#Suche nach partizipativen Zuschreibungen und Zwischenspeicherung derer Position in den Inschriften 
#und morphologischer Schlüsseinformationen

import glob, re, pickle

global KORPUS

def main():
    #Initialisierung der Zuschreibungen
    global KORPUS
    dlist = glob.glob("./"+KORPUS+"/*")
    zfinds = []
    zcount = {}
    positionslist = []
    zuschreibungen = ['moderatus', 'amo', 'probo', 'doleo', 'mereo', 'afficio', 'nascor', 'desero', 'obsequor', 'pudens', 
                    'sapiens', 'sanctus', 'praesto', 'mero']
    superlative = {'obsequentissimus' : 'obsequor', 'praestantissimus' : 'praesto'}
    for zs in zuschreibungen:
        zcount[zs]=0
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
                for i, (l, w) in enumerate (zip(lemmata, words)):
                    #Extraktion von Verbform, POS-Tag und Geschlecht des jewiligen Tokens
                    vf = ""
                    try:
                        vf = str(w.VerbForm)
                        gender = str(w.features['Gender'])
                        pos = str(w.pos)
                    except:
                        continue
                    #Prüfe auf Superlativ, tausche gegebenenfalls Lemma aus
                    for s in superlative:
                        if l==s:
                            l=superlative[s]
                    for z in zuschreibungen:
                        if l==z:
                            if vf == '[participle]' or pos =='adjective':
                                hasz = True #Die Inschrift enthält mindestens eine Zuschreibung
                                zcount[z]+=1 #Erhöhe Fundzahl für Zuschreibung
                                positions.append([id, i, l, gender]) #Notiere ID, Position im Text, Lemma und Geschlecht der Zuschreibung
        #Wenn Inschrift mindestens eine Zuschreibung hat, notiere Liste aller Funde in der Inschrift in Positionsliste und ID in zfinds
        if hasz:
            zfinds.append(id)
            positionslist.append(positions)
    #Speichere Liste aller IDs mit Funden
    with open ("./Kerndaten/"+KORPUS+"_participleOutput.txt", "w", encoding="UTF-8") as outfile:
        for i in zfinds:
            outfile.write(i+"\n")
    #Speichere Positionsliste
    with open ("./Kerndaten/"+KORPUS+"_participlePositions", "wb") as outfile:
        pickle.dump(positionslist, outfile)
    print(zcount)

if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    main()