#Importe la biblioteca json.
#Abra datos/resumen_nomina.json en modo lectura ("r").
#Utilice json.load() para guardar el contenido en una variable llamada resumen.
#Imprima el diccionario completo.
#Imprima solamente el salario total utilizando su clave.

import json

with open("datos/resumen_nomina.json", "r", encoding="utf-8") as archivo:
    resumen = json.load(archivo)

print(resumen)
print("Salario total:", resumen["salario_total"])