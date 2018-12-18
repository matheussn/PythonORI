from text import *
from func import *
from dic import *

"""
  Ler o arquivo de query
"""
def openQuery(local):
  p = open(local, 'r')
  c = p.read()
  p.close()
  return c

"""
  Ler arquivo da base
"""
def readBaseFile(local):
  f = open(local, 'r', encoding="ISO-8859-1")
  txt = f.readlines()
  f.close()
  return txt

"""
  Função para pegar uma substring dentro de uma string
"""
def getString(string, inicio, fim, number = True, remove = None):
  start = string.find(inicio) + len(inicio)
  end = string.find(fim)
  c = string[start:end].strip().lower()

  if remove != None:
    c = c.replace(remove, ' ')

  c = c.split()
  if number:
    c = removeNumber(c)
    c = removeSR(c)
  
  return c

"""
  Função que pega uma substring de uma string, porém sem remoção das quebras de linha,
  para realizar a contagem de linhas
"""
def contLines(string, inicio, fim):
  start = string.find(inicio) + len(inicio)
  end = string.find(fim)
  c = string[start:end].strip().lower()
  c = c.split('\n')
  return len(c)

"""
  Lê os arquivos da base, adicionando no indice invertido
  Calcula as médias de referencia e citações
"""
def initBase(baseFiles, texto, index, medias = dict()):
  mediaRef = 0
  mediaCit = 0

  for linha in texto:
    linha = linha.replace('\n', '')
    b = open(linha, 'r')
    name = b.name.replace('./base/', '')
    content = b.read()
    b.close()

    ref = contLines(content, "REFERENCES:", "CITATIONS:")
    mediaRef += ref
    cit = contLines(content, "CITATIONS:", "\n\n")
    mediaCit += cit

    content = patternBase(content)
    
    c = content.strip()

    title = getString(c, "TITLE:", "AUTHORS:")
    addIndex(index, title, name)

    authors = getString(c, "AUTHORS:", "SOURCE:")
    #addIndex(index, authors, name)

    source = getString(c, "SOURCE:", "ABSTRACT:")
    #addIndex(index, source, name)

    abstract = getString(c, "ABSTRACT:", "MAJOR SUBJECTS:")
    addIndex(index, abstract, name)
    
    major = getString(c, "MAJOR SUBJECTS:", "MINOR SUBJECTS:", remove=':')
    major = processSub(major)
    addIndex(index, major, name)

    minor = getString(c, "MINOR SUBJECTS:", "REFERENCES:", remove=':')
    minor = processSub(minor)
    addIndex(index, minor, name)

    baseFiles[name] = {
      'Title': title,
      'Authors': authors,
      'Source': source,
      'Abstract': abstract,
      'MajorSub': major,
      'MinorSub': minor,
      'References': ref,
      'Citations': cit
      }
      
  mediaRef = mediaRef / len(baseFiles)
  mediaCit = mediaCit / len(baseFiles)

  medias["RefMedia"] = mediaRef
  medias["CitMedia"] = mediaCit