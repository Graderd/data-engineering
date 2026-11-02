#Intente abrir datos/resumen_nomina.json.
#Lea el contenido utilizando json.load().
#Muestre la cantidad de empleados y el salario total.
#Capture FileNotFoundError si el archivo no existe.
#Capture json.JSONDecodeError si su contenido no es JSON válido.

import json

try:
    with open("datos/resumen_nomina.json", "r", encoding="utf-8") as archivo:
        resumen = json.load(archivo)
    
    print("Cantidad de empleados:", resumen["cantidad_empleados"])
    print("Salario total:", resumen["salario_total"])

except FileNotFoundError:
    print("El archivo no existe.")

except json.JSONDecodeError:
    print("El contenido del archivo no es JSON válido.")
