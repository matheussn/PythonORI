import math

def tfidf(freq, n, tam):
	return ( ( 1+ math.log(freq,10) ) * math.log( tam / n , 10) )