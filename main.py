import alumnos
import profesores
import cursos



cursos_validos = ["Programacion", "Calculo", "Administracion", "Ingles", "Estructuras"]

def menu():
    while True:
        print("\n Sistema Escolar")
        print("1.Agregar\consultar Alumnos")
        print("2.Agregar\consultar Profesores")
        print("3.Agregar\consultar Cursos")
        print("4.Consultar reporte")
        print("5.Salir")
        
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            subopcion = input("a) Agregar Alumno \n b) Consultar Alumnos \n Seleccione una opcion: ").lower()
            if subopcion == 'a':
                nombre=input("Nombre alumno: ")
                cedula=input("Cedula alumno: ")
                curso=input("Curso alumno: ")
                if curso in cursos_validos: 
                    try:
                         nota = float(input("Nota alumno: "))
                         alumnos.agregar_alumno(nombre, cedula, curso,nota)
                    except ValueError:
                         print("Error: La nota debe ser un numero.")

            else:
                 print("Error: El curso ingresado no está en la lista de cursos válidos")
        
        elif subopcion =='b':
                for a in alumnos.consultar_alumnos():
                    print(a)

        elif opcion == '2':
            subopcion = input("a) Agregar profesor\n b) Consultar profesor\n Seleccione una opcion: ").lower()
            if subopcion == 'a':
                nombre=input("Nombre profesor: ")
                cedula=input("Cedula profesor: ")
                curso=input("Curso del profesor: ")
                profesores.agregar_profesor(nombre, cedula, curso)
            elif subopcion =='b':
                for b in profesores.consultar_profesores():
                    print(b)
        
        elif opcion == '3':
            subopcion = input("a) Agregar curso\n b) Consultar cursos\n Seleccione una opcion: ").lower()
            if subopcion == 'a':
                print("Cursos válidos:", ", ".join(cursos_validos))
                curso=input("Nombre del curso: ")
                if curso in cursos_validos: 
                    codigo=input("codigo del curso: ")
                    cursos.agregar_curso(curso, codigo)
                else:
                     print("Error: El curso ingresado no está en la lista de cursos válidos.")
            elif subopcion =='b':
                for c in cursos.consultar_cursos():
                    print(c)

        elif opcion == '4':
             total_alumnos = alumnos.consultar_alumnos()
             print("reporte General: ")
             print("Total de alumnos registrado: ", len (total_alumnos))
             print("Promedio de todas las notas de los alumnos: ",
                   alumnos.consultar_promedio())
             aprobados, aplazados, reprobados, superior = alumnos.clasificar_estudiantes()
             print("Estudiantes aprobados: ", aprobados)
             print("Estudiantes aplazados: ", aplazados)
             print("Estudiantes reprobados: ", reprobados)
             print("Estudiantes con nota superior al promedio: ", superior)

             

        elif opcion == '5':
             print("Salida Exitosa")


if __name__ == "__main__":
            menu()