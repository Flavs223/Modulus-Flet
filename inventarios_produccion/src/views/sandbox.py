import flet as ft
import src.widgets.custom_widgets as cw

def main(page: ft.Page):
    page.title = "Sandbox - Widgets de prueba"
    page.scroll = "auto"

    # BLOQUE 1
    bloque1 = ft.Column([
        ft.Text("=== BLOQUE 1: FORMULARIOS Y TEXTO ===", size=20, weight="bold"),
        cw.texto_estatico("Texto estático de ejemplo"),
        cw.campo_texto("Nombre", "Escribe tu nombre"),
        cw.casilla_verificacion("Acepto términos", False),
        cw.grupo_radios("Opciones", ["Opción A", "Opción B", "Opción C"]),
        cw.lista_desplegable("Selecciona un país", ["México", "USA", "España"]),
        cw.interruptor("Activar notificaciones"),
        cw.deslizador(0, 100, 50),
        ft.Row([
            cw.boton_texto("Texto"),
            cw.boton_elevado("Elevado"),
            cw.boton_contorno("Contorno"),
            cw.boton_icono(ft.Icons.HOME),
        ]),
    ])

    # BLOQUE 2
    bloque2 = ft.Column([
        ft.Text("=== BLOQUE 2: VISUALES Y DISEÑO ===", size=20, weight="bold"),
        cw.icono(ft.Icons.STAR), #En este caso, usa el ícono de estrella
        cw.imagen("https://picsum.photos/200", 150, 100),  #Usa una imagen de un sitio de fotos aleatorias
        cw.contenedor(ft.Text("Soy un contenedor"), "#842bba", 200, 100), # Contenedor con fondo morado
        cw.contenedor_imagen(),
        cw.tarjeta(ft.Text("Contenido dentro de una tarjeta")),
        cw.separador(),
        cw.barra_progreso(0.7),
        cw.anillo_progreso(),
        cw.avatar_circular("F", "green"), #Solo funciona con 1 letra, porque con una palabra se sale del circulo y no es estetico
        
    ])

    # Agregamos ambos bloques al layout
    page.add(
        bloque1,
        ft.Divider(thickness=2),
        bloque2
    )

ft.app(target=main)
