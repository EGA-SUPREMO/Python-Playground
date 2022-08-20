def email(valor):
	cont1 = 0
	cont2 = 0
	email = "EMAIL INCORRECTO"
	arroba = False
	punto = False
	indice1 = -1
	indice2 = -1
	for i in valor:
		if i == '@':##validacion del aarroba
			arroba = True
			cont1 += 1
			indice1= valor.index('@')##ver el indice del arroba
		if cont1 == 1:
			arroba = True
		else:
			arroba = False
		if i == '.':##validacion del punto
			punto = True
			cont2 += 1
			indice2 = valor.index('.')##ver el indice del punto
		if cont2 == 1:
			punto = True
		else:
			punto = False
	if arroba and punto and indice1 < indice2:##el index del arroba debe ser menor al index del punto
		email = "EMAIL CORRECTO"
	
	return email;
#---------------------------ejecutamos la funcion---------------------------------
print(email("hola@gmail.com"))
#print(email(str(input("ingresa un email "))))