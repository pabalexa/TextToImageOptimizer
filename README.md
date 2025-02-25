# TextToImageOptimizer
Genera imágenes con texto ajustado automáticamente para que encaje perfectamente en un espacio dado. Personaliza tamaño de fuente, colores y soporta fondos transparentes o sólidos. Ideal para crear banners, citas o contenido visual con texto optimizado.

## Documentación del Código

### Objetivo del Código

Este código tiene como objetivo generar imágenes con texto optimizado para llenar el espacio disponible en la imagen. El texto se ajusta automáticamente al tamaño de la imagen, eligiendo un tamaño de fuente adecuado y distribuyendo el texto de manera que no se salga del área disponible. Esto es útil para crear banners, carteles u otros elementos visuales donde el texto debe ajustarse dinámicamente a distintas resoluciones de imagen, manteniendo una distribución estética y legible.

### Instrucciones de Uso

Para utilizar el código, sigue estos pasos:

1. **Instalación de Dependencias:**
   Asegúrate de tener las siguientes dependencias instaladas en tu entorno Python:

   - `Pillow` para la manipulación de imágenes:
     ```bash
     pip install Pillow
     ```

2. **Configuración Inicial:**

   - **RUTA_FUENTE**: Especifica el directorio donde se encuentra el archivo de fuente TrueType (por ejemplo, `Montserrat-Bold.ttf`).
   - **NOMBRE_FUENTE**: Especifica el nombre del archivo de fuente (por ejemplo, `"Montserrat-Bold.ttf"`).
   - **COLOR_TEXTO**: Define el color del texto en formato RGB, como `(255, 255, 255)` para texto blanco.
   - **COLOR_FONDO**: Define el color del fondo de la imagen en formato RGB o RGBA. Si no se proporciona, se establece un fondo transparente.
   - **TAMANO_MAX** y **TAMANO_MIN**: Determinan los rangos de tamaño de fuente que el código probará para ajustar el texto en el área disponible.

3. **Generación de Imágenes:**
   Ejecuta el código. El ciclo principal crea varias imágenes de prueba con diferentes textos y dimensiones. Las imágenes generadas se guardarán en el directorio especificado por `ruta_guardado`.

4. **Resultado:**
   El código generará imágenes con texto centrado, ajustado automáticamente al tamaño adecuado, y las guardará en el directorio local. Los archivos de salida tendrán el nombre especificado en `nombre_archivo` con una extensión `.png` o `.jpg`.

### Explicación del Funcionamiento

El código está diseñado para crear imágenes con texto optimizado para que el texto no se desborde ni quede muy pequeño dentro de una imagen de dimensiones especificadas. El proceso se desglosa en varias funciones:

1. **Funciones Internas:**

   - `obtener_dimensiones_texto()`: Calcula el tamaño (ancho y alto) que ocuparía un texto con una fuente dada.
   - `obtener_dimensiones_lineas()`: Calcula las dimensiones totales de varias líneas de texto, considerando el ancho máximo y el espacio entre líneas.
   - `ajustar_texto()`: Divide el texto en líneas para que cada línea se ajuste dentro del ancho disponible.
   - `encontrar_mejor_tamano_fuente()`: Determina el mejor tamaño de fuente que maximiza el uso del espacio disponible sin sobrepasar las dimensiones de la imagen.

2. **Flujo Principal:**
   El flujo comienza con la llamada a `crear_imagen_con_texto()`, que:
   - Llama a `encontrar_mejor_tamano_fuente()` para encontrar el tamaño óptimo de fuente.
   - Crea una imagen en blanco con el color de fondo especificado.
   - Dibuja el texto ajustado dentro de la imagen, centrado tanto vertical como horizontalmente.
   - Guarda la imagen resultante en un archivo.

### Detalles de los Algoritmos

El algoritmo implementado está basado en las siguientes etapas:

1. **Cálculo de las dimensiones del texto**:

   - Se obtiene el tamaño del texto y se calcula el espacio necesario en la imagen para que el texto quepa de manera óptima.
   - La función `ajustar_texto()` ajusta las palabras en varias líneas si es necesario para que el texto no se desborde del área disponible.

