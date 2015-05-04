calificaciones = [600, 470, 170, 430, 300]

def print_calificaciones(calificaciones):
    for calificacion in calificaciones:
        print calificacion

def notas_sum(calificaciones):
    total = 0 
    for calificacion in calificaciones: 
        total += calificacion
    return total

def promedio_notas(calificaciones):
    suma = notas_sum(calificaciones)
    promedio = suma / float(len(calificaciones))
    return promedio
 
def varianza_notas(calificaciones):
    promedio = promedio_notas(calificaciones)
    varianza = 0
    total_varianza = 0
    total_notas = notas_sum(calificaciones) 
    for c in calificaciones:
        varianza = ((c - promedio) ** 2) / float(len(calificaciones))
        total_varianza += varianza
    return total_varianza 
    

def calificaciones_std_desviacion(varianza):
    return varianza ** 0.5
    

print "Calificaciones:"
print_calificaciones(calificaciones)
print "Sumatoria de las notas:"
print notas_sum(calificaciones)
print "Promedio de las notas:"
print promedio_notas(calificaciones)
print "Varianza de las notas:"
print varianza_notas(calificaciones)
print "Desviacion estandar de las notas:"
print calificaciones_std_desviacion(varianza_notas(calificaciones))