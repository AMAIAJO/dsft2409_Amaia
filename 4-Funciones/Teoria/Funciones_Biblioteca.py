# Definición de las funciones (Divide y vencerás)

def opcion_imprimir_biblioteca(): #Imprime el contenido completo de la biblioteca usando pprint.
    pprint.pprint(biblio)
    

def opcion_buscar_libro_por_titulo(): #Busca un libro por su título, ignorando mayúsculas/minúsculas, e imprime la información si se encuentra. Muestra un mensaje si no se encuentra el libro.
    titulo = input('Introduce el título del libro que quiere consultar: ')
    encontrado = False
    for libro in biblio:
        if libro['titulo'].lower() == titulo.lower():
            print(f"Titulo: {libro['titulo']}, Autor: {libro['autor']}, Año:{libro['año']}")
            encontrado = True
            break
    if not encontrado:
            print(f"No se encontró ningún libro con ese título")

def opcion_añadir_libro(): #Añade un libro nuevo a la biblioteca con los datos proporcionados por el usuario.
    titulo = input('Introduce el título del nuevo libro a añadir')
    autor = input('Introduce el autor del nuevo libro a añadir')
    try:
        año = int(input('Introduce el año de publicación del nuevo libro a añadir'))
        nuevo_libro = {'titulo': titulo, 'autor': autor, 'año': año}
        biblio.append(nuevo_libro)
        print(f"Libro '{titulo}' añadido con éxito a la biblioteca")
    except ValueError:
        print('El año de publicación del libro debe de ser un número, no se puede añadir libro a la biblioteca')

def opcion_eliminar(): #Elimina los libros de un autor dado. Si se encuentran, los elimina y muestra un mensaje. Si no se encuentra, informa al usuario.
    autor = input('Introduce el autor del libro a eliminar de la biblioteca')
    encontrado = 0
    for libro in biblio:
        if libro['autor'].lower() == autor.lower():
            biblio.remove(libro)
            print(f"Los libros del autor {autor} han sido eliminados de la biblioteca")
            encontrado = encontrado + 1
    
    print(f"Se han borrado {encontrado} libros del autor {autor} ")

def opcion_salir(): #Muestra un mensaje cuando se decide salir del programa.
    print('Cerrando biblioteca')