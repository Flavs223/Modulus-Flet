import flet as ft
from src.widgets import custom_widgets as cw


def main(page: ft.Page):
    page.title = "Sandbox - Widgets de prueba"
    page.scroll = "auto"
    # ==========================

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

# BLOQUE 3
    bloque3 = ft.Column([
        ft.Text("=== BLOQUE 3: LISTAS Y TABLAS ===", size=20, weight="bold"),
        ft.Text("Lista vertical (ListView):"),
        cw.lista_vertical(["Elemento 1", "Elemento 2", "Elemento 3"]), #Lista vertical con 3 elementos
        ft.Text("Lista en cuadrícula (GridView):"),
        cw.lista_cuadricula([f"Item {i}" for i in range(1, 10)]), #Gridview con 9 items y 3 columnas
        ft.Text("Tabla de datos (DataTable):"),
        cw.tabla_datos(
            filas=[
                ["Ana", "25", "México"],
                ["Luis", "30", "España"],
                ["John", "28", "USA"]
            ],
            encabezados=["Nombre", "Edad", "País"]
        )
    ])
#BLOQUE 4


# Ejemplos de banners
    stack = cw.StackImagenTexto("https://picsum.photos/800/400", "Hola Mundo")
    page.add(stack.build())
    
    #page.vertical_alignment = ft.MainAxisAlignment.START

    # Banner 1 - Fondo random + texto grande
    banner1 = cw.StackImagenTexto(
        imagen_url="https://raw.githubusercontent.com/flutter/assets-for-api-docs/main/assets/widgets/owl.jpg",
        texto="Bienvenido al Sistema",
        tamano_texto=40,
        color_texto="yellow",
        alineacion=ft.alignment.center
    )
    page.add(banner1.build())
    

    # Banner 2 - Imagen local + texto arriba a la izquierda
    banner2 = cw.StackImagenTexto(
        imagen_url="src/assets/persona5.png",
        texto="IT'S SHOWTIME",
        tamano_texto=25,
        color_texto="white",
        alineacion=ft.alignment.top_left,
        ancho=500,
        alto=200
    )
    page.add(banner2.build())

    # Banner 3 - Otro estilo
    banner3 = cw.StackImagenTexto(
        imagen_url="https://picsum.photos/800/300.jpg",
        texto="Reporte de Producción",
        tamano_texto=28,
        color_texto="red",
        alineacion=ft.alignment.bottom_right
    )

    page.add(banner3.build())

    #page.add(banner1, banner2, banner3)
    
    
    #page.add(stack.build())

    # Agregamos todos los bloques
    page.add(
        bloque1,
        ft.Divider(thickness=2),
        bloque2,
        ft.Divider(thickness=2),
        bloque3
    )
    


ft.app(target=main)
