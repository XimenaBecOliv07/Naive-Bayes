# Guía fase 1: Origen y exploración de datos

| | |
|---|---|
| **Responsable** | Mateo |
| **Rama** | `mateo-fase1-origen-datos` |
| **Puedes empezar** | Desde el inicio: el CSV crudo ya está en el repositorio |
| **Dependes de** | Nadie |
| **Dependen de ti** | Pamela (los problemas que encuentres son los que ella resuelve) y Fátima (tus cifras van a la presentación) |
| **Revisa tu PR** | Pamela |
| **Tus archivos** | `scripts/fase1_exploracion.py`, `docs/fase1_origen_datos.md`, `docs/figuras/fase1_*.png` |

> Esta guía no te da el código. Te da el contexto, los conceptos, la documentación y pistas para que lo resuelvas tú. Las pistas están ocultas: ábrelas solo si te atoras, empezando por la primera.

---

## 1. Contexto

Antes de limpiar o modelar datos hay que conocerlos. Un modelo es tan bueno como los datos con que se entrena, y la mayoría de los errores en un proyecto de *machine learning* vienen de no haber entendido bien los datos al principio.

Tu fase responde preguntas básicas pero decisivas: ¿de dónde vienen estos datos?, ¿qué mide cada columna?, ¿están completos?, ¿hay registros repetidos?, ¿cómo se reparten las calificaciones de calidad? Las respuestas determinan qué tiene que hacer Pamela en la fase 2 y por qué el equipo agrupa la calidad en clases.

## 2. Objetivo general

Documentar el origen, la estructura y el contenido del dataset *Wine Quality* (vino tinto) para que todo el equipo entienda qué representan los datos y qué problemas tienen.

## 3. Objetivos específicos

1. Identificar la fuente, los autores y el contexto del dataset.
2. Describir sus dimensiones, tipos de datos, valores nulos y duplicados.
3. Explicar el significado químico de cada una de las 12 variables y su efecto esperado en la calidad.
4. Analizar la distribución de `quality` y demostrar con números que las clases están desbalanceadas.

## 4. Entradas y salidas

| | Archivo |
|---|---|
| **Entrada** | `data/raw/winequality-red.csv` (solo lectura, nunca lo modifiques) |
| **Salida** | `scripts/fase1_exploracion.py`: script que calcula todas tus cifras |
| **Salida** | `docs/fase1_origen_datos.md`: tu reporte escrito |
| **Salida** | `docs/figuras/fase1_distribucion_quality.png`: gráfica de la distribución de la calidad |

## 5. Conceptos que debes investigar

| Concepto | Pregunta que debes poder responder |
|---|---|
| Análisis exploratorio de datos (EDA) | ¿Para qué sirve explorar antes de modelar? |
| Registro duplicado | ¿Por qué una fila repetida puede inflar artificialmente los resultados de un modelo? |
| Estadísticas descriptivas | ¿Qué te dicen la media, la mediana, la desviación estándar, el mínimo y el máximo de una variable? |
| Variable objetivo y variables predictoras | ¿Cuál es cuál en este dataset? |
| Desbalance de clases | ¿Por qué es un problema que casi todos los vinos tengan calidad 5 o 6? |
| Química básica del vino | ¿Qué es la acidez volátil y por qué arruina un vino? ¿Para qué se añaden sulfatos? |

**Fuentes:**
- Página oficial del dataset: https://archive.ics.uci.edu/dataset/186/wine+quality
- Artículo original: Cortez et al. (2009), https://doi.org/10.1016/j.dss.2009.05.016. Lee al menos el resumen y la descripción de los datos.

## 6. Herramientas

