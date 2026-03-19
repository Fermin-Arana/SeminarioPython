words = (input("Ingrese una lista de palabras: "))

words_list = words.split()

for word in words_list:
    if len(word) <= 3:
        words_list.remove(word)

result = " ".join(words_list)
print(f"{result}")
