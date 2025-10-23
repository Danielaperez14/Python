print ("Calcular costo banquete")

personas = int(input("Ingrese el número de personas: "))


if personas <= 200:
    costo = 95
elif personas <= 300:
    costo = 85
else:
    costo = 75


presupuesto = personas * costo


print(f"El costo por persona es: ${costo}")
print(f"El presupuesto total es: ${presupuesto}")
