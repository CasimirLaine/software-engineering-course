from kps_tekoaly import KPSTekoaly
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        return_value = super()._toisen_siirto(ensimmaisen_siirto)
        self.tekoaly.aseta_siirto(ensimmaisen_siirto)
        return return_value
