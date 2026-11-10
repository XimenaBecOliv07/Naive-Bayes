# 👨‍💻 Guía 4 · Brau: Fase 3 (Modelo Clasificador Naive Bayes)

- **Integrante:** Brau
- **Rama asignada:** `brau-modelo-naive-bayes`
- **¿De quién dependes?:** Necesitas que **Pame** haya subido `data/processed/winequality-red-limpio.csv` a `main`. *(Mientras Pame termina, puedes ir escribiendo tu código en Spyder o Jupyter).*
- **⚠️ Quién depende de ti:** **Tavo (Fase 4)** necesita los archivos `data/processed/predicciones.csv` y `data/processed/metricas_modelo.csv` que genera tu código para poder armar el Dashboard en Power BI.
- **Archivos que debes crear y subir:**
  - `scripts/modelo_nb.py`
  - `notebooks/NaiveBayes.ipynb` (el Notebook integrador ejecutado)
  - `data/processed/predicciones.csv`
  - `data/processed/metricas_modelo.csv`
  - `docs/modelo_final.png`

---

## 🎯 1. ¿Cuál es tu objetivo en el proyecto?
Eres el responsable de la **Fase 3: Implementación y Evaluación del Modelo Naive Bayes**. Como las 11 variables fisicoquímicas del vino son números continuos (decimales), utilizaremos **`GaussianNB`** de `scikit-learn`, el cual asume que cada variable sigue una distribución normal (campana de Gauss) dentro de cada clase y aplica el **Teorema de Bayes**:

$$P(\text{Clase} \mid X) \propto P(\text{Clase}) \prod_{i=1}^{n} P(x_i \mid \text{Clase})$$

Tu trabajo consiste en programar y comparar **3 experimentos** para demostrar con evidencia científica cuál clasifica mejor:
1. **Experimento 1:** Clasificación en **3 clases** (`baja`, `media`, `alta`) con las 11 variables ($\text{Accuracy} \approx 0.58$).
2. **Experimento 2:** Clasificación **binaria** (`bueno` vs `malo`) con las **11 variables** ($\text{Accuracy} \approx 0.74$).
3. **Experimento 3 (Modelo Final):** Clasificación **binaria** seleccionando solo las **3 variables más informativas y menos redundantes** (`alcohol`, `volatile_acidity`, `sulphates`), reduciendo el impacto de la colinealidad ($\text{Accuracy} \approx 0.75$).

---

## 🛠️ 2. Paso a Paso: Lo que debes programar desde cero en Spyder / Jupyter

### Paso 1: Clonar, actualizar `main` (con el CSV de Pame) y crear tu rama
```bash
git clone https://github.com/XimenaBecOliv07/Naive-Bayes.git
cd Naive-Bayes
git checkout main
git pull origin main
git checkout -b brau-modelo-naive-bayes
```
*(Verifica que ya exista el archivo `data/processed/winequality-red-limpio.csv` que subió Pame).*

---

### Paso 2: Programar `scripts/modelo_nb.py` en Spyder
Abre **Spyder** (con el directorio de trabajo en `Naive-Bayes`) y crea el archivo **`scripts/modelo_nb.py`**. Escribe y comprende cada bloque:

