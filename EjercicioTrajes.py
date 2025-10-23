print("Calculo precio final de los trajes")

precio = float(input("Ingrese el precio del traje: "))

if precio > 2500:
    descuento = precio * 0.15
else:
    descuento = precio * 0.08

precio_final = precio - descuento

print("El descuento aplicado es: $", round(descuento, 2))
print("El precio final a pagar es: $", round(precio_final, 2))
