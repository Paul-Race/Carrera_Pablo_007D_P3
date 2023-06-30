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
