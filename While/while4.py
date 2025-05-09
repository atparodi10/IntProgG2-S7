# Producto de los primeros M números pares

while True:
    try:
        num = int(input("Ingresa un número entero: "))
    
        if num < 0:
            print("Ingresa un número mayor que 0: ")
    
        else:
            break
        
    except ValueError:
        print("Ingresa un dato valido: ")
    
pares = []
producto = 1
i = 1
contador = 0
while i <= num:
    if i % 2 == 0:
        pares.append(i)
        producto *= i
        print(f"{i}")
        contador += 1
    i += 1
    

print(f"El prodcuto de los números pares es: {pares}")
print(f"Cantidad de números pares: {contador}")
        
        