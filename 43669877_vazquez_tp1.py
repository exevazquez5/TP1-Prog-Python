#Datos: DNI, NOMBRE, DIRECCION, TELEFONO, CORREO, CLIENTE PREFERENTE S/N

clientes = {}

def agregar_cliente():
    global clientes
    dni = int(input('Ingrese un DNI: '))
    nom = input('Ingrese un nombre y apellido: ')
    direc = input('Ingrese una dirección: ')
    tel = int(input('Ingrese un número de teléfono: '))
    mail = input('Ingrese un correo electrónico: ')
    pref = input('¿El cliente es preferente? Ingrese S/N: ')

    clientes[dni] = nom, direc, tel, mail, pref
    print('*** CLIENTE AGREGADO CON ÉXITO ***')

def borrar_cliente(dni):
    global clientes
    del(clientes[dni])
    print('*** CLIENTE ELIMINADO CON ÉXITO ***')

def mostrar_datos_cliente(dni):
    global clientes
    print(clientes[dni])

def listar_clientes():
    global clientes
    for pers in clientes:
        print(
    """ 
        DNI: {}
        Nombre: {}
        Dirección: {}
        Teléfono: {}
        Correo: {}
        Preferente: {}                   
    """.format(pers, clientes[pers][0], clientes[pers][1], clientes[pers][2], clientes[pers][3], clientes[pers][4]))

def listar_clientes_pref():
    for i in range(len(clientes)):
        if clientes.get(pref) == "S" or i == "s":
            print(clientes)
        else:
            print('*** NO HAY CLIENTES PREFERENTES ***')

while True:
    print("MENÚ [SELECCIONE ALGUNA OPCIÓN]\n"
          "1. Añadir cliente: \n"
          "2. Eliminar cliente: \n"
          "3. Mostrar datos de un cliente: \n"
          "4. Listar todos los clientes con nombre y DNI: \n"
          "5. Listar clientes preferentes con nombre y DNI: \n"
          "6. Salir.\n")

    opcion = int(input('Selecciona una opcion: '))

    if opcion==1:
        agregar_cliente()
    elif opcion==2:
        dni = int(input('*** Ingrese el DNI del cliente a eliminar: '))
        borrar_cliente(dni)
    elif opcion==3:
        dni=int(input('Ingrese el DNI del cliente: '))
        mostrar_datos_cliente(dni)
    elif opcion==4:
        listar_clientes()
    elif opcion==5:
        listar_clientes_pref()
    elif opcion==6:
        exit(0)
    else:
        print('*** Opción invalida ***')