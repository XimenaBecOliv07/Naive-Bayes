# 👨‍💻 Guía 2 · Mateo: Fase 1 (Origen y Exploración de Datos)

- **Integrante:** Mateo
- **Rama asignada:** `mateo-origen-datos`
- **¿Cuándo puedes empezar?:** **Desde el Día 1** (el archivo `data/raw/winequality-red.csv` ya está en el repositorio).
- **Archivos que debes crear y subir:**
  - `docs/fase1_origen_datos.md` (tu reporte técnico y diccionario de datos)
  - `scripts/exploracion_fase1.py` (tu script en Spyder/Python donde obtienes todas las cifras y gráficas exploratorias)

---

## 🎯 1. ¿Cuál es tu objetivo en el proyecto?
Eres el responsable de la **Fase 1: Fuente y Origen de los Datos**. Debes investigar de dónde proviene el dataset de vino tinto, abrirlo en **Spyder o Jupyter Notebook**, analizarlo con `pandas` sin modificar el archivo original y documentar:
1. Cuántos registros (filas) y variables (columnas) tiene.
2. Qué significa cada una de las 12 columnas en el contexto químico de una bodega de vino.
3. Cómo se distribuye la calificación `quality` (y demostrar con números por qué el dataset está desbalanceado).

---

## 🛠️ 2. Paso a Paso: Lo que debes hacer desde cero en Spyder o Jupyter

### Paso 1: Clonar el repositorio y crear tu rama
Abre tu terminal y ejecuta:
```bash
git clone https://github.com/XimenaBecOliv07/Naive-Bayes.git
cd Naive-Bayes
git checkout main
git pull origin main
git checkout -b mateo-origen-datos
```

### Paso 2: Analizar el dataset en Spyder o Jupyter (Hazlo tú mismo)
1. Abre **Spyder** o **Jupyter Notebook** (asegúrate de estar ubicado en la carpeta raíz `Naive-Bayes`, como explica [`INSTRUCCIONES_GENERALES.md`](../INSTRUCCIONES_GENERALES.md)).
2. Crea un archivo nuevo llamado **`scripts/exploracion_fase1.py`** y escribe tú mismo el código para responder estas preguntas usando `pandas`:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar el dataset original
df = pd.read_csv("data/raw/winequality-red.csv")

# 2. ¿Cuántas filas y columnas tiene?
print("Dimensiones (filas, columnas):", df.shape)

# 3. ¿Cuáles son los nombres de las columnas y sus tipos de datos?
print("\nTipos de datos:")
print(df.dtypes)

# 4. ¿Hay valores nulos y cuántos duplicados existen?
print("\nValores nulos por columna:")
print(df.isna().sum())
print("\nTotal de filas duplicadas:", df.duplicated().sum())

# 5. Estadísticas descriptivas (mínimo, máximo, media, desviación estándar)
resumen = df.describe().T
print("\nResumen estadístico:")
print(resumen[["min", "mean", "50%", "max", "std"]])

