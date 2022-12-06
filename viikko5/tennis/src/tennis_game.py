class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def won_point(self):
        self.score += 1

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name


_SCORE_TABLE = {
    0: "Love-All",
    1: "Fifteen-All",
    2: "Thirty-All",
    3: "Forty-All",
    4: "Deuce",
}

_TEMP_SCORE_TABLE = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Forty",
}


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1.won_point()
        else:
            self.player2.won_point()

    def _get_description(self):
        difference = self.player1.score - self.player2.score
        if difference == 1:
            score = "Advantage player1"
        elif difference == -1:
            score = "Advantage player2"
        elif difference >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def get_score(self):
        if self.player1.score == self.player2.score:
            score = _SCORE_TABLE[self.player1.score]
        elif self.player1.score >= 4 or self.player2.score >= 4:
            score = self._get_description()
        else:
            score = ''
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1.score
                else:
                    score = score + "-"
                    temp_score = self.player2.score
                score = score + _TEMP_SCORE_TABLE[temp_score]
        return score
