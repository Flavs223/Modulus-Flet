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
        
        
class StackImagenTexto:
    def __init__(self, imagen_url: str, texto: str, 
                 ancho: int = 600, alto: int = 300,
                 alineacion=ft.alignment.center,
                 color_texto: str = "white", 
                 tamano_texto: int = 30):
        self.imagen_url = imagen_url
        self.texto = texto
        self.ancho = ancho
        self.alto = alto
        self.alineacion = alineacion
        self.color_texto = color_texto
        self.tamano_texto = tamano_texto

    def build(self):  # 👈 aquí está el método que antes te faltaba
        return ft.Stack(
            controls=[
                ft.Image(
                    src=self.imagen_url,
                    width=self.ancho,
                    height=self.alto,
                    fit=ft.ImageFit.COVER,
                ),
                ft.Container(
                    content=ft.Text(
                        self.texto,
                        size=self.tamano_texto,
                        weight=ft.FontWeight.BOLD,
                        color=self.color_texto,
                    ),
                    alignment=self.alineacion,
                    width=self.ancho,
                    height=self.alto,
                ),
            ],
            width=self.ancho,
            height=self.alto,
        )
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

def lista_cuadricula(elementos: list[str], columnas: int = 3):
    """GridView: lista en formato de cuadrícula con márgenes alrededor."""
    return ft.Container( # Contenedor para agregar padding alrededor de la cuadrícula
        content=ft.GridView( # Usamos GridView para la cuadrícula
            #expand=True,                            
            runs_count=columnas,#Hace que mantenga las columnasd del parametro
            max_extent=400,   # Ancho máximo de cada celda
            spacing=50, #Espacio entre filas
            run_spacing=50, #Espacio entre columnas
            controls=[ # Cada elemento es un contenedor con fondo y texto centrado
                ft.Container(
                    content=ft.Container(   # Contenedor interno que sí respeta width/height
                    # Lo realiza llamando a la función ft.Container dentro de la variable content
                    # El contenido "content" contiene el texto centrado con estilo y el color de la celda
                        content=ft.Text(e, color="white", size=12), #Estilo del texto de cada (e)lemento
                        bgcolor="#CD1A1A", 
                        border_radius=10,
                        alignment=ft.alignment.center,
                        height=300,  # Ahora sí 20x20 reales
                        width=300,
                    ),
                    alignment=ft.alignment.center,  # centra el contenido en la celda
                )
                for e in elementos
            ]
        ),
        padding=20
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

# ==========================
# BLOQUE 4: ORGANIZADORES DE LAYOUT
# ==========================
def fila_basica():
    return ft.Row(
        controls=[
            ft.Container(content=ft.Text("Elemento 1"), bgcolor="red", width=100, height=50),
            ft.Container(content=ft.Text("Elemento 2"), bgcolor="green", width=100, height=50),
            ft.Container(content=ft.Text("Elemento 3"), bgcolor="blue", width=100, height=50),
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

def columna_basica():
    return ft.Column(
        controls=[
            ft.Text("Fila 1", size=20),
            ft.Text("Fila 2", size=20),
            ft.Text("Fila 3", size=20),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )


def tabs_basicos():
    return ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Inicio", content=ft.Text("Contenido de Inicio")),
            ft.Tab(text="Perfil", content=ft.Text("Contenido de Perfil")),
            ft.Tab(text="Configuración", content=ft.Text("Contenido de Configuración")),
        ]
    )

def panel_expandible():
    return ft.ExpansionPanelList(
        expand_icon_color="blue",
        elevation=2,
        controls=[
            ft.ExpansionPanel(
                header=ft.Text("Panel 1"),
                content=ft.Text("Contenido del panel 1"),
                bgcolor="#f22727",
                expanded=False
            ),
            ft.ExpansionPanel(
                header=ft.Text("Panel 2"),
                content=ft.Text("Contenido del panel 2"),
                bgcolor="#2057ff",
                expanded=True
            ),
        ]
    )


def barra_navegacion():
    return ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Config"),
        ]
    )


def ejemplo_navigationrail():
    return ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        destinations=[
            ft.NavigationRailDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationRailDestination(icon=ft.Icons.PERSON, label="Perfil"),
            ft.NavigationRailDestination(icon=ft.Icons.SETTINGS, label="Config"),
        ]
    )

def barra_superior():
    return ft.AppBar(
        title=ft.Text("Mi Aplicación"),
        bgcolor="blue",
        leading=ft.Icon(ft.Icons.MENU),
        actions=[
            ft.IconButton(ft.Icons.SEARCH),
            ft.IconButton(ft.Icons.MORE_VERT),
        ]
    )
