posts = ["Arrancando el lunes con energía #Motivación #NuevaSemana", "Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi", "No puedo creer el final de la serie #SinSpoilers #SerieAdicta", "Nuevo video en el canal sobre #InteligenciaArtificial y #Python", "Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain", "Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología", "Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta", "Finde de lluvia, maratón de series #SerieAdicta #Relax", "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
]

resultado = []
for post in posts:
    words = post.split()
    for word in words:
        if ("#" in word):
            resultado.append(word.lower())
conteo = {}

for hashtag in resultado:
    if hashtag in conteo:
        conteo[hashtag] +=1
    else:
        conteo[hashtag] = 1

conteo_ordenado = sorted(conteo.items(), key=lambda item: item[1], reverse=True)
hashtags_unicos = list(filter(lambda item: item[1] == 1, conteo.items()))
print(conteo_ordenado)
print(f"Los hashtags que solo aparecieron una vez son: {hashtags_unicos}")