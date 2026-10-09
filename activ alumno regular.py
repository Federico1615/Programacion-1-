#Crear una solucion logica estructurada en python usando arreglos, registros y funcoines. para la siguente pregunta.


# Yo quiero saber cuando uno de los siguentes alumnos esta o no esta regular ?

#alumnos = { nombre: "Juan", notas: [7, 8, 9, 6], asistencia: 90 },
# nombre: "Maria", notas: [5, 6, 4, 7], asistencia: 60 },
#{ nombre: "Pedro", notas: [1, 9, 4, 7], asistencia: 95 },
#{ nombre: "Ana", notas: [6, 5, 7, 8], asistencia: 85 }

NOTA_MINIMA = 6
ASISTENCIA_MINIMA = 75

alumnos = [
	{"nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 90},
	{"nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 60},
	{"nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 95},
	{"nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 85},
]


def calcular_promedio(notas):
	return sum(notas) / len(notas)


def esta_regular(alumno):
	promedio = calcular_promedio(alumno["notas"])
	return promedio >= NOTA_MINIMA and alumno["asistencia"] >= ASISTENCIA_MINIMA


def main():
	for alumno in alumnos:
		if esta_regular(alumno):
			print(f"{alumno['nombre']} está regular")
		else:
			print(f"{alumno['nombre']} no está regular")


if __name__ == "__main__":
	main()



