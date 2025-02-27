import tkinter as tk                    # Importujemy standardową bibliotekę Tkinter i przypisujemy jej alias 'tk'
from tkinter.messagebox import showinfo
import customtkinter as ctk             # Importujemy CustomTkinter (ctk), który pozwala na tworzenie nowoczesnych interfejsów użytkownika

# Definiujemy funkcję, która będzie wywoływana po kliknięciu przycisku "Entry"
def clicked_entry():
    msg = f'Wpisałeś: {entry_text.get()}'       # Pobieramy tekst wpisany w pole Entry i formatujemy go do wiadomości
    showinfo(title='Pole ENTRY', message=msg)   # Wyświetlamy komunikat w oknie dialogowym
    print('Kliknęto')                           # Wypisujemy informacje w konsoli (pomocne do debugowania)
    print(f'Wpisano {entry_text.get()}')

# Definiujemy funkcję, która będzie wywoływana po kliknięciu przycisku "Text"
def clicked_text():
    content = text_field.get('1.0', tk.END)         # Pobiera tekst od początku ("1.0") do końca (tk.END)
    showinfo(title='POte tekstowe TEXT', message=content)  # Wyświetlamy pobraną treść w oknie dialogowym

root = ctk.CTk()                # Tworzymy główne okno aplikacji za pomocą CustomTkinter (ctk)
entry_text = tk.StringVar()     # Tworzymy zmienną typu StringVar(), która będzie przechowywać wpisany tekst
# StringVar() jest dynamiczną zmienną Tkintera, umożliwia śledzenie zmian w polu Entry.

frame = tk.Frame()                          # Tworzymy ramkę (frame), która posłuży do grupowania elementów interfejsu
frame.pack(padx=50, pady=50)                # Umieszczamy ramkę w głównym oknie z odstępami 50 pikseli na każdą stronę
label = tk.Label(frame, text='Wpisz cos')   # Tworzymy etykietę z tekstem "Wpisz coś"
label.pack()                                # Umieszczamy etykietę w ramce
entry = tk.Entry(                           # Tworzymy pole tekstowe Entry, w którym użytkownik może wpisać dane
    frame,
    textvariable=entry_text,                # pozwala na powiązanie pola z naszą zmienną entry_text
    show='*',                               # ukrywa wpisany tekst (np. jak w polu hasła)
    font=('Helvetica', 20)                  # ustawia czcionkę na Helveticę o rozmiarze 20
)
entry.pack(ipadx=100, ipady=30)             # Umieszczamy pole tekstowe w ramce i rozszerzamy je wewnętrznie o 100 pikseli poziomo i 30 pionowo
text_field = tk.Text(                       # Tworzymy pole tekstowe Text, które umożliwia wpisywanie wielu linii tekstu
    frame,
    height=3,                               # oznacza, że będzie miało 3 wiersze
    width=40                                # oznacza szerokość na 40 znaków
)
text_field.pack()                           # Umieszczamy pole tekstowe w ramce
button1 = tk.Button(frame, text='Entry', command=clicked_entry)     # Tworzymy przycisk "Entry", który po kliknięciu wywoła funkcję clicked_entry()
button1.pack(                               # Umieszczamy przycisk w ramce
    fill='x',                               # oznacza, że przycisk rozciągnie się na całą szerokość ramki
    ipady=5,                                # zwiększa wysokość przycisku o 5 pikseli
    pady=5                                  # odaje odstęp 5 pikseli nad i pod przyciskiem
)
button2 = tk.Button(frame, text='Text', command=clicked_text)   # Tworzymy drugi przycisk "Text", który po kliknięciu wywoła funkcję clicked_text()
button2.pack()                              # Umieszczamy drugi przycisk w ramce (bez dodatkowego rozciągania)

root.mainloop()

