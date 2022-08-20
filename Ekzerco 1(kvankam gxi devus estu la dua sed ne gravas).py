#def comprobarEmail(Email):
#	if Email.find('@')==0 or Email.rfind('@')==0 or Email.count('@')>=2 or Email.count('@')<1:
#		return "Email incorrecto"
#	else:
#		return "Email correcto"
#
#print(comprobarEmail("te@h"))

def comprobarEmail(Email):#Codigo despues de ver las soluciones
	if Email.find('@')==0 or Email.rfind('@')==(len(Email)-1) or Email.count('@')!=1:
		return "Email incorrecto"
	else:
		return "Email correcto"
		
print(comprobarEmail("theh@h"))

#def ucomprobarEmail():
#	pass
#	contador=0
#	for x in Email:
#		if x == '@':
#			contador+=1
#	if contador==1:
#
#	else:
#		return false