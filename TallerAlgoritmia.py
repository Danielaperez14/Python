print ("Promedio de notas")


#Se hace la solicitud de cada nota para poder capturar los datos 
C1 = float(input("Ingrese la calificación del primer examen: "))
C2 = float(input("Ingrese la calificación del segundo examen: "))
C3 = float(input("Ingrese la calificación del tercer examen: "))
C4 = float(input("Ingrese la calificación del cuarto examen: "))

#Se suman los datos ingresados anteriormente
S = C1 + C2 + C3 + C4

#Se saca el promedio con el número de datos capturados
P = S / 4


print("El promedio de las calificaciones es:", P)
