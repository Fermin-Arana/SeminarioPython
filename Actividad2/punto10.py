rounds = [
    {
        'theme': 'Entrada',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
            'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
        }
    },
    {
        'theme': 'Plato principal',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
            'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
        }
    },
    {
        'theme': 'Postre',
        'scores': {
            'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
            'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
            'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
            'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
        }
    },
    {
        'theme': 'Cocina internacional',
        'scores': {
            'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
            'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
            'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
            'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
            'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
        }
    },
    {
        'theme': 'Final libre',
        'scores': {
            'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
            'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
            'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
            'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
        }
    }
]

class Persona:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.win_rounds = []
        self.points_best_round = 0
        self.prom = 0.0
        self.cant_rounds = 0
    def get_name(self):
        return self.name
    def get_points(self):
        return self.points
    def sum_rounds(self):
        self.cant_rounds+=1
    def sum_points(self,new_points):
        self.points += new_points
    def sum_win_rounds (self, win_round):
        self.win_rounds.append(win_round)
    def set_best_round(self, points_best):
        if(self.points_best_round < points_best):
            self.points_best_round = points_best
    def calculate_prom(self):
        self.prom = self.points / self.cant_rounds
    def __str__ (self):
        return f"Cocinero: {self.name}, Puntaje: {self.points}, Rondas ganadas: {self.win_rounds}, Mejor ronda: {self.points_best_round}, promedio: {self.prom}"


class Torneo:
    def __init__(self, rounds):
        self.rounds = rounds
    
    def mostrar_resultado(self):
        n_round = 0
        participants = {}
        for round in self.rounds:
            n_round += 1
            theme = round["theme"]
            points = round["scores"]
            table = []
            for name, judge in points.items(): 
                total = sum(judge_note for judge_note in judge.values())
                if(name not in participants):
                    participants[name] = Persona(name)
                participants[name].sum_points(total)
                participants[name].set_best_round(total)
                participants[name].sum_rounds()
                table.append((name,total))
            table.sort(key=lambda x: x[1], reverse=True)
            winner_name, winner_points = table[0]         
            participants[winner_name].sum_win_rounds(n_round)
            print(f"\n- {theme}:")
            print(f"  Ganador: {winner_name} ({winner_points} pts)")
            print("  Tabla de posiciones:")
            for i in range(1, len(table)):
                name, points = table[i]
                print(f"{i+1}, nombre {name}: {points} pts")
        return participants
                

my_tournament = Torneo(rounds)
participants = my_tournament.mostrar_resultado()
participants_list = list(participants.values())
participants_list.sort(key = lambda p: p.get_points(), reverse = True)
for p in participants_list:
    p.calculate_prom()
    print(p)




    
