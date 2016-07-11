from tkinter import *

def almacenar(x):
    global operador
    operador=operador+str(x)
    otrav.set(operador)
    return otrav

ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("400x400")

operador=""
otrav=StringVar()

etiqueta=Label(ventana,text="CASIO Bamba",bd=5,bg="#691B1B",fg="white").pack()
caja=Entry(ventana,textvariable=otrav,font=('arial',20,'bold'),bd=30,bg="powder blue",width=20,justify='right').place(x=20,y=20)
boton1=Button(ventana,text="7",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(7),width=5).place(x=40,y=120)
boton2=Button(ventana,text="8",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(8),width=5).place(x=100,y=120)
boton3=Button(ventana,text="9",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(9),width=5).place(x=160,y=120)
boton4=Button(ventana,text="/",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("/"),width=5).place(x=220,y=120)
boton5=Button(ventana,text="AC",bd=6,bg="#102E59",fg="white",width=5).place(x=280,y=120)
boton6=Button(ventana,text="4",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(4),width=5).place(x=40,y=160)
boton7=Button(ventana,text="5",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(5),width=5).place(x=100,y=160)
boton8=Button(ventana,text="6",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(6),width=5).place(x=160,y=160)
boton9=Button(ventana,text="x",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("*"),width=5).place(x=220,y=160)
boton10=Button(ventana,text="ANS",bd=6,bg="#102E59",fg="white",width=5).place(x=280,y=160)
boton11=Button(ventana,text="1",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(1),width=5).place(x=40,y=200)
boton12=Button(ventana,text="2",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(2),width=5).place(x=100,y=200)
boton13=Button(ventana,text="3",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(3),width=5).place(x=160,y=200)
boton14=Button(ventana,text="+",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("+"),width=5).place(x=220,y=200)
boton15=Button(ventana,text="pi",bd=6,bg="#102E59",fg="white",width=5).place(x=280,y=200)
boton16=Button(ventana,text="0",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(0),width=5).place(x=40,y=240)
boton17=Button(ventana,text=".",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("."),width=5).place(x=100,y=240)
boton18=Button(ventana,text="e",bd=6,bg="#102E59",fg="white",width=5).place(x=160,y=240)
boton19=Button(ventana,text="-",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("-"),width=5).place(x=220,y=240)
boton20=Button(ventana,text="=",bd=6,bg="#102E59",fg="white",width=5).place(x=280,y=240)














ventana.mainloop()
