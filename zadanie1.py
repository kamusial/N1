#program pyta 5 pracy po imie
#program zapiosuje imiona w piście
#program pisze odpowiedni tekst w zależności od płci

lista = []
for i in range(5):
    print('imie numer',i+1)
    imie = input('Podaj imie ')
    lista.append(imie)
print(lista)

for i in range(len(lista)):
    if lista[i][-1] == 'a':
        print('Kobieta')
    else:
        print('facet')
