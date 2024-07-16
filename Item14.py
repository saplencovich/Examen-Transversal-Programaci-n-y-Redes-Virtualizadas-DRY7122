def tipo_acl(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        return "Corresponde a una Vlan Estándar"
    elif numero_acl >= 100 and numero_acl <= 99:
        return "Corresponde a una Vlan Extendida"
    else:
        return "El número no corresponde a una lista de acceso"
while True:
    try:
        numero_acl = int(input("Por favor, ingrsar el número  de ACL IPv4: "))
        tipo = tipo_acl(numero_acl)
        print("Tipo de ACL:", tipo)
        break
    except ValueError:
        print("Error, Ingrese un valor válido para ACL IPv4.")