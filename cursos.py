cursos=[]

def agregar_curso(curso, codigo):
    curso ={
        'codigo': codigo,
        'curso': curso,
    }
    cursos.append(curso)

def consultar_cursos():
    return cursos