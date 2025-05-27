from tkinter import *
from tkinter import ttk, Tk, Frame
from tkinter import font
from ttkthemes import ThemedTk
import math
#import os

#os.chdir("D:\Documentos de Trabajo\Portafolio\Repositorios\Calculadoras")

#-------------- Raiz
raiz = Tk()
#raiz = ThemedTk(theme="arc")  # Usamos ThemedTk en lugar de Tk()
raiz.title("Estimadores Financieros  -  By FIN5")
raiz.geometry("650x330")  # Un poco más grande para mejor espacio
raiz.configure(bg="#cce4e6") 
#icono = "D:\Documentos de Trabajo\Portafolio\Repositorios\Calculadoras\Icono.ico"
#raiz.iconbitmap(icono)
raiz.iconbitmap('Icono.ico')
#------------- Barra Pestañas
color0 = '#ffffff'
color1 = '#020f12'
color2 = '#05D7FF'
color3 = '#65E7FF'
color4 = 'BLACK'


notebook = ttk.Notebook(raiz)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

tab_ahorro = Frame(notebook, bd=2, bg="#ffffff", relief=RIDGE)  # Fondo blanco
tab_rendimiento = Frame(notebook, bd=2, bg="#ffffff", relief=RIDGE)
tab_retiro = Frame(notebook, bd=2, bg="#ffffff", relief=RIDGE)

notebook.add(tab_ahorro, text="Ahorro")
notebook.add(tab_rendimiento, text="Rendimiento")
notebook.add(tab_retiro, text="Retiro")

# ------ Estilo general para widgets (usando ttk)
style = ttk.Style()
style.configure("TNotebook", tabposition='n')
style.configure("TLabel", font=("Roboto", 12), background="#ffffff")  # Fuente moderna
style.configure("TButton", font=("Roboto", 12, "bold"), padding=10, background="#a6e0f1",    foreground="black", relief="raised")
#style.map("TButton",
#    background=[("active", "#0a6dee")],  # Azul neón
#    foreground=[("active", "black")],    # Texto negro para contraste
#    relief=[("active", "sunken")],
#    bordercolor=[("active", "#0077b6")],
#)
#------------------Funciones-------------------------------

#------------------Ahorro----------------------------------
M0_ahorro=StringVar(value="0")
m_ahorro=StringVar(value="0")
t_ahorro=StringVar(value="0")
tasa_ahorro=StringVar(value="0")
Mf_ahorro=StringVar(value="0")

modo_calculo_ahorro = StringVar(value="ninguno")

#------------------Rendimiento----------------------------------
M0_ren=StringVar(value="0")
m_ren=StringVar(value="0")
t_ren=StringVar(value="0")
tasa_ren=StringVar(value="0")
R_ren=StringVar(value="0")

modo_calculo_ren = StringVar(value="ninguno")


#------------------Retiro----------------------------------
gasto_imp = StringVar(value="0")
tiempo_imp = StringVar(value="0")
inflacion_imp = StringVar(value="4")
var_retiro=StringVar(value="0")
retiro_anual=StringVar(value="0")

def bloquear_entradas(seleccionado):
    # Diccionario de entradas y sus variables asociadas
    entradas = {
        "M0": [entry_M0_ahorro, entry_M0_ren],
        "m": [entry_m_ahorro, entry_m_ren],
        "t": [entry_t_ahorro, entry_t_ren],
        "Mf": [entry_Mf_ahorro],
        "R": [entry_R_ren]
    }
    
    # Bloquea todas excepto la seleccionada
    for key, entries in entradas.items():
      for entry in entries:
        if key == seleccionado:
            entry.config(state='readonly', readonlybackground="#A8E8FC", font=("Arial", 15, "bold"))
        else:
            entry.config(state='normal')  
  

