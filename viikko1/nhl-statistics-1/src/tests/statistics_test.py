import unittest
import uuid

import statistics
from statistics import Statistics, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search(self):
        assert self.statistics.search('Semenko').name == 'Semenko'

    def test_search_none(self):
        assert self.statistics.search(str(uuid.uuid4())) is None

    def test_team(self):
        assert len(self.statistics.team('EDM')) == 3

    def test_team_none(self):
        assert len(self.statistics.team(str(uuid.uuid4()))) == 0

    def test_sort_points(self):
        player = self.statistics.search('Semenko')
        assert player.points == statistics.sort_by_points(player)

    def test_sort_goals(self):
        player = self.statistics.search('Lemieux')
        assert player.goals == statistics.sort_by_goals(player)

    def test_sort_assists(self):
        player = self.statistics.search('Gretzky')
        assert player.assists == statistics.sort_by_assists(player)

    def test_top_3_points(self):
        result = self.statistics.top(2, SortBy.POINTS)
        assert len(result) == 3
        assert result[0].name == 'Gretzky'
        assert result[1].name == 'Lemieux'
        assert result[2].name == 'Yzerman'

    def test_top_3_goals(self):
        result = self.statistics.top(2, SortBy.GOALS)
        assert len(result) == 3
        assert result[0].name == 'Lemieux'
        assert result[1].name == 'Yzerman'
        assert result[2].name == 'Kurri'

    def test_top_3_assists(self):
        result = self.statistics.top(2, SortBy.ASSISTS)
        assert len(result) == 3
        assert result[0].name == 'Gretzky'
        assert result[1].name == 'Yzerman'
        assert result[2].name == 'Lemieux'

    def test_top_3_unknown(self):
        result = self.statistics.top(2, str(uuid.uuid4()))
        assert len(result) == 0
