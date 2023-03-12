def przytanie():
    print('Czesc')
    print('Konfigurowanie systemu')

def konfiguracja_systemu(username):
    print('Konfiguracja dla ',username)
    print('koniec')


print('Rozpoczytam program')
nowy = input('Czy nowy uzytkownik?   T/N    ')
if nowy == 'T':
    przytanie()
    nazwa = input('Poda nazwe uzytkownika')
    konfiguracja_systemu(nazwa)
print('Dalsza czesc programu')