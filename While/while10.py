# Suma de números pares e impares

print("Ingresa numeros uno por uno para sumar. Ingresa 0 para terminar.")

suma_pares = 0
suma_impares = 0

while True:
    num = int(input("Ingresa un número para sumar: "))
    
    if num == 0:
        break

    elif num % 2 == 0:
        suma_pares += num
    
    else:
        suma_impares += num

suma = suma_impares + suma_pares

print(f"La suma dde los números pares es de: {suma_pares}")
print(f"La suma de los números impares es de: {suma_impares}")
print(f"La suma total es de: {suma}") 