| Necesitas... | Investiga |
|---|---|
| Cargar el CSV | [`pandas.read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) |
| Ver filas, columnas y tipos | `DataFrame.shape`, `DataFrame.dtypes`, [`DataFrame.info`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html) |
| Contar nulos | [`DataFrame.isna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html) combinado con `.sum()` |
| Contar duplicados | [`DataFrame.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html) |
| Estadísticas descriptivas | [`DataFrame.describe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html) |
| Contar lotes por calificación | [`Series.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html) |
| Graficar conteos | [`seaborn.countplot`](https://seaborn.pydata.org/generated/seaborn.countplot.html) |
| Guardar una figura | [`matplotlib.pyplot.savefig`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html) |

## 7. Ruta de trabajo

### Paso 1: Crea tu rama

Sigue la [sección 5 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#5-git-y-github).

### Paso 2: Carga y describe el dataset

Crea `scripts/fase1_exploracion.py` y responde con código: ¿cuántas filas y columnas hay?, ¿de qué tipo es cada columna?, ¿hay nulos?, ¿hay duplicados?

<details>
<summary>Pista 1</summary>

Todo empieza con una sola línea de pandas que lee el archivo. Recuerda que tu directorio de trabajo debe ser la raíz del proyecto, así que la ruta es relativa: `data/raw/...`.
</details>

<details>
<summary>Pista 2</summary>

`df.duplicated()` devuelve una serie de `True`/`False`. ¿Qué pasa si le aplicas `.sum()` a una serie de booleanos?
</details>

### Paso 3: Analiza la variable `quality`

¿Qué valores toma realmente? ¿Cuántos lotes hay de cada calificación? ¿Qué porcentaje del total representan las calificaciones 5 y 6 juntas?

<details>
<summary>Pista 1</summary>

`value_counts()` cuenta, pero el resultado sale ordenado por frecuencia. Busca cómo ordenarlo por calificación.
</details>

<details>
<summary>Pista 2</summary>

`value_counts` tiene un parámetro que devuelve proporciones en lugar de conteos. Revisa su documentación.
</details>

### Paso 4: Grafica la distribución

Genera una gráfica de barras de `quality` con título y ejes en español y guárdala en `docs/figuras/fase1_distribucion_quality.png`. El color del proyecto es `#722F37`.

<details>
<summary>Pista</summary>

Guarda la figura **antes** de mostrarla: en algunos entornos, después de mostrarla la figura queda vacía.
</details>

### Paso 5: Redacta tu reporte

Crea `docs/fase1_origen_datos.md` con:
1. **Procedencia:** nombre del dataset, repositorio, autores y referencia completa.
2. **Resumen técnico:** tabla con filas, columnas, nulos, duplicados y conteo por calificación.
3. **Diccionario de datos:** las 12 variables con su unidad, qué mide y cómo afecta al vino, **con tus palabras**.
4. **Hallazgos:** qué problemas tiene el dataset y qué implican para las fases siguientes.

### Paso 6: Commits y pull request

Haz al menos dos commits (script con figura y reporte), sube tu rama y abre el PR. Ejemplo: `feat(fase1): calcular estadisticas y distribucion de quality`.

### Paso 7: Tu sección del notebook (turno 1)

Cuando tu PR esté en `main`, toma el turno del notebook siguiendo la [sección 6 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#6-notebook-integrador-por-turnos).

## 8. Criterios de aceptación

Si tus números no coinciden con estos, revisa tu código antes de abrir el PR.

- [ ] El dataset tiene **1,599 filas y 12 columnas**.
- [ ] Hay **0 valores nulos** y **240 filas duplicadas**.
- [ ] `quality` solo toma valores del 3 al 8, con estos conteos: 3 → 10, 4 → 53, 5 → 681, 6 → 638, 7 → 199, 8 → 18.
- [ ] El script corre de principio a fin sin errores desde la raíz del proyecto.
- [ ] La figura está en `docs/figuras/` y tiene título y ejes legibles.
- [ ] El reporte explica las 12 variables con tus palabras y cita la fuente.

## 9. Preparación para la defensa (minutos 3 a 8)

Debes poder responder sin leer:
- ¿De dónde salen los datos y quién los publicó?
- ¿Cuáles son las variables predictoras y cuál es la variable objetivo?
- ¿Por qué la rúbrica habla de 12 atributos si el modelo usa 11?
- ¿Qué significa que el dataset esté desbalanceado y por qué eso obligó al equipo a agrupar la calidad?
- ¿Por qué estas mediciones sirven para predecir **temprano**, antes de la cata?
