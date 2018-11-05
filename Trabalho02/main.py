# Alunos:
# Mateus Benedini de Oliveira Santiago Prates - 11621BSI200
# Matheus Santiago Neto - 11621BSI252

import sys
import os.path
import nltk
import pickle
import math

## Variaveis globais para uso nas funções
# ignore -> lista de classificação de palavras a ser ignorada
ignore = ['PREP', 'PREP|+', 'ART', 'CONJ']
# files -> lista de arquivos a serem avaliados
files = []
# cons -> Arquivo com a consulta
cons = None
# dic -> dicionário a ser utilizado para criação do indice invertido
dic = {}
# dicFile
dicFile = {}
# st -> Stem.nltk.stem.RSLPStemmer()
st = ''
# sw -> variavel para guardar as StopWords
sw = ''
# et -> etiquetador
et = ''


## Função para validar os arqumentos passados pela linha de comando
def init():
	if len(sys.argv) != 3:
		exit()

## Função para setar a lista de arquivos a ser acessada
def initFiles():
	base = open(sys.argv[1], 'r', encoding="ISO-8859-1")
	
	qnt = base.readlines()

	for linha in qnt:
		linha = linha.replace('\n', '')
		files.append(open(linha, 'r', encoding="ISO-8859-1"))

	base.close()
	global cons
	cons = open(sys.argv[2], 'r', encoding="ISO-8859-1")

## Função para executar os replaces devidos
def rep(str):
	str = str.replace(',', ' ')
	str = str.replace('.', ' ')
	str = str.replace('!', ' ')
	str = str.replace('?', ' ')
	str = str.replace('\n', ' ')
	return str


## Retorna lista de palvras não stopwords, artigo, preposição e conjunção
def filtro(num):
	conteudo = files[num].read()
	conteudo = rep(conteudo.lower())
	conteudo = conteudo.split()
	
	result = [rr for rr in conteudo if rr not in sw]

	cl = et.tag(result)

	res = [st.stem(rr[0]) for rr in cl if rr[1] not in ignore]

	return res

## Cria o dicionário
def createDic(vet, num):
	for palavra in vet:
		if dic.get(palavra) == None:
			dic[palavra] = {}

		v = dic[palavra]
		#contagem
		if v.get(num+1) == None:
			v[num+1] = 0

		v[num+1] += 1

## Cria o arquivo indice.txt e escreve no mesmo
def createpeso():
	file = open('peso.txt', 'w')
	texto = []

	for x in dicFile:
		s = ''+x+':'
		for y in dicFile[x]:
			s = s + ' ' + str(y) + ',' +str(dicFile[x][y]) + '\t'
		s = s + '\n'
		texto.append(s)

	file.writelines(texto)
	file.close()

## Função para fechar os arquivos abertos de files[]
def closefiles():
	for f in files:
		f.close()

## Inicialização das variáveis globais
def initVars():
	global st 
	st = nltk.stem.RSLPStemmer()
	global sw 
	sw = nltk.corpus.stopwords.words("portuguese")

	global et
	if os.path.isfile('etiquetador'):
		et = pickle.load( open('etiquetador', 'rb') )
	else:
		sents = nltk.corpus.mac_morpho.tagged_sents()
		et = nltk.tag.UnigramTagger(sents)

def listaInvertida():
	init()

	initFiles()
	initVars()

	for i in range(0, len(files)):
		#pegar vetor
		v = filtro(i)
		#contar as palavras e add no dicionario
		createDic(v, i)

def tfidf(freq, n):
	return ( ( 1+ math.log(freq,10) ) * math.log( len(files) / n , 10) )

def ponderacao(namefile, numfile):
	# Chaves no dicionário de termos
	keys = list(dic.keys())
	# Ordenando
	keys.sort()
	for key in keys:
		if dic[key].get(numfile) != None: # termo está no documento
			if dicFile.get(namefile) == None: # Não existe o arquivo no dicionario de arquivos
				dicFile[namefile] = {}

			v = dicFile[namefile]

			index = keys.index(key)
			f = dic[key][numfile]
			n = len(dic[key])

			if v.get(index) == None:
				if(f > 0):
					tf = tfidf(f, n)
					if tf > 0:
						v[index] = tf
				else:
					v[index] = 0

def resCons(sub):
	keys = list(dic.keys())
	keys.sort()
	print(keys)
	sub = sub.split('&')
	sub.sort()
	sub = [st.stem(c) for c in sub]
	print(sub)

def consulta():
	c = cons.read()
	c = c.replace('\n', '')
	c = c.replace(' ', '')
	c = c.split("|")
	for subc in c :
		resCons(subc)

if __name__ == '__main__':
	listaInvertida()
	
	for i in range(0, len(files)):
		ponderacao(files[i].name, i+1)
	
	createpeso()

	consulta()
	
	closefiles()

