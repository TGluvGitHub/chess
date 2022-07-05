#Chess 1.0
#Authors - Theo and Matt
#Made for summer project 2022
#class RookPiece:
from tkinter import *
from tkinter import ttk


class BoardSetup:

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
    canvas.create_image(100,100,image='terrible_rook.png', anchor=NW)
    gui.mainloop()
    BoardSetup()
##root = Tk()
##frm = ttk.Frame(root, padding=10)
##frm.grid()
##ttk.Label(frm, text="Chess!").grid(column=0, row=0)
##ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
##root.mainloop()





print("Hey, im controlling")
