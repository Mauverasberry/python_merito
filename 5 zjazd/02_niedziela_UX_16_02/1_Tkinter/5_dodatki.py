import tkinter as tk

root = tk.Tk()
root.title ('Max i min okna')
root.geometry('600x400+1200+80')
root.minsize(300,300) #Okno nie może być mniejsze niż 300x300.
root.maxsize(800,500) #Okno nie może być większe niż 800x500.
root.attributes('-alpha', 0.8) #Ustawia przezroczystość okna (wartości od 0.0 do 1.0): 1.0 → w pełni widoczne.
# 0.8 → 80% widoczności (trochę przezroczyste)
root.attributes('-topmost',1) #okno zawsze na wierzchu 1 → aktywuje tę opcję, 0 → wyłącza.
root.iconbitmap('logo.ico')  #ikonka własna (dołączona do folderu projektu)

root.mainloop()

