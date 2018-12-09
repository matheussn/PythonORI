import math

def tf(freq):
	return ( 1+ math.log(freq,10) ) 
	
def idf(TotalDocumentos,nDocumentosComTermo)
	aux = TotalDocumentos/nDocumentosComTermo
	return math.log(aux,10)