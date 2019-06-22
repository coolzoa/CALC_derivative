#modulos importados
import sympy
from sympy import*
import Tkinter
from Tkinter import*
import tkMessageBox

#defino variables para que sympy puede reconocerlas
x,c,b,y,sqrt = symbols('x c b y sqrt')

#funcion que calcula derivada de funcion
#entradas: una funcion
#salidas: la derivada de la funcion
def derivada(funcion,termino):
    return diff(funcion,termino)

#funcion que evalua valor en una funcion
#entradas, la funcion y el valor a evaluar
#salidas: la funcion evaluada en el valor
def evaluar(funcion,termino,valor):
    funcion = str(funcion)
    return eval(funcion).subs(termino,valor)

#funcion que determina c usando teorema de valor medio
#entradas: la funcion y el rango
#salida, los valores de c que cumple el teorema
def valormedio(funcion,minimo,maximo):
    f1 = evaluar(funcion,x,maximo)
    f2 = evaluar(funcion,x,minimo)
    f = (f1-f2)/(maximo - minimo)
    derivadac = derivada(evaluar(funcion,x,c),c)
    ecuacion = Eq(f,derivadac)
    temp = solve(ecuacion)
    soluciones = list()
    for i in temp:
        num = (sympify(i))
        num = (num).evalf(3)
        
        if num >= minimo and num <= maximo:
            soluciones.append(num)
    return soluciones


#funcion que calcula la recta tangente y secante
#Entradas ninguna
#salidas las 3 rectas y la funcion de graficar
def rectas():
    #tangente
    funcion = fu.get()
    minimo = sympify(a.get())
    maximo = sympify(b.get())
    soluciones = valormedio(funcion,minimo,maximo)
    if len(soluciones) == 0:
        tkMessageBox.showerror(None,'No existen valores de c')
        return
    lbv.config(text='c: '+str(soluciones))
    if len(soluciones) > 1:
        x0 = sympify(soluciones[0])
        x1 = sympify(soluciones[1])
        y0 = sympify(evaluar(funcion,x,x0))
        y1 = sympify(evaluar(funcion,x,x1))
        pendiente = sympify((y1-y0)/(x1-x0))        
    else:
        x0 = sympify(soluciones[0])
        y0 = sympify(evaluar(funcion,x,x0))
        pendiente = sympify(derivada(funcion,x))
        pendiente = sympify(evaluar(pendiente,x,x0))
    ejey = (y0-pendiente*x0)
    ecuaciont = str(pendiente) + '*' + 'x' + '+' + str(ejey)
    ecuaciont = sympify(ecuaciont)
    lbta.config(text=str(ecuaciont))
    rectatangente = sympy.plot(ecuaciont,(x,minimo,maximo),show=False,line_color='blue')

    #secante
    x2 = sympify(minimo)
    y2 = sympify(evaluar(funcion,x,x2))
    x3 = sympify(maximo)
    y3 = sympify(evaluar(funcion,x,x3))
    pendiente = sympify((y3-y2)/(x3-x2))
    ejey2 = (y3 - pendiente*x3)
    ecuacions = str(pendiente) + '*' + 'x' + '+' + str(ejey2)
    ecuacions = sympify(ecuacions)
    lbse.config(text=str(ecuacions))
    rectasecante = sympy.plot(ecuacions,(x,minimo,maximo),show=False,line_color='green')

    #funcion
    func = sympy.plot(funcion,(x,minimo,maximo),show=False,line_color='black')

    #decidir cuales se muestran
    if rs.get() == 0 and rt.get() == 0 and rf.get() == 0:
        tkMessageBox.showerror(None,'Debe elegir al menos una de las opciones')
        return
    elif rs.get() == 0 and rt.get() == 0 and rf.get() == 1:
        sympy.plotting.plot(funcion,(x,minimo,maximo))
        return
    elif rs.get() == 0 and rt.get() == 1 and rf.get() == 0:
        sympy.plotting.plot(rectatangente,(x,minimo,maximo))
        return
    elif rs.get() == 0 and rt.get() == 1 and rf.get() ==1:
        func.extend(rectatangente)
        func.show()
        return
    elif rs.get() == 1 and rt.get() == 0 and rf.get() == 0:
        sympy.plotting.plot(rectasecante,(x,minimo,maximo))
        return
    elif rs.get() == 1 and rt.get() == 0 and rf.get() == 1:
        func.extend(rectasecante)
        func.show()
        return
    elif rs.get() == 1 and rt.get() == 1 and rf.get() == 0:
        rectasecante.extend(rectatangente)
        rectasecante.show()
        return
    elif rs.get() == 1 and rt.get() == 1 and rf.get() == 1:
        func.extend(rectatangente)
        func.extend(rectasecante)
        func.show()
        return



    
#GUI

root = Tkinter.Tk()
fu = StringVar() #funcion
a = StringVar() #valor minimo de rango
b = StringVar()# valor maximo de rango
rs = IntVar()# y/n recta secante
rt = IntVar()#y/n recta tangente
rf = IntVar() #y/n funcion

root.geometry('800x500')
root.title('Tarea Derivadas')
lb = Label(root,text='Ingrese los datos solicitados').grid(row=0,column=0)
lbfu = Label(root,text='f(x) =').grid(row=1,column=0)
lba = Label(root,text='Ingrese el valor minimo del rango: ').grid(row=2,column=0)
lbb = Label(root,text='Ingrese el valor maximo del rango: ').grid(row=3,column=0)
ef = Entry(root,textvariable=fu).grid(row=1,column=1)
ea = Entry(root,textvariable=a).grid(row=2,column=1)
eb = Entry(root,textvariable=b).grid(row=3,column=1)
boton = Button(root,text='Graficar',command=rectas)
cs = Checkbutton(root,text='Mostrar recta secante',variable=rs).grid(row=1,column=2)
ct = Checkbutton(root,text='Mostrar recta tangente',variable=rt).grid(row=2,column=2)
cf = Checkbutton(root,text='Mostrar funcion',variable=rf).grid(row=3,column=2)
lbs = Label(root,text='Valores c que cumplen valor medio:').grid(row=0,column=4)
lbv = Label(root)
lbv.grid(row=1,column=4)
lbt = Label(root,text='Ecuacion de recta tangente:').grid(row=2,column=4)
lbta = Label(root)
lbta.grid(row=3,column=4)
lbs = Label(root,text='Ecuacion de recta secante:').grid(row=4,column=4)
lbse = Label(root)
lbse.grid(row=5,column=4)
boton.grid(row=4,column=0)
root.mainloop()


