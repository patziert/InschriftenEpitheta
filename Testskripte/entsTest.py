import pickle

with open ("./inscraccs_test/EDCS-84600023/EDCS-84600023_ents", "rb") as infile:
    ents = pickle.load(infile)
    print(ents)
with open ("./inscraccs_test/EDCS-84600023/EDCS-84600023_ent_iobs", "rb") as infile:
    iob = pickle.load(infile)
    print(iob)
with open ("./Kerndaten/testAdjPositions", "rb") as infile:
    pos = pickle.load(infile)
    idlist=[]
    duplettes = 0
    for p in pos:
        if len(p)>1:
            duplettes+=1
    print(duplettes)