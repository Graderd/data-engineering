#Crear una lista llamada empleados con al menos cinco diccionarios.
#Cada empleado debe contener nombre, puesto y salario.
empleados = [
    {"nombre": "Starling Feliz", "puesto": "Ingeniero de Datos", "salario": 80000},
    {"nombre": "Carlos Mendoza", "puesto": "Ingeniero de Software", "salario": 90000},
    {"nombre": "María García", "puesto": "Analista de Datos", "salario": 75000},
    {"nombre": "Juan Pérez", "puesto": "Gerente de Proyecto", "salario": 100000},
    {"nombre": "Ana López", "puesto": "Diseñadora UX", "salario": 85000}
]

#mostrar_empleados(empleados): recibe la lista e imprime el nombre y salario de cada empleado.
def mostrar_empleados(empleados):
    for empleado in empleados:
        print(f"Nombre: {empleado['nombre']}, Salario: {empleado['salario']}")
#calcular_total(empleados): recibe la lista, suma los salarios y devuelve el total con return.
def calcular_total(empleados):
    total_salario = sum(empleado['salario'] for empleado in empleados)
    return total_salario
#calcular_promedio(empleados): recibe la lista y devuelve el salario promedio.
def calcular_promedio(empleados):
    total_salario = calcular_total(empleados)
    if len(empleados) == 0:
        return 0
    promedio_salario = total_salario / len(empleados)
    return promedio_salario

def solicitar_salario():
    while True:
        try:
            salario = float(input("Ingrese el salario del nuevo empleado: "))
            if salario < 0:
                print("El salario no puede ser negativo. Por favor, ingrese un salario válido.")
                continue
            else:
                print(f"Salario ingresado correctamente: {salario} RD$")
                break
        except ValueError:
            print("Por favor, ingrese un salario válido.")
            continue
    return salario

mostrar_empleados(empleados)
print(f"Salario total: {calcular_total(empleados)}")
print(f"Salario promedio: {calcular_promedio(empleados)}")
salario_nuevo = solicitar_salario()
print(f"Valor devuelto por la función: {salario_nuevo}")