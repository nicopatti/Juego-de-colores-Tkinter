import tkinter as tk
import tkinter.font as tkFont

#hacer funciones para cada color

def corregir_r()->str:
    rojo = caja_roja_entry.get()
    if rojo == 'red':
        r_rojo.set('Fantastic')
        caja_roja_entry.delete(0, tk.END)
    else:
        r_rojo.set('Wrong')

def corregir_v()->str:
    verde = caja_verde_entry.get()
    if verde == 'green':
        r_verde.set('Fantastic')
        caja_verde_entry.delete(0, tk.END)
    else:
        r_verde.set('Wrong')

def corregir_a()->str:
    amarillo = caja_amarillo_entry.get()
    if amarillo == 'yellow':
        r_amarillo.set('Fantastic')
        caja_amarillo_entry.delete(0, tk.END)
    else:
        r_amarillo.set('Wrong')

def corregir_az()->str:
    azul = caja_azul_entry.get()
    if azul == 'blue':
        r_azul.set('Fantastic')
        caja_azul_entry.delete(0, tk.END)
    else:
        r_azul.set('Wrong')


#programa inicial

ventana = tk.Tk()
ventana.title('Colores')
ventana.config(width=500, height=220, bg='sky blue')
ventana.resizable(0,0)
    
#fuentes de letras

fuente = tkFont.Font(family='Arial', size=16, weight='bold', slant='italic')
fuente2 = tkFont.Font(family='Book Antiqua', size=9, weight='normal', slant='roman')

#Titulo

etiqueta = tk.Label(text='Escriba los Colores en Ingles', bg='sky blue',font=fuente)
etiqueta.place(x=100, y=10,)
etiqueta.configure(font= fuente)

#variables

r_rojo = tk.StringVar()
r_rojo.set('')

r_verde = tk.StringVar()
r_verde.set('')

r_amarillo = tk.StringVar()
r_amarillo.set('')

r_azul = tk.StringVar()
r_azul.set('')


#color rojo

caja_roja = tk.Label(bg='red')
caja_roja.place(x=10, y=50, width=50, height=25)

caja_roja_entry = tk.Entry()
caja_roja_entry.place(x=75, y=50, width=80, height=25)

#color verde

caja_verde = tk.Label(bg='green')
caja_verde.place(x=10, y=85, width=50, height=25)

caja_verde_entry = tk.Entry()
caja_verde_entry.place(x=75, y=85, width=80, height=25)

#color amarillo

caja_amarillo = tk.Label(bg='yellow')
caja_amarillo.place(x=10, y=120, width=50, height=25)

caja_amarillo_entry = tk.Entry()
caja_amarillo_entry.place(x=75, y=120, width=80, height=25)

#color azul

caja_azul = tk.Label(bg='blue')
caja_azul.place(x=10, y=155, width=50, height=25)

caja_azul_entry = tk.Entry()
caja_azul_entry.place(x=75, y=155, width=80, height=25)

#Botones

boto_rojo = tk.Button(text='Check', command=corregir_r, font=fuente2)
boto_rojo.place(x=180, y=50, width=80, height=25)

boto_verde = tk.Button(text='Check', command=corregir_v, font=fuente2)
boto_verde.place(x=180, y=85, width=80, height=25)

boto_amarillo = tk.Button(text='Check', command=corregir_a, font=fuente2)
boto_amarillo.place(x=180, y=120, width=80, height=25)

boto_azul = tk.Button(text='Check', command=corregir_az, font=fuente2)
boto_azul.place(x=180, y=155, width=80, height=25)

#etiqueta resultado

resultado_rojo = tk.Label(textvariable=r_rojo, state=tk.DISABLED, bg='sky blue')
resultado_rojo.place(x=265, y=50, width=220, height=25)

resultado_verde = tk.Label(textvariable=r_verde, state=tk.DISABLED, bg='sky blue')
resultado_verde.place(x=265, y=85, width=220, height=25)

resultado_amarillo = tk.Label(textvariable=r_amarillo, state=tk.DISABLED, bg='sky blue')
resultado_amarillo.place(x=265, y=120, width=220, height=25)

resultado_azul = tk.Label(textvariable=r_azul, state=tk.DISABLED, bg='sky blue')
resultado_azul.place(x=265, y=155, width=220, height=25)


ventana.mainloop()