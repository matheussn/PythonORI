import nltk

stemmer = nltk.stem.SnowballStemmer("english")
stopWords = nltk.corpus.stopwords.words("english")

# Função para remover radicais
def removeRadical(word):
  return stemmer.stem(word)

#Função para remover stopwords
def removeSR(vet):
  return [removeRadical(rr) for rr in vet if rr not in stopWords]

#função para remover números de um vetor
def removeNumber(vet):
  return [i for i in vet if not i.isdigit()]

#Função para deixar uma string com um padrão para realizar o split, ou outras manipulações
def patternBase(str):
  str = str.replace(';', ' ')
  str = str.replace(')', ' ')
  str = str.replace('(', ' ')
  str = str.replace('/', ' ')
  str = str.replace('\\', ' ')
  str = str.replace('\"', ' ')
  str = str.replace('[', ' ')
  str = str.replace(']', ' ')
  str = str.replace('%', ' ')
  str = str.replace('+', ' ')
  str = str.replace('-', ' ')
  str = str.replace(',', ' ')
  str = str.replace('.', ' ')
  str = str.replace('!', ' ')
  str = str.replace('?', ' ')
  str = str.replace('\n', ' ')
  return str

#Função para deixar uma string com um padrão para realizar o split, ou outras manipulações
def patternQuery(str):
  str = str.replace(';', ' ')
  str = str.replace(')', ' ')
  str = str.replace('(', ' ')
  str = str.replace('/', ' ')
  str = str.replace('\\', ' ')
  str = str.replace('+', ' ')
  str = str.replace('-', ' ')
  str = str.replace('.', ' ')
  str = str.replace('!', ' ')
  str = str.replace('?', ' ')
  str = str.replace(', ', ' ')
  return str

def processSub(vet):
  return [ i for i in vet if len(i) != 2 and removeString(i)]

def removeString(string):
  if len(string) > 1 or string in ['a', 'b', 'c', 'd', 'e', 'k']:
    return True

  return False