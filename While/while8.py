# Calcular la frecuencia de cada dígito en un número

while True:
    num = input("Ingresa un numero: ")
    
    if num.startswith("-"):
        temp = num[1:]
    
    else:
        temp = num
    
  
    if num.replace(".", "").isdigit():
        num = float(num)
        break

    else:
        print("Ingresa un dato valido.")
    
frecuencia = [0] * 10

i = 0

while i < len(num):
    