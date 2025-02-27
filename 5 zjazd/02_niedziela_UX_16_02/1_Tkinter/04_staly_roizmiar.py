import tkinter as tk

root = tk.Tk()
root.title('Zablokowane rozmioary okna')
root.geometry('600x400+1200+80') # Określa rozmiar i pozycję startową okna:
root.resizable(False,True) #Ogranicza możliwość zmiany rozmiaru okna:
# Szerokość (width) jest zablokowana (nie można zmienić). Wysokość (height) można zmieniać.
root.mainloop()