2. **Búsqueda del tamaño de fuente óptimo**:
   - Se prueba con diferentes tamaños de fuente dentro del rango especificado por `tamano_fuente_min` y `tamano_fuente_max`, comenzando con el tamaño más grande.
   - Para cada tamaño, el código calcula si el texto ajustado cabe dentro de las dimensiones de la imagen y elige el tamaño de fuente que mejor maximiza el uso del espacio disponible.

### Explicación Técnica de los Algoritmos

1. **Complejidad del Algoritmo de Ajuste de Texto:**
   El algoritmo de ajuste de texto tiene una complejidad de tiempo de O(n), donde n es el número de palabras en el texto. El ajuste de palabras en líneas es eficiente, ya que cada palabra se evalúa una sola vez.

2. **Complejidad del Algoritmo de Búsqueda del Tamaño de Fuente:**
   La función `encontrar_mejor_tamano_fuente()` prueba cada tamaño de fuente entre el tamaño máximo y el mínimo, lo que tiene una complejidad de O(m), donde m es el número de tamaños de fuente posibles (tamaño máximo menos el tamaño mínimo). Para cada tamaño, se ejecutan operaciones de cálculo que son lineales respecto al número de líneas, lo que da como resultado una complejidad total de O(m \* n), donde m es el número de tamaños de fuente y n es el número de palabras.

### Estructura del Código

El código está estructurado en una única función principal `crear_imagen_con_texto()`, que gestiona la creación de la imagen, y varias funciones internas que manejan los detalles del ajuste y cálculo de las dimensiones del texto. A continuación se detalla la estructura:

- **Funciones Internas:**

  - `obtener_dimensiones_texto()`: Calcula el ancho y alto del texto con una fuente dada.
  - `obtener_dimensiones_lineas()`: Calcula las dimensiones de múltiples líneas de texto.
  - `ajustar_texto()`: Ajusta el texto en líneas según el ancho máximo disponible.
  - `encontrar_mejor_tamano_fuente()`: Busca el tamaño de fuente más adecuado para maximizar el uso del espacio en la imagen.

- **Función Principal:**
  - `crear_imagen_con_texto()`: Crea la imagen, ajusta el texto, y guarda la imagen resultante.

### Ejemplos de Entrada y Salida

**Entrada:**

```python
crear_imagen_con_texto(
    texto="La programación es el arte de crear soluciones digitales",
    ancho=800,
    alto=400,
    ruta_fuente="C:\\fuentes",
    nombre_fuente="Montserrat-Bold.ttf",
    color_texto=(255, 255, 255),
    color_fondo=(0, 0, 0),
    tamano_fuente_max=120,
    tamano_fuente_min=10,
    nombre_archivo="banner1"
)
```

**Salida:**
Se genera una imagen de 800x400 píxeles con el texto "La programación es el arte de crear soluciones digitales" ajustado para caber en la imagen, con texto blanco sobre un fondo negro. La imagen se guarda con el nombre `banner1.png`.

### Manejo de Errores

El código no incluye manejo explícito de excepciones, lo que podría mejorar su robustez. Algunas posibles excepciones incluyen:

- **Archivo de fuente no encontrado**: Asegúrate de que la ruta y el nombre del archivo de fuente sean correctos.
- **Errores de dimensiones**: Si el texto no cabe en las dimensiones especificadas, el algoritmo de ajuste puede no funcionar correctamente.
- **Error al guardar la imagen**: Verifica que la ruta de guardado sea válida y que el programa tenga permisos de escritura.

Recomendación: Añadir excepciones para manejar casos como fuentes no encontradas o problemas con el acceso al directorio de salida.

### Dependencias y Requisitos

- **Bibliotecas Requeridas**:

  - `Pillow` (versión 8.0.0 o superior):
    ```bash
    pip install Pillow
    ```

- **Requisitos del Sistema**:
  - Python 3.6 o superior.

### Notas sobre Rendimiento y Optimización

El código está optimizado para generar imágenes de texto de manera eficiente. Sin embargo, la búsqueda del tamaño de fuente óptimo puede mejorar en eficiencia mediante la implementación de un enfoque más sofisticado de búsqueda binaria en lugar de una búsqueda lineal. Esto reduciría la complejidad en casos donde el rango de tamaños de fuente es muy grande.

### Comentarios Dentro del Código

Los comentarios dentro del código explican cada función y su propósito. Es recomendable mantener estos comentarios actualizados y ser lo más descriptivo posible en secciones donde el algoritmo realiza pasos complejos.
