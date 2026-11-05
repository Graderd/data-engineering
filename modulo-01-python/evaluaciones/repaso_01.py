"""
Requisitos
1. Solicitar el nombre del estudiante.
2. Solicitar tres calificaciones numéricas.
3. Calcular el promedio de las tres calificaciones.
4. Si el promedio es menor que 70, mostrar Reprobado.
5. Si el promedio está entre 70 y 89.99, mostrar Aprobado.
6. Si el promedio es 90 o mayor, mostrar Excelente.
7. Si alguna calificación es menor que 0 o mayor que 100, mostrar Calificación inválida y no calcular el promedio.
"""

nombre = input("Hola Ingresa tu nombre: ")
calificaciones = []
promedio = 0

for i in range(3):
    calificacion = (float(input(f"Ingrese la calificacion {i + 1}: ")))
    if calificacion < 0 or calificacion > 100:
        print("Calificacion invalidad")
        break

    calificaciones.append(calificacion)

if len(calificaciones) == 3:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"El promedio de {nombre} es: {promedio}")
    if promedio < 70:
        print("Reprobado")
    elif promedio < 90:
        print("Aprobado")
    else:
        print("Excelente")

    print("Gracias por participar en la evaluacion")