#Pobieranie danych od uzytkownika (Input)
'''
ileKotow = input("Podaj wysokosc schodow z kotow: ")
#print('ileKotow jest:', type(ileKotow))
#Zamiana napisu na liczbe jesli mozliwe
try:
    ileKotow = int(ileKotow)
except ValueError as owcaWywala:
    #tutaj instrukcje ktore sie wykonaja kiedy zdarzy sie error
    print(f'Wystapil blad , program przyjmuje tylko liczby naturalne')

print('ileKotow jest:', type(ileKotow))
'''
ileKotow = input("Podaj dlugosc linijek z kotow: ")
try:
    ileKotow = int(ileKotow)
except ValueError as owcaWywala:
    #tutaj instrukcje ktore sie wykonaja kiedy zdarzy sie error
    print(f'Wystapil blad , program przyjmuje tylko liczby naturalne')
for x in range(0,ileKotow):
    print("(=^.^=)" * x + "(=^.^=)")