```python
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    cross_val_score,
    cross_val_predict
)
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import GaussianNB
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    ConfusionMatrixDisplay
)

SEED = 42
RAIZ = Path(__file__).resolve().parents[1]
RUTA_LIMPIO = RAIZ / "data" / "processed" / "winequality-red-limpio.csv"

# 1. Cargar el dataset limpio que preparó Pame (1,359 lotes)
df = pd.read_csv(RUTA_LIMPIO)
X_todas = df.drop(columns=["quality", "calidad_bin", "calidad_3"])

# Creamos nuestro Pipeline (StandardScaler + GaussianNB)
# ¿Por qué Pipeline? Para que el escalador calcule media y desviación SOLO con X_train
def crear_pipeline():
    return Pipeline([
        ("escala", StandardScaler()),
        ("nb", GaussianNB())
    ])

# Función para evaluar cualquier configuración de forma justa
def evaluar_configuracion(X_datos, y_objetivo, nombre_experimento):
    X_tr, X_te, y_tr, y_te = train_test_split(
        X_datos, y_objetivo, test_size=0.20, stratify=y_objetivo, random_state=SEED
    )
    modelo = crear_pipeline()
    modelo.fit(X_tr, y_tr)
    pred_te = modelo.predict(X_te)

    # Validación cruzada estratificada de 5 pliegues sobre entrenamiento
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
    f1_cv = cross_val_score(modelo, X_tr, y_tr, cv=cv, scoring="f1_macro")

    acc = accuracy_score(y_te, pred_te)
    f1 = f1_score(y_te, pred_te, average="macro")

    print(f"\n================ {nombre_experimento} ================")
    print(f"Accuracy en prueba (20%): {acc:.4f}")
    print(f"F1 Macro en prueba:       {f1:.4f}")
    print(f"F1 Macro CV (5 pliegues): {f1_cv.mean():.4f} (+/- {f1_cv.std():.4f})")
    print("\nReporte por clase:")
    print(classification_report(y_te, pred_te, zero_division=0))
    return modelo, X_tr, X_te, y_tr, y_te, pred_te

# --- EXPERIMENTO 1: 3 Clases con las 11 variables ---
evaluar_configuracion(X_todas, df["calidad_3"], "Experimento 1: 3 Clases (11 variables)")

# --- EXPERIMENTO 2: Binario (bueno vs malo) con las 11 variables ---
evaluar_configuracion(X_todas, df["calidad_bin"], "Experimento 2: Binario (11 variables)")

# --- EXPERIMENTO 3 (MODELO FINAL): Binario con las 3 mejores variables ---
VARS_FINALES = ["alcohol", "volatile_acidity", "sulphates"]
X_3vars = df[VARS_FINALES]
modelo_final, X_tr, X_te, y_tr, y_te, pred_te = evaluar_configuracion(
    X_3vars, df["calidad_bin"], "Experimento 3 (FINAL): Binario con 3 variables clave"
)

# Comparar contra Línea Base (DummyClassifier que siempre predice la clase mayoritaria)
base = DummyClassifier(strategy="most_frequent").fit(X_tr, y_tr)
acc_base = accuracy_score(y_te, base.predict(X_te))
print(f"Accuracy Línea Base (clase mayoritaria): {acc_base:.4f}")

# 2. Guardar gráfica de la Matriz de Confusión del Modelo Final
fig, ax = plt.subplots(figsize=(6, 5))
ConfusionMatrixDisplay.from_predictions(
    y_te, pred_te, cmap="Reds", ax=ax, colorbar=False
)
ax.set_title("Matriz de Confusión · Naive Bayes Final (3 variables)")
plt.tight_layout()
plt.savefig(RAIZ / "docs" / "modelo_final.png", dpi=150)
plt.close()

# 3. Exportar metricas_modelo.csv para el Dashboard de Tavo
metricas_df = pd.DataFrame([
    {"metrica": "accuracy", "valor": round(accuracy_score(y_te, pred_te), 4)},
    {"metrica": "precision_macro", "valor": round(precision_score(y_te, pred_te, average="macro"), 4)},
    {"metrica": "recall_macro", "valor": round(recall_score(y_te, pred_te, average="macro"), 4)},
    {"metrica": "f1_macro", "valor": round(f1_score(y_te, pred_te, average="macro"), 4)},
    {"metrica": "accuracy_linea_base", "valor": round(acc_base, 4)},
])
metricas_df.to_csv(RAIZ / "data" / "processed" / "metricas_modelo.csv", index=False)

# 4. Exportar predicciones.csv sobre los 1,359 lotes (usando predicción limpia cross-val) para Power BI
cv_total = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)
y_bin = df["calidad_bin"]
y_pred_cv = cross_val_predict(crear_pipeline(), X_3vars, y_bin, cv=cv_total)
probs_cv = cross_val_predict(crear_pipeline(), X_3vars, y_bin, cv=cv_total, method="predict_proba")

clases_orden = sorted(y_bin.unique()) # ['bueno', 'malo']
idx_bueno = clases_orden.index("bueno")

salida_bi = df.copy()
salida_bi["id_lote"] = range(1, len(salida_bi) + 1)
salida_bi["y_real"] = y_bin
salida_bi["y_pred"] = y_pred_cv
salida_bi["prob_bueno"] = probs_cv[:, idx_bueno].round(4)
salida_bi["acierto"] = (salida_bi["y_real"] == salida_bi["y_pred"]).astype(int)
# Un lote está en riesgo si el modelo predice que es "malo" o su probabilidad de ser bueno es < 0.50
salida_bi["lote_en_riesgo"] = (salida_bi["y_pred"] == "malo").astype(int)

salida_bi.to_csv(RAIZ / "data" / "processed" / "predicciones.csv", index=False)
print("\n¡Listos data/processed/metricas_modelo.csv y data/processed/predicciones.csv para Power BI!")
```

