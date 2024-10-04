from Biblioteca_Ejercicio import *
from Funciones_Biblioteca import *

cerrar_programa = False
while cerrar_programa == False: #Bucle principal
    opcion = input("Selecciona una opción (1-5):\n1.Imprimir biblioteca completa\n2.Buscar libro por título\n3.Añadir libro\n4.Eliminar libro\n5.Salir de la biblioteca")

    if opcion == "1":
        opcion_imprimir_biblioteca()
    elif opcion== "2":
        opcion_buscar_libro_por_titulo()
    elif opcion== "3":
        opcion_añadir_libro()
    elif opcion== "4":
        opcion_eliminar()    
    elif opcion== "5":
        opcion_salir()
        cerrar_programa = True #Se cierra el bucle
    else:
        print("Opcion no válida, por favor selecciona una opción entre 1 y 5")
        