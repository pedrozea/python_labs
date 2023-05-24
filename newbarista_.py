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

menuStock = ["Café", "Té", "Agua", "Cola", "Refresco", "Jugo"]

menu = "Café, Té y Agua"

orden = input("Hola " + nombre + "! Que deseas ordenar de nuestro menú?\n" + menu + "\n")

precio = 10

unidades = int(input("Cuantas unidades deseas?\n"))

maxUnidades = 50

if unidades > maxUnidades:
    print("Lo sentimos, pero solo tenemos " + str(maxUnidades) + " unidades disponibles de " + orden)
else:
    valorTotal = unidades*precio
    print("El valor total de tu orden es $", valorTotal, "USD")
    print(nombre + " tu " + orden + " estará en un momento")