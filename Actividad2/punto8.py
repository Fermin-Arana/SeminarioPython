def cesar(message, value):
    result = ""
    for letter in message:
        if(letter.isalpha()):
            start = ord("A") if letter.isupper() else ord("a")
            letter_pos = ord(letter) - start
            new_letter_pos = (letter_pos + value) % 26
            result += chr(new_letter_pos + start)
        else:
            result += letter
    return result

result = cesar("Hola mundZ! 4", 3)
print("Hola mundZ! 4")
print(result)
print(cesar(result, -3))
