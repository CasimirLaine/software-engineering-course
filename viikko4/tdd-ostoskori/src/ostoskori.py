from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        self._ostokset = []

    def tavaroita_korissa(self):
        return sum(map(lambda ostos: ostos.lukumaara(), self._ostokset))

    def hinta(self):
        return sum(map(lambda ostos: ostos.hinta(), self._ostokset))

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                return
        self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        poistettavat = []
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() <= 0:
                    poistettavat.append(ostos)
        for ostos in poistettavat:
            self._ostokset.remove(ostos)

    def tyhjenna(self):
        self._ostokset = []

    def ostokset(self):
        return self._ostokset
