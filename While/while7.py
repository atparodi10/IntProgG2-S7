# Promedio de N calificaciones

while True:
    try:
        cantidad = int(input("¿Cuántas calificaciones desea ingresar?: "))
        
        if cantidad <= 0:
            print("Ingresa una cantidad de calificaciones valida.")
        
        else:
            break
        
    except ValueError:
        print("Ingrese un dato valido.")


suma = 0
i = 1
for i in range(cantidad):
    while True:
        try:
            calificaciones = int(input("Ingrese la calificaión: "))
        
            if 0 <= calificaciones <= 100:
                    suma += calificaciones
                    break
        
            else:
                    print("Ingresa una nota valida(0-100): ")
    
        except ValueError:
            print("Ingrese un dato valido.")
    

promedio = suma / cantidad

print(f"Cantidad de calificaciones: {cantidad}")
print(f"Promedio: {promedio: .2f}")