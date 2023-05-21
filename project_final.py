import tkinter as tk
from functions import pole


figury = {
    'kwadrat': [],
    'prostokąt': [],
    'koło': [],
    'trapez': []
}


def OknoPole(figura):
    window = tk.Toplevel()

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

    match figura:
        case 'kwadrat':
            label1.configure(text="podaj długość boku: ")

            def oblicz():
                x = pole(False, int(entry1.get()))
                labelOut.configure(
                    text=f'pole: {x}')
                if (x > 0):
                    figury['kwadrat'].append(x)
        case 'koło':
            label1.configure(text="podaj promień: ")

            def oblicz():
                x = pole(True, int(entry1.get()))
                labelOut.configure(
                    text=f'pole: {x}')
                if (x > 0):
                    figury['koło'].append(x)
        case 'prostokąt':
            label1.configure(text="podaj długość boku a: ")
            label2.configure(text="podaj długość boku b: ")

            entry2 = tk.Entry(window)
            entry2.grid(row=1, column=1)

            def oblicz():
                x = pole(False, int(entry1.get()), int(entry2.get()))
                labelOut.configure(
                    text=f'pole: {x}')
                if (x > 0):
                    figury['prostokąt'].append(x)
        case 'trapez':
            label1.configure(text="podaj długość podstawy a: ")
            label2.configure(text="podaj długość podstawy b: ")
            label3.configure(text="podaj wysokość: ")

            entry2 = tk.Entry(window)
            entry2.grid(row=1, column=1)

            entry3 = tk.Entry(window)
            entry3.grid(row=2, column=1)

            def oblicz():
                x = pole(False, int(entry1.get()), int(
                    entry2.get()), int(entry3.get()))
                labelOut.configure(
                    text=f'pole: {x}')
                if (x > 0):
                    figury['trapez'].append(x)

    button = tk.Button(window, text='oblicz', command=oblicz)
    button.grid(row=3, column=1)


def OknoZapisz():
    window = tk.Toplevel()

    label = tk.Label(window, text='podaj nazwę dla pliku: ')
    label.grid(row=0, column=0)

    entry = tk.Entry(window)
    entry.grid(row=0, column=1)

    def Save():
        out = ''

        for key in figury.keys():
            if len(figury[key]) > 0:
                for figura in figury[key]:
                    out += f"Pole {key}: {figura}\n"

        try:
            file2write = open(str(entry.get()) +
                              ".txt", 'w', encoding='utf-8')
            file2write.write(out)
            file2write.close()

            print("zapisano do pliku")
        except:
            print("wystąpił błąd, dane nie zostały zapisane")

    button = tk.Button(window, text='zapsiz do pliku', command=Save)
    button.grid(row=1, column=0)


ws = tk.Tk()
ws.title("Pola figur")

kwadrat = tk.Button(ws, text="kwadrat", command=lambda: OknoPole('kwadrat'))
kolo = tk.Button(ws, text="koło", command=lambda: OknoPole('koło'))
prostokat = tk.Button(ws, text="prostokąt",
                      command=lambda: OknoPole('prostokąt'))
trapez = tk.Button(ws, text="trapez", command=lambda: OknoPole('trapez'))
zapisz = tk.Button(ws, text="zapisz", command=OknoZapisz)

kwadrat.pack()
kolo.pack()
prostokat.pack()
trapez.pack()
zapisz.pack()

ws.mainloop()