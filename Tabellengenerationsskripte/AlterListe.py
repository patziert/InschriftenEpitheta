#Generiert Tabelle mit Altersangaben auf Grabsteinen nach Provinz

import pickle, glob, re, roman, pandas

global KORPUS
global SUCHTABELLE

def main():
    global KORPUS
    global SUCHTABELLE
    dlist = glob.glob("./"+KORPUS+"/*")
    edcs = pandas.read_csv('./EDCS-Tabellen/'+SUCHTABELLE+'.csv', low_memory=False)
    cats = {'0-1': 0, '2-4': 0, '5-9': 0, '10-14': 0, '14-19': 0, '20-29': 0, "30-39": 0, "40-49": 0, '50-59': 0,
            "60-69": 0, '70-79': 0, '80-89': 0, '90-99': 0, '100-120': 0}
    for cat in cats:
        cats[cat] = {'Hispania citerior': 0, 'Roma': 0, 'Venetia et Histria / Regio X': 0, 'Apulia et Calabria / Regio II': 0, 'Transpadana / Regio XI': 0, 'Lusitania': 0, 'Latium et Campania / Regio I': 0, 'Umbria / Regio VI': 0, 'Samnium / Regio IV': 0, 'Gallia Narbonensis': 0, 'Dalmatia': 0, 'Aquitani(c)a': 0, 'Lugudunensis': 0, 'Germania superior': 0, 'Moesia superior': 0, 'Dacia': 0, 'Bruttium et Lucania / Regio III': 0, 'Noricum': 0, 'Picenum / Regio V': 0, 'Aemilia / Regio VIII': 0, 'Numidia': 0, 'Mauretania Caesariensis': 0, 'Raetia': 0, 'Moesia inferior': 0, 'Pannonia inferior': 0, 'Baetica': 0, 'Sicilia': 0, 'Sardinia': 0, 'Liguria / Regio IX': 0, 'Pannonia superior': 0, 'Germania inferior': 0, 'Alpes Maritimae': 0, 'Britannia': 0, 'Mauretania Tingitana': 0, 'Etruria / Regio VII': 0, 'Africa proconsularis': 0, 'Macedonia': 0, 'Alpes Cottiae': 0, 'Cappadocia': 0, 'Provincia incerta': 0, 'Corsica': 0, 'Asia': 0, 'Arabia': 0, 'Thracia': 0, 'Italia': 0, 'Belgica | Germania superior': 0, 'Palaestina': 0, 'Galatia': 0, 'Barbaricum': 0, 'Alpes Poeninae': 0, 'Belgica': 0, 'Achaia': 0, 'Pontus et Bithynia': 0, 'Aegyptus': 0, 'Syria': 0, 'Alpes Graiae': 0, 'Lycia et Pamphylia': 0, 'Regnum Bospori': 0, 'Cyprus': 0, 'Cilicia': 0}
    for d in dlist:
        id = re.sub(r"./%s\\"%KORPUS, "", d)
        age = None
        afound = False
        with open (d+"/"+id+"_pos", "rb") as infile:
            pos=pickle.load(infile)
            i=0
            for p in pos:
                if p == "NUM":
                    with open (d+"/"+id+"_lemmata", "rb") as lemfile:
                        lemmata=pickle.load(lemfile)
                        if lemmata[i-1] == "annus":
                            with open (d+"/"+id+"_words", "rb") as wordfile:
                                words=pickle.load(wordfile)
                                if lemmata[i-2] == "vixit" or lemmata[i-1] == "decedo":
                                    num = lemmata[i]
                                    num = re.sub('unus', 'I', num)
                                    num = re.sub('duo', 'II', num)
                                    num = re.sub('tres', 'III', num)
                                    num = re.sub('U', 'V', num)
                                    num = re.sub('XXXXX', 'L', num)
                                    num = re.sub('XXXX', 'XL', num)
                                    num = re.sub('LXL', 'XC', num)
                                    num = re.sub('VIIII', 'IX', num)
                                    num = re.sub('IIII', 'IV', num)
                                    try:
                                        age = roman.fromRoman(num)
                                        afound = True
                                        break
                                    except:
                                        continue
                i+=1
        if afound:
            place = edcs.loc[edcs['ID']==id].iloc[0].loc['Provinz']
            for cat in cats:
                range = re.findall(r'\d*', cat)
                try:
                    if age>=int(range[0]) and age<=int(range[2]):
                        cats[cat][place]+=1
                except:
                    continue
    dfout = pandas.DataFrame(cats).T
    dfout.to_csv('./Ausgabetabellen/'+KORPUS+'_alter.csv', index=True, quoting=1)
        

if __name__ == "__main__":
    KORPUS = "Korpus_Sepulcrales"
    SUCHTABELLE ="searchresultSepulcralesReduziert"
    main()