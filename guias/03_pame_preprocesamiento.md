# 👩‍💻 Guía 3 · Pame: Fase 2 (Preprocesamiento y Limpieza de Datos)

- **Integrante:** Pame
- **Rama asignada:** `pame-preprocesamiento`
- **¿Cuándo puedes empezar?:** **Desde el Día 1** (el archivo `data/raw/winequality-red.csv` ya está en el repositorio).
- **⚠️ Importancia para el equipo:** **Brau depende de que tú termines** y subas `data/processed/winequality-red-limpio.csv` para poder correr la versión final de su modelo Naive Bayes.
- **Archivos que debes crear y subir:**
  - `scripts/preprocesamiento.py`
  - `data/processed/winequality-red-limpio.csv`

---

## 🎯 1. ¿Cuál es tu objetivo en el proyecto?
Eres la responsable de la **Fase 2: Preprocesamiento y Limpieza de Datos**. Debes programar desde cero en **Spyder o Jupyter** un script en Python (`scripts/preprocesamiento.py`) que tome el dataset crudo (`data/raw/winequality-red.csv`) y realice 5 tareas fundamentales:
1. Estandarizar los nombres de las columnas (cambiar espacios por guiones bajos `_`, ej. `volatile acidity` $\rightarrow$ `volatile_acidity`).
2. Verificar valores faltantes (nulos).
3. Detectar y eliminar lotes duplicados (pasando de 1,599 a **1,359 filas únicas**).
4. Analizar los valores atípicos (*outliers*) y las correlaciones entre variables.
5. Crear las nuevas columnas de clasificación (`calidad_bin` y `calidad_3`) y guardar el archivo limpio en **`data/processed/winequality-red-limpio.csv`**.

---

## 🛠️ 2. Paso a Paso: Lo que debes programar desde cero en Spyder / Jupyter

### Paso 1: Clonar el repositorio y crear tu rama
Abre tu terminal y ejecuta:
```bash
git clone https://github.com/XimenaBecOliv07/Naive-Bayes.git
cd Naive-Bayes
git checkout main
git pull origin main
git checkout -b pame-preprocesamiento
```

### Paso 2: Escribir tu script `scripts/preprocesamiento.py`
Abre **Spyder** (recuerda seleccionar la carpeta `Naive-Bayes` como directorio de trabajo en la esquina superior derecha) y crea el archivo **`scripts/preprocesamiento.py`**.

Aquí tienes la explicación paso a paso de lo que debe hacer tu código para que lo escribas, lo pruebes línea por línea y lo entiendas al 100 %:

```python
from pathlib import Path
import pandas as pd

# Definimos las rutas relativas desde la raíz del proyecto
RAIZ = Path(__file__).resolve().parents[1]
RUTA_RAW = RAIZ / "data" / "raw" / "winequality-red.csv"
RUTA_SALIDA = RAIZ / "data" / "processed" / "winequality-red-limpio.csv"

# 1. Cargar el CSV original
df = pd.read_csv(RUTA_RAW)
print(f"Filas originales: {df.shape[0]}, Columnas: {df.shape[1]}")

# 2. Homogenizar nombres de columnas (minúsculas y guión bajo en vez de espacios)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
print("Columnas renombradas:", list(df.columns))

# 3. Revisar valores nulos
nulos = df.isna().sum()
print("\nValores nulos por columna:")
print(nulos)
df = df.dropna()

# 4. Contar y eliminar duplicados exactos
duplicados = df.duplicated().sum()
print(f"\nFilas duplicadas encontradas: {duplicados}")
df = df.drop_duplicates().reset_index(drop=True)
print(f"Filas únicas tras limpiar duplicados: {df.shape[0]}")

# 5. Asegurar tipos de datos correctos (float para mediciones, int para quality)
df["quality"] = df["quality"].astype(int)
for col in df.columns.drop("quality"):
    df[col] = df[col].astype(float)

# 6. Crear las variables objetivo para el modelo Naive Bayes:
#    - calidad_bin: "bueno" si quality >= 6, "malo" si quality <= 5
#    - calidad_3: "baja" (3 a 5), "media" (6), "alta" (7 a 8)
df["calidad_bin"] = (df["quality"] >= 6).map({True: "bueno", False: "malo"})
df["calidad_3"] = pd.cut(
    df["quality"],
    bins=[0, 5, 6, 10],
    labels=["baja", "media", "alta"]
).astype(str)

print("\nDistribución de calidad_bin:")
print(df["calidad_bin"].value_counts())

print("\nDistribución de calidad_3:")
print(df["calidad_3"].value_counts())

# 7. Guardar el dataset limpio en data/processed/
RUTA_SALIDA.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(RUTA_SALIDA, index=False)
print(f"\n¡Archivo guardado con éxito en: {RUTA_SALIDA}!")
```

