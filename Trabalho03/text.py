'''
  Classe que possui todos os métodos e manipuladores de texto e o nltk
  que serão utilizados pelo sistema de RI
'''

import nltk

stemmer = nltk.stem.SnowballStemmer("english")
stopWords = nltk.corpus.stopwords.words("english")

def removeRadical(word):
  return stemmer.stem(word)

def removeSR(vet):
  return [removeRadical(rr) for rr in vet if rr not in stopWords]

def removeNumber(vet):
  return [i for i in vet if not i.isdigit()]

def pattern(str):
  '''str = str.replace(':', ' ')
  str = str.replace('TITLE', ' ')
  str = str.replace('AUTHORS', ' ')
  str = str.replace('SOURCE', ' ')
  str = str.replace('ABSTRACT', ' ')
  str = str.replace('MAJOR SUBJECTS', ' ')
  str = str.replace('MINOR SUBJECTS', ' ')
  str = str.replace('REFERENCES', ' ')
  str = str.replace('CITATIONS', ' ')'''
  str = str.replace(';', ' ')
  str = str.replace(')', ' ')
  str = str.replace('(', ' ')
  str = str.replace('/', ' ')
  str = str.replace('\\', ' ')
  str = str.replace('+', ' ')
  str = str.replace('-', ' ')
  str = str.replace(',', ' ')
  str = str.replace('.', ' ')
  str = str.replace('!', ' ')
  str = str.replace('?', ' ')
  str = str.replace('\n', ' ')
  return str