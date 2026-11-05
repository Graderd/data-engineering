"""
Requisitos:
1. Crea una lista con cinco diccionarios. Cada producto debe tener nombre, precio y cantidad.
2. Crea una función mostrar_productos(productos) que muestre todos los productos.
3. Crea una función calcular_inventario(productos) que devuelva el valor total del inventario mediante return.
4. Crea una función producto_mas_caro(productos) que devuelva el nombre del producto con el precio unitario más alto.
5. Muestra cuántos productos diferentes hay en la lista.
"""

productos = [{"nombre": "Mouse", "precio": 50, "cantidad": 10},
             {"nombre": "Teclado", "precio": 100, "cantidad": 5},
             {"nombre": "Monitor", "precio": 500, "cantidad": 2},
             {"nombre": "CPU", "precio": 300, "cantidad": 3},
             {"nombre": "GPU", "precio": 800, "cantidad": 1}
             ]

def mostrar_productos(productos):
    if not productos:
        print("No hay productos en la lista.")
        return
    for producto in productos:
        print(f"nombre: {producto['nombre']}, precio: {producto['precio']}, cantidad: {producto['cantidad']}")

def calcular_inventario(productos):
    inventario = sum(producto['precio']*producto['cantidad'] for producto in productos)
    return inventario

def producto_mas_caro(productos):
    if not productos:
        return None
    producto_caro = max(productos, key=lambda x: x['precio'])
    return producto_caro['nombre']

def contar_productos(productos):
    return len(productos)

"""print("Productos disponibles:")
mostrar_productos(productos)
print(f"Inventario: {calcular_inventario(productos)}")
print(f"Producto más caro: {producto_mas_caro(productos)}")
print(f"Cantidad de productos diferentes: {contar_productos(productos)}")
"""

print("Inventario vacío:", calcular_inventario([]))
print("Producto más caro vacío:", producto_mas_caro([]))
print("Cantidad vacía:", contar_productos([]))
mostrar_productos([])