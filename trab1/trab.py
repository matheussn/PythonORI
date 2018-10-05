# Alunos:
# Mateus Benedini de Oliveira Santiago Prates - 
# Matheus Santiago Neto - 11621BSI252

import sys
import nltk

ignore = ['PREP', 'PREP|+', 'ART', 'CONJ']
files = []
dic = {}
st = ''
sw = ''
et = ''

def init():
	if len(sys.argv) > 2 or len(sys.argv) == 1:
		exit()

def initFiles():
	base = open(sys.argv[1], 'r', encoding="ISO-8859-1")
	
	qnt = base.readlines()

	for linha in qnt:
		linha = linha.replace('\n', '')
		files.append(open(linha, 'r', encoding="ISO-8859-1"))

	base.close()

def c(str):
	str = str.replace(',', ' ')
	str = str.replace('.', ' ')
	str = str.replace('!', ' ')
	str = str.replace('?', ' ')
	str = str.replace('\n', ' ')
	return str


#Retorna lista de palvras não stopwords
def filtro(num):
	conteudo = files[num].read()
	conteudo = c(conteudo.lower())
	conteudo = conteudo.split()
	
	result = [rr for rr in conteudo if rr not in sw]

	cl = et.tag(result)

	res = [st.stem(rr[0]) for rr in cl if rr[1] not in ignore]

	return res

def createDic(vet, num):
	for palavra in vet:
		if dic.get(palavra) == None:
			dic[palavra] = {}

		v = dic[palavra]
		#contagem
		if v.get(num+1) == None:
			v[num+1] = 0

		v[num+1] += 1

def createfile():
	file = open('indice.txt', 'w')
	texto = []

	for x in dic:
		s = ''+x+':'
		for y in dic[x]:
			s = s + ' ' + str(y) + ',' +str(dic[x][y])
		s = s + '\n'
		texto.append(s)

	file.writelines(texto)
	file.close()

def closefiles():
	for f in files:
		f.close()

def initVars():
	global st 
	st = nltk.stem.RSLPStemmer()
	global sw 
	sw = nltk.corpus.stopwords.words("portuguese")
	sents = nltk.corpus.mac_morpho.tagged_sents()
	global et
	et = nltk.tag.UnigramTagger(sents)

if __name__ == '__main__':
	init()

	initFiles()
	initVars()

	for i in range(0, len(files)):
		#pegar vetor
		v = filtro(i)
		#contar as palavras e add no dicionario
		createDic(v, i)
	
	createfile()
	closefiles()