#Analyse der Inschriften mit CLTK und LatinCy, Extraktion der und Speicherung der Ergebnisdate aus dem Spacy-Doc

import cltk, pickle, os, pandas, re, multiprocessing, time, threading, math, itertools
import concurrent.futures
from cltk import NLP
from itertools import repeat
from cltk.alphabet import lat

global KORPUS
global SUCHTABELLE

def initialize(korpus):
    global KORPUS
    KORPUS = korpus

#Ausführung des CLTK-Analyse-Prozesses (LatinCy) und Extraktion der Attribute
def task_analyze(texts, textids, trueraws):
    global KORPUS
    for text, id, trueraw in zip(texts, textids, trueraws):
        print(id)
        os.makedirs(os.path.dirname(KORPUS+"/"+id+"/"), exist_ok=True)
        print(text)
        cltk_doc = cltk_nlp.analyze(text) #Analyseprozess
        #Zuweisung aller relevanten Attribute von cltk_doc in eigene Variabeln
        _get_words_attribute = cltk_doc._get_words_attribute
        embeddings = cltk_doc.embeddings
        embeddings_model = cltk_doc.embeddings_model
        language = cltk_doc.language
        lemmata = cltk_doc.lemmata
        morphosyntactic_features = cltk_doc.morphosyntactic_features
        normalized_text = cltk_doc.normalized_text
        pipeline = cltk_doc.pipeline
        pos = cltk_doc.pos
        raw = cltk_doc.raw
        sentence_embeddings = cltk_doc.sentence_embeddings
        sentences = cltk_doc.sentences
        sentences_strings = cltk_doc.sentences_strings
        sentences_tokens = cltk_doc.sentences_tokens
        spacy_doc = cltk_doc.spacy_doc
        stems = cltk_doc.stems
        tokens = cltk_doc.tokens
        tokens_stops_filtered = cltk_doc.tokens_stops_filtered
        words = cltk_doc.words
        deps = []
        ancestors = []
        ent_iobs = []
        ents = []
        #Extraktion und Konstruktion des Ancestor und Dependency-Listen
        for token in spacy_doc:
            deps.append(token.dep_)
            ancs= []
            for ancestor in token.ancestors:
                anaccs= {}
                anaccs["text"] = ancestor.text
                anaccs["i"] = ancestor.i
                anaccs["orth"] = ancestor.orth
                anaccs["idx"] = ancestor.idx
                anaccs["pos"] = ancestor.pos_
                anaccs["dep"] = ancestor.dep_
                anaccs["lemma"] =ancestor.lemma_
                ancs.append(anaccs)
            ancestors.append(ancs)
            ent_iobs.append(token.ent_iob_)
        ents = [(e.text, e.start_char, e.end_char, e.label_) for e in spacy_doc.ents] #Extraktion der Named Entities
        ancestors=list(ancestors)
        #Zusammenfassung der Attribute
        inscraccs = {#"embeddings" : embeddings, "embddings_model" : embeddings_model,
                    "language" : language, "lemmata" : lemmata, "morphosyntactic_features" : morphosyntactic_features,
                    "normalized_text" : normalized_text, "pipeline" : pipeline, "pos" : pos, "raw" : raw, 
                    #"sentence_embeddings" : sentence_embeddings, "sentences" : sentences, "sentences_strings" : sentences_strings,"sentences_tokens" : sentences_tokens,
                    "stems" : stems, "tokens" : tokens,
                    "tokens_stops_filtered" : tokens_stops_filtered, "words" : words, "deps" : deps, "ancestors" : ancestors, 
                    "ent_iobs" : ent_iobs, "ents" : ents, "trueraw" : trueraw}
        #Speicherung der Attribute der Einzeldateien in ihrem entsprechenden Verzeichnis
        for a in inscraccs:
            with open (KORPUS+"/"+id+"/"+id+"_"+a, "wb") as outfile:
                try:
                    pickle.dump(inscraccs[a], outfile)
                except:
                    print(inscraccs[a])

#Aufteilung einer Liste in Chunks der Größe chunk_size (oder kleiner), Rückgabe als Liste von Chunks
def split_list(the_list, chunk_size):
    result_list = []
    while the_list:
        result_list.append(the_list[:chunk_size])
        the_list = the_list[chunk_size:]
    return result_list                

#Hauptmethode: Vorverarbeitung und Prozesssteuerung
def main():
    global KORPUS
    global SUCHTABELLE
    #Laden der Inschriftentabellen des Webscrapers, Aufteilung in Listen von IDs und Texten
    df = pandas.read_csv('./EDCS-Tabellen/'+SUCHTABELLE+'.csv', low_memory=False)
    os.makedirs(os.path.dirname(KORPUS+"/"+KORPUS), exist_ok=True)
    texts = df['Text'].tolist()
    edcsids = df.iloc[:,0].tolist()
    #Bereinigung der Texte von bestimmten Sonderzeichen um die entsprechenden Prozesse in der Normalisierung durch
    #das CLTK zu umgehen, dann weitere Normalisierungsfunktionen des CLTKS (Beibehaltung von Editorialien,
    #Entfernung von Punktierung, Akzenten, Ligaturen), Speicherung in c(lean)texts
    ctexts = [] 
    print("Normalisierung...")
    for text in texts:
        text = str(text)
        text = re.sub(r' / ', ' ', text)
        text = re.sub(r' // ', '. ', text)
        text = re.sub(r'/', '', text)
        text = re.sub(r'k', 'c', text)
        text = re.sub(r'⟦', '', text)
        text = re.sub(r'⟧', '', text)
        text = lat.accept_editorial(text)
        text = lat.drop_latin_punctuation(text)
        text = lat.normalize_lat(text, drop_accents=True, drop_macrons=True, jv_replacement=False, ligature_replacement=True)
        ctexts.append(text)
    #Chunking durch Methode split_list und Vorbereitung des Multiprocessings
    print("Chunking...")
    i = 0
    ptexts = []
    ptextids = []
    rtexts = []
    time_start = time.time
    for ctext, id, text in zip(ctexts, edcsids, texts):
        if i>=200:
            break
        ptexts.append(ctext)  #ptexts = Bereinigte Texte zur Weiterverabeitung 
        ptextids.append(id) #IDs
        rtexts.append(text) #Rohtext aus der EDCS
    num_cpu = multiprocessing.cpu_count()
    chunk_size = math.ceil(len(ptexts)/num_cpu)
    pchunks = list(split_list(ptexts, chunk_size))
    rchunks = list(split_list(rtexts, chunk_size))
    idchunks = list(split_list(ptextids, chunk_size))
    #Ausführung von task_analyze auf den Chunks in mehreren parallelen Prozessen, entsprechend der Anzahl verfügbarer Prozessorkerne
    print("Analyse...")
    if __name__ == '__main__' or __name__ == 'Kernskripte.InschriftenAnalyse': #Verhinderung von Rekursion
        pool = multiprocessing.Pool(processes=int(num_cpu-1), initializer=initialize, initargs=(KORPUS, ))
        pool.starmap(func=task_analyze, iterable=zip(pchunks, idchunks, rchunks))
        pool.close()
    time_end = time.time
    print("Fertig: "+str(time_end))

cltk_nlp = NLP(language="lat")
if __name__ == "__main__":
    KORPUS = "inscraccs_test"
    SUCHTABELLE ="searchresult"
    main()

