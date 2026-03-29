#Ermittlung der Beziehungsformen und Personen von denen die Zuschreibungen abhängig sind und Sammlung der zugehörigen Statistiken

import pandas, pickle

global KORPUS

#Rekonstruktion eines Satzes aus seinen Einzeltoken
def getSentence(words):
    sentence=""
    for word in words:
        sentence+=word.string+" "
    return sentence

def main():
    #Initialisiere Variabeln und etrahiere IDs aus vorherigen Suchergebnissen
    global KORPUS
    df = pandas.read_csv('./Kerntabellen/'+KORPUS+'_adjsearch.csv', low_memory=False)
    df2 = pandas.read_csv('./Kerntabellen/'+KORPUS+'_participlesearch.csv', low_memory=False)
    ids =df['ID'].tolist()
    ids2 =df2['ID'].tolist()
    print(ids2)
    ids.extend(ids2)
    pos = ''
    pos2 = ''
    pos3 = ''
    bcount = 0 #Beziehungszähler
    ecount = 0 #Named Enitity - Zähler
    excount = 0 #Exceptionzähler
    earlyentcount = 0 #Zähler für Entities, die vor einem Beziehungswort in der Hierarchie auftreten
    notperscount = 0
    notpers = []
    earlyents = []
    entlist = []
    nents = [0, {}, []] #[Trefferzähler, Zuschreibungsdictionary, Trefferliste]
    beziehungen = {'mater' : 0, 'pater' : 0, 'frater' : 0, 'soror' : 0, 'noverca' : 0, 'privignus' : 0, 'amita' :0, 
                'matertera' : 0, 'nurrus' : 0, 'filius' : 0, 'filia' : 0, 'avia' : 0, 'avus' : 0, 'avunculus' :0, 
                'patruus' : 0, 'gener' : 0, 'nurus' : 0, 'uxor' : 0, 'maritus' : 0, 'coniux' : 0, 'coniunx' :0, 
                'concubinus' : 0, 'contubernalis' : 0, 'parens' : 0, 'socer' : 0, 'conubium' : 0, 'matrimonium' :0}
    for bez in beziehungen:
        beziehungen[bez]=[0, {}, []] #[Trefferzähler, Zuschreibungsdictionary, Trefferliste]
    #Laden der Positionsdaten
    with open ("./Kerndaten/"+KORPUS+"_adjPositions", "rb") as infile:
        pos=pickle.load(infile)
        print(pos)
    with open ("./Kerndaten/"+KORPUS+"_participlePositions", "rb") as infile:
        pos2=pickle.load(infile)
        print(pos2)
    pos.extend(pos2)
    #Dependencysuche, Iteration auf IDs der Fundlisten und den zugehörigen Positionslisten
    for id, p in zip(ids, pos):
        print(p)
        words = []
        #Iteriere auf Positionsliste mit l als Zähler
        for l, (o) in enumerate (p):
            print(l)
            #Lade Wörter und Ancestors zur Fundinschrift
            with open ("./"+KORPUS+"/"+p[l][0]+"/"+p[l][0]+"_words", "rb") as infile:
                words=pickle.load(infile)
            print(getSentence(words))
            with open ("./"+KORPUS+"/"+p[l][0]+"/"+p[l][0]+"_ancestors", "rb") as infile:
                ancs=pickle.load(infile)
                print(ancs[p[l][1]])
                find = False
                efind = False
                enttemp = ""
                #Iteriere über die Ancestors zum Treffertoken anhand seiner Position im Satz nach Positionsliste
                for a in ancs[p[l][1]]: #Erster Index in p: Aktuelle Positionsliste, Zweiter Index: Zugriffe auf den zur Position abgespeicherten Daten (siehe AdjStat.py)
                    print(a)
                    gender = ''
                    #Extrahiere, falls vorhanden, das Geschlecht des aktuellen Ancestors nach SEINER Satzposition 'i'      
                    try:
                        gender=words[a['i']].features['Gender']  
                        print(gender)
                    except:
                        pass
                    #Iteriere über und prüfe alle Beziehungswörter
                    for b in beziehungen:
                        if a['lemma']==b:
                            #Ist das Lemma coniunx, verwende Geschlecht der Zuschreibung statt des Beziehungswortes
                            if a['lemma']=='coniunx':
                                gender = p[l][3]
                            beziehungen[b][0]+=1 #Erhöhe Trefferzähler für Beziehungswort
                            if p[l][2] in beziehungen[b][1]: #Prüfe ob Zuschreibung diesem Beziehungswort bereits zugeordnet wurde
                                beziehungen[b][1][p[l][2]][0]+=1 #Erhöhe Trefferzähler für Zuschreibung in Bezug auf Beziehungswort
                                try:
                                    beziehungen[b][1][p[l][2]][1][str(gender[0])][0]+=1 #Erhöhe Trefferzähler für Geschlecht in Bezug auf Zuschreibung in Bezug auf Beziehungswort
                                    beziehungen[b][1][p[l][2]][1][str(gender[0])][1].append(p[l][0]) #Ordne Inschriften ID dem Geschlecht in Bezug auf Zuschreibung in Bezug auf Beieziehungswort zu (Einfügen in Liste)
                                    beziehungen[b][1][p[l][2]][2].append(p[l][0]) #Ordne Inschriften ID der Zuschreibung in Bezug auf Beziehungswort zu (Einfügen in Liste)
                                except:
                                    pass
                            else:
                                beziehungen[b][1][p[l][2]]=[1, {'masculine' : [0, []], 'feminine' : [0, []], 'neuter' : [0, []]}, []] #Initialisiere Zuschreibung in Dictionary des Beziehungswortes mit Geschlechterdictionary und Trefferzähler auf 1                            
                                try:
                                    #Das Selbe wie Zeile 86-88
                                    beziehungen[b][1][p[l][2]][1][str(gender[0])][0]+=1
                                    beziehungen[b][1][p[l][2]][1][str(gender[0])][1].append(p[l][0])
                                    beziehungen[b][1][p[l][2]][2].append(p[l][0])
                                except:
                                    pass
                            beziehungen[b][2].append([p[l][0], gender, p[l][2], a['text']]) #Füge Tupel aus EDCS-ID, Geschlecht, Zuschreibung und Ancestor als Repräsentation des Treffers in Trefferliste des Beziehungswortes ein
                            bcount+=1
                            find=True
                    #Wenn an dieser Stelle noch kein Beziehungswort oder Named Entity gefunden wurde, prüfe auf Named Entities
                    if find == False and efind == False:
                        with open ("./"+KORPUS+"/"+p[l][0]+"/"+p[l][0]+"_ents", "rb") as entfile:
                                    ents=pickle.load(entfile)
                                    try:
                                        #Iteriere über Named Entities der Inschrift und prüfe Identität mit aktuellem Lemma
                                        for e in ents:
                                            if e[0]==a['text'] or e[0]==a['lemma']:
                                                print(e[0])
                                                entlist.append(e) #Notiere Entity in Liste bei Treffer
                                                ecount+=1
                                                efind=True
                                                enttemp = [gender, e] #Zwischenspeicher von Entity und Geschlecht bei Treffer
                                                break
                                    except:
                                        excount+=1
                                        pass
                    #Notiere frühe Entities, die vor dem Beziehungswort in der Ahnenliste auftreten (eher selten)
                    if find:
                        if efind:
                            earlyentcount+=1
                            earlyents.append(p[l][2])
                            earlyents.append(getSentence(words))
                            earlyents.append(ancs[p[l][1]])
                        break #Überspringe reguläre Registrierung der Named Entities, falls ein Beziehungswort gefunden werden konnte
                #Wurde kein Beziehungswort gefunden, aber eine Named Entity, prüfe die zwischengespeicherte Entity auf den Typ Person               
                if efind and enttemp[1][3] == 'PERSON':
                    nents[0]+=1 #Erhöher Trefferzähler für Named Entities
                    if p[l][2] in nents[1]: #Prüfe ob Zuschreibung bereits mit Named Entity verzeichnet wurde
                        nents[1][p[l][2]][0]+=1 #Erhöhe Trefferzähler der Zuschreibung
                        try:
                            nents[1][p[l][2]][1][str(enttemp[0][0])][0]+=1 #Erhöhe Trefferzähler für Geschlecht bei Named Entities in Bezug auf Zuschreibung
                            nents[1][p[l][2]][1][str(enttemp[0][0])][1].append([p[l][0], enttemp[1]]) #Füge Named Entity der Trefferliste für Geschlecht hinzu
                            nents[1][p[l][2]][2].append([p[l][0], enttemp[1]]) #Füge Named Entity der Trefferliste für Zuschreibung hinzu
                        except:
                            pass
                    #Initialisier Zuschreibung in Named Entities, dann wie oben
                    else:
                        nents[1][p[l][2]]=[1, {'masculine' : [0, []], 'feminine' : [0, []], 'neuter' : [0, []]}, []]
                        try:
                            nents[1][p[l][2]][1][str(enttemp[0][0])][0]+=1
                            nents[1][p[l][2]][1][str(enttemp[0][0])][1].append([p[l][0], enttemp[1]])
                            nents[1][p[l][2]][2].append([p[l][0]])
                        except:
                            pass
                    #Füge Innschrift der Trefferliste hinzu, vgl. Zeile 100
                    nents[2].append([[p[l][0], enttemp[1]], str(enttemp[0]), p[l][2]])
    #Erstelle Geschlechter-Gesamtstatistik für Named Entities aus obiger Sammlung 
    nentgen = {'masculine' : [0, {}, []], 'feminine' : [0, {}, []], 'neuter' : [0, {}, []]}
    genrenames = {'masculine' : 'Person M', "feminine" : "Person W", "neuter" : "Person N"}
    for n in nents[1]:
        for g in nents[1][n][1]:
            for i in nents[1][n][1][g][1]:
                nentgen[g][0]+=1
                if n in nentgen[g][1]:
                    nentgen[g][1][n][0]+=1
                else:
                    nentgen[g][1][n]=[1, {'masculine' : [0, []], 'feminine' : [0, []], 'neuter' : [0, []]}, []]
                nentgen[g][1][n][1][g][0]+=1
                nentgen[g][1][n][1][g][1].append(i[0])
                nentgen[g][1][n][2].append(i[0])
                nentgen[g][2].append([i[0], g, n, i[1][0]])
    #Bennene Geschlechter in Ausgabeschema um und füge sie den Beziehungen hinzu
    for r in genrenames:
        nentgen[genrenames[r]] = nentgen.pop(r)
    beziehungen.update(nentgen)
    #Output
    with open ("./Kerndaten/"+KORPUS+"_BeziehungenStatsDict", "wb") as outfile:
        pickle.dump(beziehungen, outfile)


if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    main()