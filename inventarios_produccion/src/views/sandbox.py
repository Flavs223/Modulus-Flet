import flet as ft
from src.widgets import custom_widgets as cw

def main(page: ft.Page):
    page.title = "Sandbox Flet"
    
    def click_boton(e):
        print("Botón presionado!")
    
    # Probando widgets
    boton = cw.mi_boton("Presioname", click_boton)
    input_text = cw.mi_input("Escribe algo...")
    
    page.add(boton, input_text)

ft.app(target=main)
