edad = 22
tiene_entrada = False
es_invitado = False
esta_bloqueado = False

#Reglas del sistema:
#1. La persona debe tener 18 años o más.
#2. Debe tener una entrada o ser invitada.
#3. No puede estar bloqueada.
#4. Si cumple todo, imprime "Acceso permitido". De lo contrario, "Acceso denegado".

if edad >= 18 and (tiene_entrada or es_invitado) and not esta_bloqueado:
    print("Acceso permitido")
else:
    print("Acceso denegado")

