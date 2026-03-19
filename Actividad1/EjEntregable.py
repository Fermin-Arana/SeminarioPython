import random

score = 0

categories = {
    "Programación": ["python", "programa", "variable", "funcion", "bucle", "cadena", "entero", "lista"],
    "Animales": ["perro", "gato", "elefante", "jirafa", "tigre"],
    "Frutas": ["manzana", "banana", "naranja", "uva", "pera"]
}

words_played = []

while True:
    print("\n--- NUEVA PARTIDA ---")
    print("Categorías disponibles:")
    options = list(categories.keys())
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

    choice = int(input("Elegí una categoría (número): ")) - 1
    categoria_actual = options[choice]
    
    posibility = [p for p in categories[categoria_actual] if p not in words_played]
    
    if not posibility:
        print(f"Ya no quedan palabras en {categoria_actual}. ¡Elegí otra!")
        continue

    word = random.sample(posibility, 1)[0]
    words_played.append(word)
    
    guessed = []
    attempts = 6

    print(f"¡Bienvenido al Ahorcado! (Categoría: {categoria_actual})")
    print()

    while attempts > 0:
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        if "_" not in progress:
            print("¡Ganaste!")
            score += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ").lower()
        while (len(letter) > 1 and (letter < "a" or letter > "z")):
            letter = input("Entrada no valida, pone UNA letra: ").lower()

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            score -= 1
            print("Esa letra no está en la palabra.")
        print()

    else:
        score = 0
        print(f"¡Perdiste! La palabra era: {word}")

    print(f"Tu puntuacion actual es de {score}")
    
    if input("¿Querés seguir jugando? (s/n): ").lower() != "s":
        break

print("Gracias por jugar.")