#! /usr/bin/python3

import sys
import datetime
import socket

nombre = input("Como te llamas?\n")

fecha_actual = datetime.date.today()
mysystem=sys.version

#Funciones----------------------------------------------------

def prueba1(nombre):
    saludo="estimado " + nombre
    return saludo
    
def obtener_direccion_ip():
    hostname = socket.gethostname()
    direccion_ip = socket.gethostbyname(hostname)
    return direccion_ip

#Imprimir resultado en pantalla-----------------------------------------

print("--------------------------------------------\nHola", prueba1(nombre), "!! Bienvenido a AWS Cloud9. Has ejecutado este script usando Python en", fecha_actual, "y tu IP address es", obtener_direccion_ip(), "\n--------------------------------------------")