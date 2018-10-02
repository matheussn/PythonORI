# Alunos:
# Mateus Benedini de Oliveira Prates - 
# Matheus Santiago Neto - 11621BSI252

import sys

if __name__ == '__main__':
	if len(sys.argv) > 2 or len(sys.argv) == 1:
		exit()

	files = []
	base = open(sys.argv[1], 'r')
	
	for linha in base:
		linha = linha.split()
		files.append(open(linha[0], 'r'))

	print(files)
	
	base.close()