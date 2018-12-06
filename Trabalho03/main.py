import sys

from dic import Dicionarios
from files import Files
from text import Text
from query import *

def init():
  if len(sys.argv) != 3:
    print("Por favor, a forma correta de executar este arquivo é:")
    print("python3 main.py base.txt consulta.txt")
    exit()

if __name__ == '__main__':
  init()

  # Objeto que possui os manipuladores de texto e o nltk
  txt = Text()
  # Objeto que possui os arquivos e os métodos para manipula-los
  files = Files(sys.argv, txt)
  # Objeto que possui os dicionários e os métodos para manipula-los
  dic = Dicionarios(files)
  
  #for i in range(1, files.lenBase() +1):
  #  v = files.readBase(str(i))
  #  dic.addToIndex(v, i)

  #dic.initFileWeight()

  #files.createWeightFile(dic.getFileWeight())
  #print('termos: ' +str(len(dic.getIndex())))


  query = initDicQuery()

  filequery = openQuery(sys.argv[2])

  query = createDicQuery(query, filequery)

  print(query)