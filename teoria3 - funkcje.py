def pole_trojkata(dlugosc_podstawy, wysokosc):
    return dlugosc_podstawy * wysokosc

def zdolnosc_kredytowa(plec, wiek, suma_rat_kredytow, zarobki):
    if (plec == 'M' and wiek > 65) or (plec == 'M' and wiek > 70):
        return 100
    else:
        zdolnosc = (67 - wiek) * (zarobki - suma_rat_kredytow)
        return zdolnosc


lista_z_pliku = [12, 2, 43.6]
print(pole_trojkata(5, 8))
print(pole_trojkata(len(lista_z_pliku), lista_z_pliku[2]))

print(zdolnosc_kredytowa('M', 34, 1400, 7300))

if zdolnosc_kredytowa('M', 34, 1400, 7300) > 800:
    print('mozesz kupic te pralke')