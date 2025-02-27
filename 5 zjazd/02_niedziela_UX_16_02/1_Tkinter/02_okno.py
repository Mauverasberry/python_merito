import tkinter as tk                 # Import biblioteki Tkinter i przypisanie aliasu "tk"

root = tk.Tk()                       # tk.Tk() inicjalizuje główne okno aplikacji GUI (Graphical User Interface)
root.title('Tkinter')                # Ustawia nazwę okna, która pojawi się na pasku tytułowym.
root.geometry('600x400+1300+100')    # Okno będzie miało szerokość 600 px i wysokość 400 px.
# Okno zostanie przesunięte względem lewego górnego rogu ekranu: 1300 px od lewej krawędzi ekranu i 100 px od góry ekranu.

message = tk.Label(root, text='Witamy we Wrocławiu')    # Tworzy etykietę z tekstem
message.pack()                                          # Umieszcza etykietę w oknie na pierwszym dostępnym miejscu

message2 = tk.Label(root, text='')                      # Tworzy pustą etykietę (brak tekstu)
message2.pack()                                         # Umieszcza ją w oknie

message3 = tk.Label(root, text='...')                   # Tworzy etykietę z trzema kropkami
message3.pack()                                         #  # Umieszcza ją w oknie

root.mainloop()

