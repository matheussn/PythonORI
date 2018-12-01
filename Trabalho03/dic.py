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

  def addToFileWeight(self, num):
    key = list(self.__index.keys())
    key.sort()
    print(key)

  def getIndex(self):
    return self.__index
  
  def getFileWeight(self):
    return self.__fileWeight
  
  def getQueryWeight(self):
    return self.__queryWeight
  
  def getAnswer(self):
    return self.__answer