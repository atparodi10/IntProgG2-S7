# Contar vocales en una cadena

while True:
    
    cadena = input("Ingresa una palabra, frase o una oración: ").strip()
    
    if not cadena:
        print("Campo vacío. Intente nuevamente.")
    
    
    elif cadena.isdigit():
        print("Ingresa una cadena de texto.")
        
    else:
        break
    

cadena = cadena.lower()


contador = 0
contadorA = 0
contadorE = 0
contadorI = 0
contadorO = 0
contadorU = 0

for letra in cadena:
    if letra == "a":
        contador += 1
        contadorA += 1
        
    elif letra == "e":
        contador += 1
        contadorE += 1
    
    elif letra == "i":
        contador += 1
        contadorI += 1
    
    elif letra == "o":
        contador += 1
        contadorO += 1
    
    elif letra == "u":
        contador += 1
        contadorU += 1
    
    
print(f"{cadena.capitalize()}")
print(f"Cantidad de A: {contadorA}")
print(f"Cantidad de E: {contadorE}")
print(f"Cantidad de I: {contadorI}")        
print(f"Cantidad de O: {contadorO}")
print(f"Cantidad de U: {contadorU}")
print(f"Cantidad total de vocales: {contador}")
    