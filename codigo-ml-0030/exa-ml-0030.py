# Cepeda Darrell
# NC = 0030

import sys
import os
import io
import pandas as pd

# Datos correspondientes al número de lista 10
datos_eventos = {
    "Evento": ["Conferencia", "Taller", "Seminario", "Congreso", "Simposio", "Foro"],
    "Asistentes": [500, 150, 300, 800, 250, 400],
    "Duracion_dias": [3, 1, 2, 5, 2, 4]
}

# Encabezado y Pie de página con tus datos personales
encabezado_pie = "Cepeda Darrell Machine Learning pandas, NC 0030"
print(encabezado_pie)

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(datos_eventos)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Asistentes)
registrar("3. Estadísticas Generales de la Columna 'Asistentes'", df['Asistentes'].describe())

# 4. Ordenar Ascendente por Asistentes
df_asc_asistentes = df.sort_values(by="Asistentes", ascending=True)
registrar("4. Ordenar Ascendente por Asistentes", df_asc_asistentes)

# 5. Ordenar Descendente por Duracion_dias
df_desc_duracion = df.sort_values(by="Duracion_dias", ascending=False)
registrar("5. Ordenar Descendente por Duracion_dias", df_desc_duracion)

# 6. Guardar el archivo resultados-ml-0030.md dentro de resultados-0030
carpeta_resultados = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados-0030'))
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0030.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print(encabezado_pie)

print("Cepeda Darrell NC = 0030")