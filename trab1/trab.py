# Alunos:
# Mateus Benedini de Oliveira Santiago Prates - 
# Matheus Santiago Neto - 11621BSI252

import sys
import nltk

files = []
dic = {}

def init():
	if len(sys.argv) > 2 or len(sys.argv) == 1:
		exit()

def initFiles():
	base = open(sys.argv[1], 'r')
	
	qnt = base.readlines()

	for linha in qnt:
		linha = linha.replace('\n', '')
		files.append(open(linha, 'r'))

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
	st = nltk.stem.RSLPStemmer()
	sw = nltk.corpus.stopwords.words("portuguese")
	conteudo = files[num].read()
	conteudo = conteudo.lower()
	conteudo = c(conteudo)
	conteudo = conteudo.split()
	
	result = [rr for rr in conteudo if rr not in sw]

	res = []

	for palavra in result:
		res.append(st.stem(palavra))

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


if __name__ == '__main__':
	init()

	initFiles()

	for i in range(0, len(files)):
		#pegar vetor
		v = filtro(i)
		#contar as palavras e add no dicionario
		createDic(v, i)
	
	createfile()
