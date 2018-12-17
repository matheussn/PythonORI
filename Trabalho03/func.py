import math

def tf(freq, porcent=1.0):
	v = 1+ math.log(freq,10)
	v += v *porcent
	return v
	
def idf(TotalDocumentos,nDocumentosComTermo, porcent=1.0):
	aux = TotalDocumentos/nDocumentosComTermo
	aux += aux * porcent
	return math.log(aux,10)