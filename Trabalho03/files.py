'''
  Classe que possui todos os arquivos que serão utilizados pelo sistema de RI
'''

from text import Text

class Files:
  def __init__(self, argv):
    self.baseFiles = []
    self.consFile = None

    base = open(argv[1], 'r', encoding="ISO-8859-1")
    qnt = base.readlines()

    for linha in qnt:
      linha = linha.replace('\n', '')
      self.baseFiles.append(open(linha, 'r', encoding="ISO-8859-1"))
    
    base.close()
    self.consFile = open(argv[2], 'r')
  
  '''
    Ler arquivo na posição indicada
  '''
  def read(self, index):
    if index >= len(self.baseFiles):
      print("Indice Maior q o tamanho do vetor")
      return None

    c = self.baseFiles[index].read()
    c = Text.pattern(c.lower())

    return c.split()

  def lenBase(self):
    return len(self.baseFiles)

  def teste(self):
    print(self.baseFiles)
    print(self.consFile)