---

### Paso 3: Crear el Jupyter Notebook integrador (`notebooks/NaiveBayes.ipynb`)
Además del script `.py`, la rúbrica pide un **Jupyter Notebook** (`notebooks/NaiveBayes.ipynb`) donde estén integradas con celdas de texto Markdown y celdas de código:
1. La exploración de **Mateo** (Fase 1).
2. La limpieza de **Pame** (Fase 2).
3. Tus 3 experimentos de **Naive Bayes**, las gráficas y las matrices de confusión (Fase 3).

Abre Jupyter Notebook (`jupyter notebook`), crea `notebooks/NaiveBayes.ipynb`, pega cada sección en orden con explicaciones en Markdown, haz clic en **`Kernel > Restart & Run All`** para que todas las celdas queden numeradas (`[1]`, `[2]`, `[3]`...) con sus gráficas visibles y guárdalo.

---

### Paso 4: Subir tu trabajo a GitHub y avisarle a Tavo y Fátima
```bash
git status
git add scripts/modelo_nb.py docs/modelo_final.png
git commit -m "feat: entrenar GaussianNB comparando 3 clases, binario 11 vars y binario 3 vars"

git add data/processed/predicciones.csv data/processed/metricas_modelo.csv
git commit -m "data: exportar predicciones.csv y metricas_modelo.csv para el dashboard de Power BI"

git add notebooks/NaiveBayes.ipynb
git commit -m "feat: integrar Jupyter Notebook completo ejecutado de principio a fin"

git push -u origin brau-modelo-naive-bayes
```
Abre tu **Pull Request** en GitHub hacia `main` y avísale a **Tavo** que ya puede descargar `predicciones.csv` y `metricas_modelo.csv`.

---

## 🎤 3. Qué te toca decir en la Defensa (Minuto 13 al 20)
- **Diapositivas 7, 8 y 9 (Modelo Naive Bayes y Evaluación):**
  1. **Por qué `GaussianNB`:** Porque nuestras 11 variables son continuas. Explica que Naive Bayes asume independencia condicional entre las variables dada la clase.
  2. **¿Se cumple el supuesto de independencia en el vino?:** (Pregunta segura del profesor). Responde que **no al 100 %**, porque variables como `fixed_acidity`, `citric_acid`, `density` y `pH` están fuertemente correlacionadas entre sí. Justamente por eso, cuando redujimos el modelo de 11 variables a las **3 variables menos redundantes y más predictivas (`alcohol`, `volatile_acidity`, `sulphates`)**, eliminamos el ruido de variables colineales y el Accuracy subió de **0.74 a 0.75** (superando ampliamente el **0.53** de la línea base).
  3. **Matriz de Confusión:** En los **272 lotes de prueba** (20 % de 1,359), el modelo final acertó **204 lotes (75 %)** y los errores estuvieron equilibrados entre falsos positivos y falsos negativos.
