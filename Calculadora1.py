from tkinter import *
from tkinter import font

raiz=Tk()

raiz.title("Calculadora")
raiz.geometry("400x500")
miFrame=Frame(raiz)

miFrame.pack(fill="both", expand=True)

# Configuración de grid para que sea expansible
miFrame.grid_rowconfigure(0, weight=1)  # Fila 0 (para posibles elementos superiores)
miFrame.grid_rowconfigure(7, weight=1)  # Fila 7 (para posibles elementos inferiores)
miFrame.grid_columnconfigure(0, weight=1)  # Columna 0 (lado izquierdo)
miFrame.grid_columnconfigure(5, weight=1)  # Columna 5 (lado derecho)

operacion = ""
op_guardada = ""
resultado = 0


#-------------------------------------------------
#----------------------pantalla-------------------

numeroPantalla=StringVar()
pantalla_font = font.Font(size=24)

pantalla=Entry(miFrame,  textvariable=numeroPantalla,width=20, font= pantalla_font)
pantalla.grid(row=1, column=1, padx=10, pady=2, columnspan=4, rowspan=1, sticky="nsew")
pantalla.config(background="black", fg="#03f943", justify="right", borderwidth=0)

def ajustar_fuente_pantalla(event):
    nuevo_tamano = max(
        min(event.width // 20, 28),  # Máx 36px basado en ancho
        min(event.height // 3, 36)    # Máx 48px basado en alto
    )
    pantalla_font.configure(size=nuevo_tamano)

pantalla.bind('<Configure>', ajustar_fuente_pantalla)

numeroPantalla.set("0")

#------------------------------------------------------------
#--------------------------funciones pantalla-----------------

def numeroPulsado(num):

	global operacion


	if operacion != "":
		numeroPantalla.set(num)
		operacion = ""

	else:

		if numeroPantalla.get() == "0" and num == "0":
			numeroPantalla.set("0")
	
		elif numeroPantalla.get() == "0" and num != ".":
			numeroPantalla.set(num)

		elif "." in numeroPantalla.get() and num == ".":
			numeroPantalla.set(numeroPantalla.get())

		else:

			numeroPantalla.set(numeroPantalla.get() + num)
									# "get" recupera la informacion que ya estaba ahi 


def clearB():

	global operacion
	global op_guardada
	global num 
	global num1 
	global resultado

	numeroPantalla.set("0")
	operacion=""
	op_guardada=""
	num=""
	num1=0
	resultado=0 


#-------------------------- operaciones ---------------------

#--------------------------- suma ----------------------------------

def suma():
	global operacion
	global op_guardada
	global resultado

	operacion = "suma"
	resultadoparcial()
	op_guardada = "suma"
	
	
#	num1 = float(numeroPantalla.get())
#	resultado += num1
#	numeroPantalla.set(resultado)


#--------------------------- resta ----------------------------------

def resta():
	global operacion
	global op_guardada
#	global resultado

	operacion = "resta"
	resultadoparcial()
	op_guardada = "resta"

#--------------------------- multiplicacion ----------------------------------

def multiplicacion():
	global operacion
	global op_guardada
	global resultado

	operacion = "multiplicacion"
	resultadoparcial()
	op_guardada = "multiplicacion"


#--------------------------- division ----------------------------------

def division():
	global operacion
	global op_guardada
	global resultado

	operacion = "division"
	resultadoparcial()
	op_guardada = "division"

#--------------------------- factorial ----------------------------------

def factorial():
	global operacion
	global op_guardada
	global resultado

	resultadoparcial()

	if numeroPantalla.get() == "0":
		numeroPantalla.set(1)

	elif "." not in numeroPantalla.get():
		resultado = 1
		n= int(numeroPantalla.get())
		for i in range(1,n+1):
			resultado *= i
		numeroPantalla.set(resultado)

	else:
		numeroPantalla.set(numeroPantalla.get())

#--------------------------- inverso ----------------------------------

def inverso():
	global operacion
	global op_guardada
	global resultado

	resultadoparcial()

	if numeroPantalla.get() == "0":
		numeroPantalla.set("Error")

	else:
		x= float(numeroPantalla.get())
		resultado = 1/x
		numeroPantalla.set(resultado)

#--------------------------- exponente ----------------------------------

def exponente():
	global operacion
	global op_guardada
	global resultado

	
	if op_guardada == "exponente":
		elresultado()

	else:
		operacion = "exponente"
		resultadoparcial()
		op_guardada = "exponente"
	

#--------------------------- resultado parcial ----------------------------------

def resultadoparcial():
#	global op_guardada
	global resultado

#	num1 = float(numeroPantalla.get())
#	resultado += num1
#	numeroPantalla.set(resultado)

	if op_guardada == "":
		resultado = float(numeroPantalla.get())


	elif op_guardada == "suma":
		num1 = float(numeroPantalla.get())
		resultado += num1
		numeroPantalla.set(resultado)

	elif op_guardada == "resta":
		num1 = float(numeroPantalla.get())
		resultado -= num1
		numeroPantalla.set(resultado)

	elif op_guardada == "multiplicacion":
		num1 = float(numeroPantalla.get())
		resultado *= num1
		numeroPantalla.set(resultado)

	elif op_guardada == "division":
		num1 = float(numeroPantalla.get())
		resultado /= num1
		numeroPantalla.set(resultado)

	elif op_guardada == "exponente":
		num1 = float(numeroPantalla.get())
		resultado = resultado ** num1
		numeroPantalla.set(resultado)

#--------------------------- resultado ----------------------------------

def elresultado():
	global op_guardada
	global resultado
	global operacion

#	num1 = float(numeroPantalla.get())
#	resultado += num1
#	numeroPantalla.set(resultado)

	if op_guardada == "":
		resultado = float(numeroPantalla.get())


	elif op_guardada == "suma":
		num1 = float(numeroPantalla.get())
		resultado += num1
		numeroPantalla.set(resultado)

	elif op_guardada == "resta":
		num1 = float(numeroPantalla.get())
		resultado -= num1
		numeroPantalla.set(resultado)

	elif op_guardada == "multiplicacion":
		num1 = float(numeroPantalla.get())
		resultado *= num1
		numeroPantalla.set(resultado)

	elif op_guardada == "division":
		num1 = float(numeroPantalla.get())
		resultado /= num1
		numeroPantalla.set(resultado)

	elif op_guardada == "exponente":
		num1 = float(numeroPantalla.get())
		resultado = resultado ** num1
		numeroPantalla.set(resultado)


#	else:
#		numeroPantalla.set(resultado)

	operacion=""
	op_guardada=""
	num=""
	num1=0


#---------------------Interfas-------------------------
# Columnas
miFrame.grid_columnconfigure(0, weight=1)  # Margen izquierdo
miFrame.grid_columnconfigure(1, weight=1, uniform="btn_col")
miFrame.grid_columnconfigure(2, weight=1, uniform="btn_col")
miFrame.grid_columnconfigure(3, weight=1, uniform="btn_col")
miFrame.grid_columnconfigure(4, weight=1, uniform="btn_col")
miFrame.grid_columnconfigure(5, weight=1)  # Margen derecho

# Filas
miFrame.grid_rowconfigure(1, weight=1)  # Fila pantalla
for row in range(2, 7):  # Filas de botones
    miFrame.grid_rowconfigure(row, weight=1, uniform="btn_row")

#---------------------fila 0-----------------

botonFactorial=Button(miFrame, text="n!", font=("Arial", 14, "bold"), command=lambda:factorial())
botonFactorial.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)
botonExponente=Button(miFrame, text="x^y", font=("Arial", 14, "bold"), command=lambda:exponente())
botonExponente.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)
botoninverso=Button(miFrame, text="1/x",font=("Arial", 14, "bold"), command=lambda:inverso())
botoninverso.grid(row=2, column=3, sticky="nsew", padx=1, pady=1)
botonDiv=Button(miFrame, text="/", font=("Arial", 14, "bold"), command=lambda:division())
botonDiv.grid(row=2, column=4, sticky="nsew", padx=1, pady=1)

