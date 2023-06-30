import numpy
import msvcrt
import os
import time
import random

def limpiarPantalla():
    os.system('cls')

def esperarTecla(p_incluirtiempo: bool, p_cantseg=0):
    if p_incluirtiempo == True:
        time.sleep(p_cantseg)
    print("Pulse cualquier tecla para continuar")
    msvcrt.getch()

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre(p_str):
    while True:
        nombre = input(f"Ingrese nombre {p_str}: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_correo():
    while True:
        correo = input("Ingrese correo: ")
        if "@" in correo:
            return correo
        else:
            print("ERROR! CORREO INCORRECTO!")

def MostrarMenu(p_titulo, p_opcion1, p_opcion2, p_opcion3, p_opcion4):
    print(f"""Menu {p_titulo}
            1. {p_opcion1}
            2. {p_opcion2}
            3. {p_opcion3}
            4. {p_opcion4}
            """)

def validar_cantidad(p_str:str ,p_num:int):
    while True:
        try:
            cantidad = int(input(f"Ingrese cantidad de {p_str}(1-{p_num}): "))
            if cantidad >= 1 and cantidad <= p_num:
                return cantidad
            else:
                print(f"ERROR! LA CANTIDAD DEBE ESTAR ENTRE 1 Y {p_num}!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_opcion_menu():
    while True:
        try:
            opc = int(input("Seleccione una opción: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_cantidad_simple():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de dias que se ospedara la mascota: "))
            if cantidad >= 1:
                return cantidad
            else:
                print("ERROR! LA MASCOTA DEBE HOSPEDARSE ALMENOS 1 DIA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validarAsiento(p_str, p_num):
    while True:
        try:
            num = int(input(f"Ingrese la {p_str} de la reserva: "))
            if num > 0 and num <= p_num:
                return num
            else:
                print(f"ERROR! debe ingresar una cantidad de {p_str} valida")
        except:
            print(f"ERROR! debe ingresar una cantidad de {p_str} valida")

def MostrarMenuCarta(p_producto, p_alim1, p_alim2, p_alim3, p_lista1, p_lista2, p_lista3):
    print(f"""Menu Carta {p_producto}
            Que {p_producto} desea:
            1. {p_alim1} ${p_lista1}
            2. {p_alim2} ${p_lista2}
            3. {p_alim3} ${p_lista3}
            4. Volver al menu principal
            """)

def mostrarArray(p_array):
    for x in range(2):
        print(f"Fila numero {x+1}:", end=" ")
        for i in range(5):
            print(p_array[x][i], end=" ")
        print("")
    print("      Columna: 1 2 3 4 5")

def funcionSalir():
    print("Usted saldra de la aplicacion")
    esperarTecla(True, 2)

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
