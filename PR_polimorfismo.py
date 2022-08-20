class Coche(object):
	def desplazarse(self):
		print("Me muevo con 4 patas")

class Moto(object):
	def desplazarse(self):
		print("Me muevo con 2 patas")

class Camion(object):
	def desplazarse(self):
		print("Me muevo con 6 patas")

def desplazarseVehiculo(vehiculo):#METODO POLIMORFICO MUY ZUCULENTOZO
	vehiculo.desplazarse()

desplazarseVehiculo(Camion())
desplazarseVehiculo(Moto())