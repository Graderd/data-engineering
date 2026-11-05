"""
Escenario: una empresa necesita un programa que calcule cuánto debe pagar un cliente por una compra, pero el sistema debe manejar entradas incorrectas.
Requisitos
1. Solicitar al usuario el nombre de un producto.
2. Solicitar el precio unitario y la cantidad de unidades.
3. Convertir el precio a float y la cantidad a int.
4. Calcular el total de la compra (precio × cantidad).
5. Si el usuario introduce letras donde se esperan números, capturar ValueError y mostrar "Error: debes introducir un número válido".
6. Si el precio es negativo o cero, o la cantidad es menor o igual a cero, mostrar "Error: el precio y la cantidad deben ser mayores que cero".
7. Si los datos son válidos, mostrar el producto, la cantidad y el total de la compra.
"""

producto = input("Nombre del producto: ")
try:
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad de unidades: "))
    if precio <= 0 or cantidad <= 0:
        print("Error: el precio y la cantidad deben ser mayores que cero")
    else:
        total = precio * cantidad
        print(f"Producto: {producto}, Cantidad: {cantidad}, Total de la compra: {total}")
except ValueError:
    print("Error: debes introducir un número válido")