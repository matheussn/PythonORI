import math

def tfidf(freq, TotalDocumentos, nDocumentosComTermo, porcent=0.0):
	tf = 1+ math.log(freq,10)
	idf = TotalDocumentos/nDocumentosComTermo
	idf = math.log(idf,10)

	total = tf * idf
	total += total * porcent
	return total