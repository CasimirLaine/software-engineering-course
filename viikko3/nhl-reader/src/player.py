import requests


class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.natinality = nationality
        self.assists = assists
        self.goals = goals
        self.penalities = penalties
        self.team = team
        self.games = games

    def __str__(self):
        return f'{self.name:20} {self.team} {self.goals:5} + {self.assists:2} = {self.goals + self.assists}'


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        players.sort(key=lambda player: player.goals + player.assists, reverse=True)
        players = filter(lambda player: player.natinality == nationality, players)
        return players


class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url).json()
        players = []

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )

            players.append(player)

        return players
