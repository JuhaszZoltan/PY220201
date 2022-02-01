import gyakorlo_feladatok_fuggvenyei as f
import random as r

# szamok = f.veletlen_lista()
# f.lista_kiir(szamok)

for n in range(10):
    f.lista_kiir(f.veletlen_lista_1())

for n in range(10):
    f.lista_kiir(f.veletlen_lista_2(r.randint(1, 10)))

# 15 elemű, 3 számjegyű számokat tartamazó lista:
f.lista_kiir(f.veletlen_lista_3(15, 100, 999))

# 4 elemű, [20; 50] számokat t. listát:
f.lista_kiir(f.veletlen_lista_3(4, 20, 50))