import pickle
import nltk

if __name__ == '__main__':
    sents = nltk.corpus.mac_morpho.tagged_sents()
    et = nltk.tag.UnigramTagger(sents)

    f = open('etiquetador', 'wb')

    pickle.dump(et, f)