### Paso 3: Ejecutar y verificar que el archivo se creó bien
Ejecuta tu script en Spyder (botón verde **Run / F5**) o desde la terminal con:
```bash
python scripts/preprocesamiento.py
```
Comprueba que:
1. En la consola diga: `Filas duplicadas encontradas: 240` y `Filas únicas tras limpiar duplicados: 1359`.
2. En `calidad_bin` haya **719 lotes `"bueno"`** (52.9 %) y **640 lotes `"malo"`** (47.1 %). ¡Nota cómo al usar corte binario ($\ge 6$) las clases quedan casi perfectamente balanceadas (53 % vs 47 %)!
3. Se haya creado el archivo **`data/processed/winequality-red-limpio.csv`** con **1,359 filas y 14 columnas** (las 12 originales + `calidad_bin` + `calidad_3`).

---

### Paso 4: Analizar correlaciones para explicárselas al equipo
En la consola de Spyder o en una celda de Jupyter, corre esto para ver qué variables se relacionan más con la calidad del vino:
```python
correlaciones = df.drop(columns=["calidad_bin", "calidad_3"]).corr()["quality"].sort_values(ascending=False)
print(correlaciones)
```
Observa los 3 hallazgos más importantes que tú vas a explicar en la presentación:
1. **`alcohol` (+0.48):** Es la variable con mayor correlación positiva (a mayor grado de alcohol, mejor calidad del vino).
2. **`sulphates` (+0.25) y `citric_acid` (+0.23):** También suben en los vinos buenos porque protegen contra la oxidación y dan frescura.
3. **`volatile_acidity` (-0.39):** Tiene la correlación negativa más fuerte (mientras más ácido acético/volátil tiene el lote, peor es su calificación porque sabe a vinagre).

---

### Paso 5: Subir tu trabajo a GitHub y avisarle a Brau
```bash
git status
git add scripts/preprocesamiento.py
git commit -m "feat: programar script de limpieza de datos y creacion de clases binaria y 3 niveles"

git add data/processed/winequality-red-limpio.csv
git commit -m "data: exportar winequality-red-limpio.csv con 1359 lotes unicos"

git push -u origin pame-preprocesamiento
```
Entra a GitHub, abre tu **Pull Request** hacia `main` y avisa en el grupo para que Xime le dé **Merge** y **Brau** pueda descargar tu CSV limpio.

---

## 🎤 3. Qué te toca decir en la Defensa (Minuto 8 al 13)
- **Diapositivas 5 y 6 (Preprocesamiento y Hallazgos Exploratorios):**
  1. **Limpieza:** Explica que revisaste nulos (no había) y eliminaste **240 registros duplicados** (misma medición repetida), quedando **1,359 lotes únicos**.
  2. **¿Por qué NO eliminamos los valores atípicos (*outliers*)?:** (Pregunta clásica de examen). Explica que en control de calidad de una bodega, un valor extremo de acidez o cloruros no es un "error de dedo", sino precisamente **un lote defectuoso real** que el modelo necesita aprender a detectar.
  3. **¿Dónde se hace el escalado (`StandardScaler`)?:** Explica que no escalaste todo el CSV de golpe para **evitar fuga de datos (*data leakage*)**; el escalado se aplica dentro del Pipeline de entrenamiento (Fase 3) usando únicamente la media y desviación estándar del conjunto de entrenamiento.
  4. **Hallazgos químicos:** Menciona que los vinos buenos se distinguen claramente por tener **más alcohol, menos acidez volátil y más sulfatos**.
