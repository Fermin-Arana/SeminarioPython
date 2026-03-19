seconds = int(input("Ingrese una cantidad de segundos: "))

def Hours(seconds):
    result = int(seconds/3600)
    seconds -= int(result*3600)
    return result, seconds

def Minutes(seconds):
    result = int(seconds/60)
    seconds -= int(result*60)
    return result, seconds

hours, seconds = Hours(seconds)
minutes, seconds = Minutes(seconds)

print(f"Son {hours} horas, {minutes} minutos y {seconds} segundos")
