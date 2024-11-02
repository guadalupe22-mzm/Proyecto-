Edad= int(input("Digite su edad"))

if Edad <= 10:
    precio=3000
elif Edad <15 and Edad > 10:
    precio=5000
elif Edad<=18 and Edad>15:
    precio=7500
elif Edad> 18:
    precio=10000
print("La cantida a pagar: ", precio)
    