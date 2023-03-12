lista = []

for i in range(5):
    lista_wewnetrza = []
    print('imie numer',i+1)
    imie = input('Podaj imie ')
    lista_wewnetrza.append(imie)
    wiek = int(input('Podaj wiek '))
    lista_wewnetrza.append(wiek)
    lista.append(lista_wewnetrza)
print(lista)

for i in range(len(lista)):
    if lista[i][0][-1] == 'a':
        print('Kobieta')
    else:
        print('facet')