import math

def tf(freq, porcent=0.0):
	v = 1+ math.log(freq,10)
	v += v *porcent
	return v
	
def idf(TotalDocumentos,nDocumentosComTermo, porcent=0.0):
	aux = TotalDocumentos/nDocumentosComTermo
	aux += aux * porcent
	return math.log(aux,10)