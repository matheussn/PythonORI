'''
  Classe que possui todos os arquivos que serão utilizados pelo sistema de RI
'''
class Files:
  
  def __init__(self, argv, text):
    self.__baseFiles = []
    self.__consFile = None
    self.__text = text

    base = open(argv[1], 'r', encoding="ISO-8859-1")
    qnt = base.readlines()

    for linha in qnt:
      linha = linha.replace('\n', '')
      self.__baseFiles.append(open(linha, 'r', encoding="ISO-8859-1"))
    
    base.close()
    self.__consFile = open(argv[2], 'r')

  '''--------------------------------------------'''

  def lenBase(self):
    return len(self.__baseFiles)

  def getBaseFile(self):
    return self.__baseFiles

  '''
    Ler arquivo na posição indicada
  '''
  def read(self, index):
    if index >= len(self.__baseFiles):
      print("Indice Maior q o tamanho do vetor")
      return None

    c = self.__baseFiles[index].read()
    c = self.__text.pattern(c.lower())
    c = c.split()
    c = self.__text.removeSR(c)

    return c

  '''--------------------------------------------'''

  def createWeightFile(self,dicFile):
    f = open('peso.txt', 'w')
    texto = []

    for x in dicFile:
      s = ''+x+':'
      for y in dicFile[x]:
        s = s + ' ' + str(y) + ',' +str(dicFile[x][y])
      
      s = s + '\n'
      texto.append(s)

    f.writelines(texto)
    f.close()