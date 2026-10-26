#Cree un diccionario llamado empleado con nombre, edad, puesto y salario.
empleado = {
    "nombre": "Staling Feliz",
    "edad": 29,
    "puesto": "Ingeniero de Datos",
    "salario": 80000
}
#Muestre el nombre y puesto utilizando sus claves.
print(f"Nombre: {empleado["nombre"]}")
print(f"Puesto: {empleado["puesto"]}")
#Solicite al usuario un nuevo salario mediante input().
nuevo_salario = float(input("Ingrese un nuevo salario para el empleado: "))
#Actualice el salario del empleado.
empleado["salario"] = nuevo_salario
#Agregue una nueva clave llamada departamento.
empleado["departamento"] = input("Ingrese el departamento del empleado: ")
#Recorra el diccionario utilizando un for y muestre todos sus campos y valores.
for clave, valor in empleado.items():
    print(f"{clave}: {valor}")