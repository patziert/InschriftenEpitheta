import cltk, pickle, os

with open("./Testdaten/cltktest", "rb") as infile:
    cltk_doc_rec = pickle.load(infile)
_get_words_attribute = cltk_doc_rec._get_words_attribute
embeddings = cltk_doc_rec.embeddings
embeddings_model = cltk_doc_rec.embeddings_model
language = cltk_doc_rec.language
lemmata = cltk_doc_rec.lemmata
morphosyntactic_features = cltk_doc_rec.morphosyntactic_features
normalized_text = cltk_doc_rec.normalized_text
pipeline = cltk_doc_rec.pipeline
pos = cltk_doc_rec.pos
raw = cltk_doc_rec.raw
sentence_embeddings = cltk_doc_rec.sentence_embeddings
sentences = cltk_doc_rec.sentences
sentences_strings = cltk_doc_rec.sentences_strings
sentences_tokens = cltk_doc_rec.sentences_tokens
spacy_doc = cltk_doc_rec.spacy_doc
stems = cltk_doc_rec.stems
tokens = cltk_doc_rec.tokens
tokens_stops_filtered = cltk_doc_rec.tokens_stops_filtered
words = cltk_doc_rec.words
inscraccs = {"_get_words_attribute" : _get_words_attribute, "embeddings" : embeddings, "embddings_model" : embeddings_model,
             "language" : language, "lemmata" : lemmata, "morphosyntactic_features" : morphosyntactic_features,
             "normalized_text" : normalized_text, "pipeline" : pipeline, "pos" : pos, "raw" : raw, 
             "sentence_embeddings" : sentence_embeddings, "sentences" : sentences, "sentences_strings" : sentences_strings,
             "sentences_tokens" : sentences_tokens, "spacy_doc" : spacy_doc, "stems" : stems, "tokens" : tokens,
             "tokens_stops_filtered" : tokens_stops_filtered, "words" : words}
os.makedirs(os.path.dirname("inscraccs_test/inscraccs_test"), exist_ok=True)
print(sentences)
#print(spacy_doc)
for a in inscraccs:
    with open ("inscraccs_test/inscraccs_test_"+a, "wb") as outfile:
        pickle.dump(inscraccs[a], outfile)
for token in spacy_doc:
    ancs = ""
    for ancestor in token.ancestors:
        ancs=ancs+" "+ancestor.text
    print(token.lemma_+" "+token.dep_+" "+ancs)
print(raw)
ents = [(e.text, e.start_char, e.end_char, e.label_) for e in spacy_doc.ents]
print(ents)
print(spacy_doc[10].ent_iob_)
print(spacy_doc[10].ent_kb_id_)