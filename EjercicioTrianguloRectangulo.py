
import math


Hipotenusa = float(input("Ingrese el valor de la hipotenusa: "))
Radio = float(input("Ingrese el valor del radio: "))


h = math.sqrt(Hipotenusa**2 - Radio**2)

# Se saca el calculo del área de los dos triángulos
AT = Radio * h   

# Se saca el calculo del área de la semicircunferencia
AS = (math.pi * Radio**2) / 2

# Se realiza el calculo del área total
Area = AT + AS


print("\nRESULTADOS:")
print("La altura del triángulo es:", round(h, 2))
print("El área total de la figura es:", round(Area, 2))
