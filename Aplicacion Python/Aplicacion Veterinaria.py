import mysql.connector
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class Animal():
    def __inint__(ani, nombre, edad, raza, color, dni_dueño, fecha, servicio):
        ani.nombre = nombre
        ani.edad = edad
        ani.raza = raza
        ani.color = color
        ani.dni_dueño = dni_dueño
        ani.fecha = fecha
        ani.servicio = servicio
class perro(Animal):
    def __inint__(ani, nombre, edad, raza, color, dni_dueño, fecha, servicio,alimento, especie):
        super().__inint__(nombre, edad, raza, color, dni_dueño, fecha, servicio)
        ani.alimento = 'Croquetas, carne, etc'
        ani.especie = 'Canina'
class gato(Animal):
    def __inint__(ani, nombre, edad, raza, color, dni_dueño, fecha, servicio,alimento, especie):
        super().__inint__(nombre, edad, raza, color, dni_dueño, fecha, servicio)
        ani.alimento = 'Croquetas, atun, etc'
        ani.especie = 'Felina'
class conejo(Animal):
    def __inint__(ani, nombre, edad, raza, color, dni_dueño, fecha, servicio,alimento, especie):
        super().__inint__(nombre, edad, raza, color, dni_dueño, fecha, servicio)
        ani.alimento = 'Hoja de verduras, heno, etc'
        ani.especie = 'Conejo'
class perico(Animal):
    def __inint__(ani, nombre, edad, raza, color, dni_dueño, fecha, servicio,alimento, especie):
        super().__inint__(nombre, edad, raza, color, dni_dueño, fecha, servicio)
        ani.alimento = 'Alpiste, hojas de verduras, etc.'
        ani.especie = 'Ave'
class otro(Animal):
    def __inint__(ani, nombre, edad, raza, color, dni_dueño, fecha, servicio,alimento, especie):
        super().__inint__(nombre, edad, raza, color, dni_dueño, fecha, servicio)
        ani.alimento = alimento
        ani.especie = especie

def perro():
    txt8.delete(0,'end')
    txt9.delete(0,'end')
    txt8.insert(0,str('Croquetas, carne, etc'))
    txt9.insert(0,str('Canina'))
    messagebox.showinfo(title='Mensaje', message='Datos rellenados')
def gato():
    txt8.delete(0,'end')
    txt9.delete(0,'end')
    txt8.insert(0,str('Croquetas, atun, etc'))
    txt9.insert(0,str('Felino'))
    messagebox.showinfo(title='Mensaje', message='Datos rellenados')
def conejo():
    txt8.delete(0,'end')
    txt9.delete(0,'end')
    txt8.insert(0,str('Hoja de verduras, heno, etc'))
    txt9.insert(0,str('Conejo'))
    messagebox.showinfo(title='Mensaje', message='Datos rellenados')
def perico():
    txt8.delete(0,'end')
    txt9.delete(0,'end')
    txt8.insert(0,str('Alpiste, hojas de verduras, etc.'))
    txt9.insert(0,str('Ave'))
    messagebox.showinfo(title='Mensaje', message='Datos rellenados')
def otro():
    txt8.delete(0,'end')
    txt9.delete(0,'end')
    messagebox.showinfo(title='Mensaje', message='No se relleno ningun dato')

def obtenerfila(event):
    rowName = list_elemts.identify_row(event.y)
    item = list_elemts.item(list_elemts.focus())
    a = item['values'][0]
    b = item['values'][1]
    c = item['values'][2]
    d = item['values'][3]
    e = item['values'][4]
    f = item['values'][5]
    g = item['values'][6]
    h = item['values'][7]
    i = item['values'][8]
    j = item['values'][9]  
    txt0.delete(0,'end')
    txt0.insert(0,str(a))
    txt1.delete(0,'end')
    txt1.insert(0,str(b))
    txt2.delete(0,'end')
    txt2.insert(0,str(c))
    txt3.delete(0,'end')
    txt3.insert(0,str(d))
    txt4.delete(0,'end')
    txt4.insert(0,str(e))
    txt5.delete(0,'end')
    txt5.insert(0,str(f))
    txt6.delete(0,'end')
    txt6.insert(0,str(g))
    txt7.delete(0,'end')
    txt7.insert(0,str(h))
    txt8.delete(0,'end')
    txt8.insert(0,str(i))
    txt9.delete(0,'end')
    txt9.insert(0,str(j))
