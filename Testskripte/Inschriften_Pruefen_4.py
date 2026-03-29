import glob, re, pickle

dlist = glob.glob("./inscraccs_test/*")
zfinds = []
zuschreibungen = ['incomparabilis', 'pientissimus', 'pietas', 'pius', 'obsequentissimus', 'obsequens', 'dulcus', 
                  'dulcis', 'carus', 'pudens', 'impudens', 'castitas', 'castus', 'rarus', 'felix', 'clarus', 'luctus',
                    'lucio', 'fortis', 'honestus', 'modestus', 'moderatus', 'sollicitus', 'securus', 'anxius', 
                    'studiosus', 'beatus', 'laetus', 'fidus', 'placidus', 'clemens', 'integer', 'prudens', 'amabilis',
                    'amo', 'amantus', 'probus', 'probitas', 'probo', 'frugi', 'pulcher', 'lepidus', 'laetitia',
                    'gaudeo', 'uirtus', 'fructus', 'recte', 'fatum', 'acerbus', 'acerbum', 'fatum', 'dolor', 'maeror', 
                    'fletus', 'lacrima', 'doleo', 'fleo', 'honor', 'honoratum' 'bonus', 'mereo', 'meritus', 'bene', 
                    'mero', 'merentus', 'sapiens', 'forma', 'exemplum', 'desiderius', 'desiderium', 'querela', 
                    'studium', 'parilis', 'mellitus', 'incomparabilis', 'concordia', 'tristia', 'dignus', 'afficio', 
                    'suauis', 'nascor', 'miserus', 'amoena', 'simplex', 'desero', 'iucundus', 'iuncundus', 'sanctus']
for d in dlist:
    id = re.sub(r"./inscraccs_test\\", "", d)
    hasz = False
    with open (d+"/"+id+"_lemmata", "rb") as infile:
        lemmata = pickle.load(infile)
        for l in lemmata:
            for z in zuschreibungen:
                if l==z:
                        hasz = True
    if hasz:
        zfinds.append(id)
with open ("./Testdaten/test4output.txt", "w", encoding="UTF-8") as outfile:
    for i in zfinds:
        outfile.write(i+"\n")