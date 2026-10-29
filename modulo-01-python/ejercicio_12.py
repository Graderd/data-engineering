import json
import csv

empleados = []

with open("datos/empleados.csv", "r", encoding="utf-8", newline="") as archivo:
    lector = csv.DictReader(archivo)

    for empleado in lector:
        empleado["salario"] = float(empleado["salario"])
        empleados.append(empleado)
        print(empleado)


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

print("Cantidad de empleados:", len(empleados))
print(f"Salario total: {calcular_total(empleados)}")
print(f"Salario promedio: {calcular_promedio(empleados)}")

with open("datos/empleados_procesados.json", "w", encoding="utf-8") as archivo:
    json.dump(empleados, archivo, indent=4, ensure_ascii=False)

resumen = {"cantidad_empleados": len(empleados),
           "salario_total": calcular_total(empleados),
           "salario_promedio": calcular_promedio(empleados)}

with open("datos/resumen_nomina.json", "w", encoding= "utf-8") as archivo:
    json.dump(resumen, archivo, indent=4, ensure_ascii=False)