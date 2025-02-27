import tkinter as tk

root = tk.Tk()
root.attributes('-topmost',1)           # Ustawiamy, aby okno zawsze było na wierzchu
root.attributes('-alpha', 0.9)          # Ustawiamy przezroczystość okna (0 = całkowicie przezroczyste, 1 = pełna widoczność)
root.geometry('500x600+1300+100')       # Ustawiamy rozmiar okna: szerokość 500, wysokość 600, oraz jego pozycję (x=1300, y=100)
root.title('moj program')               # Nadajemy tytuł okna

label = tk.Label(
    root, text='Siema',                 # Tworzymy etykietę (label) z napisem "Siema"
    font=('Arial',20),                  # - Czcionka: Arial, rozmiar 20
    background='#265ECE',               # Tło etykiety: kolor #265ECE (niebieski)
    fg='red'                            # Kolor tekstu (fg - foreground): czerwony
)
label.pack(padx=20, pady=20)            # Umieszczamy etykietę w oknie z odstępami 20 pikseli na zewnątrz (padding)
textbox = tk.Text(root, height=3, font=('Arial',14))    # Tworzymy pole tekstowe (Text) o wysokości 3 linii i czcionce Arial, 14 px
textbox.pack(padx=10, pady=20)          # Umieszczamy pole tekstowe w oknie z odstępami 10 pikseli na boki i 20 na górę/dó

buttonframe = tk.Frame(root)            # Tworzymy ramkę (Frame) do przechowywania przycisków
buttonframe.columnconfigure(0, weight=1)        # Konfigurujemy kolumny w ramce, aby przyciski były równomiernie rozmieszczone
buttonframe.columnconfigure(1,  weight=1,)
buttonframe.columnconfigure(2,  weight=1)
# buttonframe.rowconfigure - ustawianie szerokosci wierszy

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 15))         # Pierwszy przycisk (1) w pierwszym wierszu, pierwszej kolumnie
btn1.grid(row=0, column=0, sticky=tk.W+tk.E, pady =10, padx=10)     # Rozciąganie poziome
btn2 = tk.Button(buttonframe, text='2', font=('Arial', 15))         # Drugi przycisk (2) w pierwszym wierszu, drugiej kolumnie
btn2.grid(row=0, column=1, sticky=tk.W+tk.E, pady=10)
btn3 = tk.Button(buttonframe, text='3', font=('Arial', 15))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(buttonframe, text='4', font=('Arial', 15))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(buttonframe, text='5', font=('Arial', 15))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
btn6 = tk.Button(buttonframe, text='6', font=('Arial', 15))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')          # Umieszczamy ramkę z przyciskami w głównym oknie fill='x' oznacza, że ramka będzie się rozciągać w poziomie

# Tworzymy przycisk "Wyjdź", który zamyka aplikację po kliknięciu
quit_btn = tk.Button(root, text='Wyjdź', command=root.quit, bg='red')   # Kolor tła: czerwony (bg='red')

# Umieszczamy przycisk "Wyjdź" w oknie w określonej pozycji (x=200, y=450)
quit_btn.place(x=200, y=450, height=100, width= 100)    # - height=100, width=100 oznacza, że przycisk ma wymiary 100x100 pikseli
root.mainloop()