from tkinter import *
from PIL import ImageTk, Image
import os, random




def tiedoston_valinta():
    dir = random.randrange(0, 2);
    return dir
  

def kuvanpaikka(image, okno):
    imagesprite = okno.create_image(15, 10, anchor='nw', image=image)

def kuvan_valinta(okno, spisok):
    
         
    papka = tiedoston_valinta()
    
    if  papka == 0:
        path = "AA\Acters"
    
    else:
        path = "AA\Actress"
        
    kuva = random.choice(os.listdir(path));

    tie = os.path.join(path, kuva)
    
    pilImage = Image.open(tie)
    image = ImageTk.PhotoImage(pilImage)
    kuvanpaikka(image, okno)

    
    Hkl = kuva[0:-4]
    Act = Hkl.rsplit("_")
    lista = []

    if len(spisok) == 50:
            you_win()
            
    else:
        if Act in spisok:
            click_button()
               
            
        else:
           lista.append(Hkl)

        while len(lista) < 4:
            add = random.choice(os.listdir(path))
            if add != Hkl:
                add = add[0:-4]
                if add not in lista:
                    lista.append(add)
        
        

        text1 = random.choice(lista)
        lista.remove(text1)
        Act1 = text1.rsplit("_")

        text2 = random.choice(lista)
        lista.remove(text2)
        Act2 = text2.rsplit("_")

        text3 = random.choice(lista)
        lista.remove(text3)
        Act3 = text3.rsplit("_")

        text4 = random.choice(lista)
        Act4 = text4.rsplit("_")
        spisok.append(Act)
       

                              
        if Act1 == Act:        
            button1 = Button(text=Act1, background="#555", foreground="#ccc",
                 padx="30", pady="10", font="24", command=clair)
                
        else:
            button1 = Button(text=Act1, background="#555", foreground="#ccc",
                 padx="30", pady="10", font="24", command=game_over)
    
        if Act2 == Act:
            button2 = Button(text=Act2, background="#555", foreground="#ccc",
                 padx="30", pady="10", font="16", command=clair)
        else:
            button2 = Button(text=Act2, background="#555", foreground="#ccc",
                 padx="30", pady="10", font="24", command=game_over)

        if Act3 == Act:
            button3 = Button(text=Act3, background="#555", foreground="#ccc",
                 padx="30", pady="10", font="16", command=clair)
        else:
            button3 = Button(text=Act3, background="#555", foreground="#ccc",
                 padx="30", pady="10", font="24", command=game_over)

        if Act4 == Act:
            button4 = Button(text=Act4, background="#555", foreground="#ccc",
                 padx="30", pady="10", font="16", command=clair)
        else:
            button4 = Button(text=Act4, background="#555", foreground="#ccc",
                 padx="30", pady="10", font="24", command=game_over)
    
        button1_window = okno.create_window(350, 30, width=300, height=50, anchor=NW, window=button1)
        button2_window = okno.create_window(350, 130, width=300, height=50, anchor=NW, window=button2)
        button3_window = okno.create_window(350, 230, width=300, height=50, anchor=NW, window=button3)
        button4_window = okno.create_window(350, 330, width=300, height=50, anchor=NW, window=button4)

        root.mainloop()
        
        

def clair():
    canvas.delete(all)
    click_button()    

   
        

def click_button():
    
    kuvan_valinta(canvas, arvottu)
    

def game_over():
    post_over(root, canvas)
    
def post_over(root, vas):
    root.destroy()
    arvottu.clear()
    root = Tk()
    root.title("Wrong")
    root.geometry("700x415")
    vas = Canvas(root, width=700, height=415)
    vas.pack(side=LEFT)
    
    
    knopka = Button(text="Game over :(", background="#555", foreground="#ccc",
                 padx="30", pady="10", font="36", command=vyhod_von)
    knopka_window = vas.create_window(150, 100, width=400, height=100, anchor=NW, window=knopka)
    knopka2 = Button(text="New game", background="#555", foreground="#ccc",
                 padx="30", pady="10", font="24", command=root.destroy)
    knopka2_window = vas.create_window(225, 300, width=250, height=50, anchor=NW, window=knopka2)
    
    
    

    
    

def you_win():
    post_win(root, canvas)
def post_win(root, vas):    
    root.destroy()
    arvottu.clear()
    root = Tk()
    root.title("You win!")
    root.geometry("700x415")
    vas = Canvas(root, width=700, height=415)
    vas.pack(side=LEFT)
    
    
    knopka = Button(text="You win!", background="#fff5ee", foreground="#cd853f",
                 padx="30", pady="10", font="36", command=vyhod_von)
    knopka_window = vas.create_window(150, 100, width=400, height=100, anchor=NW, window=knopka)
    knopka2 = Button(text="New game", background="#555", foreground="#ccc",
                 padx="30", pady="10", font="24", command=root.destroy)
    knopka2_window = vas.create_window(225, 300, width=250, height=50, anchor=NW, window=knopka2)
    
def vyhod_von():
    
    sl["a"] = 1
    

arvottu = []
z = 0
sl = {
    "a" : z
    }
while sl["a"] == 0:
    try:
        root = Tk()
        root.title("Guess 50 stars of classic Hollywood")
        root.geometry("700x415")
    
    
    
        canvas = Canvas(root, width=700, height=415)
        canvas.pack(side=LEFT)
    
        button = Button
        click_button()
    except UnboundLocalError:
       continue
