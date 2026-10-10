# ===============================================================
# TRABAJO PRÁCTICO: SISTEMA DE VENTAS DEL BUFFET
# Estudiante: Federico Molina
# ===============================================================

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
ARCHIVO_PRODUCTOS = "productos.txt"
ARCHIVO_VENTAS = "ventas.txt"


def inicializar_catalogo():
    return {
        101: {"nombre": "Café con leche", "precio": 1500},
        102: {"nombre": "Medialuna", "precio": 700},
        103: {"nombre": "Sándwich de miga", "precio": 1800},
        104: {"nombre": "Agua mineral 500 ml", "precio": 1000},
        105: {"nombre": "Empanada", "precio": 1200},
        106: {"nombre": "Chipá (100 g)", "precio": 1300}
    }


def inicializar_matriz_ventas():
    matriz = []
    for f in range(5):
        fila = []
        for c in range(6):
            fila.append(0)
        matriz.append(fila)
    return matriz


def guardar_catalogo(catalogo):
    archivo = open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8")
    for codigo in catalogo:
        nombre = catalogo[codigo]["nombre"]
        precio = catalogo[codigo]["precio"]
        archivo.write(str(codigo) + ";" + nombre + ";" + str(precio) + "\n")
    archivo.close()


def cargar_catalogo():
    catalogo = {}
    try:
        archivo = open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8")
        for linea in archivo:
            linea = linea.strip()
            if linea != "":
                partes = linea.split(";")
                if len(partes) == 3:
                    codigo = int(partes[0])
                    nombre = partes[1]
                    precio = float(partes[2])
                    
                    if codigo not in catalogo:
                        catalogo[codigo] = {"nombre": nombre, "precio": precio}
                    else:
                        print("Atención: Código repetido en el archivo, se ignora:", codigo)
        archivo.close()
    except FileNotFoundError:
        print("No se encontró el archivo de productos. Se crea el catálogo por defecto.")
        catalogo = inicializar_catalogo()
        guardar_catalogo(catalogo)
    
    return catalogo


def guardar_ventas(ventas):
    archivo = open(ARCHIVO_VENTAS, "w", encoding="utf-8")
    for fila in ventas:
        linea = ""
        for i in range(len(fila)):
            linea += str(fila[i])
            if i < len(fila) - 1:
                linea += ";"
        archivo.write(linea + "\n")
    archivo.close()


