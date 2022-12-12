from statistics import Statistics
from player_reader import PlayerReader
from matchers import *


class QueryBuilder:

    def __init__(self):
        self._matchers = []

    def playsIn(self, param) -> 'QueryBuilder':
        self._matchers.append(PlaysIn(param))
        return self

    def hasAtLeast(self, param, param1) -> 'QueryBuilder':
        self._matchers.append(HasAtLeast(param, param1))
        return self

    def hasFewerThan(self, param, param1) -> 'QueryBuilder':
        self._matchers.append(HasFewerThan(param, param1))
        return self

    def oneOf(self, param, param1) -> 'QueryBuilder':
        self._matchers.append(Or(param, param1))
        return self

    def build(self):
        result =  And(*self._matchers)
        self._matchers = []
        return result


def main():
    url = "https://studies.cs.helsinki.fi//nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    m1 = (
        query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
        query
        .playsIn("EDM")
        .hasAtLeast(50, "points")
        .build()
    )

    matcher = query.oneOf(m1, m2).build()
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
