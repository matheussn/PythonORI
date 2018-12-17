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

def patternBase(str):
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

def patternQuery(str):
  str = str.replace(';', ' ')
  str = str.replace(')', ' ')
  str = str.replace('(', ' ')
  str = str.replace('/', ' ')
  str = str.replace('\\', ' ')
  str = str.replace('+', ' ')
  str = str.replace('-', ' ')
  str = str.replace('.', ' ')
  str = str.replace('!', ' ')
  str = str.replace('?', ' ')
  str = str.replace(', ', ' ')
  return str

def processSub(vet):
  return [ i for i in vet if len(i) != 2 and removeString(i)]

def removeString(string):
  if len(string) > 1 or string in ['a', 'b', 'c', 'd', 'e', 'k']:
    return True

  return False