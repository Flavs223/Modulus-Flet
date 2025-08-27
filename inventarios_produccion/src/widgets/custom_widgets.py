import flet as ft
from PIL import Image 
import customtkinter as ctk

# ==================================
# CLASES PARA WIDGETS PERSONALIZADOS
# ==================================
#   CREO LA CLASE DE ContenedorImagen PARA USARLA EN EL BLOQUE 2
#    - Esta clase hereda de ctk.CTkFrame para crear un contenedor personalizado
#    - Permite mostrar una imagen dentro de un fondo con estilo
#    - Puedes ajustar el tamaño, color de fondo y radio de esquina
#    - Usa PIL para cargar imágenes si es necesario (aunque aquí no se usa directamente)

class ContenedorImagen(ctk.CTkFrame):
    #Toma como parámetros 
    def __init__(self, parent, ruta_imagen: str,
                 width: int = 200, height: int = 200,
                 bg_color: str = "transparent",
                 corner_radius: int = 10,
                 *args, **kwargs):
        super().__init__(parent, fg_color=bg_color,
                         corner_radius=corner_radius, *args, **kwargs)



# ==========================
# BLOQUE 1: CONTROLES BÁSICOS DE TEXTO Y FORMULARIOS
# ==========================

def texto_estatico(valor: str):
    """Texto estático (solo muestra información)."""
    return ft.Text(valor)

def campo_texto(etiqueta: str, placeholder: str = ""):
    """Caja de texto para entrada de datos."""
    return ft.TextField(label=etiqueta, hint_text=placeholder)

def casilla_verificacion(texto: str, valor: bool = False):
    """Casilla de verificación (checkbox)."""
    return ft.Checkbox(label=texto, value=valor)

def grupo_radios(nombre: str, opciones: list[str]):
    """Grupo de botones de opción (RadioGroup)."""
    return ft.RadioGroup(
        content=ft.Column([ft.Radio(value=o, label=o) for o in opciones]),
        value=opciones[0] if opciones else None
    )

def lista_desplegable(etiqueta: str, opciones: list[str]):
    """Lista desplegable (Dropdown)."""
    return ft.Dropdown(
        label=etiqueta,
        options=[ft.dropdown.Option(o) for o in opciones]
    )

def interruptor(texto: str, valor: bool = False):
    """Interruptor ON/OFF (Switch)."""
    return ft.Switch(label=texto, value=valor)

def deslizador(minimo: int, maximo: int, valor: int = 0):
    """Deslizador numérico (Slider)."""
    return ft.Slider(min=minimo, max=maximo, value=valor)

def boton_texto(texto: str):
    """Botón de texto simple."""
    return ft.TextButton(texto)

def boton_elevado(texto: str):
    """Botón elevado con sombra."""
    return ft.ElevatedButton(texto)

def boton_contorno(texto: str):
    """Botón con contorno (OutlinedButton)."""
    return ft.OutlinedButton(texto)

def boton_icono(icono):
    """Botón de ícono (usa ft.Icons)."""
    return ft.IconButton(icon=icono)


# ==========================
# BLOQUE 2: WIDGETS VISUALES Y DE DISEÑO
# ==========================

def icono(icono):
    """Ícono de Material Design (usa ft.Icons)."""
    return ft.Icon(icono)

def imagen(ruta: str, ancho: int = 100, alto: int = 100):
    """Muestra una imagen desde ruta local o URL."""
    return ft.Image(src=ruta, width=ancho, height=alto)

def contenedor(contenido, color: str = "#eeeeee", ancho: int = 200, alto: int = 100):
    """Contenedor con fondo, borde y padding."""
    return ft.Container(
        content=contenido,
        width=ancho,
        height=alto,
        bgcolor=color,
        padding=10,
        border_radius=10
    )
def contenedor_imagen():
    """
    Contenedor que muestra una imagen dentro de un fondo personalizado.
    
    - Usa ft.Container como caja principal
    - content puede ser cualquier widget, en este caso un ft.Image
    - bgcolor, padding y border_radius son estilos decorativos
    """
    return ft.Container(
        content=ft.Image(
            src="https://picsum.photos/200",  # URL de la imagen
            width=200,
            height=200,
            fit=ft.ImageFit.COVER            # Ajusta cómo se escala la imagen
        ),
        bgcolor="blue200",
        padding=10,
        border_radius=15
    )

def tarjeta(contenido):
    """Tarjeta con sombra y bordes redondeados."""
    return ft.Card(
        content=ft.Container(
            content=contenido,
            padding=10
        )
    )

def separador():
    """Línea divisoria."""
    return ft.Divider()

def barra_progreso(valor: float = 0.5):
    """Barra de progreso lineal (0.0 a 1.0)."""
    return ft.ProgressBar(value=valor)

def anillo_progreso():
    """Progreso circular (indefinido por defecto)."""
    return ft.ProgressRing()

def avatar_circular(texto: str = "U", color: str = "blue"):
    """Avatar circular con inicial o ícono."""
    return ft.CircleAvatar(content=ft.Text(texto), bgcolor=color)

# ==========================
# BLOQUE 3: LISTAS Y TABLAS
# ==========================

def lista_vertical(elementos: list[str]):
    """ListView: lista vertical desplazable."""
    return ft.ListView(
        controls=[ft.Text(e) for e in elementos],
        height=120,
        spacing=5,
        padding=10,
    )

def lista_cuadricula(elementos: list[str], columnas: int = 2):
    """GridView: lista en formato de cuadrícula con márgenes alrededor."""
    return ft.Container( # Contenedor para agregar padding alrededor de la cuadrícula
        content=ft.GridView(# Usamos GridView para la cuadrícula
            runs_count=columnas,#Número deseado de columnas en este caso
            max_extent=200,#Ancho máximo de cada celda
            spacing=55,# Espacio entre filas
            run_spacing=55,# Espacio entre columnas
            controls=[# Cada elemento es un contenedor con fondo y texto centrado
                ft.Container(
                    ft.Text(e, color="#FFFFFF"), #Define el colo del texto de cada (e)lemento
                    bgcolor="#CD1A1A", #Fondo de cada cuadro
                    border_radius=10, # Bordes redondeados
                    alignment=ft.alignment.center, # Centra el texto
                    height=400, # Altura fija para cada cuadro
                    width=400, # Ancho fijo para cada cuadro
                ) for e in elementos #Todo esto se repite por cada elemento en la lista de entrada
            ]
        ),
        padding=ft.padding.all(30)  # Espacio alrededor de la cuadrícula
    )
def tabla_datos(filas: list[list[str]], encabezados: list[str]):
    """DataTable: tabla con columnas y filas."""
    return ft.DataTable(
        columns=[ft.DataColumn(ft.Text(col)) for col in encabezados],
        rows=[
            ft.DataRow(
                cells=[ft.DataCell(ft.Text(celda)) for celda in fila]
            )
            for fila in filas
        ]
    )