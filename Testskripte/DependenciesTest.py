import pickle

inscription = open("./Korpus_Sepulcrales/EDCS-04900497/EDCS-04900497_ancestors", "rb")
lemmata = pickle.load(open("./Korpus_Sepulcrales/EDCS-15900537/EDCS-15900537_lemmata", "rb"))
raw = pickle.load(open("./Korpus_Sepulcrales/EDCS-04900497/EDCS-04900497_raw", "rb"))
tokens = pickle.load(open("./Korpus_Sepulcrales/EDCS-15900537/EDCS-15900537_tokens", "rb"))
pos = pickle.load(open("./Korpus_Sepulcrales/EDCS-15900537/EDCS-15900537_pos", "rb"))
morph = pickle.load(open("./Korpus_Sepulcrales/EDCS-15900537/EDCS-15900537_morphosyntactic_features", "rb"))
ancestors = pickle.load(inscription)
#for a in ancestors:
   # print(a)
print(lemmata)
print(raw)
print(tokens)
print(pos)
print(morph)
print(ancestors[3])