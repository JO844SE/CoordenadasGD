import os

def latitud(grados, minutos, segundos):
    """
    Convierte coordenadas de grados, minutos y segundos (GMS) a grados decimales (GD).
    
    :param grados: Grados (int)
    :param minutos: Minutos (int)
    :param segundos: Segundos (int)
    :return: Grados decimales (float)
    """
    return grados + (minutos / 60) + (segundos / 3600)

def longitud(gradoslo, minutoslo, segundoslo):
    return gradoslo + (minutoslo / 60) + (segundoslo / 3600)

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n\n\t\tMenu:\n")
    print("1. Convertir coordenadas a decimales")
    print("2. Limpiar pantalla")
    print("3. Salir\n")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == '1':
            limpiar_pantalla()
            print("\n\t\t\t\tConversión de GMS a GD\n\n")
            
            # Entrada de coordenadas
            print("\t\t*** Ingreso de datos de Latitud ***\n")
            grados = int(input("Ingrese los grados de latitud: "))
            minutos = int(input("Ingrese los minutos de latitud: "))
            segundos = float(input("Ingrese los segundos de latitud: "))
            
            print("\n\t\t*** Ingreso de datos de Longitud ***\n")
            gradoslo = int(input("Ingrese los grados de longitud: "))
            minutoslo = int(input("Ingrese los minutos de longitud: "))
            segundoslo = float(input("Ingrese los segundos de longitud: "))
            
            # Conversión
            grados_decimales_latitud = latitud(grados, minutos, segundos)
            grados_decimales_longitud = longitud(gradoslo, minutoslo, segundoslo)
            
            # Resultado
            print(f"\nCoordenadas en grados decimales: {grados_decimales_latitud:.6f}, -{grados_decimales_longitud:.6f}\n")

        elif opcion == '2':
            limpiar_pantalla()

        elif opcion == '3':
            print("Saliendo del programa...")
            limpiar_pantalla()
            break

        else:
            print("Opción no válida, por favor seleccione de nuevo.")

if __name__ == "__main__":
    main()