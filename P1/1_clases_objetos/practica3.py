import os

class Profesores:
    
    def __init__(self, nombre, experiencia, num):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num=num

    @property # NOMBRE
    def nombreProfesor(self):
        return self.__nombre
    @nombreProfesor.setter
    def nombreProfesor(self,nombre):
        self.__nombre=nombre 
    
    @property # EXPERIENCIA
    def experienciaProfesor(self):
        return self.__experiencia
    @experienciaProfesor.setter
    def experienciaProfesor(self,experiencia):
        self.__experiencia=experiencia

    @property # NUM
    def numProfesor(self):
        return self.__num
    @numProfesor.setter
    def numProfesor(self,num):
        self.__num=num 
    
    # Metodos
    
    def impartir():
        pass

    def evaluar():
        pass

class Alumnos:

    def __init__(self, nombre, edad, matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula

    @property # NOMBRE
    def nombreAlumno(self):
        return self.__nombre
    @nombreAlumno.setter
    def nombreAlumno(self,nombre):
        self.__nombre=nombre 
    
    @property # EDAD
    def edadAlumno(self):
        return self.__edad
    @edadAlumno.setter
    def edadAlumno(self,edad):
        self.__edad=edad

    @property # MATRICULA
    def matriculaAlumno(self):
        return self.__matricula
    @matriculaAlumno.setter
    def matriculaAlumno(self,matricula):
        self.__matricula=matricula

    # Metodos

    def inscribirse():
        pass

    def estudiar():
        pass

class Cursos:

    def __init__(self, nombre, codigo, creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    @property # NOMBRE
    def nombreCurso(self):
        return self.__nombre
    @nombreCurso.setter
    def nombreCurso(self,nombre):
        self.__nombre=nombre 
    
    @property # CODIGO
    def codigoCurso(self):
        return self.__codigo
    @codigoCurso.setter
    def codigoCurso(self,codigo):
        self.__codigo=codigo

    @property # CODIGO
    def creditosCurso(self):
        return self.__creditos
    @creditosCurso.setter
    def creditosCurso(self,creditos):
        self.__creditos=creditos
    
    # Metodos

    def asignar():
        pass

# Insatancias

profesor1=Profesores("Ana Torres Guzman", 40, 123)
profesor2=Profesores("Daniel Contreras", 35, 124)

alumno1=Alumnos("Juan Correa Simental", 25, 100123)
alumno2=Alumnos("Maria Serrano Mata", 22, 100124)

curso1=Cursos("Poo", 100, 6)
curso2=Cursos("FOSOS", 101, 4)