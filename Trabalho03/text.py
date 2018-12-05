'''
  Classe que possui todos os métodos e manipuladores de texto e o nltk
  que serão utilizados pelo sistema de RI
'''

import nltk

class Text:
  def __init__(self):
    self.__stemmer = nltk.stem.SnowballStemmer("english")
    self.__stopWords = nltk.corpus.stopwords.words("english")
  
  '''
    Função que remove o radical da string 'word'
  '''
  def removeRadical(self, word):
    return self.__stemmer.stem(word)
  
  '''
    Função que remove as Stopwords e realiza a extração de radicais de um vetor
    retorna um vetor contendo apenas palavras consideradas não stopwords e sem seus radicais
  '''
  def removeSR(self, vet):
    return [self.removeRadical(rr) for rr in vet if rr not in self.__stopWords]

  def removeNumber(self, vet):
    return [i for i in vet if not i.isdigit()]

  def pattern(self,str):
    str = str.replace(':', ' ')
    str = str.replace('TITLE', ' ')
    str = str.replace('AUTHORS', ' ')
    str = str.replace('SOURCE', ' ')
    str = str.replace('ABSTRACT', ' ')
    str = str.replace('MAJOR SUBJECTS', ' ')
    str = str.replace('MINOR SUBJECTS', ' ')
    str = str.replace('REFERENCES', ' ')
    str = str.replace('CITATIONS', ' ')
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