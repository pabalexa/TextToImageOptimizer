from PIL import Image, ImageDraw, ImageFont
import os

def crear_imagen_con_texto(
    texto: str,
    ancho: int,
    alto: int,
    ruta_fuente: str,
    nombre_fuente: str,
    color_texto: tuple,
    color_fondo: tuple or None,
    tamano_fuente_max: int,
    tamano_fuente_min: int,
    nombre_archivo: str
) -> None:
    """
    Crea una imagen con texto optimizado para llenar el espacio disponible.
    """
    
    def obtener_dimensiones_texto(texto: str, fuente: ImageFont.FreeTypeFont) -> tuple:
        """Obtiene las dimensiones que ocuparía el texto con una fuente dada."""
        ancho = fuente.getlength(texto)
        ascent, descent = fuente.getmetrics()
        alto_linea = ascent + descent
        return (ancho, alto_linea, ascent, descent)

    def obtener_dimensiones_lineas(lineas: list, fuente: ImageFont.FreeTypeFont) -> tuple:
        """Obtiene las dimensiones totales que ocuparían las líneas de texto."""
        ancho_maximo = 0
        dimensiones_por_linea = []
        ascent, descent = fuente.getmetrics()
        alto_linea = ascent + descent
        espacio_entre_lineas = int(fuente.size * 0.3)
        
        for linea in lineas:
            ancho = fuente.getlength(linea)
            ancho_maximo = max(ancho_maximo, ancho)
            dimensiones_por_linea.append((ancho, alto_linea, ascent, descent))
        
        altura_total = len(lineas) * alto_linea + (len(lineas) - 1) * espacio_entre_lineas if len(lineas) > 0 else 0
        
        return ancho_maximo, altura_total, dimensiones_por_linea, espacio_entre_lineas

    def ajustar_texto(texto: str, fuente: ImageFont.FreeTypeFont, max_width: int) -> list:
        """Ajusta el texto para que quepa en el ancho máximo."""
        palabras = texto.split()
        lineas = []
        linea_actual = []
        ancho_actual = 0
        
        for palabra in palabras:
            ancho_palabra, _, _, _ = obtener_dimensiones_texto(palabra, fuente)
            ancho_espacio = fuente.getlength(" ")
            
            if not linea_actual:
                if ancho_palabra <= max_width:
                    linea_actual.append(palabra)
                    ancho_actual = ancho_palabra
                else:
                    return None
                continue
            
            if ancho_actual + ancho_espacio + ancho_palabra <= max_width:
                linea_actual.append(palabra)
                ancho_actual += ancho_espacio + ancho_palabra
            else:
                lineas.append(' '.join(linea_actual))
                linea_actual = [palabra]
                ancho_actual = ancho_palabra
        
        if linea_actual:
            lineas.append(' '.join(linea_actual))
        
        return lineas

    def encontrar_mejor_tamano_fuente():
        """Encuentra el mejor tamaño de fuente que maximice el uso del espacio."""
        margen = 20  # margen en cada lado
        area_disponible = (ancho - margen * 2) * (alto - margen * 2)
        mejor_tamano = tamano_fuente_min
        mejor_relacion = 0
        mejores_lineas = None
        
        for tamano in range(tamano_fuente_max, tamano_fuente_min - 1, -1):
            fuente = ImageFont.truetype(os.path.join(ruta_fuente, nombre_fuente), tamano)
            lineas = ajustar_texto(texto, fuente, ancho - margen * 2)
            
            if lineas is None:
                continue
                
            ancho_total, altura_total, _, _ = obtener_dimensiones_lineas(lineas, fuente)
            
            if altura_total > alto - margen * 2 or ancho_total > ancho - margen * 2:
                continue
                
            area_texto = ancho_total * altura_total
            relacion_area = area_texto / area_disponible
            
            if relacion_area > mejor_relacion:
                mejor_relacion = relacion_area
                mejor_tamano = tamano
                mejores_lineas = lineas
        
        fuente_final = ImageFont.truetype(os.path.join(ruta_fuente, nombre_fuente), mejor_tamano)
        return mejor_tamano, mejores_lineas, fuente_final

    tamano_optimo, lineas_ajustadas, fuente = encontrar_mejor_tamano_fuente()
    
    if color_fondo is None:
        modo = 'RGBA'
        extension = '.png'
        color_fondo = (0, 0, 0, 0)
    else:
        modo = 'RGB'
        extension = '.jpg'
    
    imagen = Image.new(modo, (ancho, alto), color_fondo)
    draw = ImageDraw.Draw(imagen)
    
    ancho_total, altura_total, dimensiones_lineas, espacio_entre_lineas = obtener_dimensiones_lineas(lineas_ajustadas, fuente)
    
    y_inicial = (alto - altura_total) // 2
    y_inicial = max(y_inicial, 0)
    
    y_actual = y_inicial
    for i, linea in enumerate(lineas_ajustadas):
        ancho_linea = dimensiones_lineas[i][0]
        x = (ancho - ancho_linea) // 2
        
        draw.text((x, y_actual), linea, font=fuente, fill=color_texto)
        
        y_actual += dimensiones_lineas[i][1] + espacio_entre_lineas
    
    ruta_guardado = r"C:\Users\Pablo\Trabajo\Banner_Bot\codigo\CenterTextInBox"
    imagen.save(os.path.join(ruta_guardado, nombre_archivo + extension))

if __name__ == "__main__":
    RUTA_FUENTE = r"C:\Users\Pablo\Trabajo\Banner_Bot\ttf\static"
    NOMBRE_FUENTE = "Montserrat-Bold.ttf"
    COLOR_TEXTO = (255, 255, 255)
    COLOR_FONDO = (0, 0, 0)
    TAMANO_MAX = 120
    TAMANO_MIN = 10
    
    textos_prueba = [
        "La programación es el arte de crear soluciones digitales.",
        "El desarrollo de software requiere creatividad paciencia y dedicación para resolver problemas complejos.",
        "La inteligencia artificial está transformando la manera en que interactuamos con la tecnología creando nuevas posibilidades y desafíos.",
        "Los lenguajes de programación evolucionan constantemente adaptándose a las necesidades del mundo moderno. La programación es el arte de crear soluciones digitales.",
        "El aprendizaje continuo es fundamental para mantenerse actualizado en el campo de la tecnología y el desarrollo. La programación es el arte de crear soluciones digitales. El desarrollo de software requiere creatividad paciencia y dedicación para resolver problemas complejos."
    ]
    
    dimensiones = [
        (800, 400),
        (800, 400),
        (800, 400),
        (800, 400),
        (800, 400)
    ]

    for i, (texto, (ancho, alto)) in enumerate(zip(textos_prueba, dimensiones)):
        crear_imagen_con_texto(
            texto=texto,
            ancho=ancho,
            alto=alto,
            ruta_fuente=RUTA_FUENTE,
            nombre_fuente=NOMBRE_FUENTE,
            color_texto=COLOR_TEXTO,
            color_fondo=COLOR_FONDO,
            tamano_fuente_max=TAMANO_MAX,
            tamano_fuente_min=TAMANO_MIN,
            nombre_archivo=f"imagen_prueba_{i+1}"
        )
        print(f"Imagen {i+1} creada con dimensiones {ancho}x{alto}")
