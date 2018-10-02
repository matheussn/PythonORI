# Alunos:
# Mateus Benedini de Oliveira Santiago Prates - 
# Matheus Santiago Neto - 11621BSI252

import sys
from nltk.corpus import stopwords

# {'amor': {1: 3, 2:0}, ''}

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
	sw = stopwords.words("portuguese")
	conteudo = files[num].read()
	conteudo = conteudo.lower()
	conteudo = c(conteudo)
	conteudo = conteudo.split()
	
	result = [rr for rr in conteudo if rr not in sw]

	return result

def createDic(vet, num):
	for palavra in vet:
		if dic.get(palavra) == None:
			dic[palavra] = {}

		v = dic[palavra]
		#contagem 
		qnt = contar(palavra, num)

		v[num+1] = qnt


def contar(palavra, num):
	return 0


if __name__ == '__main__':
	init()

	initFiles()

	for i in range(0, len(files)):
		#pegar vetor
		v = filtro(i)
		#contar as palavras e add no dicionario
		createDic(v, i)
	print(dic)
