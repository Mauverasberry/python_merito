import tkinter as tk
# import customtkinter as ctk

root = tk.Tk()
root.title('Tkinter')

# Pobranie rozmiaru ekranu
window_width = 300                          # Ustawienie szerokości okna na 300 pikseli
window_height = 200
screen_width = root.winfo_screenwidth()     # pobranie szerokosci  ekranu w pikselach
screen_height = root.winfo_screenheight()   # Pobiera wysokość ekranu w pikselach
print(screen_width, screen_height)

# Oblicza środek ekranu, aby okno było wyśrodkowane. Dzieli szerokość i wysokość ekranu na pół, a następnie odejmuje połowę szerokości i wysokości okna.
# Dzielimy szerokość i wysokość ekranu przez 2 (środek ekranu).
# Odejmujemy połowę szerokości i wysokości okna, aby okno było wycentrowane.
center_x = int(screen_width/2 - window_width / 2)   # Oblicza środek ekranu w poziomie
center_y = int(screen_height/2 - window_height / 2) # Oblicza środek ekranu w pionie

#Ustawia pozycję i rozmiar okna na 300x200 pikseli.Ustawia położenie okna na środku ekranu.
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

message1 = tk.Label(root, text='Witamy we Wrocławiu') # Tworzy etykietę (Label) z tekstem "Witamy we Wrocławiu".
message1.pack()                                       # automatycznie dodaje ją do okna i ustawia jej pozycję w 1 wolnym miejscu
message2 = tk.Label(root, text='')
message2.pack()
message3 = tk.Label(root, text='...')
message3.pack()

root.mainloop()