def limpiar():
    txt0.delete(0,'end')
    txt1.delete(0,'end')
    txt2.delete(0,'end')
    txt3.delete(0,'end')
    txt4.delete(0,'end')
    txt5.delete(0,'end')
    txt6.delete(0,'end')
    txt7.delete(0,'end')
    txt8.delete(0,'end')
    txt9.delete(0,'end')
def listar():
    list_elemts.delete(*list_elemts.get_children())
    conn=mysql.connector.connect(user='root', password='',host='localhost',database='VETERINARIABD')
    cursor = conn.cursor()
    sql = 'select * from pacientes'
    cursor.execute(sql)
    list_elemts.bind('<Double 1>', obtenerfila)
    list_elemts.heading(1,text='ID Paciente', anchor=CENTER)
    list_elemts.heading(2,text='Nombre', anchor=CENTER)
    list_elemts.heading(3,text='Edad', anchor=CENTER)
    list_elemts.heading(4,text='Raza', anchor=CENTER)
    list_elemts.heading(5,text='Color', anchor=CENTER)
    list_elemts.heading(6,text='DNI Dueño', anchor=CENTER)
    list_elemts.heading(7,text='Fecha', anchor=CENTER)
    list_elemts.heading(8,text='Servicio', anchor=CENTER)
    list_elemts.heading(9,text='Alimento', anchor=CENTER)
    list_elemts.heading(10,text='Especie', anchor=CENTER)
    
    list_elemts.column(1,width = 75, anchor=CENTER)
    list_elemts.column(2,width = 75, anchor=CENTER)
    list_elemts.column(3,width = 75, anchor=CENTER)
    list_elemts.column(4,width = 75, anchor=CENTER)
    list_elemts.column(5,width = 75, anchor=CENTER)
    list_elemts.column(6,width = 75, anchor=CENTER)
    list_elemts.column(7,width = 75, anchor=CENTER)
    list_elemts.column(8,width = 165, anchor=CENTER)
    list_elemts.column(9,width = 165, anchor=CENTER)
    list_elemts.column(10,width = 75, anchor=CENTER)
    rows = cursor.fetchall()
    for i in rows:
        list_elemts.insert('','end',values=i)
    list_elemts.place(x = 35, y = 440)
    limpiar()
def guardar():
    conn=mysql.connector.connect(user='root', password='',host='localhost',database='VETERINARIABD')
    cursor = conn.cursor()
    sql= "insert into pacientes(Nombre,Edad,Raza,Color,DNI_Dueño,Fecha,Servicio,Alimento,Especie) values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(txt1.get(),txt2.get(),txt3.get(),txt4.get(),txt5.get(),
                                                                                                                                                               txt6.get(),txt7.get(),txt8.get(),txt9.get())
    cursor.execute(sql)
    conn.commit()
    messagebox.showinfo(title='Mensaje', message='Datos Guardados')
    limpiar()
def modificar():
    conn = mysql.connector.connect(user='root', password='',host='localhost',database='VETERINARIABD')
    cursor = conn.cursor()
    sql= "update pacientes set nombre = '{}',edad = '{}',raza = '{}',color = '{}',dni_dueño = '{}',fecha = '{}',servicio = '{}',alimento = '{}',especie = '{}' where id_paciente = '{}'".format(txt1.get(),txt2.get(),txt3.get(),txt4.get(),txt5.get(),txt6.get(),txt7.get(),txt8.get(),txt9.get(),txt0.get())
    cursor.execute(sql)
    conn.commit()
    messagebox.showinfo(title='Mensaje', message='Datos Modificados')
    limpiar()
