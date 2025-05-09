# Suma de los primeros N números

while True:
    
    try: 
        num = int(input("Ingresa un numero entero: "))
    
        if num < 0:
            print("Por favor ingresa un numero entero.")
    
        else: 
            break
        
    except ValueError:
        print("Ingrese un dato valido.")

i = 1
suma = 0
for i in range(num+1):
    suma += i 
    print(f"La suma va en: {suma}")

print(f"La suma de todos los numeros enteros es de: {suma}")