import cltk
from cltk import NLP
sentlist = []
sentlist.append("Marius in officium honoratum est")
sentlist.append("Hoc officium honoratum est")
sentlist.append("Tullia poeta optima flemur")
sentlist.append("Lucius veteranus meritus est")
sentlist.append("Claudia mulier forma est")
sentlist.append("filia merentissima")
sentlist.append("Gnaeus studiosus est")
sentlist.append("filius studiosus")
sentlist.append("ogi obstarique animae misera de sede volenti")
sentlist.append("tabula amoena")
sentlist.append('virtus est medium uitiorum')
sentlist.append('tuom nec sit marita quae rotundioribus')
sentlist.append('en carus maritus')
sentlist.append('si iubeat coniunx durum est')
sentlist.append('quod genus in parentes cognatos')
sentlist.append('decii pater et natus')
sentlist.append('decii pater et nata')
sentlist.append('quicumque mihi natus genitus fuerit')
sentlist.append('egregia parta tristis tamen duobus tam')
sentlist.append('Dis Manibus Terentiae Stiba dis Marcus Terentius Theodotianus aviae carissimae fecit vivus')
sentlist.append('Osciae Modestae Marci filiae Corneliae Publianae clarissimae feminae aviae carissimae et educatrici dulcissimae Marcus Flavius Arrius Oscius Honoratus nepos vir tribunus militum legionis')
sentlist.append('soror panthia carus endymion hic')
sentlist.append('si ab uxore carissima et tot communium')
sentlist.append('[D(is)] M(anibus) / [I]ulio Argio / IIII(quadriere) Fort(una) / [n]ation(e) Ital(icus) st(ipendiorum) / [X]VIII q(ui) vixit a(nnos) XXXVIII / [m]ens(es) VI dies XI')
sentlist.append('D(is) M(anibus) s(acrum) / Seiia Honorata in flore decessit prudens / demandat nat[os] marito karissimo / lucemque caruit vixit annis viginti / sex')
wordslist = []
cltk_nlp = NLP(language="lat")
for sent in sentlist:
    cltk_doc = cltk_nlp.analyze(sent)
    wordslist.append(cltk_doc.words)
for words in wordslist:
    for word in words:
        if str(word.string) == 'honoratum':
            print (word)
        if str(word.string) == 'optima':
            print (word)
        if str(word.string) == 'meritus':
            print (word)
        if str(word.string) == 'forma':
            print (word)
        if str(word.string) == 'merentissima':
            print (word)
        if str(word.string) == 'studiosus':
            print (word)
        if str(word.string) == 'misera':
            print (word)
        if str(word.string) == 'amoena':
            print (word)
        if str(word.string) == 'virtus':
            print (word)
        if str(word.string) == 'maritus':
            print (word)
        if str(word.string) == 'marita':
            print (word)
        if str(word.string) == 'coniunx':
            print (word)
        if str(word.string) == 'parentes':
            print (word)
        if str(word.string) == 'natus':
            print (word)
        if str(word.string) == 'nata':
            print (word)
        if str(word.string) == 'tristis':
            print (word)
        if str(word.lemma) == 'avia':
            print (word)
        if str(word.string) == 'carissimae':
            print (word)
        if str(word.string) == 'carus':
            print (word)
        if str(word.string) == 'carissima':
            print (word)
        if str(word.string) == 'vixit':
            print (word)
        if str(word.string) == 'decessit':
            print (word)


