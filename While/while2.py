while True:
    print("Ingresa una palabra: ")

    for palabra in iter(input, "fin"):
        print(f"{palabra.capitalize()} tiene {len(palabra)} letras")
        print("\n")
        print("Ingresa una palabra: ")
    
    
    else: 
        print("Saliendo del programa.")
        break