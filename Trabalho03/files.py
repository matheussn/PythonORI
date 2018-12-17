from text import *
from func import *
from dic import *

def readBaseFile(local):
  f = open(local, 'r', encoding="ISO-8859-1")
  txt = f.readlines()
  f.close()
  return txt

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
  
def initBase(baseFiles, texto, index):
  for linha in texto:
    linha = linha.replace('\n', '')
    b = open(linha, 'r')
    name = b.name.replace('./base/', '')
    content = b.read()
    b.close()

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

    ref = getString(c, "REFERENCES:", "CITATIONS:")
    #addIndex(index, ref, name)

    cit = getString(c, "CITATIONS:", "\n\n")
    #addIndex(index, cit, name)

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


def createWeightFile(dicFile):
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
