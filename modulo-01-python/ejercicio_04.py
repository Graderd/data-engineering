nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 0: 
    print("Edad inválida")
elif edad <= 12: 
    print(f"Hola {nombre}, eres un niño.")
elif edad < 18:
    print(f"Hola {nombre}, eres un adolescente.")
else:
    print(f"Hola {nombre}, eres un adulto.")