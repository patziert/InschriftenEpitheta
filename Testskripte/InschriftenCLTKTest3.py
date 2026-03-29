import cltk, pickle, os, glob, re

with open ("/Testdaten/test3output.txt", "w", encoding="UTF-16") as outfile:
    outfile.write("")
dlist = glob.glob("./inscraccs_test/*")
for d in dlist:
    id = re.sub(r"./inscraccs_test\\", "", d)
    with open (d+"/"+id+"_trueraw", "rb") as infile:
        raw = str(pickle.load(infile))
    with open (d+"/"+id+"_raw", "rb") as infile:
        trueraw = str(pickle.load(infile))
    with open (d+"/"+id+"_tokens", "rb") as infile:
        tokens = pickle.load(infile)
    with open ("/Testdaten/test3output.txt", "a", encoding="UTF-16") as outfile:
        outfile.write(raw+"\n")
        outfile.write(trueraw+"\n")
        for t in tokens:
            t = str(t)
            outfile.write("[\'"+t+"\'], ")
        outfile.write("\n\n")