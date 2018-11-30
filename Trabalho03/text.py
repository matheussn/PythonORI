'''
  Classe que possui todos os métodos e manipuladores de texto e o nltk
  que serão utilizados pelo sistema de RI
'''

import nltk

class Text:
  def __init__(self):
    self.stemmer = nltk.stem.RSLPStemmer()
    self.stopWords = nltk.corpus.stopwords.words("portuguese")
  
  '''
    Função que remove o radical da string 'word'
  '''
  def removeRadical(self, word):
    return self.stem(word)
  
  '''
    Função que remove as Stopwords e realiza a extração de radicais de um vetor
    retorna um vetor contendo apenas palavras consideradas não stopwords e sem seus radicais
  '''
  def removeSR(self, vet):
    return [self.removeRadical(rr) for rr in vet if rr not in self.stopWords]

  def pattern(str):
    str = str.replace(',', ' ')
    str = str.replace('.', ' ')
    str = str.replace('!', ' ')
    str = str.replace('?', ' ')
    str = str.replace('\n', ' ')
    return str