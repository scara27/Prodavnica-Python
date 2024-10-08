import Proizvodi
import Korisnici
import Racun

def main():
    if not login():
        print("\nUneli ste nepostojeće ime i/ili lozinku.")
        return
    komanda = "0"
    while komanda != "":
        komanda = menu()
        if komanda == "1":
            pregledProizvoda()
        elif komanda == "2":
            findProizvod()
        elif komanda == "3":
            dodajProizvod()
        elif komanda == "4":
            updateProizvod()
        elif komanda == "5":
            grafikon()
        elif komanda == "6":
            racun()
    print("\nUspešno ste zatvorili program!")


def login():
    korisnik = input("Unesite korisničko ime: ")
    lozinka = input("Unesite lozinku: ")
    return Korisnici.login(korisnik, lozinka)


def menu():
    printMenu()
    komanda = input("--> ")
    while komanda not in ("1", "2", "3", "4", "5", "6", ""):
        print("\nUneli ste pogrešnu komandu.\n")
        printMenu()
        komanda = input("--> ")
    return komanda


def printMenu():
    print("\n\n---Unesite komandu za jednu od ponuđenih opcija---\n")
    print("1) Prikaz svih proizvoda")
    print("2) Pronalaženje proizvoda po unetoj šifri")
    print("3) Dodavanje novog proizvoda")
    print("4) Promena cene proizvoda")
    print("5) Proizvodi i njihove cene prikazani na grafikonu")
    print("6) Kreiranje računa")
    print("\n---Da bi ste zatvorili program, pritisnite <Enter>---")


def findProizvod():
    print("2) Pronalaženje proizvoda po unetoj šifri")
    sifra = input("Unesite šifru proizvoda: ")
    proizvod = Proizvodi.findProizvod(sifra)
    print("\n")
    if proizvod != None:
        print(Proizvodi.formatHeader())
        print(Proizvodi.formatProizvod(proizvod))


def updateProizvod():
    print("4) Promena cene proizvoda")
    sifra = input("Unesite šifru proizvoda: ")
    proizvod = Proizvodi.findProizvod(sifra)
    if proizvod != None:
        proizvod["cena"] = input("Unesite novu cenu proizvoda: ")
        Proizvodi.sacuvajProizvode()


def dodajProizvod():
    print("3) Dodavanje novog proizvoda")
    proizvod = {}
    proizvod["sifra"] = input("Unesite šifru proizvoda: ")
    proizvod["naziv"] = input("Unesite naziv proizvoda: ")
    proizvod["cena"] = input("Unesite cenu proizvoda: ")
    Proizvodi.addProizvod(proizvod)
    Proizvodi.sacuvajProizvode()


def pregledProizvoda():
    print("1) Prikaz svih proizvoda\n")
    print(Proizvodi.formatHeader())
    print(Proizvodi.formatAllProizvodi())


def grafikon():
    print("5) Proizvodi i njihove cene prikazani na grafikonu")
    Proizvodi.grafikon()


def racun():
    print("6) Kreiranje računa")
    Proizvodi.racun()
    Racun.ucitajRacun()
    print(Racun.formatHeader())
    print(Racun.formatAllRacuni())
    


print(__name__)
if __name__ == "__main__":
    main()