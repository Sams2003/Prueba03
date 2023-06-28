import os
import time
import numpy

hotel = numpy.zeros((5,2),int)
lista_nombre = []
lista_rut = []
lista_nom_mas = []
lista_id_mascota = []
lista_fila = []
lista_columna = []
lista_cant_dias = []
total_pagar = 0

def ver_menu():
    print("Menú")
    print("******")
    print("1) grabar")
    print("2) buscar")
    print("3) retirarse")
    print("4) salir")
    
def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese unas de las opciones: "))
            if opcion in (1,2,3,4):
                return opcion
        except:
            print("ERROR! DEBE INGRESAR NÚMERO ENTEROS")

def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut(sin punto ni digito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! RUT INVALIDO")
        except:
            print("ERROR! DEBE INGRESAR NÚMEROS ENTEROS")
            
def validar_nombre():
    while True:
        nom = input("Ingrese nombre: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
            
def validar_dia():
    while True:
        try:
            cant_dias= int(input("Ingrese cantidad de dias"))
            if cant_dias > 0:
                return cant_dias
        except:
            print("ERROR! DEBE INGRESAR NÚMERO ENTEROS")
            
def validar_nom_mas():
    while True:
        nom = input("Ingrese nombre de la mascota: ")
        if len(nom.strip()) >= 3 and nom.isalpha():
            return nom
        else:
            print("ERROR! DEBE TENER AL MENOS 3 LETRAS!")
            
def ind_mas():
    contador = 1
    print("El id de su mascota es el: ", contador)
    contador += 1
            
def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese número columna(1-2): "))
            if columna >= 1 and columna <= 2:
                return columna
            else:
                print("ERROR! COLUMNA INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            
def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese número fila(1-5): "))
            if fila >= 1 and fila <= 5:
                return fila
            else:
                print("ERROR! FILA INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
            
def grabar():
    os.system('cls')
    print("RESERVA")
    for x in range (5):
        for y in range(2):
            print( "\t" [x],[y], end=" " "\n")
            print()
        print("llene sus datos")
        rut = validar_rut()
        nombre = validar_nombre()
        id_mascota = ind_mas()
        nom_mascota = validar_nom_mas()
        cant_dias = validar_dia()
        fila = validar_fila()
        columna = validar_columna()
        lista_rut.append(rut)
        lista_nombre.append(nombre)
        lista_id_mascota.append(id_mascota)
        lista_nom_mas.append(nom_mascota)
        lista_cant_dias.append(cant_dias)
        lista_fila.append(fila)
        lista_columna.append(columna)
        print("Mascota registrada")
        return
time.sleep(3)            
            
def buscar():
    os.system('cls')
    print("Busca tu mascota")
    rut = validar_rut()
    for rut in (lista_rut):
        if rut in lista_rut:
            print (f"Su mascota se ubica en: {lista_columna} {lista_fila}")
            return
        else:
            print("Rut no encontrado")
            return
time.sleep(3)
        
def retirarse():
    os.system('cls')
    print("Retirarse y pagar")
    rut = validar_rut()
    for rut in (lista_rut):
        if rut in lista_rut:
            print(f"Su mascota se quedo {lista_cant_dias}")
            total_pagar = lista_cant_dias * 15000
            print(f"El total a pagar es de {total_pagar}")
            x = "mascota_eliminada"
            lista_rut.pop(x)
            lista_nombre.pop(x)
            lista_nom_mas.pop(x)
            lista_id_mascota.pop(x)
            lista_cant_dias.pop(x)
            lista_fila.pop(x)
            lista_columna.pop(x)
            return
        else:
            print("Rut no encontrado")
time.sleep(3)
        
def salir():
    print("Gracias por preferirnos")
    exit