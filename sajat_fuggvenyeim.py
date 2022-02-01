def szamot_beker(szoveg):
    szam = int(input(szoveg))
    return szam


def osszeadas(lista) -> int:
    sum: int = 0
    for x in lista:
        sum += x
    return sum