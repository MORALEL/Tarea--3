lista_alumnos = []

def agregar_alumno(nombre, cedula, curso, nota):
    alumno ={
        'nombre': nombre,
        'cedula': cedula,
        'curso': curso,
        'nota': nota
    }
    lista_alumnos.append(alumno)


def consultar_alumnos():
    return lista_alumnos

def contar_alumnos():
    return len(lista_alumnos)

#Da el promedio
def consultar_promedio():
    if not lista_alumnos:
        return 0 
    
    total= 0
    cantidad = 0
    for alumno in lista_alumnos:
        try:
            nota= float(alumno["nota"])
            total += nota
            cantidad += 1
        except (ValueError, TypeError):
            print(f"Nota inválida para el alumno: {alumno['nombre']}")
    if cantidad == 0:
        return 0
    
    return total / cantidad

#Da las Calificaciones de los estudiante
def clasificar_estudiantes():
    aprobados = 0
    aplazados = 0
    reprobados = 0
    superior = 0

    promedio = consultar_promedio()

    for alumno in lista_alumnos:
        try:
            nota = float(alumno["nota"])
            if nota > 70:
                aprobados += 1
            elif 60 <= nota <= 69:
                aplazados += 1
            else:
                reprobados +=1
            if nota > promedio:
                superior += 1

        except (ValueError, TypeError):
             print(f"Nota inválida para el alumno: {alumno['nombre']}")

    return aprobados, aplazados, reprobados, superior
