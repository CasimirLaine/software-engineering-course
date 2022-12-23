from uusi import luo_peli

virheviesti = "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )
        vastaus = input()
        peli = luo_peli(vastaus)
        if peli is None:
            break
        print(virheviesti)
        peli.pelaa()


if __name__ == "__main__":
    main()
