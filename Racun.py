def str2racun(line):
    if line [-1]=="\n":
        line = line[:-1]
    rbr, naziv, cena, kol = line.split("|")
    rac = {"rbr":rbr, "naziv":naziv, "cena":cena, "kol":kol}
    return rac


def formatAllRacuni():
    result = ''
    for rac in racun:
        result += "{0:10}|{1:20}|{2:8}|{3:8}".format(
      rac["rbr"],
      rac["naziv"],
      rac["cena"],
      rac["kol"]) + '\n'
    return result


def ucitajRacun():
    for line in open("Racun.txt", "r").readlines():
        if len(line) > 1:
            rac = str2racun(line)
            racun.append(rac)


def formatHeader():
    return \
        "Redni broj|Naziv proizvoda     |Cena    |Količina\n" \
        "----------+--------------------+--------+--------"


print(__name__)
racun = []