def cargar_ventas():
    matriz = inicializar_matriz_ventas()
    try:
        archivo = open(ARCHIVO_VENTAS, "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
        
        if len(lineas) == 5:
            for f in range(5):
                partes = lineas[f].strip().split(";")
                if len(partes) == 6:
                    for c in range(6):
                        matriz[f][c] = int(partes[c])
    except FileNotFoundError:
        pass
        
    return matriz


def registrar_venta(ventas, catalogo, lista_codigos):
    print("\n--- REGISTRAR VENTA ---")
    print("1: Lunes | 2: Martes | 3: Miércoles | 4: Jueves | 5: Viernes")
    
    dia = int(input("Ingrese día (1 a 5): "))
    while dia < 1 or dia > 5:
        print("Día no válido.")
        dia = int(input("Ingrese día (1 a 5): "))
    
    codigo = int(input("Ingrese código del producto: "))
    if codigo not in catalogo:
        print("Error: El producto no existe en el catálogo.")
        return

    cantidad = int(input("Ingrese cantidad vendida: "))
    while cantidad <= 0:
        print("La cantidad debe ser mayor a 0.")
        cantidad = int(input("Ingrese cantidad vendida: "))

    columna = -1
    for i in range(len(lista_codigos)):
        if lista_codigos[i] == codigo:
            columna = i

    ventas[dia - 1][columna] += cantidad
    print("-> Venta registrada con éxito:", cantidad, "x", catalogo[codigo]["nombre"], "para el día", DIAS[dia - 1])


def mostrar_informes(ventas, catalogo, lista_codigos):
    print("\n==================================================")
    print("           INFORMES DE VENTAS DE LA SEMANA         ")
    print("==================================================")

    # 1. Unidades vendidas por producto
    print("\n1. UNIDADES VENDIDAS POR PRODUCTO:")
    totales_por_producto = []
    for c in range(6):
        suma_columna = 0
        for f in range(5):
            suma_columna += ventas[f][c]
        totales_por_producto.append(suma_columna)
        codigo = lista_codigos[c]
        print(" -", catalogo[codigo]["nombre"], ":", suma_columna, "unidades")

    # 2. Recaudación por día
    print("\n2. RECAUDACIÓN POR DÍA:")
    recaudacion_dias = []
    recaudacion_total = 0
    for f in range(5):
        suma_fila = 0
        for c in range(6):
            codigo = lista_codigos[c]
            precio = catalogo[codigo]["precio"]
            suma_fila += ventas[f][c] * precio
        recaudacion_dias.append(suma_fila)
        recaudacion_total += suma_fila
        print(" -", DIAS[f], ": $", suma_fila)

    # 3. Producto más vendido
    max_unidades = 0
    for cant in totales_por_producto:
        if cant > max_unidades:
            max_unidades = cant

    print("\n3. PRODUCTO(S) MÁS VENDIDO(S):")
    if max_unidades > 0:
        for i in range(len(totales_por_producto)):
            if totales_por_producto[i] == max_unidades:
                codigo = lista_codigos[i]
                print(" -", catalogo[codigo]["nombre"], "(", max_unidades, "unidades )")
    else:
        print(" - No se registraron ventas en la semana.")

    # Día de mayor recaudación
    max_recaudacion = 0
    for rec in recaudacion_dias:
        if rec > max_recaudacion:
            max_recaudacion = rec

    print("\n   DÍA DE MAYOR RECAUDACIÓN:")
    if max_recaudacion > 0:
        for f in range(5):
            if recaudacion_dias[f] == max_recaudacion:
                print("   -", DIAS[f], "( $", max_recaudacion, ")")
    else:
        print("   - No hubo ingresos registrados.")

    # 4. Productos sin ventas
    print("\n4. PRODUCTOS SIN VENTAS:")
    hubo_sin_ventas = False
    for i in range(len(totales_por_producto)):
        if totales_por_producto[i] == 0:
            codigo = lista_codigos[i]
            print(" -", catalogo[codigo]["nombre"])
            hubo_sin_ventas = True
    if not hubo_sin_ventas:
        print(" - Todos los productos registraron al menos una venta.")

    # 5. Recaudación Total
    print("\n5. RECAUDACIÓN TOTAL DE LA SEMANA: $", recaudacion_total)
    print("==================================================\n")


def cargar_datos_prueba_cuaderno(ventas, lista_codigos):
    ventas[0] = [30, 40, 10, 20, 15, 0]  # Lunes
    ventas[1] = [25, 38, 12, 22, 0, 0]   # Martes
    ventas[2] = [28, 45, 8, 18, 20, 0]   # Miércoles
    ventas[3] = [35, 50, 15, 25, 18, 0]  # Jueves
    ventas[4] = [20, 30, 9, 30, 25, 0]   # Viernes
    print("-> Datos del cuaderno cargados exitosamente.")


def main():
    catalogo = cargar_catalogo()
    
    lista_codigos = []
    for k in catalogo:
        lista_codigos.append(k)
    lista_codigos.sort()

    ventas = cargar_ventas()

    opcion = 0
    while opcion != 4:
        print("\n=== MENU BUFFET FACULTAD ===")
        print("1. Registrar una venta")
        print("2. Ver informes semanales")
        print("3. Cargar datos del cuaderno (Prueba)")
        print("4. Guardar y salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registrar_venta(ventas, catalogo, lista_codigos)
            guardar_ventas(ventas)
        elif opcion == 2:
            mostrar_informes(ventas, catalogo, lista_codigos)
        elif opcion == 3:
            cargar_datos_prueba_cuaderno(ventas, lista_codigos)
            guardar_ventas(ventas)
        elif opcion == 4:
            guardar_ventas(ventas)
            print("Datos guardados. Saliendo del sistema...")
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()