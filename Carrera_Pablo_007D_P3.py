
from funciones import *

lista_ruts = []
lista_nombres = []
lista_ids = []
lista_nombres_m = []
lista_cantidad_dias = []
lista_filas = []
lista_columnas = []
array = numpy.zeros((2,5),int)
contador = 0
while True:
    limpiarPantalla()
    MostrarMenu("Hotel de mascotas", "Grabar","Buscar","Retirarse","Salir")
    op = validar_opcion_menu()
    if op == 1:
        if 0 not in array:
            print("No quedan habitaciones disponibles):\nRegrese mas tarde")
            continue
        rut = validar_rut()
        if rut in lista_ruts:
            print("Usted ya a registrado a su mascota")
            continue
        nombre_d = validar_nombre("del dueño")
        contador += 1
        for x in range(rut):
            pid = str(x * 2)
        id = str(contador)+pid
        nombre_m = validar_nombre("de la mascota")
        cantidad_dias = validar_cantidad_simple()
        lista_ruts.append(rut)
        lista_nombres.append(nombre_d)
        lista_ids.append(id)
        lista_nombres_m.append(nombre_m)
        lista_cantidad_dias.append(cantidad_dias)
        mostrarArray(array)
        while True:
            fila = validarAsiento("fila", 2)
            columna = validarAsiento("columna", 5)
            if array[fila-1][columna-1] == 0:
                break
            else:
                print("Esta habitacion ya esta ocupada, porfavor tome otra")
        lista_filas.append(fila-1)
        lista_columnas.append(columna-1)
        posicion = lista_ruts.index(rut)
        array[fila-1][columna-1] = 1
        esperarTecla(True, 1)
    elif op == 2:
        rut = validar_rut()
        if rut in lista_ruts:
            posicion = lista_ruts.index(rut)
            print(f"Su mascota {lista_nombres_m[posicion]} esta en la habitacion de la fila {lista_filas[posicion]+1} de la columna {lista_columnas[posicion]+1} comiendo sobrecitos")
            esperarTecla(True, 2)
        else:
            print("Usted aun no registra a ninguna mascota")
    elif op == 3:
        rut = validar_rut()
        if rut in lista_ruts:
            posicion = lista_ruts.index(rut)
            total = lista_cantidad_dias[posicion] * 15000
            print(f"Su total a pagar es {total}")
            array[lista_filas[posicion]][lista_columnas[posicion]] = 0
            lista_ruts.pop(posicion)
            lista_nombres.pop(posicion)
            lista_ids.pop(posicion)
            lista_nombres_m.pop(posicion)
            lista_cantidad_dias.pop(posicion)
            lista_filas.pop(posicion)
            lista_columnas.pop(posicion)
            esperarTecla(True, 1)
        else:
            print("Usted aun no registra a ninguna mascota")
    else:
        funcionSalir()
        break
print("Muchas gracias vielva pronto")
