# Objetivos de la semana: Introducir la estructura de datos en memoria mediante arreglos unidimensionales (vectores).
# Aplicar las operaciones básicas con vectores: inicialización, carga de datos por teclado y recorrido.

# Ningún torneo empieza con los jugadores ya anotados por arte de magia. Nuestro sistema necesita un módulo de inscripción
# para que el juez registre a los competidores antes de repartir puntos.

# a) Ingreso de jugadores
def cargar_jugadores():
    jugadores = []
    
    while True:
        try:
            cantidad_jugadores = int(input("¿Cuántos jugadores van a participar en el torneo? "))
            if cantidad_jugadores > 0:
                break
            print("Debe ingresar un número mayor a 0.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    for i in range(cantidad_jugadores):
        print(f"\n--- Jugador {i + 1} ---")
        nombre = input("Ingrese el nombre del jugador: ").strip()
        categoria = input("Ingrese la categoría (por ejemplo 4ª, 5ª o 6ª): ").strip()
        
        # Guardamos a cada jugador como un diccionario en el vector de jugadores
        jugadores.append({'nombre': nombre, 'categoria': categoria})

    return jugadores


# b) Armado de parejas
def armar_parejas(jugadores):
    parejas = []
    # Hacemos una copia para ir sacando a los jugadores que ya fueron elegidos
    jugadores_disponibles = jugadores.copy()
    
    cantidad_parejas = len(jugadores) // 2

    if cantidad_parejas == 0:
        print("\nNo hay suficientes jugadores para armar al menos una pareja.")
        return parejas

    for i in range(cantidad_parejas):
        print(f"\n=== Armado de la Pareja {i + 1} ===")
        nombre_pareja = input("Ingrese el nombre de la pareja: ").strip()

        mientras_sea_invalido = True
        while mientras_sea_invalido:
            print("\nJugadores disponibles:")
            for j, jugador in enumerate(jugadores_disponibles):
                print(f"{j + 1}. {jugador['nombre']} (Categoría: {jugador['categoria']})")

            try:
                indices_input = input("\nIngrese los números de los dos jugadores separados por una coma (ejemplo: 1,2): ")
                indices = [int(x.strip()) - 1 for x in indices_input.split(',')]

                if len(indices) != 2:
                    print("Error: Debe seleccionar exactamente dos jugadores.")
                    continue

                if indices[0] == indices[1]:
                    print("Error: No puede seleccionar al mismo jugador dos veces.")
                    continue

                if any(idx < 0 or idx >= len(jugadores_disponibles) for idx in indices):
                    print("Error: Uno o ambos números seleccionados no corresponden a la lista.")
                    continue

                # Selección válida
                j1 = jugadores_disponibles[indices[0]]
                j2 = jugadores_disponibles[indices[1]]

                pareja = {
                    'nombre': nombre_pareja,
                    'jugadores': [j1, j2]
                }
                parejas.append(pareja)

                # Eliminamos los jugadores seleccionados para que no vuelvan a elegirse
                # Eliminamos primero el índice mayor para no desordenar el menor
                for idx in sorted(indices, reverse=True):
                    jugadores_disponibles.pop(idx)

                mientras_sea_invalido = False

            except ValueError:
                print("Error: Ingrese números válidos separados por coma.")

    # Aviso si quedó alguien sin pareja
    if len(jugadores_disponibles) > 0:
        print("\n[Aviso] El siguiente jugador quedó sin pareja por ser un número impar de inscriptos:")
        for j in jugadores_disponibles:
            print(f"- {j['nombre']}")

    return parejas


def main():
    print("=== SISTEMA DE INSCRIPCIÓN Y PAREJAS DE PÁDEL ===")
    
    # 1. Carga de jugadores en memoria
    jugadores = cargar_jugadores()

    # 2. Armado de parejas en memoria
    parejas = armar_parejas(jugadores)

    # 3. Mostrar resumen de los datos procesados en la ejecución
    print("\n" + "="*40)
    print("RESUMEN DEL TORNEO")
    print("="*40)

    print("\nJugadores inscriptos:")
    for jugador in jugadores:
        print(f"- {jugador['nombre']} (Categoría: {jugador['categoria']})")

    print("\nParejas formadas:")
    if parejas:
        for pareja in parejas:
            print(f"• Pareja: {pareja['nombre']}")
            print(f"  Integrantes: {pareja['jugadores'][0]['nombre']} y {pareja['jugadores'][1]['nombre']}")
            print("-" * 20)
    else:
        print("No se formaron parejas.")


if __name__ == "__main__":
    main()