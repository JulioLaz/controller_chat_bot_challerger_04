import tkinter as tk
from time import sleep
import os
from PIL import ImageGrab
import pyautogui as pt

#Ajuste del Pixel
pct_x = pt.size()[0]/ImageGrab.grab().size[0]
pct_y = pt.size()[1]/ImageGrab.grab().size[1]

os.system("start WhatsApp:")

#Enviar Respuesta
def enviar_respuesta():
	os.system("start WhatsApp:")
	posicion = pt.locateCenterOnScreen('imagenes/clip.png', grayscale=False, confidence=.9)
	if posicion is not None:
		x = int(posicion[0])*pct_x
		y = int(posicion[1])*pct_y
		pt.moveTo(x + 100, y, duration=.5)
		pt.click()
		pt.hotkey('ctrl', 'v')
		pt.typewrite("\n", interval=.01)
		sleep(1)

#Decidir que responder
def buscar_respuesta():

		# pegar texto
	posicion = pt.locateCenterOnScreen('imagenes/pegar_pregunta.png', grayscale=False, confidence=.9)
	if posicion is not None:
		x = (int(posicion[0])*pct_x)+50
		y = int(posicion[1])*pct_y
		pt.moveTo(x,y, duration=.05)
		sleep(1)
		pt.click()
		pt.hotkey("ctrl", "v")
		pt.press("enter")
		# pt.write(". utiliza como max 100 palabras")
		sleep(12)

		# copy respuesta: 
	posicion = pt.locateCenterOnScreen('imagenes/copy_tilde.png', grayscale=False, confidence=.9)
	if posicion is not None:
		x = int(posicion[0])*pct_x
		y = int(posicion[1])*pct_y
		pt.moveTo(x,y, duration=.05)
		sleep(1)
		pt.click()
		pt.click()
		pt.click()
		pt.hotkey("ctrl", "c")
		print("copy")
		sleep(1)
	enviar_respuesta()
	sleep(1)
		
#Capturar una foto del mensaje
def extraer_mensaje():

	posicion = pt.locateCenterOnScreen('imagenes/nuevo.png', grayscale=False, confidence=.9)
	if posicion is not None:
		x = int(posicion[0])*pct_x
		y = int(posicion[1])*pct_y
		pt.moveTo(x,y, duration=.05)
		pt.click()
		sleep(1)

	posicion = pt.locateCenterOnScreen('imagenes/clip.png', grayscale=False, confidence=.9)
	if posicion is not None:
		x = int(posicion[0])*pct_x
		y = int(posicion[1])*pct_y
		pt.moveTo(x,y, duration=.05)
		sleep(1)
		pt.moveTo(x*0.925+30, y*0.92, duration = .05)	
		pt.click()
		pt.click()
		pt.click()
		sleep(1)
		pt.hotkey('ctrl', 'c')
		sleep(1)
		buscar_respuesta()
		sleep(1)
		# enviar_respuesta()
		# sleep(1)

#Buscar nuevos mensajes
def buscar_nuevo_mensaje():

	posicion = pt.locateCenterOnScreen('imagenes/circulo.png', grayscale=False, confidence=.9)
	posicion_02 = pt.locateCenterOnScreen('imagenes/circulo_02.png', grayscale=False, confidence=.9)
	posicion_lupa = pt.locateCenterOnScreen('imagenes/lupa.png', grayscale=False, confidence=.9)
	if posicion is not None  and posicion_lupa is not None:
		x = int(posicion[0])*pct_x
		y = int(posicion[1])*pct_y
		pt.moveTo(x,y, duration=.05)
		# sleep(1)
		pt.click()
		sleep(1)
		extraer_mensaje()
	elif posicion_02 is not None  and posicion_lupa is not None:
		x = int(posicion_02[0])*pct_x
		y = int(posicion_02[1])*pct_y
		pt.moveTo(x,y, duration=.05)
		sleep(1)
		pt.click()
		sleep(1)
		extraer_mensaje()
	else:
		sleep(1)
		posicion = pt.locateCenterOnScreen('imagenes/inicio.png', grayscale=False, confidence=.9)
		if posicion is not None:
			x = int(posicion[0])*pct_x
			y = int(posicion[1])*pct_y
			pt.moveTo(x-50,y, duration=.05)
			pt.click()
		print('No hay nuevos mensajes')

ejecutar_proceso = False

def iniciar_proceso():
    global ejecutar_proceso
    ejecutar_proceso = True
    btn_iniciar.pack_forget()
    btn_detener.pack(side="top", pady=40)
    ventana.iconify()
    ejecutar_busqueda()

def detener_proceso():
    global ejecutar_proceso
    ejecutar_proceso = False
    btn_detener.pack_forget()
    btn_iniciar.pack(side="top", pady=40)

def ejecutar_busqueda():
    if ejecutar_proceso:
        buscar_nuevo_mensaje()
        ventana.after(5000, ejecutar_busqueda)

ventana = tk.Tk()
ventana.title("WhatsApp Bot")
ventana.geometry("400x200")

frame = tk.Frame(ventana)
frame.pack(side="bottom", expand=True, padx=50)

btn_iniciar = tk.Button(ventana, text="Iniciar bot de whatsapp", command=iniciar_proceso,bg="#3fd5cd",pady=10,padx=10, font=("Helvetica", 12))
btn_iniciar.pack(side="top", pady=40)

btn_detener = tk.Button(ventana, text="Detener bot de WhatsApp", command=detener_proceso, pady=10, bg="#a93653", fg="white", font=("Helvetica", 12))

ventana.mainloop()