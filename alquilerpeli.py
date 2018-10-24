import os
global listPeli
global listUsu


listUsu = list()
listPeli = list()
dicusuario = {}
dicpelis = {}

class Usuario:
    nombre = ""
    apellido = ""

class Pelicula():
      codigo=""
      titulo=""

def menu():
    os.system('clear')
    print("-------------------------------")
    print("Seleccione la opcion que desee")
    print("-------------------------------")
    print("1.Ingresar usuarios")
    print("2.Ingreso de peliculas")
    print("3.Busqueda de usuario/peliculas")
    print("4.Arrendar ")
    print("5.Eliminacion de usuario/peliculas")
    print("6.Ver arrendamientos")
    print("7.Administar peliculas")
    print("8.Listar Usuarios Registrados")
    print("9. salir","\n")
    print("-------------------------------")

def submenu():

    print("-------------------------------")
    print("Seleccione una de las 3 opciones que desee")
    print("1.Busqueda de Usuario")
    print("2.Busqueda de Pelicula")
    print("3. Atras")
    print("--------------------------------")
    while True:
      opsubmenu=input("Ingrese una opcion")
      if(opsubmenu=="1"):
        print("")
        buscarUsuario()
      elif(opsubmenu=="2"):
        print ("")
        buscarPelicula()
      elif opsubmenu=="3":
        break
      else:
        print ("")
        input("No has pulsado ninguna opción correcta")


def registrarUsuario():
    print("Registro de usuario","\n")
    a = Usuario()

    while True:
       name=a.nombre = input("Ingrese nombre: ")
       lastname=a.apellido = input("Ingrese apellido: ")
       listUsu.append(a)
       dicusuario[name]=lastname
       terminar = input ("Termina? (S, N) :")
       if terminar == "S" :
          menu()
          break
       print(dicusuario)
    return dicusuario

def registrarPelicula():
    print("Registro de peliculas","\n")
    p = Pelicula()
    dicpelis={}
    while True:
       code=p.codigo = input("Ingrese el codigo de la pelicula: ")
       title=p.titulo = input("Ingrese el titulo de la pelicula: ")
       listPeli.append(p)
       dicpelis[code]=title
       terminar = input ("Termina? (S, N) :")
       if terminar == "S" :
          menu()
          break
       print(dicpelis)
    return dicpelis


def listarUsuario():
    print("Listado de usuarios: ","\n")
    for nom, ape in dicusuario.items():
      print(nom, ":", ape)
    print("------------------")

def listarPelicula():
    print("Listado de peliculas: ","\n")
    for codi, ti in dicpelis.items():
      print(codi, ":", ti)
    print("------------------")

def buscarUsuario():
    print("Búsqueda de usuario")

    busqueda = input("Ingrese el nombre o apellido a buscar: ")
    for nom,ape in dicusuario.items():
        if(nom == busqueda or ape == busqueda):
            print("------------------")
            print("Su dato ha sido encontrado con exito!")
            print("--> ",nom, ":", ape)
            print("------------------")

def buscarPelicula():
    print("Búsqueda de Pelicula")

    busquedapeli = input("Ingrese el titulo de la pelicula a buscar: ")
    for cod,tit in dicpelis.items():
        if(cod == busquedapeli or tit == busquedapeli):
            print("------------------")
            print("Su dato ha sido encontrado con exito!")
            print("--> ",cod, ":", tit)
            print("------------------")

while True:
    menu()
    opmenu=input("Ingrese una opcion")
    if opmenu=="1":
        print("")

        registrarUsuario()
    elif opmenu=="2":
        print ("")
        registrarPelicula()

    elif opmenu=="3":
        print ("")
        submenu()

    elif opmenu=="4":
        print ("")
        input("Seleccionaste opcion 4")
    elif opmenu=="5":
        print ("")
        input("Seleccionaste opcion 5")
    elif opmenu=="6":
        print ("")
        listarPelicula()
    elif opmenu=="7":
        print ("")
        input("Seleccionaste opcion 7")
    elif opmenu=="8":
        print ("")
        listarUsuario()
    elif opmenu=="9":
        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta")
