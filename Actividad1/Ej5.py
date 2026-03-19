total = 0
while True:
    price = int(input("Ingrese un precio: "))
    total += price
    if (price == 0):
        break
print (total)