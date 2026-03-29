import pandas, re, csv

df = pandas.read_csv('./Testdaten/kookinschriften.csv') 
texts = df['Text'].tolist()
df=df.transpose()
sl = [df[col] for col in df]
print(len(sl))
outputtexts = []
zuschreibungen = {"incomparabil" : 0, "pi(us|a|um)" : 0, "pientissim":0 , "obsequen": 0,"dulcis" : 0, "carissim" : 0, 
                  "puden" : 0, "cast(us|a|um)" : 0, "rarissim" : 0, "felix" : 0, "clarissim" : 0, "luct" : 0, "fortis" : 0, 
                  "honest" : 0, "modest": 0, "moderat": 0, "sollicit" : 0, "secur" : 0, "anxi" : 0, "studios" : 0, "beat" : 0,
                  "laet" : 0, "fid(us|a|um)" : 0, "placid" : 0, "clemen" : 0, "integ(er|ra|rum)" : 0, "prudens" : 0, "amabil" : 0,
                  "amat" : 0, "aman" : 0, "prob(us|a|um)" : 0, "frugi" : 0, "pulch(er|ra|rum)" : 0, "lepid" : 0, "laetitia gaudens" : 0, 
                  "virtus" : 0, "fructusque recte" : 0, "(fatum acerbum|acerbo fato)": 0, "dolor" : 0, "in maeribus" : 0, "flet" : 0,
                  "lacrim" : 0, "dolens" : 0, "flevit" : 0, "hono(r|s|ratum)" : 0, "optim(us|a)" : 0, "mer(ens|itus|enti|erentissima)" : 0,
                  "sapien" : 0, "form(us|a|um)" : 0, "exemplum" : 0, "desideri(us|um)" : 0, "sine querella" :0, "studio parili" : 0,
                  "mellitissim" : 0, "incomparabil" : 0, "tristia" : 0, "dign(us|a|um)" : 0, "adfect" : 0, "suav(is|e)" : 0, "nat(us|a)" : 0,
                  "miser" : 0, "amoen" : 0, "simplex" : 0, "desert(us|a|um)" : 0, "iucund" : 0, "sanct(us|a|um|issim)" : 0}
beziehungen = {"mat(er|ri|rum|re)" : 0, "pat(er|ri|rum|re)" : 0, "frat(er|ri|rum|re)" : 0, "soror" : 0, "noverca" : 0, "privign" : 0,
               "amita" : 0, "nurr" : 0, "filia": 0, "fili(us|i|o|um)" : 0, "nepo(s|ti|te|tum)" : 0, "\savia" : 0, "\sav(us|i|o|um)\s" : 0,
               "avuncul" : 0, "patru(us|i|o|um)" : 0, "\sgener(\s|i\s|o\s|um\s)" : 0, "\snur(us|ui|um|u)\s": 0, "\suxor" : 0,
               "\smarit(us|i|o|um)" : 0, "\smarita" : 0, "\sconiu(n?)(x|gi)" : 0, "concubina" :0, "contubernal(|i|e)" : 0, 
               "\sparen(s|ti|te|tum)": 0, "socer" : 0, "\sconiugi(um|i|o|a|orum|is)\s" : 0, "\sconubi" : 0, "\smatrimoni" : 0}
kookkurrenz = 0
j = 0
for i in texts:
    i=str(i).lower()
    zit = False
    bit = False
    for z in zuschreibungen:
        if re.search(z, i):
           zuschreibungen[z]+=1
           zit = True
    for b in beziehungen:
        if re.search(b, i):
           beziehungen[b]+=1
           bit = True
    if zit & bit:
        kookkurrenz +=1
        outputtexts.append(sl[j])
    j+=1
print(zuschreibungen)
print(beziehungen)
print(kookkurrenz)

csv_file_path = './Testdaten/preresults.csv'
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
data[0].append('Anzahl_Auswahl')
i = 1
for key in zuschreibungen:
    data[i].append(zuschreibungen[key])
    i+=1
data[i].append('')
i+=1
for key in beziehungen:
    data[i].append(beziehungen[key])
    i+=1
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)