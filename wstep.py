#do jezd gomendarz, tego kompjuter nje czyta
"""
To jest string ale można go 
uzyc jako komentarz bo tak
"""
#Podstawowe typy w pythonie:
#String, np:
owca = 'ala ma kota'
krowa = "kot zabil ale"
#Fajne operacje na napisach:
owca[0] #wybierze pierwszy znak z napisu
owca[0:4] #wyciaga znaki od indexu 0 do 3
owca[3:7] #wyciaga indexy 3-6
#print wyswietla w konsoli
print(owca[:7])
#sprawdzanie dlugosci napisu
len("napis")
#Liczby
#Som 2 typy liczbowe w pythonie int i float
owcaInt = -5
owcaFloat = 7.5
#ciekawe zapisy
2**5 #32 -> potega 2 do 5
2e2 # 2*10 do 2
7%5 #zwraca reszte z dzielenia
#boolean 
prawda = True
falsz = False
#Uwaga roznice
# 1 + "7" Error
str(1) + "7"
print(1,"7",owca)
#Format napisow
print(f'Ala ma {17} kotow: {prawda} ')