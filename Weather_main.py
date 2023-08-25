import numpy as np
import matplotlib.pyplot as plt

oznaczenia = ['index','M','D','H','DBT','RH','HR','WS','WD','ITH','IDH','ISH','TSKY','N_0',
              'N_30','NE_30','E_30','SE_30','S_30','SW_30','W_30','NW_30',
              'N_45','NE_45','E_45','SE_45','S_45','SW_45','W_45','NW_45',
              'N_60','NE_60','E_60','SE_60','S_60','SW_60','W_60','NW_60',
              'N_90','NE_90','E_90','SE_90','S_90','SW_90','W_90','NW_90']


        
def odczyt_danych(sciezka):
        with open(sciezka, mode = 'r') as plik:
                tablica = []
                for linia in plik:
                        wiersz_1 = []
                        for komorka in linia.split():
                                 wiersz_1.append(float(komorka))
                        tablica.append(wiersz_1)
                return tablica

class obliczenia():
        
        def miesiac_wektor(self,rok, miesiac):
                output = []
                pop = -1
                for wiersz in rok:
                        if wiersz[1] == miesiac:
                                output.append(wiersz)
                                pop = miesiac
                        elif pop == miesiac:
                                break
                return output                 

        def tydzien_wektor(self,rok, tydzien):
                return rok[(tydzien -1)*168:tydzien*168]

        def doba_wektor(self,rok, dzien):
                return rok[(dzien -1)*24:dzien*24]

        def do_column(self,typ_danych, lista):
                columna =[]
                for wiersz in lista:
                        columna.append(wiersz[oznaczenia.index(typ_danych)])
                return columna

            
class wykresy():

        def korelacja(self,x,y):
                np.corrcoef(X, Y)
                plt.scatter(X, Y)
                plt.show()
                
        def autokorelacja(self,x):
                plt.title("Wykres autokorelacji")  
                plt.acorr(np_dbt_col, maxlags = 23)  
                plt.grid(True) 
                plt.show()  
        


sciezka = '.\\Data\\elblag.txt'       
obj = obliczenia()
tablica = odczyt_danych(sciezka)
 

while(True):

        print('Wybierz czynność:\n')
        print('1. Wyznacz parametry')
        print('2. Wyznacz wektor tygodniowy')
        print('3. Wyznacz wektor dobowy')
        print('4. Wyznacz wektor miesięczny')
        print('5. Pokaż wykres korelacji')
        print('6. Pokaż wykres autokorelacji')
        print('7. Zakończ')

        decyzja = int(input())
        
        if decyzja == 1:         
                print('1. Podaj typ danych:')
                print(oznaczenia)
                dane = input()
                kolumna = obj.do_column(dane, obj.miesiac_wektor(tablica,2))
                np_dbt_col = np.array(kolumna)
                print(np_dbt_col)
                print('Dla ',dane,':')
                print('* Odchylenie standardowe: ',np.std(np_dbt_col))
                print('* Średnia arytmetyczna: ',np.mean(np_dbt_col))
                print('* Wartość minimalna : ',np.min(np_dbt_col))
                print('* Wartość maksymalna: ',np.max(np_dbt_col))
                print('* Mediana: ',np.median(np_dbt_col),'\n\n\n')



        elif decyzja == 2:               
                print('2. Podaj numer tygodnia:')
                T = int(input())
                print('a) Liczba danych w wektorze: ')
                liczba_wyswietlanych_danych = input()
                print('Wektor tygodniowy (dla ',T,' tygodnia w roku):\n')
                zmienna = obj.tydzien_wektor(tablica, T)
                i = 0
                for el in zmienna:
                        print(el[:int(liczba_wyswietlanych_danych)])
                        i+=1
                        if i > 167:
                                break
                print('\n')


        elif decyzja == 3:
                print('3. Podaj numer doby:')
                D = int(input())
                print('a) Liczba danych w wektorze: ')
                liczba_wyswietlanych_danych = input()
                print('Wektor dobowy (dla ',D,' doby w roku):\n')                                   
                zmienna = obj.doba_wektor(tablica, D)
                i = 0
                for el in zmienna:
                        print(el[:int(liczba_wyswietlanych_danych)])
                        i+=1
                        if i > 23:
                                break
                print('\n')

        elif decyzja == 4:
                print('4. Podaj numer miesiąca:')
                M = int(input())
                print('a) Liczba danych w wektorze: ')
                liczba_wyswietlanych_danych = input()
                print('Wektor miesieczny (dla ',M,' miesiąca w roku):\n')
                zmienna = obj.miesiac_wektor(tablica, M)
                i = 0
                for el in zmienna:
                        print(el[:int(liczba_wyswietlanych_danych)])
                        i+=1
                        if i > 743:
                                break


        elif decyzja == 5:
                wykres = wykresy()
                print('5. Wybierz rodzaj wektora:')
                print('1 - Wektor dobowy')
                print('2 - Wektor tygodniowy')
                print('3 - Wektor miesieczny')
                wybor = input()

                if wybor == '1':
                        print('a) Podaj numer  pierwszego wektora:')
                        X = obj.doba_wektor(tablica, int(input()))
                        print('b) Podaj numer  drugiego wektora:')
                        Y = obj.doba_wektor(tablica, int(input()))
                        cos = wykres.korelacja(X,Y)
                elif wybor == '2':
                        print('a) Podaj numer  pierwszego wektora:')
                        X = obj.tydzien_wektor(tablica, int(input()))
                        print('b) Podaj numer  drugiego wektora:')
                        Y = obj.tydzien_wektor(tablica, int(input()))
                        cos = wykres.korelacja(X,Y)
                elif wybor == '3':
                        print('a) Podaj numer  pierwszego wektora:')
                        X = obj.miesiac_wektor(tablica, int(input()))
                        print('b) Podaj numer  drugiego wektora:')
                        Y = obj.miesiac_wektor(tablica, int(input()))
                        cos = wykres.korelacja(X,Y)
                else:
                        print('Niepoprawny numer')



        elif decyzja == 6:
                wykres = wykresy()
                print('a) Wybierz zakres danych: ')
                print('1 - Zakres dobowy')
                print('2 - Zakres tygodniowy')
                print('3 - Zakres miesieczny')
                wybor = input()

                if wybor == '1':
                        print('b) Podaj numer dnia:')
                        numer = input()
                        print('c) Podaj typ danych:')
                        typ = input()
                        kolumna = obj.do_column(typ, obj.doba_wektor(tablica,int(numer)))
                        np_dbt_col = np.array(kolumna)
                        cos = wykres.autokorelacja(np_dbt_col)
                elif wybor == '2':
                        print('b) Podaj numer tygodnia:')
                        numer = input()
                        print('c) Podaj typ danych:')
                        typ = input()
                        kolumna = obj.do_column(typ, obj.tydzien_wektor(tablica,int(numer)))
                        np_dbt_col = np.array(kolumna)
                        cos = wykres.autokorelacja(np_dbt_col)
                elif wybor == '3':
                        print('b) Podaj numer miesiąca:')
                        numer = input()
                        print('c) Podaj typ danych:')
                        typ = input()
                        kolumna = obj.do_column(typ, obj.miesiac_wektor(tablica,int(numer)))
                        np_dbt_col = np.array(kolumna)
                        cos = wykres.autokorelacja(np_dbt_col)

        elif decyzja == 7:
                break
