def divideMal(numero, numero1):
	try:
		return numero-numero1
	except Exception as e:#catch(TypeError e) en java
		raise e("hola como estas cometi un error en esta linea y me da flojera arreglarlo")#lanzar un error igual a throws en java
	finally:
		pass

print(divideMal("1",2))