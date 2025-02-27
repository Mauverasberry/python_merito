import tkinter as tk

def hello():
    print('Leci akcja')

root = tk.Tk()
#exit_button = tk.Button(text='Wyjście', command=hello)  # utworzy przycisk z tekstem 'Wyjście', który po kliknięciu wywoływałby wcześniej zdefiniowaną funkcję hello()
exit_button = tk.Button(text='Wyjście', command=root.quit) # Tworzymy przycisk z etykietą 'Wyjście', który po kliknięciu zamknie aplikację
# 'command=root.quit' sprawia, że aplikacja zostanie zamknięta po kliknięciu przycisku

exit_button.pack(ipadx=10, ipady=50) #ustawia sposób rozmieszczenia przycisku w oknie.
# Umieszczamy przycisk w oknie i określamy jego wewnętrzne marginesy (padding)
# 'ipadx=10' - powiększa przycisk w poziomie o 10 pikseli
# 'ipady=50' - powiększa przycisk w pionie o 50 pikseli

root.mainloop()

