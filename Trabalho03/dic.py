from func import *

'''
  Classe que possui todos os dicionários que serão utilizados pelo sistema de RI
'''
class Dicionarios:
  def __init__(self, files):
    self.__index = {}       # Indice invertido
    self.__fileWeight = {}  # Peso dos arquivos
    self.__queryWeight = {} # Peso da consulta
    self.__answer = {}      # Conjunto da resposta
    self.__file = files     # 
    
  '''
    Add palavras no indice invertido
  '''
  def addToIndex(self, vet, num):
    for p in vet:
      if self.__index.get(p) == None:
        self.__index[p] = {}
      
      v = self.__index[p]

      if v.get(num) == None:
        v[num] = 0
      
      v[num] += 1

  def initFileWeight(self):
    keys = list(self.__index.keys())
    keys.sort()

    for key in keys:
      print("termo: " + key)
      for i in self.__index.get(key):
        nameFile = i
        
        if self.__fileWeight.get(nameFile) == None:
            self.__fileWeight[nameFile] = {}
          
        index = keys.index(key)
        self.__fileWeight[nameFile][index] = tfidf(
                                                  self.__index[key].get(i),
                                                  len(self.__index[key]),
                                                  self.__file.lenBase())      

    '''for i in range(1, self.__file.lenBase() +1):
      print(str(i))
      for key in keys:
        if self.__index[key].get(i) != None:
          nameFile = i

          if self.__fileWeight.get(nameFile) == None:
            self.__fileWeight[nameFile] = {}

          index = keys.index(key)
          print('\t indice: '+str(index))

          # Calcular TF-IDF
          self.__fileWeight[nameFile][index] = tfidf(
                                                  self.__index[key].get(i),
                                                  len(self.__index[key]),
                                                  self.__file.lenBase())'''

  def getIndex(self):
    return self.__index
  
  def getFileWeight(self):
    return self.__fileWeight
  
  def getQueryWeight(self):
    return self.__queryWeight
  
  def getAnswer(self):
    return self.__answer