def calcular(funcion):

  if funcion == "retiro":
    gasto = float(gasto_imp.get())
    tiempo = float(tiempo_imp.get())
    inflacion = float(inflacion_imp.get())
    retiro_estimado = round(25*(gasto*12)*(1+inflacion/100)**tiempo)
    retiro_year = round(retiro_estimado/25)
    var_retiro.set(f"${retiro_estimado}") 
    retiro_anual.set(f"${retiro_year}")

  
  elif funcion == "ahorro":
    monto_i = float(M0_ahorro.get())
    monto_f = float(Mf_ahorro.get())
    m = float(m_ahorro.get())
    tiempo = float(t_ahorro.get())
    tasa = float(tasa_ahorro.get())
    r = 1+ tasa/100
    r_m = r**(1/12)
    fact_m = (1-r_m**13)/(1-r_m)
    if modo_calculo_ahorro.get() == "Mf":
       monto_f = round(monto_i*(r)**tiempo + m*fact_m*(1-r**tiempo)/(1-r))
       Mf_ahorro.set(f"${monto_f}")
    elif modo_calculo_ahorro.get() == "M0":
       monto_i = round((monto_f - m*fact_m*(1-r**tiempo)/(1-r))/(r)**tiempo)
       M0_ahorro.set(f"${monto_i}")
    elif modo_calculo_ahorro.get() == "m":
       m =  round(((monto_f - monto_i*(r)**tiempo)/fact_m)*((1-r)/(1-r**tiempo)))
       m_ahorro.set(f"${m}")
    elif modo_calculo_ahorro.get() == "t":
      t =  round(math.log(((monto_f - monto_i)*(1-r))/ ( monto_i*(1-r) - m*fact_m) +1, r), 1)
      t_ahorro.set(f"{t}")

  elif funcion == "rendimiento":
    monto_i = float(M0_ren.get())
    rendimiento = float(R_ren.get())
    m = float(m_ren.get())
    tiempo = float(t_ren.get())
    tasa = float(tasa_ren.get())
    r = 1+ tasa/100
    r_m = r**(1/12)
    fact_m = (1-r_m**13)/(1-r_m)
    if modo_calculo_ren.get() == "R":
       rendimiento = round((monto_i - m*fact_m/(1-r))*(r)**tiempo*math.log(r))
       R_ren.set(f"${rendimiento}")
    elif modo_calculo_ren.get() == "M0":
       monto_i = round(rendimiento/(math.log(r)*(r)**tiempo)  + m*fact_m/(1-r))
       M0_ren.set(f"${monto_i}")
    elif modo_calculo_ren.get() == "m":
       m =  round((monto_i- rendimiento/(math.log(r)*(r)**tiempo))*(1-r)/fact_m)
       m_ren.set(f"${m}")
    elif modo_calculo_ren.get() == "t":
      t =  round(math.log(rendimiento,r)  - math.log(math.log(r),r)  - math.log(monto_i-(m*fact_m/(1-r)),r))
      t_ren.set(f"{t}")


def reset(ventana):
    if ventana == "retiro":
      gasto_imp.set("0")
      tiempo_imp.set("0")
      inflacion_imp.set("4")
      var_retiro.set("0")
      retiro_anual.set("0")
    elif ventana == "rendimiento":
      modo_calculo_ren.set("ninguno")
      # Reinicia todas las variables
      M0_ren.set("0")
      m_ren.set("0")
      t_ren.set("0")
      tasa_ren.set("0")
      R_ren.set("0")
    
      # Desbloquea todas las entradas
      entry_M0_ren.config(state='normal', font="normal")
      entry_m_ren.config(state='normal', font="normal")
      entry_t_ren.config(state='normal', font="normal")
      entry_R_ren.config(state='normal', font="normal")

    else:
      #modo_calculo_ahorro.set("ninguno")
      # Reinicia todas las variables
      M0_ahorro.set("0")
      m_ahorro.set("0")
      t_ahorro.set("0")
      tasa_ahorro.set("0")
      Mf_ahorro.set("0")
    
      # Desbloquea todas las entradas
      entry_M0_ahorro.config(state='normal',font="normal")
      entry_m_ahorro.config(state='normal',font="normal")
      entry_t_ahorro.config(state='normal',font="normal")
      entry_Mf_ahorro.config(state='normal',font="normal")


