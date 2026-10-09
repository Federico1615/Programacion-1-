#Crear una solucion logica estructurada en python usando arreglos, registros y funcoines. para la siguente pregunta.


# Yo quiero saber cuando uno de los siguentes alumnos esta o no esta regular ?

#alumnos = { nombre: "Juan", notas: [7, 8, 9, 6], asistencia: 90 },
# nombre: "Maria", notas: [5, 6, 4, 7], asistencia: 60 },
#{ nombre: "Pedro", notas: [1, 9, 4, 7], asistencia: 95 },
#{ nombre: "Ana", notas: [6, 5, 7, 8], asistencia: 85 }

def esta_regular(alumno):
    promedio = sum(alumno['notas']) / len(alumno['notas'])
    if promedio >= 6 and alumno['asistencia'] >= 75:
        return True
    else:
        return False

alumnos = [
    { "nombre": "Juan", "notas": [7, 8, 9, 6], "asistencia": 90 },
    { "nombre": "Maria", "notas": [5, 6, 4, 7], "asistencia": 60 },
    { "nombre": "Pedro", "notas": [1, 9, 4, 7], "asistencia": 95 },
    { "nombre": "Ana", "notas": [6, 5, 7, 8], "asistencia": 85 }
]

for alumno in alumnos:
    if esta_regular(alumno):
        print(f"{alumno['nombre']} está regular.")
    else:
        print(f"{alumno['nombre']} no está regular.")

def main():
    for alumno in alumnos:
        if esta_regular(alumno):
            print(f"{alumno['nombre']} está regular.")
        else:
            print(f"{alumno['nombre']} no está regular.")

if __name__ == "__main__":
    main()  



