import flet as ft

def mi_boton(texto, on_click):
    return ft.ElevatedButton(text=texto, on_click=on_click)

def mi_input(hint_text):
    return ft.TextField(hint_text=hint_text)
