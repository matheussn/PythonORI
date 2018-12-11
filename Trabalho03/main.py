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
  fileWeight = dict()
  initBase(baseFiles, base, invertedIndex, fileWeight) #baseFile Dicionário dos arquivos

  query = dict()

  filequery = openQuery(sys.argv[2])

  totalFiles = len(baseFiles)
  baseQuery = createDicQuery(query, filequery, invertedIndex, totalFiles)
  #createDicQueryPonderacao(query, totalFiles, invertedIndex)
  print(query)