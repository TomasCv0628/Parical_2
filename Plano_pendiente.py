import tkinter as tk
from tkinter import INSERT, Label, Frame, Button, Tk, Canvas, IntVar,Entry
from fractions import Fraction

def graficar():
    C.create_line(x1.get()+190,-y1.get()+190,x2.get()+190,-y2.get()+190)

def pendientes():
    r = (y2.get()-y1.get())/(x2.get()-x1.get())
    z = Fraction(r).limit_denominator()
    resultado_pendiente.insert(INSERT, z)
    
    

ventana_principal= Tk()
ventana_principal.title("PLANO CARTESIANO")
ventana_principal.resizable(False, False)
ventana_principal.geometry("600x400")


frame_1= Frame(ventana_principal)
frame_1.config(bg="aquamarine",width=380,height=380)
frame_1.place(x=10,y=10)

C = Canvas(frame_1, width=360, height=360,bg="LightSkyBlue2")
C.place(x=10,y=10)

# Plano cartesiano

X = C.create_line(0,190,380,190)
Y = C.create_line(190,0,190,380)
origen = C.create_oval(192,188,188,192, fill="black")

X_label=C.create_text(355,200, text="X")
Y_label=C.create_text(200,8, text="Y")



# Coordenadas


frame_coordenadas=Frame(ventana_principal, width=190, height=380, bg="LightSkyBlue")
frame_coordenadas.place(x= 400,y= 10)

titulo = Label(frame_coordenadas, text="PLANO \nCARTESIANO", font="TranscendsGames 18")
titulo.config(bg="LightSkyBLue")
titulo.place(x=10,y=10)

x1=IntVar()
y1=IntVar()
x2=IntVar()
y2=IntVar()

X1 = Label(frame_coordenadas, text= "X1 =", bg="LightSkyBlue")
X1.place(x= 10,y= 80)

Entry_X1 = Entry(frame_coordenadas,textvariable=x1,width=5)
Entry_X1.place(x=45 ,y= 80)


Y1 = Label(frame_coordenadas, text= "Y1 = ", bg="LightSkyBlue")
Y1.place(x=10, y= 105 )

Entry_Y1 = Entry(frame_coordenadas,textvariable=y1,width=5)
Entry_Y1.place(x= 45 ,y= 105)

X2 = Label(frame_coordenadas, text= "X2 =", bg="LightSkyBlue")
X2.place(x= 10,y= 165)

Entry_X2 = Entry(frame_coordenadas,textvariable=x2,width=5)
Entry_X2.place(x= 45 ,y= 165)

Y2 = Label(frame_coordenadas, text= "Y2 =", bg="LightSkyBlue")
Y2.place(x=10, y= 190 )

Entry_Y2 = Entry(frame_coordenadas,textvariable=y2,width=5)
Entry_Y2.place(x= 45,y= 190)

Graficar_button=Button(frame_coordenadas,text="Graficar", command=graficar)
Graficar_button.place(x=10,y= 250)

Pendiente=Button(frame_coordenadas, text="Pendiente", command=pendientes )
Pendiente.place(x=10,y= 290)
resultado_pendiente=tk.Text(frame_coordenadas,width=11,height=1)
resultado_pendiente.place(x=10,y=330)


ventana_principal.mainloop()



