# Factorial de un numero

while True:
    num = input("Ingresa un número: ").strip()
    
    if num.isdigit():
        num = int(num)
        break
    
    else:
        print("Ingresa un dato valido.")


factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1

print(f"El factorial de {num} es: {factorial}")




