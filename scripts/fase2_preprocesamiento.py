"""Fase 2: Preprocesamiento del dataset Wine Quality (vino tinto).

Entrada : data/raw/winequality-red.csv (solo lectura, nunca se modifica)
Salida  : data/processed/winequality-red-limpio.csv (14 columnas, contrato de datos)
          docs/figuras/fase2_atipicos.png
          docs/figuras/fase2_correlaciones.png

Uso (desde la raiz del proyecto):
    python scripts/fase2_preprocesamiento.py
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # guarda figuras sin abrir ventanas
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# ---------------------------------------------------------------------------
# 1. Rutas reproducibles (funcionan desde cualquier carpeta y computadora)
# ---------------------------------------------------------------------------
# __file__ = scripts/fase2_preprocesamiento.py -> parents[1] = raiz del proyecto
RAIZ = Path(__file__).resolve().parents[1]
RUTA_CRUDO = RAIZ / "data" / "raw" / "winequality-red.csv"
RUTA_LIMPIO = RAIZ / "data" / "processed" / "winequality-red-limpio.csv"
DIR_FIGURAS = RAIZ / "docs" / "figuras"

RUTA_LIMPIO.parent.mkdir(parents=True, exist_ok=True)
DIR_FIGURAS.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 2. Carga del CSV crudo
# ---------------------------------------------------------------------------
df = pd.read_csv(RUTA_CRUDO)
print(f"Filas y columnas originales: {df.shape}")

# ---------------------------------------------------------------------------
# 3. Formato homogeneo: nombres en minusculas y con guion bajo; tipos de datos
# ---------------------------------------------------------------------------
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

df["quality"] = df["quality"].astype(int)
columnas_decimales = [c for c in df.columns if c != "quality"]
df[columnas_decimales] = df[columnas_decimales].astype(float)

print("Columnas:", list(df.columns))
print(df.dtypes.to_string())

# ---------------------------------------------------------------------------
# 4. Nulos y duplicados
# ---------------------------------------------------------------------------
nulos = int(df.isna().sum().sum())
print(f"\nValores nulos totales: {nulos}")
if nulos > 0:
    df = df.dropna()

filas_antes = len(df)
df = df.drop_duplicates().reset_index(drop=True)
duplicados = filas_antes - len(df)
print(f"Duplicados eliminados: {duplicados}")
print(f"Filas finales: {len(df)}")

# ---------------------------------------------------------------------------
# 5. Valores atipicos: se DETECTAN y se documentan, pero se CONSERVAN.
#    Un valor extremo puede ser justo un lote defectuoso real que el modelo
#    debe aprender a reconocer; no son errores de captura.
# ---------------------------------------------------------------------------
variables = [c for c in df.columns if c != "quality"]

q1 = df[variables].quantile(0.25)
q3 = df[variables].quantile(0.75)
iqr = q3 - q1
limite_inf = q1 - 1.5 * iqr
limite_sup = q3 + 1.5 * iqr
atipicos = ((df[variables] < limite_inf) | (df[variables] > limite_sup)).sum()
print("\nAtipicos por variable (regla 1.5 * IQR):")
print(atipicos.to_string())

fig, ejes = plt.subplots(3, 4, figsize=(16, 10))
for eje, var in zip(ejes.ravel(), variables):
    sns.boxplot(y=df[var], ax=eje, color="#8e3b46")
    eje.set_title(var)
    eje.set_ylabel("")
for eje in ejes.ravel()[len(variables):]:
    eje.axis("off")  # oculta los ejes sobrantes
fig.suptitle("Diagramas de caja por variable fisicoquimica", fontsize=14)
fig.tight_layout()
fig.savefig(DIR_FIGURAS / "fase2_atipicos.png", dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# 6. Correlaciones (Pearson) entre variables y con quality
# ---------------------------------------------------------------------------
correlaciones = df[variables + ["quality"]].corr()
print("\nCorrelacion con quality:")
print(correlaciones["quality"].drop("quality").sort_values(ascending=False).round(2).to_string())

fig, eje = plt.subplots(figsize=(11, 9))
sns.heatmap(correlaciones, annot=True, fmt=".2f", cmap="coolwarm",
            center=0, vmin=-1, vmax=1, square=True, ax=eje)
eje.set_title("Matriz de correlacion (Pearson)")
fig.tight_layout()
fig.savefig(DIR_FIGURAS / "fase2_correlaciones.png", dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# 7. Variables objetivo
#    calidad_bin: bueno (>= 6) / malo (<= 5)
#    calidad_3  : baja (<= 5) / media (= 6) / alta (>= 7)
# ---------------------------------------------------------------------------
df["calidad_bin"] = (df["quality"] >= 6).map({True: "bueno", False: "malo"})
df["calidad_3"] = pd.cut(
    df["quality"],
    bins=[0, 5, 6, 10],           # intervalos (0,5], (5,6], (6,10]: incluyen el limite derecho
    labels=["baja", "media", "alta"],
).astype(str)

print("\ncalidad_bin:")
print(df["calidad_bin"].value_counts().to_string())
print("\ncalidad_3:")
print(df["calidad_3"].value_counts().to_string())

# ---------------------------------------------------------------------------
# 8. Exportacion segun el contrato de datos (SIN estandarizar)
# ---------------------------------------------------------------------------
COLUMNAS_CONTRATO = [
    "fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar",
    "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide", "density",
    "ph", "sulphates", "alcohol", "quality", "calidad_bin", "calidad_3",
]
df = df[COLUMNAS_CONTRATO]
df.to_csv(RUTA_LIMPIO, index=False)

print(f"\nArchivo guardado en: {RUTA_LIMPIO.relative_to(RAIZ)}")
print(f"Forma final: {df.shape}")