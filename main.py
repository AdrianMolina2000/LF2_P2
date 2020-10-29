import os


def datos_del_estudiante():
    print("\n==========================================")
    print("Adrian Samuel Molina Cabrera \n201903850")
    print("==========================================\n\n")



def opciones_del_menu():
    print("1. Cargar Archivo")
    print("2. Generar Grafica")
    print("3. Salir\n")


def menu_principal():
    while True:
        opciones_del_menu() 
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion in range(4):

                if opcion == 1:
                    print("Ha marcado la opcion Cargar Archivo")
                    print("==========================================\n")
                    
                elif opcion == 2:
                    print("Ha marcado la opcion Generar Grafica")
                    print("==========================================\n")
                            
                elif opcion == 3:
                    print("Saliendo...\n")
                    break
            else:
                print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                print("/////Error -> ingrese numeros del 1 al 3/////")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
        except ValueError:

            print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
            print("/////Error -> ingrese datos nuevamente/////") 
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    
if __name__ == "__main__":
    datos_del_estudiante()
    menu_principal()
    # try:
    #     menu_principal()
    # except Exception as e:
    #     print("\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    #     print("///// Error -> Error -> Error ->  Error /////") 
    #     print(e)
    #     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    #     menu_principal()