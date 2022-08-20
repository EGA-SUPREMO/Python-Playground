def pildorasinformaticas ():
    print ("Acabas de entrar en el canal de Juan!")
    print ("Como definirias a Juan por su labor de divulgar conocimiento gratuito?")
    answer = input("Escribelo en un comentario y dale a like'.").lower()
    if answer == "Es un heroe" or answer == "like":
        print ("Pues no olvides suscribirte")
    elif answer == "tampoco es para tanto..." or answer == "dislike":
        print ("Creo que deberias suscribirte para comprobarlo")
    else:
        print ("like  o dislike, no te lies, prueba otra vez.")
        pildorasinformaticas()

print (pildorasinformaticas())﻿