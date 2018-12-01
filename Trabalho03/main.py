import sys

from dic import Dicionarios
from files import Files
from text import Text

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
  
  for i in range(0, files.lenBase()):
    v = files.read(i)
    dic.addToIndex(v, i)
  
  dic.addToFileWeight(i)


  print(str(dic.index))