def borrar():
    conn = mysql.connector.connect(user='root', password='',host='localhost',database='VETERINARIABD')
    cursor = conn.cursor()
    sql= "delete from pacientes where id_paciente='{}'".format(txt0.get())
    cursor.execute(sql)
    conn.commit()
    messagebox.showinfo(title='Mensaje', message='Datos Borrados')
    limpiar()
    
frame = tkinter.Tk()
frame.title('Safari SAC')
frame.geometry('1000x600')
list_elemts = ttk.Treeview(frame, columns=(1,2,3,4,5,6,7,8,9,10), show='headings')
label=tkinter.Label(frame, text = 'Registro de pacientes', font=("Arial", 17))
l0=tkinter.Label(frame, text = 'ID Paciente (No llenar / modificar)')
txt0 = tkinter.Entry(frame, width=50)
l1=tkinter.Label(frame, text = 'Nombre')
txt1 = tkinter.Entry(frame, width=50)
l2=tkinter.Label(frame, text = 'Edad')
txt2 = tkinter.Entry(frame, width=50)
l3=tkinter.Label(frame, text = 'Raza')
txt3 = tkinter.Entry(frame, width=50)
l4=tkinter.Label(frame, text = 'Color')
txt4 = tkinter.Entry(frame, width=50)
l5=tkinter.Label(frame, text = 'DNI del dueño')
txt5 = tkinter.Entry(frame, width=50)
l6=tkinter.Label(frame, text = 'Fecha')
txt6 = tkinter.Entry(frame, width=50)
l7=tkinter.Label(frame, text = 'Servicio')
txt7 = tkinter.Entry(frame, width=50)
btn1=tkinter.Button(frame,text='Perro',command=perro)
btn2=tkinter.Button(frame,text='Gato',command=gato)
btn3=tkinter.Button(frame,text='Conejo',command=conejo)
btn4=tkinter.Button(frame,text='Perico',command=perico)
btn5=tkinter.Button(frame,text='Otros',command=otro)
l8=tkinter.Label(frame, text = 'Alimento')
txt8 = tkinter.Entry(frame, width=50)
l9=tkinter.Label(frame, text = 'Especie')
txt9 = tkinter.Entry(frame, width=50)

btnlistar=tkinter.Button(frame,text='Listar',command=listar)
btnguardar=tkinter.Button(frame,text='Guardar',command=guardar)
btnmodificar=tkinter.Button(frame,text='Modificar',command=modificar)
btnborrar=tkinter.Button(frame,text='Borrar', command=borrar)


label.pack()
l0.place(x = 200, y = 40)
txt0.place(x = 400, y = 40)
l1.place(x = 200, y = 70)
txt1.place(x = 400, y = 70)
l2.place(x = 200, y = 100)
txt2.place(x = 400, y = 100)
l3.place(x = 200, y = 130)
txt3.place(x = 400, y = 130)
l4.place(x = 200, y = 160)
txt4.place(x = 400, y = 160)
l5.place(x = 200, y = 190)
txt5.place(x = 400, y = 190)
l6.place(x = 200, y = 220)
txt6.place(x = 400, y = 220)
l7.place(x = 200, y = 250)
txt7.place(x = 400, y = 250)
btn1.place(x = 250, y = 280,width=90, height=30)
btn2.place(x = 350, y = 280,width=90, height=30)
btn3.place(x = 450, y = 280,width=90, height=30)
btn4.place(x = 550, y = 280,width=90, height=30)
btn5.place(x = 650, y = 280,width=90, height=30)
l8.place(x = 200, y = 320)
txt8.place(x = 400, y = 320)
l9.place(x = 200, y = 350)
txt9.place(x = 400, y = 350)

btnlistar.place(x = 290, y = 390,width=90, height=30)
btnguardar.place(x = 390, y = 390,width=90, height=30)
btnmodificar.place(x = 490, y = 390,width=90, height=30)
btnborrar.place(x = 590, y = 390,width=90, height=30)


    
frame.mainloop()



