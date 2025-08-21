import flet as ft

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
