KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        self.kapasiteetti = kapasiteetti
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kasvatuskoko")
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, number):
        on = 0
        for i in range(0, self.alkioiden_lkm):
            if number == self.ljono[i]:
                on = on + 1
        return on > 0

    def lisaa(self, number):
        ei_ole = 0
        if self.alkioiden_lkm == 0:
            self.ljono[0] = number
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        if not self.kuuluu(number):
            self.ljono[self.alkioiden_lkm] = number
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            if self.alkioiden_lkm % len(self.ljono) == 0:
                taulukko_old = self.ljono
                self.kopioi_taulukko(self.ljono, taulukko_old)
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.ljono)
            return True
        return False

    def poista(self, number):
        kohta = -1
        apu = 0
        for i in range(0, self.alkioiden_lkm):
            if number == self.ljono[i]:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.ljono[kohta] = 0
                break
        if kohta != -1:
            for j in range(kohta, self.alkioiden_lkm - 1):
                apu = self.ljono[j]
                self.ljono[j] = self.ljono[j + 1]
                self.ljono[j + 1] = apu
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True
        return False

    def kopioi_taulukko(self, taulukko1, taulukko2):
        for i in range(0, len(taulukko1)):
            taulukko2[i] = taulukko1[i]

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm
        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]
        return taulu

    def get_int_joukko(self, a, b, komento):
        int_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(0, len(a_taulu)):
            int_joukko.lisaa(a_taulu[i])
        for i in range(0, len(b_taulu)):
            if komento == 'yhdiste':
                int_joukko.lisaa(b_taulu[i])
            elif komento == 'erotus':
                int_joukko.poista(b_taulu[i])
        return int_joukko

    @staticmethod
    def yhdiste(a, b):
        return a.get_int_joukko(a, b, 'yhdiste')

    @staticmethod
    def erotus(a, b):
        return a.get_int_joukko(a, b, 'erotus')

    @staticmethod
    def leikkaus(a, b):
        int_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()
        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    int_joukko.lisaa(b_taulu[j])

        return int_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
