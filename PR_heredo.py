class Vehiculo(object):
	"""docstring for Coche"""
	def __init__(self):#la nomo de la "contructores" cxiam estas "__init__"
		self.__largo=500#Oni uzas du sub-dividostreko por informi ke la varieblo aux metodo estas privata
		self.__ancho=300
		self.__destruido=False

	def autodestrucion(self):#cxiuj funkcioj kiu estas en iu klaso(metodo) ilia unua argumento estas "self"
		self.__destruido=True

class Auto(Vehiculo):
	def tirarseUnPeo(self):
		autodestrucion()
		print("Se tiro un peo de los buenos! felicidades! estoy orgulloso de mi.\nPosdata se autodestruyo(el auto yo lo hare en el 2018-2019) :D")

class VehiculoElectrico(Vehiculo):
	"""docstring for VehiculoElectrico"""
	def __init__(self):
		super().__init__()
		self.arg = arg
		self.__Electrificado=True

	def Deseslectrificar(self):
		self.__Electrificado=False

class AutoElectrico(VehiculoElectrico, Auto):#El que esta delante tiene prioridad
	"""docstring for AutoElectrico"""
	def tirarseUnPeo(self):
		autodestrucion()
		if(self.__Electrificado):
			print("HOSTIA CHAVAL LA HAS LIADO PARDA CON ESE PEDO ELECTRIFICADO. me medio engorgullesco :S")
		else:
			print("Para la proxima prueba hacerlo electrificado ;).")

autoelectrico = AutoElectrico()

print(isinstance(autoelectrico, AutoElectrico))#isinstance() es lo mismo que intanceof de java