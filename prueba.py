import json

def agregar():
    with open("biblioteca.json","r") as archivo:
     contenido = archivo.read()
 
    datos = json.loads(contenido)
    libros = datos.get("Libro", [])


    id_libro = int(input("Ingrese el ID del libro: "))
    titulo_libro = (input("Ingrese el titulo del libro: "))
    id_autor = int(input("Ingrese el ID del autor del libro: "))
    id_categoria = int(input("Ingrese el ID de la categoria del libro: "))
    publicacion_ano = int(input("Ingrese el año de publicacion del libro: "))
    isbn = (input("Ingrese el isbn del libro: "))

    agregar = {
                    "LibroID": id_libro,
                    "Titulo": titulo_libro,
                    "AutorID": id_autor,
                    "CategoriaID": id_categoria,
                    "AnoPublicacion": publicacion_ano,
                    "ISBN": isbn
    }

    libros.append(agregar)

    with open("biblioteca.json","w") as archivo:
        json.dump(datos,archivo, indent=4)

def reportes():
    with open("biblioteca.json","r") as archivo:
     contenido = archivo.read()
 
    datos = json.loads(contenido)
    libros = datos.get("Libro", [])
   
    for libro in libros:
       print(f'{libros["Titulo"]}')
   
   
   
    



while True:
    print("""
    ***********************************************
    *                MUNDO LIBRO                  *
    ***********************************************
    [1]- Mantenedores de libros
    [2]- Reportes
    [3]- Salir

    """)

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        
        print("""
        ***********************************************
        *             MANTENEDOR LIBROS               *
        ***********************************************
            
        [1]- Agregar libro
        [2]- Editor Libro
        [3]- Eliminar Libro
        [4]- Buscar Libro
        [5]- Volver
        """)
        opcion_mantenedores = int(input("Seleccione una opcion: "))

        if opcion_mantenedores == 1:
         agregar()
        
        
         
        
    elif opcion == 3:
     print("Saliendo...")
     break

    elif opcion == 2:
     None

    else:
     print("No existe esa opcion.")