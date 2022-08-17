analizar = input ("¿Analizar calificaciones? ‘S’ para ‘sí’: ")

aprobados = 0
alumnos_aprobados = 0
alumnos = 0
nota = 0
while analizar == "S":
    calificacion = float (input("Calificación del alumno: "))
    if calificacion > 4:
        aprobados += 1
        alumnos_aprobados += 1
        nota =  nota + calificacion
    alumnos += 1    
    analizar = input ("¿Continuar? ‘S’ para ‘sí’: ")


porcentaje = (alumnos_aprobados * 100) / alumnos
media = nota / alumnos_aprobados

print (f"El porcentaje de aprobados es: {porcentaje} \n")
print (f"El promedio de aprobados es: {media}")