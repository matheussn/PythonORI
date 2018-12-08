import sys

from dic import *
from files import *
from query import *

def init():
  if len(sys.argv) != 3:
    print("Por favor, a forma correta de executar este arquivo é:")
    print("python3 main.py base.txt consulta.txt")
    exit()

if __name__ == '__main__':
  init()
  
  base = readBaseFile(sys.argv[1])
  baseFiles = dict()
  invertedIndex = dict()
  initBase(baseFiles, base, invertedIndex) #baseFile Dicionário dos arquivos

  print(invertedIndex)

  '''for i in range(1, len(baseFile) +1):
    v = files.readBase(str(i))
    dic.addToIndex(v, i)'''

  #dic.initFileWeight()

  #files.createWeightFile(dic.getFileWeight())
  #print('termos: ' +str(len(dic.getIndex())))


  '''query = {}

  filequery = openQuery(sys.argv[2])

  query = createDicQuery(query, filequery)

  print(query)'''