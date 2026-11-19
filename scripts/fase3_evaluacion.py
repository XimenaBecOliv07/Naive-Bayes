#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:52:32 2026

@author: tavobecerril
"""
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

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

