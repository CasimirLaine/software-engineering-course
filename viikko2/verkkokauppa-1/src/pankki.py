import kirjanpito


class Pankki:

    def __init__(self, kirjanpito):
        self._kirjanpito = kirjanpito

    def tilisiirto(self, nimi, viitenumero, tililta, tilille, summa):
        self._kirjanpito.lisaa_tapahtuma(
            f"tilisiirto: tililtä {tililta} tilille {tilille} viite {viitenumero} summa {summa}e"
        )

        # täällä olisi koodi joka ottaa yhteyden pankin verkkorajapintaan
        return True


the_pankki_olio = Pankki(kirjanpito=kirjanpito.the_kirjanpito_olio)
