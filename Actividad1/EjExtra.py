class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.points = 0
    
    def get_name(self):
        return self.team_name
    
    def add_points(self, more_points):
        self.points += more_points

    def get_points(self):
        return self.points
    
    def __str__(self):
        return self.team_name

class Match:
    def __init__(self, home_team, away_team, home_goals, away_goals):
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = home_goals
        self.away_goals = away_goals
    
    def final_score(self):
        if (self.home_goals > self.away_goals):
            self.home_team.add_points(3)
            print(f"El equipo local {self.home_team.get_name()} gano al visitante {self.away_team.get_name()} con un resultado de {self.home_goals} - {self.away_goals} ")
        elif(self.home_goals < self.away_goals):
            self.away_team.add_points(3)
            print(f"El equipo local {self.home_team} perdio frente al visitante {self.away_team} con un resultado de {self.home_goals} - {self.away_goals} ")
        else:
            self.home_team.add_points(1)
            self.away_team.add_points(1)
            print(f"El equipo local {self.home_team} empato frente al visitante {self.away_team} con un resultado de {self.home_goals} - {self.away_goals} ")

class Tournament:
    teams = []
    matchs = []

    def add_team(self, team_to_add):
        self.teams.append(team_to_add)

    def search_team(self, team_name):
        for team in self.teams:
            if(team.get_name() == team_name):
                return True
                break
        return False

    def get_team(self, team_name):
        for team in self.teams:
            if team.get_name() == team_name:
                return team
                break
        return False
    
    def add_match(self, home_team, away_team, home_goals, away_goals):
        home_name = home_team.get_name()
        away_name = away_team.get_name()
        if(self.search_team(home_name) and self.search_team(away_name)):
            actual_match = Match(home_team, away_team, home_goals, away_goals)
            self.matchs.append(actual_match)
            actual_match.final_score()
            self.sort_league_table()
        else:
            print("Uno de los dos equipos no existe en esta liga")

    def sort_league_table(self):
        self.teams = sorted(self.teams, key=lambda t: t.get_points(), reverse = True)

    def league_table(self):
        pos = 1
        for team in self.teams:
            print(f"{pos}. {team.get_name()} pts {team.get_points()}")
            pos+=1

tournament = Tournament()

team_name = (input("Ingrese el nombre del equipo: "))
while (team_name != "fin"):
    actual_team = Team(team_name)
    tournament.add_team(actual_team)
    team_name = (input("Ingrese el nombre del equipo: "))

first_team = (input("Ingrese el nombre del primer equipo: "))
first_team = tournament.get_team(first_team)
second_team = (input("Ingrese el nombre del segundo equipo: "))
second_team = tournament.get_team(second_team)
while (first_team == False or second_team == False):
    first_team = (input("Ingrese el nombre del primer equipo (que exista): "))
    first_team = tournament.get_team(first_team)
    second_team = (input("Ingrese el nombre del segundo equipo (que exista): "))
    second_team = tournament.get_team(second_team)

while (first_team != second_team):
    score = (input("Ingrese el resultado final (ej: 4-2): "))
    sorted_score = score.split("-")
    first_score = sorted_score[0]
    second_score = sorted_score[1]
    while(first_score.isdigit() == False or second_score.isdigit() == False):
        score = (input("Ingrese el resultado final con el formato correcto (ej: 4-2): "))
        sorted_score = score.split("-")
        first_score = sorted_score[0]
        second_score = sorted_score[0]
    tournament.add_match(first_team, second_team, first_score, second_score)
    first_team = (input("Ingrese el nombre del primer equipo: "))
    first_team = tournament.get_team(first_team)
    second_team = (input("Ingrese el nombre del segundo equipo: "))
    second_team = tournament.get_team(second_team)

tournament.league_table()