#----------------------------------------------
#---------------------fila 1-----------------

boton7=Button(miFrame, text="7", font=("Arial", 14, "bold"), command=lambda:numeroPulsado("7"))
boton7.grid(row=3, column=1, sticky="nsew", padx=1, pady=1)
boton8=Button(miFrame, text="8", font=("Arial", 14, "bold"), command=lambda:numeroPulsado("8"))
boton8.grid(row=3, column=2, sticky="nsew", padx=1, pady=1)
boton9=Button(miFrame, text="9", font=("Arial", 14, "bold"), command=lambda:numeroPulsado("9"))
boton9.grid(row=3, column=3, sticky="nsew", padx=1, pady=1)
botonMult=Button(miFrame, text="x", font=("Arial", 14, "bold"), command=lambda:multiplicacion())
botonMult.grid(row=3, column=4, sticky="nsew", padx=1, pady=1)


#---------------------------------------------
#---------------------fila 2-----------------


												# "lambda:" sirve para no llamar a la funcion automaticamente, esta queda en espera a la llamada del boton
boton4=Button(miFrame, text="4", font=("Arial", 14, "bold"), command=lambda:numeroPulsado("4"))
boton4.grid(row=4, column=1, sticky="nsew", padx=1, pady=1)
boton5=Button(miFrame, text="5", font=("Arial", 14, "bold"), command=lambda:numeroPulsado("5"))
boton5.grid(row=4, column=2, sticky="nsew", padx=1, pady=1)
boton6=Button(miFrame, text="6", font=("Arial", 14, "bold"), command=lambda:numeroPulsado("6"))
boton6.grid(row=4, column=3, sticky="nsew", padx=1, pady=1)
botonRest=Button(miFrame, text="-", font=("Arial", 18, "bold"), command=lambda:resta())
botonRest.grid(row=4, column=4, sticky="nsew", padx=1, pady=1)


