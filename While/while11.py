# Encontrar el mayor y el menor de N números

while True:
    try:
        cantidad = int(input("¿Cuántos números desea ingresar: "))
         
        if cantidad <= 0:
                print("Ingresa una cantidad valida.")
                
        else:
            break
    
    except ValueError:
        print("Ingrese un dato valido.")
        

mayor = None
menor = None

for i in range(cantidad):
    while True:
        try:
            num = int(input(f"Ingrese el numero {i+1}: "))
        
            if mayor is None or num > mayor:
                mayor = num
        
            if menor is None or num < menor:
                menor = num
    
            break
    
        except ValueError:
            print("Ingresa un dato valido.")


print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")            
    