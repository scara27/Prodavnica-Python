import matplotlib.pyplot as plt

def str2proizvod(line):
    if line [-1]=="\n":
        line = line[:-1]
    sifra, naziv, cena = line.split("|")
    proizvod = {"sifra":sifra, "naziv":naziv, "cena":cena}
    return proizvod


def ucitajProizvode():
    for line in open("Proizvodi.txt", "r").readlines():
        if len(line) > 1:
            proizvod = str2proizvod(line)
            proizvodi.append(proizvod)


def sacuvajProizvode():
    file = open("Proizvodi.txt", "w")
    for i in proizvodi:
        file.write(proizvod2str(i))
        file.write("\n")
    file.close


def proizvod2str(proizvod):
    return "|".join([proizvod["sifra"], proizvod["naziv"], proizvod["cena"]])


def findProizvod(sifra):
    for i in proizvodi:
        if i["sifra"]==sifra:
            return i
    print("Uneli ste nepostojeću šifru.")


def addProizvod(proizvod):
    proizvodi.append(proizvod)


def formatAllProizvodi():
    result = ''
    for proizvod in proizvodi:
        result += "{0:5}|{1:20}|{2:8}".format(
      proizvod['sifra'],
      proizvod['naziv'],
      proizvod['cena']) + '\n'
    return result


def formatProizvod(proizvod):
    return u"{0:5}|{1:20}|{2:8}".format(
      proizvod['sifra'],
      proizvod['naziv'],
      proizvod['cena'])


def formatHeader():
    return \
        "Šifra|Naziv proizvoda     |Cena    \n" \
        "-----+--------------------+--------"


def grafikon():
    cene = []
    nazivi = []
    for i in proizvodi:
        cene.append(float(i["cena"]))
        nazivi.append(i["naziv"])
    plt.bar(nazivi, cene)
    plt.ylim(ymin = 10, ymax = 1000)
    plt.xlabel("Proizvodi")
    plt.xticks(rotation=45)
    plt.ylabel("Cene")
    plt.show()

     
def racun():
    fajl = open("Racun.txt", "w")
    moredata = "1"
    suma = 0.0
    count = 0
    while moredata != "":
        sifra = input("Unesite šifru proizvoda: ")
        proizvod = findProizvod(sifra)
        if proizvod != None:
            kolicina = eval(input("Unesite količinu proizvoda: "))
            suma = suma + kolicina * float(proizvod["cena"])
            count = count + 1
            fajl.write(str(count))
            fajl.write("|")
            fajl.write(proizvod["naziv"])
            fajl.write("|")
            fajl.write(proizvod["cena"])
            fajl.write("|")
            fajl.write(str(kolicina))
            fajl.write("\n")
            print("\nUkoliko želite da nastavite unos, ukucajte bilo šta: ")
            print("Pritisnite <Enter> ukoliko želite da prekinete unos. ")
            moredata = input("--> ")
        else:
            print("\nUneli ste nepostojeću šifru.")
            print("Ukoliko želite da unesete novu šifru, ukucajte bilo šta.")
            print("Ukoliko zelite da izadjete, pritisnite <Enter>.")
            moredata = input("--> ")
    print("\nUkupan račun iznosi", str(round(suma, 2)) + " dinara.\n")
    fajl.close()
        

print(__name__)
proizvodi = []
ucitajProizvode()