import json
from pathlib import Path


ARCHIVO_JUGADORES = Path(__file__).with_name("jugadores.json")
ARCHIVO_PAREJAS = Path(__file__).with_name("parejas.json")


#Objetivos de la semana: Introducir la estructura de datos en memoria mediante arreglos unidimensionales (vectores). Aplicar las operaciones básicas con vectores: inicialización, carga de datos por teclado y recorrido.

#Ningún torneo empieza con los jugadores ya anotados por arte de magia. Nuestro sistema necesita un módulo de inscripción para que el juez registre a los competidores antes de repartir puntos.

#Para poder poner en marcha el torneo, lo primero que necesitamos del sistema es
#poder cargar a los jugadores y luego armar las parejas que van a
#competir. Recuerden que en el pádel se juega de a dos: ninguna pareja puede
#tener más ni menos de 2 jugadores.

#a) Ingreso de jugadores

# Al iniciar el programa, el sistema debe preguntarle al juez:
 # "¿Cuántos jugadores van a participar en el torneo?".
 #A partir de esa respuesta, debe permitir registrar cada competidor, uno por
 # uno, con la siguiente información:
 #  su nombre (con el que se lo identificará dentro del torneo), y
 #  su categoría (el nivel en el que juega, por ejemplo 4ª, 5ª o 6ª).

#b) Armado de parejas

 #Una vez cargados todos los jugadores, el sistema debe permitir formar las
  #parejas del torneo.
 #Cada pareja debe tener:
  # un nombre que la identifique dentro del torneo (por ejemplo,
   # "Los Tanos"), y
   #exactamente 2 jugadores, elegidos entre los que ya fueron inscriptos.
 
def guardar_json(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, ensure_ascii=False, indent=4)


def leer_json(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def cargar_jugadores():
    jugadores = []
    cantidad_jugadores = int(input("¿Cuántos jugadores van a participar en el torneo? "))
    
    for i in range(cantidad_jugadores):
        nombre = input(f"Ingrese el nombre del jugador {i + 1}: ")
        categoria = input(f"Ingrese la categoría del jugador {i + 1} (por ejemplo 4ª, 5ª o 6ª): ")
        jugadores.append({'nombre': nombre, 'categoria': categoria})
    
    return jugadores

def armar_parejas(jugadores):
    parejas = []
    cantidad_parejas = len(jugadores) // 2
    
    for i in range(cantidad_parejas):
        nombre_pareja = input(f"Ingrese el nombre de la pareja {i + 1}: ")
        print("Seleccione los jugadores para esta pareja:")
        
        for j, jugador in enumerate(jugadores):
            print(f"{j + 1}. {jugador['nombre']} (Categoría: {jugador['categoria']})")
        
        indices_jugadores = input("Ingrese los números de los dos jugadores separados por una coma (por ejemplo: 1,2): ")
        indices_jugadores = [int(x.strip()) - 1 for x in indices_jugadores.split(',')]
        
        if len(indices_jugadores) != 2 or any(index < 0 or index >= len(jugadores) for index in indices_jugadores):
            print("Error: Debe seleccionar exactamente dos jugadores válidos.")
            continue
        
        pareja = {
            'nombre': nombre_pareja,
            'jugadores': [jugadores[indices_jugadores[0]], jugadores[indices_jugadores[1]]]
        }
        parejas.append(pareja)
    
    return parejas

def main():
    print("1. Crear un torneo nuevo")
    print("2. Consultar el último torneo guardado")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        jugadores = cargar_jugadores()
        guardar_json(ARCHIVO_JUGADORES, jugadores)
        parejas = armar_parejas(jugadores)
        guardar_json(ARCHIVO_PAREJAS, parejas)
    elif opcion == "2":
        jugadores = leer_json(ARCHIVO_JUGADORES)
        parejas = leer_json(ARCHIVO_PAREJAS)
        if not jugadores and not parejas:
            print("Todavía no hay un torneo guardado.")
            return
    else:
        print("Opción no válida.")
        return

    print("\nJugadores inscriptos:")
    for jugador in jugadores:
        print(f"{jugador['nombre']} (Categoría: {jugador['categoria']})")

    print("\nParejas formadas:")
    for pareja in parejas:
        print(f"Pareja: {pareja['nombre']}")
        print(f"Jugadores: {pareja['jugadores'][0]['nombre']} y {pareja['jugadores'][1]['nombre']}")
        print("-----")


if __name__ == "__main__":
    main()