#---------------------------------------------
#---------------------fila 3-----------------


boton1=Button(miFrame, text="1", font=("Arial", 14, "bold"), command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1, sticky="nsew", padx=1, pady=1)
boton2=Button(miFrame, text="2", font=("Arial", 14, "bold"), command=lambda:numeroPulsado("2"))
boton2.grid(row=5, column=2, sticky="nsew", padx=1, pady=1)
boton3=Button(miFrame, text="3", font=("Arial", 14, "bold"), command=lambda:numeroPulsado("3"))
boton3.grid(row=5, column=3, sticky="nsew", padx=1, pady=1)
botonSum=Button(miFrame, text="+", font=("Arial", 14, "bold"), command=lambda:suma())
botonSum.grid(row=5, column=4, sticky="nsew", padx=1, pady=1)


#-----------------------------------------------
#---------------------fila 4-----------------


botonClear=Button(miFrame, text="C", font=("Arial", 14, "bold"), command=lambda:clearB())
botonClear.grid(row=6, column=1, sticky="nsew", padx=1, pady=1)
boton0=Button(miFrame, text="0", font=("Arial", 14, "bold"), command=lambda:numeroPulsado("0"))
boton0.grid(row=6, column=2, sticky="nsew", padx=1, pady=1)
botonpunto=Button(miFrame, text=".", font=("Arial", 14, "bold"), command=lambda:numeroPulsado("."))
botonpunto.grid(row=6, column=3, sticky="nsew", padx=1, pady=1)
botonIgual=Button(miFrame, text="=", font=("Arial", 14, "bold"), command=lambda:elresultado())
botonIgual.grid(row=6, column=4, sticky="nsew", padx=1, pady=1)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
raiz.mainloop()
