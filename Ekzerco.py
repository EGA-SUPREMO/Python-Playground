def pono(int):
	print("houla moundou, poupou")
	print(int)

pono(5)
pono(5)

m = ["popo", "hey", 3, 7, 0, 2]
print(m.index("popo"))

diccionario = {"poiop":"peee", "mojon":3, True:False}

diccionario["mojon"]=7
diccionario[3]="CAGONES"

print(m[1:2])

print(diccionario)
print(diccionario[3])

hol = "diccionario"

print("descanso")

for i in diccionario:
	print(i)
else:
	print("""En python el else se ejecuta despues de ejecutar todo el bucle sea for sea while siempre y cuando no se
ejecute ningun break o pass.""")
for i in range(len(diccionario)):
	print(i)
#	print("heulou", end = " ")