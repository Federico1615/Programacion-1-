
	Algoritmo BuffetFacultad
		
		// ---------------------------------------------------
		// DECLARACIÓN DE VARIABLES Y ESTRUCTURAS
		// ---------------------------------------------------
		Dimension dias[5]
		dias[1] <- "Lunes"
		dias[2] <- "Martes"
		dias[3] <- "Miércoles"
		dias[4] <- "Jueves"
		dias[5] <- "Viernes"
		
		// Matriz de ventas: 5 días (filas) x 6 productos (columnas)
		Dimension ventas[5, 6]
		
		// Inicialización de la matriz en cero
		Para f <- 1 Hasta 5 Con Paso 1 Hacer
			Para c <- 1 Hasta 6 Con Paso 1 Hacer
				ventas[f, c] <- 0
			FinPara
		FinPara
		
		// Catálogo de productos (Código, Nombre, Precio)
		Dimension codigos[6]
		Dimension nombres[6]
		Dimension precios[6]
		
		codigos[1] <- 101; nombres[1] <- "Café con leche"; precios[1] <- 1500
		codigos[2] <- 102; nombres[2] <- "Medialuna"; precios[2] <- 700
		codigos[3] <- 103; nombres[3] <- "Sándwich de miga"; precios[3] <- 1800
		codigos[4] <- 104; nombres[4] <- "Agua mineral 500 ml"; precios[4] <- 1000
		codigos[5] <- 105; nombres[5] <- "Empanada"; precios[5] <- 1200
		codigos[6] <- 106; nombres[6] <- "Chipá (100 g)"; precios[6] <- 1300
		
		opcion <- 0
		
		// ---------------------------------------------------
		// MENÚ PRINCIPAL
		// ---------------------------------------------------
		Repetir
			Escribir ""
			Escribir "=== MENU BUFFET FACULTAD ==="
			Escribir "1. Registrar una venta"
			Escribir "2. Ver informes semanales"
			Escribir "3. Cargar datos del cuaderno (Prueba)"
			Escribir "4. Salir"
			Escribir "Seleccione una opción: " Sin Saltar
			Leer opcion
			
			Según opcion Hacer
		1:
			Escribir ""
			Escribir "--- REGISTRAR VENTA ---"
			Escribir "1: Lunes | 2: Martes | 3: Miércoles | 4: Jueves | 5: Viernes"
			Escribir "Ingrese día (1-5): " Sin Saltar
			Leer numDia
			
			Si numDia >= 1 Y numDia <= 5 Entonces
				Escribir "Ingrese código del producto (101-106): " Sin Saltar
				Leer codIngresado
				
				// Buscamos la posición del producto
				posProd <- -1
				Para i <- 1 Hasta 6 Con Paso 1 Hacer
					Si codigos[i] = codIngresado Entonces
						posProd <- i
					FinSi
				FinPara
				
				Si posProd <> -1 Entonces
					Escribir "Ingrese cantidad vendida: " Sin Saltar
					Leer cantidad
					
					Si cantidad > 0 Entonces
						ventas[numDia, posProd] <- ventas[numDia, posProd] + cantidad
						Escribir "-> Venta registrada: ", cantidad, " x ", nombres[posProd], " para el ", dias[numDia]
					Sino
						Escribir "Error: La cantidad debe ser mayor a 0."
					FinSi
				Sino
					Escribir "Error: El producto no existe en el catálogo."
				FinSi
			Sino
				Escribir "Error: Día no válido."
			FinSi
			
		2:
			Escribir ""
			Escribir "=================================================="
			Escribir "           INFORMES DE VENTAS DE LA SEMANA        "
			Escribir "=================================================="
			
			// 1. Unidades vendidas por producto
			Escribir ""
			Escribir "1. UNIDADES VENDIDAS POR PRODUCTO:"
			Dimension totalesProd[6]
			Para c <- 1 Hasta 6 Con Paso 1 Hacer
				sumaProd <- 0
				Para f <- 1 Hasta 5 Con Paso 1 Hacer
					sumaProd <- sumaProd + ventas[f, c]
				FinPara
				totalesProd[c] <- sumaProd
				Escribir " - ", nombres[c], ": ", totalesProd[c], " unidades"
			FinPara
			
			// 2. Recaudación por día
			Escribir ""
			Escribir "2. RECAUDACIÓN POR DÍA:"
			Dimension recDias[5]
			recTotalSemana <- 0
			Para f <- 1 Hasta 5 Con Paso 1 Hacer
				sumaDia <- 0
				Para c <- 1 Hasta 6 Con Paso 1 Hacer
					sumaDia <- sumaDia + (ventas[f, c] * precios[c])
				FinPara
				recDias[f] <- sumaDia
				recTotalSemana <- recTotalSemana + sumaDia
				Escribir " - ", dias[f], ": $", recDias[f]
			FinPara
			
			// 3. Producto más vendido
			maxUnidades <- totalesProd[1]
			Para c <- 2 Hasta 6 Con Paso 1 Hacer
				Si totalesProd[c] > maxUnidades Entonces
					maxUnidades <- totalesProd[c]
				FinSi
			FinPara
			
			Escribir ""
			Si maxUnidades > 0 Entonces
				Escribir "3. PRODUCTO(S) MÁS VENDIDO(S) (", maxUnidades, " unidades):"
				Para c <- 1 Hasta 6 Con Paso 1 Hacer
					Si totalesProd[c] = maxUnidades Entonces
						Escribir " - ", nombres[c]
					FinSi
				FinPara
			Sino
				Escribir "3. PRODUCTO MÁS VENDIDO: No se registraron ventas."
			FinSi
			
			// Día de mayor recaudación
			maxRec <- recDias[1]
			Para f <- 2 Hasta 5 Con Paso 1 Hacer
				Si recDias[f] > maxRec Entonces
					maxRec <- recDias[f]
				FinSi
			FinPara
			
                Si maxRec
FinAlgoritmo
