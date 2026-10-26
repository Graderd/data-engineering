#Cree una lista con cinco lenguajes de programación.
lenguajes= ["python", "java", "c++", "javascript", "ruby"]
print("Lenguajes:", lenguajes, "\n")

#Pida al usuario que escriba un lenguaje para agregarlo.
lenguaje_nuevo = input("Agregue un lenguaje de programacion a la lista: ").strip().lower()

#Agregue ese lenguaje con append().
lenguajes.append(lenguaje_nuevo)
print("Lenguaje agregado con exito.\n")

#Pida al usuario un lenguaje para eliminar.
print("Lenguajes:", lenguajes, "\n")
lenguaje_eliminar = input("Ingrese un lenguaje de programacion para eliminarlo de la lista: ").strip().lower()

#Compruebe con in si existe antes de eliminarlo con remove().
if lenguaje_eliminar in lenguajes:
    lenguajes.remove(lenguaje_eliminar)
    print(f"El lenguaje {lenguaje_eliminar} ha sido eliminado con exito. \n")
#Si no existe, muestre un mensaje indicándolo.
else:
    print(f"El lenguaje {lenguaje_eliminar} no ha sido encontrado en la lista. \n")

#Recorra la lista final utilizando for y muestre la cantidad de elementos restantes.
print("\nLenguajes de programación restantes en la lista:")
for lang in lenguajes:
    print(f"Lenguaje: {lang}")

print(f"La lista tiene {len(lenguajes)} lenguajes de programación.")