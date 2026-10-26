#Crear una lista llamada empleados con al menos cinco diccionarios.
#Cada empleado debe contener nombre, puesto y salario.
empleados = [
    {"nombre": "Starling Feliz", "puesto": "Ingeniero de Datos", "salario": 80000},
    {"nombre": "Carlos Mendoza", "puesto": "Ingeniero de Software", "salario": 90000},
    {"nombre": "María García", "puesto": "Analista de Datos", "salario": 75000},
    {"nombre": "Juan Pérez", "puesto": "Gerente de Proyecto", "salario": 100000},
    {"nombre": "Ana López", "puesto": "Diseñadora UX", "salario": 85000}
]
#Recorrer la lista e imprimir el nombre y salario de cada empleado.
total_salarios = 0
for empleado in empleados:
    total_salarios += empleado['salario']
    print(f"Nombre: {empleado['nombre']}, Salario: {empleado['salario']}")
#Calcular cuánto paga la empresa en salarios en total.
print(f"Salario total: {total_salarios}")
#Calcular el salario promedio.
salario_promedio = total_salarios / len(empleados)
print(f"Salario promedio: {salario_promedio}")
#Mostrar cuántos empleados tiene la empresa.
print(f"Cantidad de empleados: {len(empleados)}")