#------------------Interfas-------------------------------

#--------------------Interfas Ahorro-------------------------
tab_ahorro.grid_columnconfigure(1, weight=1)
#-----------------Fila 0----------------------------------
Label(tab_ahorro, text="").grid(row=0, column=0, pady=1)  # Margen superior
#-----------------Fila 1----------------------------------
rboton_M0_ahorro = Radiobutton(tab_ahorro, text="Monto inicial de inversión:", background=color0, font=("Arial", 13, "bold"),
    variable=modo_calculo_ahorro,  # Misma variable para todos
    value="M0",  # Valor único para este botón
    command=lambda: bloquear_entradas("M0"))
entry_M0_ahorro = Entry(tab_ahorro, textvariable=M0_ahorro, width=24, justify="right", font=20)
rboton_M0_ahorro.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_M0_ahorro.grid(row=1, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 2----------------------------------
rboton_m_ahorro = Radiobutton(tab_ahorro, text="Cantidad mensual a invertir:", background=color0, font=("Arial", 13, "bold"),
    variable=modo_calculo_ahorro,  # Misma variable para todos
    value="m",  # Valor único para este botón
    command=lambda: bloquear_entradas("m"))
entry_m_ahorro = Entry(tab_ahorro, textvariable=m_ahorro, width=24, justify="right", font=20)
rboton_m_ahorro.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_m_ahorro.grid(row=2, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 3----------------------------------
rboton_t_ahorro = Radiobutton(tab_ahorro, text="Tiempo de inversión en años:", background=color0, font=("Arial", 13, "bold"),
    variable=modo_calculo_ahorro,  # Misma variable para todos
    value="t",  # Valor único para este botón
    command=lambda: bloquear_entradas("t"))
entry_t_ahorro = Entry(tab_ahorro, textvariable=t_ahorro, background=color0, width=24, justify="right", font=20)
rboton_t_ahorro.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_t_ahorro.grid(row=3, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 4----------------------------------
rboton_tasa_ahorro = Label(tab_ahorro, text="Tasa anual de inversión en %:", background=color0, font=("Arial", 13, "bold"))
entry_tasa_ahorro = Entry(tab_ahorro, textvariable=tasa_ahorro, width=24, justify="right", font=20)
rboton_tasa_ahorro.grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_tasa_ahorro.grid(row=4, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 5----------------------------------
rboton_Mf_ahorro = Radiobutton(tab_ahorro, text="Monto final:", background=color0,  font=("Arial", 13, "bold"),
    variable=modo_calculo_ahorro,  # Misma variable para todos
    value="Mf",  # Valor único para este botón
    command=lambda: bloquear_entradas("Mf"))
entry_Mf_ahorro = Entry(tab_ahorro, textvariable=Mf_ahorro, width=24, justify="right", font=20)
rboton_Mf_ahorro.grid(row=5, column=0, padx=5, pady=5, sticky="e")
entry_Mf_ahorro.grid(row=5, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 6----------------------------------
#boton_reset_ahorro=ttk.Button(tab_ahorro, text="Restaurar",  style="TButton", command=lambda:reset("ahorro"))
#boton_reset_ahorro.grid(row=6, column=0, sticky="nsew", padx=1, pady=1)
#boton_calcular_ahorro=ttk.Button(tab_ahorro, text="Calcular", style="TButton", command=lambda:calcular("ahorro"))
#boton_calcular_ahorro.grid(row=6, column=1, sticky="nsew", padx=1, pady=1)

boton_reset_ahorro=Button(tab_ahorro, text="Restaurar", background=color2, foreground=color4,
                          activebackground=color3, activeforeground=color4, highlightthickness=2, 
                          highlightbackground=color2, highlightcolor='WHITE', cursor= "hand1", font=("Arial", 16, "bold"), command=lambda:reset("ahorro"))
boton_reset_ahorro.grid(row=6, column=0, sticky="nsew", padx=1, pady=1)
boton_calcular_ahorro=Button(tab_ahorro, text="Calcular", background=color2, foreground=color4,
                          activebackground=color3, activeforeground=color4, highlightthickness=2, 
                          highlightbackground=color2, highlightcolor='WHITE', cursor= "hand1", font=("Arial", 16, "bold"), command=lambda:calcular("ahorro"))
boton_calcular_ahorro.grid(row=6, column=1, sticky="nsew", padx=1, pady=1)

#--------------------Interfas Rendimiento-------------------------
tab_rendimiento.grid_columnconfigure(1, weight=1)
#-----------------Fila 0----------------------------------
Label(tab_rendimiento, text="").grid(row=0, column=0, pady=1)  # Margen superior
#-----------------Fila 1----------------------------------
rboton_M0_ren = Radiobutton(tab_rendimiento, text="Monto inicial de inversión:", background=color0, font=("Arial", 13, "bold"),
    variable=modo_calculo_ren,  # Misma variable para todos
    value="M0",  # Valor único para este botón
    command=lambda: bloquear_entradas("M0"))
entry_M0_ren = Entry(tab_rendimiento, textvariable=M0_ren, width=24, justify="right", font=25)
rboton_M0_ren.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_M0_ren.grid(row=1, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 2----------------------------------
rboton_m_ren = Radiobutton(tab_rendimiento, text="Cantidad mensual a invertir:", background=color0, font=("Arial", 13, "bold"),
    variable=modo_calculo_ren,  # Misma variable para todos
    value="m",  # Valor único para este botón
    command=lambda: bloquear_entradas("m"))
entry_m_ren = Entry(tab_rendimiento, textvariable=m_ren, width=24, justify="right", font=20)
rboton_m_ren.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_m_ren.grid(row=2, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 3----------------------------------
rboton_t_ren = Radiobutton(tab_rendimiento, text="Tiempo de inversión en años:", background=color0, font=("Arial", 13, "bold"),
    variable=modo_calculo_ren,  # Misma variable para todos
    value="t",  # Valor único para este botón
    command=lambda: bloquear_entradas("t"))
entry_t_ren = Entry(tab_rendimiento, textvariable=t_ren, width=24, justify="right", font=20)
rboton_t_ren.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_t_ren.grid(row=3, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 4----------------------------------
rboton_tasa_ren = Label(tab_rendimiento, text="Tasa anual de inversión en %:", background=color0, font=("Arial", 13, "bold"))
entry_tasa_ren = Entry(tab_rendimiento, textvariable=tasa_ren, width=24, justify="right", font=20)
rboton_tasa_ren.grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_tasa_ren.grid(row=4, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 5----------------------------------
rboton_R_ren = Radiobutton(tab_rendimiento, text="Rendimiento neto:", background=color0, font=("Arial", 13, "bold"),
    variable=modo_calculo_ren,  # Misma variable para todos
    value="R",  # Valor único para este botón
    command=lambda: bloquear_entradas("R"))
entry_R_ren = Entry(tab_rendimiento, textvariable=R_ren, width=24, justify="right", font=20)
rboton_R_ren.grid(row=5, column=0, padx=5, pady=5, sticky="e")
entry_R_ren.grid(row=5, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 6----------------------------------
boton_reset_ren=Button(tab_rendimiento, text="Restaurar", background=color2, foreground=color4,
                          activebackground=color3, activeforeground=color4, highlightthickness=2, 
                          highlightbackground=color2, highlightcolor='WHITE', cursor= "hand1", font=("Arial", 16, "bold"), command=lambda:reset("rendimiento"))
#ttk.Button(tab_rendimiento, text="Restaurar", style="TButton", command=lambda:reset("rendimiento"))
boton_reset_ren.grid(row=6, column=0, sticky="nsew", padx=1, pady=1)
boton_calcular_ren=Button(tab_rendimiento, text="Calcular", background=color2, foreground=color4,
                          activebackground=color3, activeforeground=color4, highlightthickness=2, 
                          highlightbackground=color2, highlightcolor='WHITE', cursor= "hand1", font=("Arial", 16, "bold"), command=lambda:calcular("rendimiento"))
#ttk.Button(tab_rendimiento, text="Calcular", style="TButton", command=lambda:calcular("rendimiento"))
boton_calcular_ren.grid(row=6, column=1, sticky="nsew", padx=1, pady=1)


#--------------------Interfas Retiro-------------------------
tab_retiro.grid_columnconfigure(1, weight=1)

#-----------------Fila 0----------------------------------
Label(tab_retiro, text="").grid(row=0, column=0, pady=1)  # Margen superior
#-----------------Fila 1----------------------------------
label_gasto = Label(tab_retiro, text="Gasto mensual estimado:", background=color0, font=("Arial", 13, "bold"))
entry_gasto = Entry(tab_retiro, width=24, font= 24, justify="right", textvariable=gasto_imp)
label_gasto.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_gasto.grid(row=1, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 2----------------------------------
label_tretiro = Label(tab_retiro, text="Número de años para tu retiro:", background=color0, font=("Arial", 13, "bold"))
entry_tretiro = Entry(tab_retiro, width=24, font= 24, justify="right", textvariable=tiempo_imp)
label_tretiro.grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_tretiro.grid(row=2, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 3----------------------------------
label_inflacion = Label(tab_retiro, text="Inflación anual promedio:", background=color0, font=("Arial", 13, "bold"))
entry_inflacion = Entry(tab_retiro, width=24, font= 24, justify="right", textvariable=inflacion_imp)
label_inflacion.grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_inflacion.grid(row=3, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 4----------------------------------
Label(tab_retiro, text="___________________________", font=("Arial", 13, "bold")).grid(row=4, column=0, pady=5, sticky="we")  # Margen intermedio
Label(tab_retiro, text="_______________________________________", font=("Arial", 13, "bold")).grid(row=4, column=1, pady=5, sticky="we")  # Margen intermedio
#-----------------Fila 5----------------------------------
boton_reset=Button(tab_retiro, text="Restaurar", background=color2, foreground=color4,
                          activebackground=color3, activeforeground=color4, highlightthickness=2, 
                          highlightbackground=color2, highlightcolor='WHITE', cursor= "hand1", font=("Arial", 16, "bold"), command=lambda:reset("retiro"))
#ttk.Button(tab_retiro, text="Restaurar", style="TButton", command=lambda:reset("retiro"))
boton_reset.grid(row=5, column=0, sticky="nsew", padx=1, pady=1)
boton_calcular_retiro=Button(tab_retiro, text="Calcular", background=color2, foreground=color4,
                          activebackground=color3, activeforeground=color4, highlightthickness=2, 
                          highlightbackground=color2, highlightcolor='WHITE', cursor= "hand1", font=("Arial", 16, "bold"), command=lambda:calcular("retiro"))
#ttk.Button(tab_retiro, text="Calcular", style="TButton", command=lambda:calcular("retiro"))
boton_calcular_retiro.grid(row=5, column=1, sticky="nsew", padx=1, pady=1)
#-----------------Fila 6----------------------------------
label_retiro = Label(tab_retiro, text="Monto requerido para tu retiro:", background=color0, font=("Arial", 13, "bold"))
entry_retiro=Entry(tab_retiro, textvariable=var_retiro, justify="right", font=("Arial", 13, "bold"), state='readonly',readonlybackground="gray85")
label_retiro.grid(row=6, column=0, padx=5, pady=5, sticky="e")
entry_retiro.grid(row=6, column=1, padx=5, pady=5, sticky="we")
#-----------------Fila 7----------------------------------
label_retiro_anual = Label(tab_retiro, text="Retiro anual:", background=color0, font=("Arial", 13, "bold"))
entry_retiro_anual=Entry(tab_retiro, textvariable=retiro_anual, justify="right",  font=("Arial", 13, "bold"), state='readonly',readonlybackground="gray85")
label_retiro_anual.grid(row=7, column=0, padx=5, pady=5, sticky="e")
entry_retiro_anual.grid(row=7, column=1,  padx=5, pady=5, sticky="we")



# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
raiz.mainloop()
