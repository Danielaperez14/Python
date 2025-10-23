print ("Calcule el pago diario de la venta de leche")

litros = float(input("Ingrese la cantidad de litros producidos: "))
precio = float(input("Ingrese el precio por litro: "))
dias = int(input("Ingrese el número de días de producción: "))


total_leche = litros * dias
pago_total = total_leche * precio


print("Cantidad total de leche producida:", total_leche, "litros")
print("Pago total al productor: $", pago_total)