# 6. ¿Cuántos vinos hay de cada calificación (quality)?
print("\nConteo de lotes por calificación (quality):")
print(df["quality"].value_counts().sort_index())
```

3. **Ejecuta tu código y anota los números que te salgan en la consola:**
   - Verás que hay **1,599 filas y 12 columnas**.
   - Verás que hay **0 nulos** y **240 filas duplicadas** (por lo que quedan 1,359 lotes únicos).
   - Verás que la columna `quality` solo tiene valores del **3 al 8** (no hay vinos con 0, 1, 2, 9 ni 10), y que más del 80 % de los vinos tienen calificación **5** (681 lotes) o **6** (638 lotes), mientras que en los extremos casi no hay muestras (calidad 3 tiene 10 lotes; calidad 8 tiene 18 lotes). **¡Este hallazgo tuyo es importantísimo porque justifica por qué Pame y Brau tendrán que agrupar la calidad en clases!**

4. **Genera también una gráfica de barras de `quality`:**
```python
plt.figure(figsize=(7, 4))
sns.countplot(data=df, x="quality", color="#722F37")
plt.title("Distribución de la calidad del vino tinto (1,599 lotes)")
plt.xlabel("Calificación sensorial (quality)")
plt.ylabel("Número de lotes")
plt.tight_layout()
plt.savefig("docs/distribucion_quality.png", dpi=150)
plt.show()
```

---

### Paso 3: Redactar tu documento `docs/fase1_origen_datos.md`
Con los resultados que obtuviste en tu consola, crea el archivo **`docs/fase1_origen_datos.md`** e incluye:

1. **Procedencia y Referencia Bibliográfica:**
   - Nombre: *Wine Quality Dataset (Red Wine - Vinho Verde de Portugal)*.
   - Repositorio: UCI Machine Learning Repository.
   - Autores: Cortez, P., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). *Modeling wine preferences by data mining from physicochemical properties*. Decision Support Systems, 47(4), 547-553.
2. **Resumen Técnico del Dataset:**
   - Tabla con número de registros (1,599), columnas (12: 11 predictoras continuas + 1 objetivo entera), nulos (0), duplicados detectados (240) y distribución exacta de `quality` (cuántos lotes hay de calificación 3, 4, 5, 6, 7 y 8).
3. **Diccionario de las 12 Variables (explicado con tus palabras):**
   - `fixed acidity` (acidez fija - ácido tartárico): Aporta estructura al vino.
   - `volatile acidity` (acidez volátil - ácido acético): **Muy importante**, si es alta le da olor y sabor a vinagre.
   - `citric acid` (ácido cítrico): Aporta frescura.
   - `residual sugar` (azúcar residual): Azúcar que queda tras la fermentación.
   - `chlorides` (cloruros): Cantidad de sal en el vino.
   - `free sulfur dioxide` ($\text{SO}_2$ libre): Previene microbios y oxidación.
   - `total sulfur dioxide` ($\text{SO}_2$ total): Conservador total.
   - `density` (densidad): Depende del porcentaje de alcohol y azúcar.
   - `pH`: Nivel de acidez en escala de 0 a 14 (en vino suele estar entre 2.7 y 4.0).
   - `sulphates` (sulfatos): Aditivo antioxidante y antimicrobiano.
   - `alcohol` (% vol.): Grado alcohólico del lote.
   - `quality` (variable objetivo): Calificación mediana otorgada en cata ciega por al menos 3 expertos enólogos.

---

### Paso 4: Subir tu trabajo a GitHub (Commits y Pull Request)
Cuando tengas listos `scripts/exploracion_fase1.py`, `docs/distribucion_quality.png` y `docs/fase1_origen_datos.md`:

```bash
git status
git add scripts/exploracion_fase1.py docs/distribucion_quality.png
git commit -m "feat: agregar script de exploracion inicial y grafica de distribucion de quality"

git add docs/fase1_origen_datos.md
git commit -m "docs: documentar origen de datos UCI y diccionario de las 12 variables"

git push -u origin mateo-origen-datos
```
Entra a GitHub y crea tu **Pull Request** hacia `main`.

---

## 🎤 3. Qué te toca decir en la Defensa (Minuto 3 al 8)
- **Diapositivas 3 y 4:**
  - Explica de dónde salieron los datos (1,599 muestras de vino tinto portugués *Vinho Verde* del repositorio UCI, publicadas por Cortez et al., 2009).
  - Explica que las 11 variables de entrada son mediciones objetivas de laboratorio (acidez, sulfatos, alcohol, pH) y que la variable `quality` es la calificación sensorial.
  - Muestra la gráfica de distribución de `quality` y explica que casi todos los vinos caen en 5 y 6, razón por la cual el equipo decidió agrupar las calidades para entrenar el clasificador.
