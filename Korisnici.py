def str2korisnik(line):
    if line [-1]=="\n":
        line = line[:-1]
    korisnik, lozinka = line.split("|")
    korisnik = {"korisnik":korisnik, "lozinka":lozinka}
    return korisnik


def ucitajKorisnike():
    for line in open("Korisnici.txt", "r").readlines():
        if len(line) > 1:
            korisnik = str2korisnik(line)
            korisnici.append(korisnik)


def login(username, password):
    for i in korisnici:
        if i["korisnik"] == username and i["lozinka"] == password:
            return True
    return False


print(__name__)
korisnici = []
ucitajKorisnike()