#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:52:32 2026

@author: tavobecerril
"""
from pathlib import Path
import pandas as pd
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




