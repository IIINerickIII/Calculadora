from tkinter import *
from math import pi, e

def almacenar(x):
    global operador
    operador=operador+str(x)
    otrav.set(operador)
    return otrav
def limpiar():
    global operador
    operador=""
    otrav.set(operador)
    return otrav
def resultado():
    global operador
    total = str(eval(operador))
    otrav.set(total)
    if len(operador)>=4:
        tri=operador[0]+operador[1]+operador[2]+operador[3]
        if tri=='sin(' or tri=='cos(' or tri=='tan(':
            a=""
            for x in range(4,len(operador)):
                if operador[x] in '0123456789': 
                    a=a+operador[x]       
            a=tri+a+"*pi/180)"
            total = str(eval(a))
            total=str(round(float(total),2))
            otrav.set(total)
            operador = ""
    operador = ""
    return otrav

ventana=Tk()
ventana.title("CALCULADORA")
ventana.geometry("400x400")
ventana.configure(background="black")
operador=""
otrav=StringVar()
messagebox.showinfo("CALCULADORA","BIENBENIDOS A NUESTRA CALCULADORA")
etiqueta=Label(ventana,text="CASIO Bamba",bd=5,bg="#691B1B",fg="white").pack()
caja=Entry(ventana,font=('arial',20,'bold'),bd=30,bg="powder blue",width=20,justify='right').place(x=20,y=20)
boton1=Button(ventana,text="7",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(7),width=5).place(x=40,y=120)
boton2=Button(ventana,text="8",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(8),width=5).place(x=100,y=120)
boton3=Button(ventana,text="9",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(9),width=5).place(x=160,y=120)
boton4=Button(ventana,text="/",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("/"),width=5).place(x=220,y=120)
boton5=Button(ventana,text="AC",bd=6,bg="#102E59",fg="white",command=limpiar,width=5).place(x=280,y=120)
boton6=Button(ventana,text="4",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(4),width=5).place(x=40,y=160)
boton7=Button(ventana,text="5",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(5),width=5).place(x=100,y=160)
boton8=Button(ventana,text="6",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(6),width=5).place(x=160,y=160)
boton9=Button(ventana,text="x",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("*"),width=5).place(x=220,y=160)
boton10=Button(ventana,text="ANS",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(operador),width=5).place(x=280,y=160)
boton11=Button(ventana,text="1",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(1),width=5).place(x=40,y=200)
boton12=Button(ventana,text="2",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(2),width=5).place(x=100,y=200)
boton13=Button(ventana,text="3",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(3),width=5).place(x=160,y=200)
boton14=Button(ventana,text="+",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("+"),width=5).place(x=220,y=200)
boton15=Button(ventana,text="pi",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(str(pi)),width=5).place(x=280,y=200)
boton16=Button(ventana,text="0",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(0),width=5).place(x=40,y=240)
boton17=Button(ventana,text=".",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("."),width=5).place(x=100,y=240)
boton18=Button(ventana,text="e",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(str(e)),width=5).place(x=160,y=240)
boton19=Button(ventana,text="-",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("-"),width=5).place(x=220,y=240)
boton20=Button(ventana,text="=",bd=6,bg="#102E59",fg="white",command=resultado,width=5).place(x=280,y=240)
boton21=Button(ventana,text="sen",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("sin("),width=10).place(x=40,y=300)
boton22=Button(ventana,text="cos",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("cos("),width=10).place(x=140,y=300)
boton23=Button(ventana,text="tan",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("tan("),width=10).place(x=240,y=300)
boton24=Button(ventana,text="log",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("log10("),width=10).place(x=40,y=340)
boton25=Button(ventana,text="ln",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("log("),width=10).place(x=140,y=340)
boton26=Button(ventana,text="(",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("("),width=3).place(x=240,y=340)
boton27=Button(ventana,text=")",bd=6,bg="#102E59",fg="white",command=lambda:almacenar(")"),width=3).place(x=290,y=340)
boton28=Button(ventana,text="fact !",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("factorial("),width=10).place(x=40,y=380)
boton29=Button(ventana,text="abs | |",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("abs("),width=10).place(x=140,y=380)
boton30=Button(ventana,text="exp e^x",bd=6,bg="#102E59",fg="white",command=lambda:almacenar("exp("),width=10).place(x=240,y=380)
boton31=Button(ventana,text="SALIR",bd=6,bg="#102E59",fg="white",command=ventana.quit,width=10).place(x=150,y=460)

ventana.mainloop()
