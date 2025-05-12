# Calcular la frecuencia de cada dígito en un número

while True:
    num = input("Ingresa un numero: ")
    
    if num.startswith("-"):
        temp = num[1:]
    
    else:
        temp = num
    
  
    if temp.replace(".", "").isdigit():
        num = float(num)
        break

    else:
        print("Ingresa un dato valido.")
    
frecuencia = [0] * 10

num_solo_digito = temp.replace("-", "").replace(".", "")

i = 0

while i < len(num_solo_digito):
    digito = int(num_solo_digito[i])
    frecuencia[digito] += 1
    i += 1

for i in range(10):
    print(f"Digito {i}: {frecuencia[i]} veces")
    