import random

def validation(friends):
    if("," not in friends):
        print("No ingresaste los nombres de la forma que se te pidio")
        return False
    friends_list = [t.strip().lower() for t in friends.split(",")]
    unique = list(set(friends_list))
    if(len(friends_list) != len(unique)):
        print("Ingresaste el mismo nombre mas de una vez.")
        return False
    if(len(friends_list) < 3):
        print("Hay menos de 3 participantes.")
        return False
    return friends_list

def secret_friend(friends):
    friends_list = validation(friends)
    if (friends_list == False):
        return
    giving_friends = friends_list.copy()
    gifted_friends = friends_list.copy()
    final_list = []
    while friends_list:
        first_friend = random.choice(giving_friends)
        giving_friends.remove(first_friend)
        second_friend = random.choice(gifted_friends)
        attemps = 0
        while first_friend == second_friend:
            second_friend = random.choice(gifted_friends)
            attemps+=1
            if (attemps == 100):
                print("fallo")
                break
        gifted_friends.remove(second_friend)
        if(first_friend not in giving_friends and first_friend not in gifted_friends):
            friends_list.remove(first_friend)
        if(second_friend not in giving_friends and second_friend not in gifted_friends):
            friends_list.remove(second_friend)
        final_gift = f"{first_friend} -> {second_friend}"
        final_list.append(final_gift)
    print(final_list)

friends = str(input(f"Ingrese una lista de amigos separados por coma ',' (Ej Juan, Pedro, Lorenzo) "))        
secret_friend(friends)

        

