#Chess 1.0
#Authors - Theo and Matt
#Made for summer project 2022
#class RookPiece:
from tkinter import *
from tkinter import ttk
import PIL
from PIL import ImageTk
from PIL import Image
from pynput import mouse


def ReturnClickCoords(x, y):
    if x >= 0 and x<= 100 and y>=900 and y <=1000 :
        print("a1")
        return "a1"
    if x >= 0 and x<= 100 and y>=800 and y <=900 :
        print("a2")
        return "a2"
    if x >= 0 and x<= 100 and y>=700 and y <=800 :
        print("a3")
        return "a3"
    if x >= 0 and x<= 100 and y>=600 and y <=700 :
        print("a4")
        return "a4"
    if x >= 0 and x<= 100 and y>=500 and y <=600 :
        print("a5")
        return "a5"
    if x >= 0 and x<= 100 and y>=400 and y <=500 :
        print("a6")
        return "a6"
    if x >= 0 and x<= 100 and y>=300 and y <=400 :
        print("a7")
        return "a7"
    if x >= 0 and x<= 100 and y>=200 and y <=300 :
        print("a8")
        return "a8"
    if x >= 100 and x<= 200 and y>=900 and y <=1000:
        print("b1")             
        return "b1"             
    if x >= 100 and x<= 200 and y>=800 and y <=900  :
        print("b2")             
        return "b2"             
    if x >= 100 and x<= 200 and y>=700 and y <=800  :
        print("b3")             
        return "b3"             
    if x >= 100 and x<= 200 and y>=600 and y <=700  :
        print("b4")             
        return "b4"             
    if x >= 100 and x<= 200 and y>=500 and y <=600 : 
        print("b5")             
        return "b5"             
    if x >= 100 and x<= 200 and y>=400 and y <=500:  
        print("b6")             
        return "b6"             
    if x >= 100 and x<= 200 and y>=300 and y <=400  :
        print("b7")             
        return "b7"             
    if x >= 100 and x<= 200 and y>=200 and y <=300  :
        print("b8")
        return "b8"
    if x >= 200 and x<= 300 and y>=900 and y <=1000 :
        print("c1")           
        return "c1"           
    if x >= 200 and x<= 300 and y>=800 and y <=900 : 
        print("c2")           
        return "c2"           
    if x >= 200 and x<= 300 and y>=700 and y <=800 : 
        print("c3")           
        return "c3"           
    if x >= 200 and x<= 300 and y>=600 and y <=700  :
        print("c4")           
        return "c4"           
    if x >= 200 and x<= 300 and y>=500 and y <=600 : 
        print("c5")           
        return "c5"           
    if x >= 200 and x<= 300 and y>=400 and y <=500 : 
        print("c6")           
        return "c6"           
    if x >= 200 and x<= 300 and y>=300 and y <=400 : 
        print("c7")           
        return "c7"           
    if x >= 200 and x<= 300 and y>=200 and y <=300 : 
        print("c8")
        return "c8"
    if x >= 300 and x<= 400 and y>=900 and y <=1000 :
        print("d1")           
        return "d1"           
    if x >= 300 and x<= 400 and y>=800 and y <=900 : 
        print("d2")           
        return "d2"           
    if x >= 300 and x<= 400 and y>=700 and y <=800 : 
        print("d3")           
        return "d3"           
    if x >= 300 and x<= 400 and y>=600 and y <=700 : 
        print("d4")           
        return "d4"           
    if x >=300 and x<= 400 and y>=500 and y <=600 : 
        print("d5")           
        return "d5"           
    if x >= 300 and x<= 400 and y>=400 and y <=500  :
        print("d6")           
        return "d6"           
    if x >= 300 and x<= 400 and y>=300 and y <=400 : 
        print("d7")           
        return "d7"           
    if x >= 300 and x<= 400 and y>=200 and y <=300  :
        print("d8")
        return "d8"
    if x >= 400 and x<= 500 and y>=900 and y <=1000 :
        print("e1")           
        return "e1"           
    if x >= 400 and x<= 500 and y>=800 and y <=900 : 
        print("e2")           
        return "e2"           
    if x >= 400 and x<= 500 and y>=700 and y <=800 : 
        print("e3")           
        return "e3"           
    if x >= 400 and x<= 500 and y>=600 and y <=700  :
        print("e4")           
        return "e4"           
    if x >= 400 and x<= 500 and y>=500 and y <=600 : 
        print("e5")           
        return "e5"           
    if x >= 400 and x<= 500 and y>=400 and y <=500  :
        print("e6")           
        return "e6"           
    if x >= 400 and x<= 500 and y>=300 and y <=400  :
        print("e7")           
        return "e7"           
    if x >= 400 and x<= 500 and y>=200 and y <=300  :
        print("e8")
        return "e8"
    if x >= 500 and x<= 600 and y>=900 and y <=1000 :
        print("f1")           
        return "f1"           
    if x >= 500 and x<= 600 and y>=800 and y <=900  :
        print("f2")           
        return "f2"           
    if x >= 500 and x<= 600 and y>=700 and y <=800  :
        print("f3")           
        return "f3"           
    if x >= 500 and x<= 600 and y>=600 and y <=700  :
        print("f4")           
        return "f4"           
    if x >= 500 and x<= 600 and y>=500 and y <=600  :
        print("f5")           
        return "f5"           
    if x >= 500 and x<= 600 and y>=400 and y <=500  :
        print("f6")           
        return "f6"           
    if x >= 500 and x<= 600 and y>=300 and y <=400  :
        print("f7")           
        return "f7"           
    if x >= 500 and x<= 600 and y>=200 and y <=300  :
        print("f8")
        return "f8"
    if x >= 600 and x<= 700 and y>=900 and y <=1000 :
        print("g1")           
        return "g1"           
    if x >= 600 and x<= 700 and y>=800 and y <=900:  
        print("g2")           
        return "g2"           
    if x >= 600 and x<= 700 and y>=700 and y <=800 : 
        print("g3")           
        return "g3"           
    if x >= 600 and x<= 700 and y>=600 and y <=700  :
        print("g4")           
        return "g4"           
    if x >= 600 and x<= 700 and y>=500 and y <=600 : 
        print("g5")           
        return "g5"           
    if x >= 600 and x<= 700 and y>=400 and y <=500 : 
        print("g6")           
        return "g6"           
    if x >= 600 and x<= 700 and y>=300 and y <=400  :
        print("g7")           
        return "g7"           
    if x >= 600 and x<= 700 and y>=200 and y <=300  :
        print("g8")
        return "g8"
    if x >= 700 and x<= 800 and y>=900 and y <=1000 :
        print("h1")           
        return "h1"           
    if x >= 700 and x<= 800 and y>=800 and y <=900 : 
        print("h2")           
        return "h2"           
    if x >= 700 and x<= 800 and y>=700 and y <=800 : 
        print("h3")           
        return "h3"           
    if x >= 700 and x<= 800 and y>=600 and y <=700  :
        print("h4")           
        return "h4"           
    if x >= 700 and x<= 800 and y>=500 and y <=600 : 
        print("h5")           
        return "h5"           
    if x >= 700 and x<= 800 and y>=400 and y <=500 : 
        print("h6")           
        return "h6"           
    if x >= 700 and x<= 800 and y>=300 and y <=400  :
        print("h7")           
        return "h7"	          
    if x >= 700 and x<= 800 and y>=200 and y <=300  :
        print("h8")
        return "h8"	

    return "Outside"


