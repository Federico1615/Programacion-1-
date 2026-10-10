# 1. Arreglo de Diccionarios para el catálogo
catalogo = [
    {"codigo": 101, "nombre": "Café con leche", "precio": 1500},
    {"codigo": 102, "nombre": "Medialuna", "precio": 700},
    {"codigo": 103, "nombre": "Sándwich de miga", "precio": 1800},
    {"codigo": 104, "nombre": "Agua mineral", "precio": 1000},
    {"codigo": 105, "nombre": "Empanada", "precio": 1200},
    {"codigo": 106, "nombre": "Chipá", "precio": 1300}
]

def cargar_ventas(matriz): 
    #Creamos el archivo de ventas si no existe, para evitar errores al leerlo
    archivo_crear = open("ventas_facultad.txt", "a")
    archivo_crear.close()
    
    #Ahora que sabemos que existe, lo leemos sin problemas.
    archivo = open("ventas_facultad.txt", "r")
    for linea in archivo:
        datos = linea.strip().split(",")
        if len(datos) == 3:
            dia = int(datos[0])
            codigo = int(datos[1])
            cantidad = int(datos[2])
            
            #Buscar el índice del producto en el catálogo
            for i in range(len(catalogo)):
                if catalogo[i]["codigo"] == codigo:
                    matriz[i][dia - 1] = matriz[i][dia - 1] + cantidad
    archivo.close()

def guardar_venta(dia, codigo, cantidad):
    #Guardamos cada venta para no perder datos
    archivo = open("ventas_facultad.txt", "a")
    archivo.write(str(dia) + "," + str(codigo) + "," + str(cantidad) + "\n")
    archivo.close()

def main():
    # 2. Matriz Bidimensional (6 productos x 5 días)
    matriz_ventas = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    
    #Cargar datos previos al arrancar
    cargar_ventas(matriz_ventas)
    
    opcion = 0
    # 3. Estructura de control repetitiva para el menú
    while opcion != 4:
        print("\nBUFFET DE LA FACULTAD")
        print("1. Ver Catálogo")
        print("2. Registrar una venta")
        print("3. Ver informes semanales")
        print("4. Salir")
        
        #Pedimos al usuario que ingrese una opcion
        opcion = int(input("Elija una opción: "))

        if opcion == 1:
            print("\nCATÁLOGO DE PRODUCTOS:")
            for prod in catalogo:
                print("[" + str(prod["codigo"]) + "] " + prod["nombre"] + " - $" + str(prod["precio"]))
                
        elif opcion == 2:
            dia = int(input("Ingrese el día (1=Lun a 5=Vie): "))
            
            if dia >= 1 and dia <= 5:
                codigo = int(input("Ingrese el código del producto: "))
                cantidad = int(input("Ingrese la cantidad vendida: "))
                
                indice_prod = -1
                # Búsqueda secuencial
                for i in range(len(catalogo)):
                    if catalogo[i]["codigo"] == codigo:
                        indice_prod = i
                        break
                        
                # 4. Estructura condicional para procesar
                if indice_prod != -1 and cantidad > 0:
                    matriz_ventas[indice_prod][dia - 1] = matriz_ventas[indice_prod][dia - 1] + cantidad
                    guardar_venta(dia, codigo, cantidad)
                    print("Venta registrada con éxito.")
                else:
                    print("Error: Código inexistente o cantidad inválida.")
            else:
                print("Día inválido. Ingrese un valor entre 1 y 5.")

        elif opcion == 3:
            print("\nINFORMES DE LA SEMANA")
            
            print("a) Unidades vendidas por producto:")
            for i in range(len(catalogo)):
                total_unid = 0
                for j in range(5):
                    total_unid = total_unid + matriz_ventas[i][j]
                print(" - " + catalogo[i]["nombre"] + ": " + str(total_unid) + " unidades")
            
            print("\nb) Recaudación por día:")
            dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
            total_semana = 0
            
            for j in range(5):
                rec_dia = 0
                for i in range(6):
                    rec_dia = rec_dia + (matriz_ventas[i][j] * catalogo[i]["precio"])
                print(" - " + dias[j] + ": $" + str(rec_dia))
                total_semana = total_semana + rec_dia
                
            print("\nRECAUDACIÓN TOTAL DE LA SEMANA: $" + str(total_semana))
            
        elif opcion == 4:
            print("Saliendo del sistema... ¡Hasta luego!")
        else:
            print("Opción inválida.")

# Llamada a la función principal
main()