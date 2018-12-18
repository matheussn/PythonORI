import matplotlib.pyplot as plt
import math

"""
	Função para calculo do TF-IDF
"""
def tfidf(freq, TotalDocumentos, nDocumentosComTermo, porcent=0.0):
	tf = 1+ math.log(freq,10)
	idf = TotalDocumentos/nDocumentosComTermo
	idf = math.log(idf,10)

	total = tf * idf
	total += total * porcent
	return total

"""
  Função que aplica a regra de interpolação em um dicionário, add em um vetor
"""
def interpolar(media):
  v = list(media.values())

  for i in v:
    flag = max(v[v.index(i):], key=float)
    if i < flag:
      v[i] = flag
  
  return v

"""
  Função que plota gráficos dado um dicionário de revocação e precisão
"""
def plot(media):
  y = interpolar(media)
  x = media.keys()

  plt.plot(x, y, 'g')
  plt.axis( [0, 100, 0, 100])

  plt.title('Média de precisão por revocação')

  plt.xlabel('Revocação')
  plt.ylabel('Precisão')
  plt.show()