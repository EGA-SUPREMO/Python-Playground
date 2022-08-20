def generadorDeParesEficiente(limite):
	num = 1

	while num<=limite:
		yield num*2
		num+=1

def generadorDeParesDeficiente(limite):
	num = 1
	numerolista=[]
	while num<=limite:
		numerolista.append(num*2)
		num+=1
	return numerolista

hola=generadorDeParesEficiente(3)
print(next(hola))
print(next(hola))
print(generadorDeParesDeficiente(5))

print("""MALDITO PYTHON POR SIMPLIFICAR LA SINTAXIS DE MIERDA D:< NO JODAS MALDITA SEAS COGNO DE SU
MALDITA PUTA MAQUINA MIERDA, ESTO ES PURA MIERDA. uff ya me desaoge que bueno :D""")

def generadorDeParesDeficiente(limite):
#cuando un argumento se necesita que sea obligatoriamente una tupla, lista o un numero no determinado de elementos