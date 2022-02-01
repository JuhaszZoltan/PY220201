import random

def veletlen_lista_1():
    """visszaad egy 10 elemű,
    2 számjegyű véletlen számokat tartalmazó listát"""
    lista = []
    for x in range(10):
        lista.append(random.randint(10, 99))
    return lista


def veletlen_lista_2(elemszam):
    """visszaad egy, a paraméterben kapott elemszámú
    2 számjegyű véletlenszámokat tartalmazó listát"""
    lista = []
    for x in range(elemszam):
        lista.append(random.randint(10, 99))
    return lista

def veletlen_lista_3(elemszam, min, max):
    """visszaad egy a paraméterben kapott elemszámú listát,
    melynek elemei a paraméterben kapott
    [min; max] intervallumon belül vannak"""
    lista = []
    for x in range(elemszam):
        lista.append(random.randint(min, max))
    return lista


def lista_kiir(lista):
    """kiírja paraméterben kapott lista elemeit
    egy sorba, szóközzel elválasztva"""
    for e in lista:
        print(e, end=' ')
    print()