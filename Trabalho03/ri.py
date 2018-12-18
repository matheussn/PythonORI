from dic import *
from files import *
from query import *
from func import *

"""
  Função que executa os comandos necessários para simulação do modelo vetorial
"""
def vetorial(sys):
  base = readBaseFile(sys.argv[1])
  baseFiles = dict()
  invertedIndex = {"BaseFiles": dict(), "Queries": dict()}
  fileWeight = dict()
  initBase(baseFiles, base, invertedIndex["BaseFiles"]) #baseFile Dicionário dos arquivos
  
  totalFiles = len(baseFiles)
  
  for i in baseFiles:
    fileWeight[i] = dict()
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('Title'), i, totalFiles)
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('Abstract'), i, totalFiles)
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('MajorSub'), i, totalFiles)
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('MinorSub'), i, totalFiles)

  query = dict()
  sim = dict()

  filequery = openQuery(sys.argv[2])

  baseQuery = createDicQuery(query, filequery, invertedIndex, totalFiles)
  calcSim(query, fileWeight, sim)

  metrica = dict()

  initMetricas(metrica, sim, baseQuery)
  media = calcMedia(metrica, len(baseQuery))

  plot(media)

"""
  Função que executa os comandos necessários para simulação do modelo vetorial modificado
"""
def modificado(sys, values):
  base = readBaseFile(sys.argv[1])
  baseFiles = dict()
  invertedIndex = {"BaseFiles": dict(), "Queries": dict()}
  fileWeight = dict()
  medias = dict()
  initBase(baseFiles, base, invertedIndex["BaseFiles"], medias) #baseFile Dicionário dos arquivos
  
  totalFiles = len(baseFiles)
  
  for i in baseFiles:
    fileWeight[i] = dict()
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('Title'), i, totalFiles, values['titulo'])
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('Abstract'), i, totalFiles, values['abstract'])
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('MajorSub'), i, totalFiles, values['majorSub'])
    initFileWeight(invertedIndex["BaseFiles"], fileWeight, baseFiles[i].get('MinorSub'), i, totalFiles, values['minorSub'])

  query = dict()
  sim = dict()

  filequery = openQuery(sys.argv[2])

  baseQuery = createDicQuery(query, filequery, invertedIndex, totalFiles)
  calcSim(query, fileWeight, sim, baseFiles, medias, values['referencia'])

  metrica = dict()

  initMetricas(metrica, sim, baseQuery)
  metricaMedia = calcMedia(metrica, len(baseQuery))

  plot(metricaMedia)