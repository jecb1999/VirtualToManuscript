import pywhatkit
print("Ingrese el texto que desea convertir a manuescrito")
texto=input()
pywhatkit.text_to_handwriting({texto}, rgb=(0,0,255))
print("El manuescrito se encuentra en la misma ruta del .py disfrutalo!!!")
