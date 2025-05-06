palabra = input("Escribe una palabra: ")

while palabra.lower() != "salir":
    print(f"{(palabra.upper)()} tiene {len(palabra)} letras")
    palabra = input("Escribe una palabra: ")
    
else:
    print("Fin del programa.")