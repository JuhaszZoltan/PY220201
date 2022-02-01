import sajat_fuggvenyeim as f

egesz_szam = f.szamot_beker('add meg az első számot: ')
print(f'{egesz_szam} * 10 = {10 * egesz_szam}')

# itt még történnek dolgok

masik_szam = f.szamot_beker('add meg a másik számot: ')
print(f'ez meg a másik: {masik_szam}')

print(int(20.8))

# print(fgv.osszeadas([2, 4, 4, 5]))
szamok = [2, 4, 4, 5]
osszeg = f.osszeadas(szamok)
print(osszeg)

valtozo = f.osszeadas([20, 30, 40])