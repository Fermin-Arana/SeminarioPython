number = int(input("Ingrese un numero: "))
multipleofive = []
others = []
for i in range(1,(number+1)):
    if (i%5 == 0):
        multipleofive.append(i)
    else:
        others.append(i)

print(f"los multiplos de 5 son: {multipleofive} y el resto son: {others}")
    