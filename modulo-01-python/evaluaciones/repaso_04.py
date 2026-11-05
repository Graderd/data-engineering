import csv
import json

total = 0
producto_mas_alto = ""
mas_alto = 0
cantidad_productos = 0

try:
    with open("datos/ventas.csv", "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)

        for venta in lector:
            venta["precio"] = float(venta["precio"])
            venta["cantidad"] = int(venta["cantidad"])
            venta["total_venta"] = venta["precio"] * venta["cantidad"]
            total += venta["total_venta"]
            cantidad_productos += 1
            if venta["total_venta"] > mas_alto:
                mas_alto = venta["total_venta"]
                producto_mas_alto = venta["producto"]
            print(venta)

    print(f"Total de ventas: {total}")
    print(f"Producto con venta más alta: {producto_mas_alto} - Ingreso generado: {mas_alto}")

    resumen = {"ingresos_totales": total,
                "producto_mayores_ingresos": producto_mas_alto,
                "ingresos_producto": mas_alto,
                "cantidad_productos": cantidad_productos}

    with open("datos/resumen_ventas.json", "w", encoding="utf-8") as archivo:
        json.dump(resumen, archivo, indent=4,  ensure_ascii=False)

except FileNotFoundError:
    print("Error: No se encontró el archivo de ventas.")

except ValueError:
    print("Error: El archivo contiene datos numéricos inválidos.")