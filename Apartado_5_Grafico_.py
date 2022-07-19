import tkinter as tk
from tkinter import filedialog as fd
import io

def cuadro_dialogo():
    nom_arxiu = fd.askopenfilename()
    llibre = io.open(nom_arxiu,"r")
    linies = llibre.readlines()
    llibre.close()

    cuarenta_palabras(linies)

def cuarenta_palabras(linies):
    lista_3 = []
    contador = 1
    while contador <= 40:
        lista_3.append(linies[contador])
        contador += 1

    for cadena in lista_3:
        listbox1.insert(tk.END, cadena)

# inicializador de root
root = tk.Tk()
amplada = root.winfo_screenwidth()
alcada = root.winfo_screenheight()
strink = '{}x{}'.format(amplada,alcada)
root.geometry(strink)
root.attributes('-fullscreen',True)

# inicializador Frame
frame1 = tk.Frame(root,bg='#22afe8')
frame1.place(x=0, y=0, width = amplada, height = alcada)

#Definicio de Widget Listbox
listbox1 = tk.Listbox(frame1)
listbox1.place( x = 6 * amplada//10, y = 4*alcada//10, width= 3*amplada//10, height= 4*alcada//10, anchor = tk.CENTER)

#Definicio de Widget Button
boto1 = tk.Button(frame1, text = "Resultat", command = cuadro_dialogo)
boto1.place(  x = 3 * amplada//10, y = 3 * alcada // 10, width= 1 * amplada // 10, height= 0.5 * alcada // 10, anchor = tk.CENTER)

#Definicio de Widget Button
boto2 = tk.Button(frame1, text = "Salir", command = root.destroy)
boto2.place(x = 3 * amplada//10, y = 5 * alcada // 10, width= 1 * amplada // 10, height= 0.5 * alcada // 10, anchor = tk.CENTER)

#Definicio de Widget Text Label
labeltext1 = tk.Label(frame1, text = "Botones", bg = frame1.cget('bg'))
labeltext1.place( x = 3 * amplada//10, y = 1.5*alcada//10, anchor = tk.CENTER)

#Definicio de Widget Listbox Label
labellistbox1 = tk.Label(frame1, text = "Las 40 primeras palabras", bg = frame1.cget('bg'))
labellistbox1.place( x = 6 * amplada//10, y = 1.5*alcada//10, anchor = tk.CENTER) 

# mantenedor de root
root.mainloop()
