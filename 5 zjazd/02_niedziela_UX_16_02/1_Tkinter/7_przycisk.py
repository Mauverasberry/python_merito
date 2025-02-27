import tkinter as tk                        # Importujemy bibliotekę Tkinter i przypisujemy jej alias 'tk'
from tkinter.messagebox import showinfo     # Importujemy funkcję 'showinfo' z modułu 'messagebox' w Tkinter pozwala wyświetlać okna dialogowe z komunikatami

root = tk.Tk()

def clicked():                              # Definiujemy funkcję, która zostanie wywołana po kliknięciu przycisku
    showinfo(title='Info', message='kliknięto') # Wyświetlamy okno dialogowe z tytułem 'Info' i wiadomością 'kliknięto'

icon = tk.PhotoImage(file='logo.png')   # Tworzymy obiekt obrazu z pliku 'logo.png'
button = tk.Button(                     # Tworzymy przycisk, który będzie zawierał obraz oraz tekst
    text="Przycisk",                    # Tekst, który pojawi się na przycisku
    image=icon,                         # Ustawienie obrazu na przycisku
    compound=tk.TOP,                    # Ustawienie pozycji tekstu względem obrazu (tutaj: obraz na górze)
    command=clicked)                    # Przypisanie funkcji do obsługi kliknięcia przycisku

# Umieszczamy przycisk w oknie i określamy jego właściwości
button.pack(ipadx=11, ipady=11,expand=True) # Powiększenie przycisku poziomo i pionowo o 11 pikseli i Rozciąganie przycisku w dostępnej przestrzeni okna
root.mainloop()