class BuildBoard:

    gui = Tk(className='Chess')
    # set window size
    gui.geometry("1000x1000")
    canvas = Canvas(gui,width=1000,height=1000)
    canvas.pack()
    a1 = canvas.create_rectangle(0,900,100,1000,fill='brown')
    a2 = canvas.create_rectangle(0,800,100,900,fill='white')
    a3 = canvas.create_rectangle(0,700,100,800,fill='brown')
    a4 = canvas.create_rectangle(0,600,100,700,fill='white')
    a5 = canvas.create_rectangle(0,500,100,600,fill='brown')
    a6 = canvas.create_rectangle(0,400,100,500,fill='white')
    a7 = canvas.create_rectangle(0,300,100,400,fill='brown')
    a8 = canvas.create_rectangle(0,200,100,300,fill='white')

    b1 = canvas.create_rectangle(100,900,200,1000,fill='white')
    b2 = canvas.create_rectangle(100,800,200,900,fill='brown')
    b3 = canvas.create_rectangle(100,700,200,800,fill='white')
    b4 = canvas.create_rectangle(100,600,200,700,fill='brown')
    b5 = canvas.create_rectangle(100,500,200,600,fill='white')
    b6 = canvas.create_rectangle(100,400,200,500,fill='brown')
    b7 = canvas.create_rectangle(100,300,200,400,fill='white')
    b8 = canvas.create_rectangle(100,200,200,300,fill='brown')

    c1 = canvas.create_rectangle(200,900,300,1000,fill='brown')
    c2 = canvas.create_rectangle(200,800,300,900,fill='white')
    c3 = canvas.create_rectangle(200,700,300,800,fill='brown')
    c4 = canvas.create_rectangle(200,600,300,700,fill='white')
    c5 = canvas.create_rectangle(200,500,300,600,fill='brown')
    c6 = canvas.create_rectangle(200,400,300,500,fill='white')
    c7 = canvas.create_rectangle(200,300,300,400,fill='brown')
    c8 = canvas.create_rectangle(200,200,300,300,fill='white')

    d1 = canvas.create_rectangle(300,900,400,1000,fill='white')
    d2 = canvas.create_rectangle(300,800,400,900,fill='brown')
    d3 = canvas.create_rectangle(300,700,400,800,fill='white')
    d4 = canvas.create_rectangle(300,600,400,700,fill='brown')
    d5 = canvas.create_rectangle(300,500,400,600,fill='white')
    d6 = canvas.create_rectangle(300,400,400,500,fill='brown')
    d7 = canvas.create_rectangle(300,300,400,400,fill='white')
    d8 = canvas.create_rectangle(300,200,400,300,fill='brown')    

    e1 = canvas.create_rectangle(400,900,500,1000,fill='brown')
    e2 = canvas.create_rectangle(400,800,500,900,fill='white')
    e3 = canvas.create_rectangle(400,700,500,800,fill='brown')
    e4 = canvas.create_rectangle(400,600,500,700,fill='white')
    e5 = canvas.create_rectangle(400,500,500,600,fill='brown')
    e6 = canvas.create_rectangle(400,400,500,500,fill='white')
    e7 = canvas.create_rectangle(400,300,500,400,fill='brown')
    e8 = canvas.create_rectangle(400,200,500,300,fill='white')

    f1 = canvas.create_rectangle(500,900,600,1000,fill='white')
    f2 = canvas.create_rectangle(500,800,600,900,fill='brown')
    f3 = canvas.create_rectangle(500,700,600,800,fill='white')
    f4 = canvas.create_rectangle(500,600,600,700,fill='brown')
    f5 = canvas.create_rectangle(500,500,600,600,fill='white')
    f6 = canvas.create_rectangle(500,400,600,500,fill='brown')
    f7 = canvas.create_rectangle(500,300,600,400,fill='white')
    f8 = canvas.create_rectangle(500,200,600,300,fill='brown')

    g1 = canvas.create_rectangle(600,900,700,1000,fill='brown')
    g2 = canvas.create_rectangle(600,800,700,900,fill='white')
    g3 = canvas.create_rectangle(600,700,700,800,fill='brown')
    g4 = canvas.create_rectangle(600,600,700,700,fill='white')
    g5 = canvas.create_rectangle(600,500,700,600,fill='brown')
    g6 = canvas.create_rectangle(600,400,700,500,fill='white')
    g7 = canvas.create_rectangle(600,300,700,400,fill='brown')
    g8 = canvas.create_rectangle(600,200,700,300,fill='white')

    h1 = canvas.create_rectangle(700,900,800,1000,fill='white')
    h2 = canvas.create_rectangle(700,800,800,900,fill='brown')
    h3 = canvas.create_rectangle(700,700,800,800,fill='white')
    h4 = canvas.create_rectangle(700,600,800,700,fill='brown')
    h5 = canvas.create_rectangle(700,500,800,600,fill='white')
    h6 = canvas.create_rectangle(700,400,800,500,fill='brown')
    h7 = canvas.create_rectangle(700,300,800,400,fill='white')
    h8 = canvas.create_rectangle(700,200,800,300,fill='brown')

    canvas.create_text(10, 990, text="a", fill="black", font=('Helvetica 14'))
    canvas.create_text(110, 990, text="b", fill="black", font=('Helvetica 14'))
    canvas.create_text(210, 990, text="c", fill="black", font=('Helvetica 14'))
    canvas.create_text(310, 990, text="d", fill="black", font=('Helvetica 14'))
    canvas.create_text(410, 990, text="e", fill="black", font=('Helvetica 14'))
    canvas.create_text(510, 990, text="f", fill="black", font=('Helvetica 14'))
    canvas.create_text(610, 985, text="g", fill="black", font=('Helvetica 14'))
    canvas.create_text(710, 990, text="h", fill="black", font=('Helvetica 14'))
    
    canvas.create_text(10, 910, text="1", fill="black", font=('Helvetica 14'))
    canvas.create_text(10, 810, text="2", fill="black", font=('Helvetica 14'))
    canvas.create_text(10, 710, text="3", fill="black", font=('Helvetica 14'))
    canvas.create_text(10, 610, text="4", fill="black", font=('Helvetica 14'))
    canvas.create_text(10, 510, text="5", fill="black", font=('Helvetica 14'))
    canvas.create_text(10, 410, text="6", fill="black", font=('Helvetica 14'))
    canvas.create_text(10, 310, text="7", fill="black", font=('Helvetica 14'))
    canvas.create_text(10, 210, text="8", fill="black", font=('Helvetica 14'))
    img = ImageTk.PhotoImage(Image.open("terrible_black_rook.png"))
    img1 = ImageTk.PhotoImage(Image.open("keen_black_queen.png"))
    img2 = ImageTk.PhotoImage(Image.open("fling_black_king.png"))
    img3 = ImageTk.PhotoImage(Image.open("terribishop_black.png"))
    img4 = ImageTk.PhotoImage(Image.open("terrihorseakaknight.png"))
    img5 = ImageTk.PhotoImage(Image.open("ponny.png"))    
    
    canvas.create_image(10,910,image=img, anchor=NW)
    canvas.create_image(410,910,image=img1, anchor=NW)
    canvas.create_image(310,910,image=img2, anchor=NW)
    canvas.create_image(210,910,image=img3, anchor=NW)
    canvas.create_image(510,910,image=img3, anchor=NW)
    canvas.create_image(610,900,image=img4, anchor=NW)
    canvas.create_image(110,900,image=img4, anchor=NW)
    canvas.create_image(10,800,image=img5, anchor=NW)
    canvas.create_image(410,800,image=img5, anchor=NW)
    canvas.create_image(310,800,image=img5, anchor=NW)
    canvas.create_image(210,800,image=img5, anchor=NW)
    canvas.create_image(510,800,image=img5, anchor=NW)
    canvas.create_image(610,800,image=img5, anchor=NW)
    canvas.create_image(110,800,image=img5, anchor=NW)
    canvas.create_image(700,800,image=img5, anchor=NW)
    canvas.create_image(700,900,image=img, anchor=NW)

    def selectPiece(event):  
        print("clicked at: ", event.x, event.y)
        click1 = ReturnClickCoords(event.x, event.y)
        canvas.bind("<Button-3>", movePiece)
        if click1 == "a1" :
            print("Done")

    def movePiece(event):
        print("MoveX= ",event.x, "MoveY= ",event.y) 
        return event.x, event.y
    
    #menu= StringVar()
    #menu.set("Select Any Language")
    #drop= OptionMenu(gui, menu,"C++", "Java","Python","JavaScript","Rust","GoLang")
    #drop.pack()

    canvas.bind("<Button-1>", selectPiece)
    

    
    gui.mainloop()
    
class SetAllMovement:
   print("theo")
    
    
BuildBoard()
##root = Tk()
##frm = ttk.Frame(root, padding=10)
##frm.grid()
##ttk.Label(frm, text="Chess!").grid(column=0, row=0)
##ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
##root.mainloop()





