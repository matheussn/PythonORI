'''
  Classe que possui todos os arquivos que serão utilizados pelo sistema de RI
'''
class Files:
  
  def __init__(self, argv, text):
    self.__baseFiles = {}
    self.__consFile = None
    self.__text = text

    base = open(argv[1], 'r', encoding="ISO-8859-1")
    qnt = base.readlines()
    base.close()

    for linha in qnt:
      linha = linha.replace('\n', '')
      b = open(linha, 'r')
      name = b.name.replace('./base/', '')
      content = self.__text.pattern(b.read()).lower()
      b.close()
      content = content.split()
      content = self.__text.removeSR(content)
      print(content[0])
      content = self.__text.removeNumber(content)
      self.__baseFiles[name] = content
  
    self.__consFile = open(argv[2], 'r')

  '''--------------------------------------------'''

  def lenBase(self):
    return len(self.__baseFiles)

  def getBaseFile(self):
    return self.__baseFiles

  '''
    Ler arquivo na posição indicada
  '''
  def readBase(self, index):
    return self.__baseFiles[index]

  '''--------------------------------------------'''

  def createWeightFile(self,dicFile):
    f = open('peso.txt', 'w')
    texto = []

    for x in dicFile:
      s = ''+str(x)+':'
      for y in dicFile[x]:
        s = s + ' ' + str(y) + ',' +str(dicFile[x][y])
      
      s = s + '\n'
      texto.append(s)

    f.writelines(texto)
    f.close()