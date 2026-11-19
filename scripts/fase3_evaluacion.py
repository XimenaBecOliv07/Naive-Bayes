#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:52:32 2026

@author: tavobecerril
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score

RAIZ = Path(__file__).resolve().parents[1]

CSV_LIMPIO= RAIZ/"data"/"processed"/"winequality-red-limpio.csv"
CSV_METRICAS = RAIZ/"data"/"processed"/"metricas_modelo.csv"

TEST_SIZE = 0.20
RANDOM_STATE = 42

print(CSV_LIMPIO.exists())
df = pd.read_csv(CSV_LIMPIO)
print(df.shape)

X = df.drop(columns = ["quality", "calidad_bin", "calidad_3"])

print(X.shape)
print(list(X.columns))

y = df["calidad_bin"]

print(y.shape)
print(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    stratify=y,
    random_state=RANDOM_STATE,
)

print(len(X_test))
print(y_test.value_counts())

base = DummyClassifier(strategy="most_frequent")
base.fit(X_train, y_train)
y_pred_base = base.predict(X_test)
acc_base = accuracy_score(y_test, y_pred_base)
print("Accuracy linea base:", round(acc_base, 4))

def crear_pipeline(var_smoothing=1e-9):
    """Pipeline nuevo: estandarizar y GaussianNB."""
    return Pipeline([
        ("scaler", StandardScaler()),
        ("nb", GaussianNB(var_smoothing=var_smoothing)),
    ])


CV = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)


def evaluar(variables, var_smoothing=1e-9):
    """Devuelve F1 de validacion cruzada (train) y metricas sobre prueba."""
    modelo = crear_pipeline(var_smoothing)
    f1_cv = cross_val_score(
        modelo, X_train[variables], y_train, cv=CV, scoring="f1_macro"
    ).mean()

    modelo.fit(X_train[variables], y_train)
    y_pred = modelo.predict(X_test[variables])

    return {
        "n_variables": len(variables),
        "var_smoothing": var_smoothing,
        "f1_cv": round(float(f1_cv), 4),
        "accuracy": round(accuracy_score(y_test, y_pred), 4),
        "precision_macro": round(precision_score(y_test, y_pred, average="macro"), 4),
        "recall_macro": round(recall_score(y_test, y_pred, average="macro"), 4),
        "f1_macro": round(f1_score(y_test, y_pred, average="macro"), 4),
    }


VARIABLES_11 = list(X.columns)
print(evaluar(VARIABLES_11))

quality_train = df.loc[X_train.index, "quality"]
correlaciones = X_train.corrwith(quality_train).abs().sort_values(ascending=False)
print("\nCorrelacion |r| con quality (solo entrenamiento):")
print(correlaciones.round(3))

resultados_k = []
for k in [3, 5, 7, 9, 11]:
    variables_k = list(correlaciones.index[:k])
    resultados_k.append(evaluar(variables_k))

tabla_k = pd.DataFrame(resultados_k)
print(tabla_k.to_string(index=False))

mejor_k = int(tabla_k.loc[tabla_k["f1_cv"].idxmax(), "n_variables"])
VARIABLES_FINALES = list(correlaciones.index[:mejor_k])
print("Mejor numero de variables segun F1 de CV:", mejor_k)
print("Variables finales:", VARIABLES_FINALES)

busqueda = GridSearchCV(
    crear_pipeline(),
    param_grid={"nb__var_smoothing": np.logspace(-9, 2, 23)},
    cv=CV,
    scoring="f1_macro",
)
busqueda.fit(X_train[VARIABLES_FINALES], y_train)

MEJOR_VAR_SMOOTHING = float(busqueda.best_params_["nb__var_smoothing"])
print("Mejor var_smoothing:", MEJOR_VAR_SMOOTHING)
print("F1 CV con ese valor:", round(busqueda.best_score_, 4))

metricas_final = evaluar(VARIABLES_FINALES, MEJOR_VAR_SMOOTHING)
print("Modelo final:", metricas_final)

X_train3, X_test3, y_train3, y_test3 = train_test_split(
    X,
    df["calidad_3"],
    test_size=TEST_SIZE,
    stratify=df["calidad_3"],
    random_state=RANDOM_STATE,
)
modelo_3 = crear_pipeline().fit(X_train3, y_train3)
y_pred_3 = modelo_3.predict(X_test3)

metricas_11 = evaluar(VARIABLES_11)
metricas_3var = evaluar(VARIABLES_FINALES)

comparacion = pd.DataFrame([
    {"modelo": "Linea base",
     "accuracy": round(acc_base, 4),
     "f1_macro": round(f1_score(y_test, y_pred_base, average="macro"), 4)},
    {"modelo": "3 clases, 11 variables",
     "accuracy": round(accuracy_score(y_test3, y_pred_3), 4),
     "f1_macro": round(f1_score(y_test3, y_pred_3, average="macro"), 4)},
    {"modelo": "Binario, 11 variables",
     "accuracy": metricas_11["accuracy"],
     "f1_macro": metricas_11["f1_macro"]},
    {"modelo": "Binario, 3 variables",
     "accuracy": metricas_3var["accuracy"],
     "f1_macro": metricas_3var["f1_macro"]},
    {"modelo": "Binario optimizado",
     "accuracy": metricas_final["accuracy"],
     "f1_macro": metricas_final["f1_macro"]},
])
print(comparacion.to_string(index=False))

CARPETA_FIGURAS = RAIZ / "docs" / "figuras"

modelo_final = crear_pipeline(MEJOR_VAR_SMOOTHING).fit(X_train[VARIABLES_FINALES], y_train)
y_pred_final = modelo_final.predict(X_test[VARIABLES_FINALES])

ConfusionMatrixDisplay.from_predictions(y_test, y_pred_final, cmap="Reds", colorbar=False)
plt.title("Modelo final - conjunto de prueba (272 lotes)")
plt.xlabel("Prediccion del modelo")
plt.ylabel("Clase real")
plt.tight_layout()
plt.savefig(CARPETA_FIGURAS / "fase3_matriz_confusion.png", dpi=150)
plt.close()

ax = comparacion.plot.barh(
    x="modelo", y=["accuracy", "f1_macro"], color=["#722F37", "#C98B92"], figsize=(8, 4)
)
ax.set_xlim(0, 1)
ax.set_xlabel("Valor en el conjunto de prueba")
ax.set_ylabel("")
ax.set_title("Comparacion de configuraciones")
plt.tight_layout()
plt.savefig(CARPETA_FIGURAS / "fase3_comparacion_modelos.png", dpi=150)
plt.close()

metricas_csv = pd.DataFrame({
    "metrica": ["accuracy", "precision_macro", "recall_macro", "f1_macro", "accuracy_linea_base"],
    "valor": [
        metricas_final["accuracy"],
        metricas_final["precision_macro"],
        metricas_final["recall_macro"],
        metricas_final["f1_macro"],
        round(acc_base, 4),
    ],
})
metricas_csv.to_csv(CSV_METRICAS, index=False)
print(metricas_csv.to_string(index=False))






