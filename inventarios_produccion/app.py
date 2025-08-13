import flet as ft

def main(page: ft.Page):
    page.title = "Sistema de Inventarios"
    page.add(ft.Text("¡Hola, Flet está funcionando!"))

ft.app(target=main)
