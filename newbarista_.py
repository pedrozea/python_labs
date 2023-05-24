# Requerimientos:
# - Menu dinámico
#       - Ya no debe ser un string, sino dinamico con una lista.
#       - Si ya no hay unidades dipsoniles, lo debe eliminar de la lista. Debe controlarse el stock para cada producto.
#       - Cada producto debe tener un máximo de unidades
# - Precios dinámicos
#       - Cada producto debe tener un precio diferente
# - Valores que se puedan modificar

# User arrays, inventarios, tuplas. Condicionales, reocrridos, for o while.

#INGRESO AL SERVICIO
print("---------------------------\nHola! Bienvenido a la cafetería de Alejo.\n---------------------------")
nombre = input("Como te llamas?\n")

#DEFINICION DE PRODUCTOS Y MENU
menuStock = {
    "Cafe": {
        "Unidades":50,
        "Precio" : 1.5
    },
    "Te":{
        "Unidades":30,
        "Precio" : 2.2
        },  
    "Agua":{
        "Unidades":50,
        "Precio" : 1
        },  
    "Jugo":{
        "Unidades":45,
        "Precio" : 3
        },
    "Soda":{
    "Unidades":36,
    "Precio" : 4
    }
    }

#TOMA DE ORDEN
menuCliente = "\n -".join(menuStock)
precioTotal = 0

barAbierto=True
while barAbierto == True:
    orden = input("Hola " + nombre + "! Que deseas ordenar de nuestro menú?\n -" + menuCliente+ "\n")
    print(f"El precio unitario de {orden} es {menuStock[orden]['Precio']} USD")
    unidades = int(input("Cuantas unidades deseas?\n"))

    #CALCULO DE PRECIOS
    precioTotal += (menuStock[orden]["Precio"]) * unidades

    #EVALUACION DE UNIDADES
    if unidades > (menuStock[orden]["Unidades"]):
        print(f"Lo sentimos, pero solo tenemos {menuStock[orden]['Unidades']} unidades disponibles de {orden}")
    else:
    #RESULTADO EN PANTALLA
        menuStock[orden]["Unidades"] -= unidades 
        print(nombre, ", el valor total de tu orden es $", precioTotal, "USD")
        print("Tu " + orden + " estará lista en un momento!")
        print(f"Quedan {menuStock[orden]['Unidades']} unidades de {orden}")

    continuar = input(f"¿Deseas agregar mas productos a tu orden?\nsi\nno\n")
    if continuar == "no":
        barAbierto = False

print(f"Aqui está el resumen de tu orden:\n Productos: {orden} \n Cantidad: {unidades} \n Precio Total: {precioTotal} USD")