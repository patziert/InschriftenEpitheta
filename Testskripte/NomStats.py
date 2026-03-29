import glob, re, pickle

dlist = glob.glob("./inscraccs_test/*")
zfinds = []
zcount = {}
positionslist = []
zuschreibungen = ['pietas', 'castitas', 'luctus', 'probitas', 'uirtus', 'dolor', 'fletus', 'lacrima', 'honor', 'exemplum',
                  'desiderium', 'concordia']
for zs in zuschreibungen:
    zcount[zs]=0
for d in dlist:
    id = re.sub(r"./inscraccs_test\\", "", d)
    hasz = False
    positions = []
    with open (d+"/"+id+"_lemmata", "rb") as infile:
        lemmata = pickle.load(infile)
        with open (d+"/"+id+"_words", "rb") as infile2:
            words = pickle.load(infile2)
            for i, (l, w) in enumerate(zip(lemmata, words)):
                xpos = ""
                upos = ""
                pos = ""
                try:
                    xpos = str(w.xpos)
                    upos = str(w.upos)
                    pos = str(w.pos)
                except:
                    continue
                for z in zuschreibungen:
                    if l==z:
                        if xpos == 'noun' or upos == 'Noun' or pos == 'noun':
                            if xpos != 'noun': print (l+" !xpos "+id)
                            if upos != 'NOUN': print (l+" !upos "+id)
                            if pos != 'noun': print (l+" !pos "+id)
                            hasz = True
                            zcount[z]+=1
                            positions.append([id, i, l])
    if hasz:
        zfinds.append(id)
        positionslist.append(positions)
with open ("./Testdaten/testNomOutput.txt", "w", encoding="UTF-8") as outfile:
    for i in zfinds:
        outfile.write(i+"\n")
with open ("./Testdaten/testNomPositions", "wb") as outfile:
    pickle.dump(positionslist, outfile)
print(zcount)