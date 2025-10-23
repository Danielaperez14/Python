print("Se calcula el área  del terreno A")

A = float(input("Ingrese la altura del lado (A): "))
B = float(input("Ingrese la base del lado (B): "))
C = float(input("Ingrese la altura del lado (C): "))


AT = (B * (A - C)) / 2   
AR = B * C              


Area = AT + AR


print("El área total del terreno es:", Area)