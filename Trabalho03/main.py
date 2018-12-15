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
  invertedIndex = {"BaseFiles": dict(), "Queries": dict()}
  fileWeight = dict()
  initBase(baseFiles, base, invertedIndex["BaseFiles"]) #baseFile Dicionário dos arquivos
  
  totalFiles = len(baseFiles)
  
  for i in baseFiles:
    fileWeight[i] = dict()
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('Title'), i, totalFiles)
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('Authors'), i, totalFiles)
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('Source'), i, totalFiles)
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('Abstract'), i, totalFiles)
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('MajorSub'), i, totalFiles)
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('MinorSub'), i, totalFiles)
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('References'), i, totalFiles)
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('Citations'), i, totalFiles)

  query = dict()
  sim = dict()

  filequery = openQuery(sys.argv[2])

  baseQuery = createDicQuery(query, filequery, invertedIndex, totalFiles)
  calcSim(query, fileWeight, sim)

  print("SIMILARIDADE DA CONSULTA 1: ")
  for i in sim.get(1):
    print("DOC: " + i + " Sim: " + str(sim[1][i]))