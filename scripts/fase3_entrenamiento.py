from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.model_selection import StratifiedKFold, cross_val_predict, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

RAIZ = Path(__file__).resolve().parent.parent
RUTA_LIMPIO = RAIZ / "data" / "processed" / "winequality-red-limpio.csv"
RUTA_PREDICCIONES = RAIZ / "data" / "processed" / "predicciones.csv"

RANDOM_STATE = 42
TEST_SIZE = 0.20

VARIABLES_11 = [
    "fixed_acidity",
    "volatile_acidity",
    "citric_acid",
    "residual_sugar",
    "chlorides",
    "free_sulfur_dioxide",
    "total_sulfur_dioxide",
    "density",
    "ph",
    "sulphates",
    "alcohol",
]

# Preliminar con 11 variables; actualizar cuando Octavio envie [MODELO]
VARIABLES_SELECCIONADAS = VARIABLES_11
VAR_SMOOTHING_FINAL = 1e-9


def cargar_datos() -> pd.DataFrame:
    """Carga el CSV limpio oficial generado en la Fase 2."""
    print(f"Cargando dataset limpio desde: {RUTA_LIMPIO.relative_to(RAIZ)}")
    return pd.read_csv(RUTA_LIMPIO)


def crear_pipeline(var_smoothing: float = 1e-9) -> Pipeline:
    """Devuelve un pipeline nuevo con estandarizacion y GaussianNB."""
    return Pipeline([
        ("scaler", StandardScaler()),
        ("nb", GaussianNB(var_smoothing=var_smoothing)),
    ])


def ejecutar_experimento(
    X: pd.DataFrame,
    y: pd.Series,
    nombre: str,
    var_smoothing: float = 1e-9,
) -> Pipeline:
    """Divide en 80/20 estratificado, entrena el pipeline e imprime metricas en prueba."""
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        stratify=y,
        random_state=RANDOM_STATE,
    )

    pipeline = crear_pipeline(var_smoothing=var_smoothing)
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    f1_mac = f1_score(y_test, y_pred, average="macro")

    print(f"\n{'=' * 65}")
    print(f"EXPERIMENTO: {nombre}")
    print(f"Lotes entrenamiento: {len(X_train)} | Lotes prueba: {len(X_test)}")
    print(f"Variables ({X.shape[1]}): {list(X.columns)}")
    print(f"var_smoothing: {var_smoothing}")
    print(f"Accuracy (prueba): {acc:.4f} | F1 Macro (prueba): {f1_mac:.4f}")
    print("-" * 65)
    print(classification_report(y_test, y_pred, digits=4))

    return pipeline


def generar_predicciones_dashboard(
    df: pd.DataFrame,
    variables: list[str],
    var_smoothing: float = 1e-9,
) -> pd.DataFrame:
    """Genera predicciones y probabilidades honestas (CV=5) para los 1,359 lotes."""
    X = df[variables]
    y = df["calidad_bin"]

    pipeline = crear_pipeline(var_smoothing=var_smoothing)
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

    probas = cross_val_predict(pipeline, X, y, cv=cv, method="predict_proba")

    pipeline.fit(X, y)
    clases = list(pipeline.named_steps["nb"].classes_)
    idx_bueno = clases.index("bueno")

    prob_bueno = probas[:, idx_bueno]
    y_pred = np.array([clases[i] for i in np.argmax(probas, axis=1)])

    df_pred = df.copy()
    df_pred["id_lote"] = np.arange(1, len(df_pred) + 1)
    df_pred["y_real"] = y.values
    df_pred["y_pred"] = y_pred
    df_pred["prob_bueno"] = np.round(prob_bueno, 6)
    df_pred["acierto"] = (df_pred["y_real"] == df_pred["y_pred"]).astype(int)
    df_pred["lote_en_riesgo"] = (df_pred["y_pred"] == "malo").astype(int)

    RUTA_PREDICCIONES.parent.mkdir(parents=True, exist_ok=True)
    df_pred.to_csv(RUTA_PREDICCIONES, index=False)

    print(f"\n{'=' * 65}")
    print(f"Archivo exportado: {RUTA_PREDICCIONES.relative_to(RAIZ)}")
    print(f"Dimensiones: {df_pred.shape[0]} filas x {df_pred.shape[1]} columnas")
    print(f"Accuracy global en CV (1,359 lotes): {df_pred['acierto'].mean():.4f}")
    print(f"Lotes detectados en riesgo (malo): {df_pred['lote_en_riesgo'].sum()}")
    return df_pred


def main() -> None:
    df = cargar_datos()

    ejecutar_experimento(
        X=df[VARIABLES_11],
        y=df["calidad_3"],
        nombre="1. Tres clases (baja/media/alta) - 11 variables",
    )

    ejecutar_experimento(
        X=df[VARIABLES_11],
        y=df["calidad_bin"],
        nombre="2. Binario (bueno/malo) - 11 variables",
    )

    ejecutar_experimento(
        X=df[VARIABLES_SELECCIONADAS],
        y=df["calidad_bin"],
        nombre="3. Binario final - Variables seleccionadas (Fase 3B)",
        var_smoothing=VAR_SMOOTHING_FINAL,
    )

    generar_predicciones_dashboard(
        df=df,
        variables=VARIABLES_SELECCIONADAS,
        var_smoothing=VAR_SMOOTHING_FINAL,
    )


if __name__ == "__main__":
    main()
