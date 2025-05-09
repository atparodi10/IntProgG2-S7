# Contar palabras en una frase

while True:
    frase = input("Ingresa una frase: ").strip()
    
    if frase.isdigit():
        print("Ingresa una cadena de texto.")
        
    elif not frase:
        print("Campo Vacío. Intente Nuevamente.")
        
    else:
        break

palabras  = frase.split()
numero_de_palabras = len(palabras)

for i, palabra in enumerate(palabras, start=1):
    print(f"{i}. {palabra}")

print(f"{frase}")
print(f"Cantidad de palabras: {numero_de_palabras}")