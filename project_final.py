import tkinter as tk
from functions import pole

# inicjalizacja słownika przechowującego figury i ich pola
figury = {
    'kwadrat': [],
    'prostokąt': [],
    'koło': [],
    'trapez': []
}

# fukcja tworząca okno do obliczenia pola wybranej figury
def OknoPole(figura):
    window = tk.Toplevel()     # stworzenie nowego okna             

    label1 = tk.Label(window, text='')
    label1.grid(row=0, column=0)

    entry1 = tk.Entry(window)
    entry1.grid(row=0, column=1)

    label2 = tk.Label(window, text='')
    label2.grid(row=1, column=0)

    label3 = tk.Label(window, text='')
    label3.grid(row=2, column=0)

    labelOut = tk.Label(window, text='')
    labelOut.grid(row=4, column=1)

    # dopasowanie funkcji oraz ilości i nazw parametrów w zależności od typu figury 
    match figura:
        case 'kwadrat':
            label1.configure(text="podaj długość boku: ")

            # zdefiniowanie funkcji liczącej pole
            def oblicz():
                x = pole(False, int(entry1.get()))
                labelOut.configure(
                    text=f'pole: {x}')
                if (x > 0):     # sprawdzenie, czy nie wystąpił błąd (-1)
                    figury['kwadrat'].append(x)     # dodanie wyniku do słownika
        case 'koło':
            label1.configure(text="podaj promień: ")

            # zdefiniowanie funkcji liczącej pole
            def oblicz():
                x = pole(True, int(entry1.get()))
                labelOut.configure(
                    text=f'pole: {x}')
                if (x > 0):     # sprawdzenie, czy nie wystąpił błąd (-1)
                    figury['koło'].append(x)        # dodanie wyniku do słownika
        case 'prostokąt':
            label1.configure(text="podaj długość boku a: ")
            label2.configure(text="podaj długość boku b: ")

            entry2 = tk.Entry(window)
            entry2.grid(row=1, column=1)

            # zdefiniowanie funkcji liczącej pole
            def oblicz():
                x = pole(False, int(entry1.get()), int(entry2.get()))
                labelOut.configure(
                    text=f'pole: {x}')
                if (x > 0):     # sprawdzenie, czy nie wystąpił błąd (-1)
                    figury['prostokąt'].append(x)   # dodanie wyniku do słownika
        case 'trapez':
            label1.configure(text="podaj długość podstawy a: ")
            label2.configure(text="podaj długość podstawy b: ")
            label3.configure(text="podaj wysokość: ")

            entry2 = tk.Entry(window)
            entry2.grid(row=1, column=1)

            entry3 = tk.Entry(window)
            entry3.grid(row=2, column=1)

            # zdefiniowanie funkcji liczącej pole
            def oblicz():
                x = pole(False, int(entry1.get()), int(
                    entry2.get()), int(entry3.get()))
                labelOut.configure(
                    text=f'pole: {x}')
                if (x > 0):     # sprawdzenie, czy nie wystąpił błąd (-1)
                    figury['trapez'].append(x)  # dodanie wyniku do słownika

    button = tk.Button(window, text='oblicz', command=oblicz)   # przycisk do wykonania obliczenia
    button.grid(row=3, column=1)

# fukcja tworząca okno zapisu
def OknoZapisz():
    window = tk.Toplevel()      # utworzenie nowego okna

    label = tk.Label(window, text='podaj nazwę dla pliku: ')
    label.grid(row=0, column=0)

    entry = tk.Entry(window)
    entry.grid(row=0, column=1)

    # funkcja zapisująca dane ze słownika do pliku txt
    def Save():
        out = ''

        for key in figury.keys():
            if len(figury[key]) > 0:
                for figura in figury[key]:
                    out += f"Pole {key}: {figura}\n"

        try:
            file2write = open(str(entry.get()) +
                              ".txt", 'w', encoding='utf-8')    # otwarcie pliku do zapisu
            file2write.write(out)       # zapis do pliku
            file2write.close()          # zamknięcie pliku

            print("zapisano do pliku")
        except:
            print("wystąpił błąd, dane nie zostały zapisane")

    button = tk.Button(window, text='zapsiz do pliku', command=Save)    # przycisk do zapisu
    button.grid(row=1, column=0)


ws = tk.Tk()            # utworzenie okna głównego
ws.title("Pola figur")  # ustawienie tytułu okna

# utworzenie przycisków dla figur
kwadrat = tk.Button(ws, text="kwadrat", command=lambda: OknoPole('kwadrat'))
kolo = tk.Button(ws, text="koło", command=lambda: OknoPole('koło'))
prostokat = tk.Button(ws, text="prostokąt", command=lambda: OknoPole('prostokąt'))
trapez = tk.Button(ws, text="trapez", command=lambda: OknoPole('trapez'))
zapisz = tk.Button(ws, text="zapisz", command=OknoZapisz)

# wyświetlenie przycisków
kwadrat.pack()
kolo.pack()
prostokat.pack()
trapez.pack()
zapisz.pack()

# uruchomienie pętli okna głównego
ws.mainloop()