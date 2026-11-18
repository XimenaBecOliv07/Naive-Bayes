"""
Fase 1: Origen y exploración de datos
Proyecto: Predicción de la calidad del vino tinto con Naive Bayes
Responsable: Mateo

Lee el dataset crudo, describe su estructura, revisa nulos y duplicados,
analiza la distribución de quality y guarda la gráfica de la fase.

Uso (desde la raíz del proyecto):
    python scripts/fase1_exploracion.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Las rutas se calculan a partir de la ubicación de este archivo
# (scripts/ -> parents[1] es la raíz), así el script funciona sin importar
# desde qué carpeta se ejecute ni en qué computadora.
RAIZ = Path(__file__).resolve().parents[1]
RUTA_CSV = RAIZ / "data" / "raw" / "winequality-red.csv"
RUTA_FIGURA = RAIZ / "docs" / "figuras" / "fase1_distribucion_quality.png"

COLOR_VINO = "#722F37"  # color del proyecto


def titulo(texto):
    """Imprime un encabezado para separar cada parte del reporte en consola."""
    print()
    print("=" * 60)
    print(texto)
    print("=" * 60)


def describir_estructura(df):
    """Muestra cuántas filas y columnas hay y el tipo de dato de cada columna."""
    titulo("1. Estructura del dataset")
    filas, columnas = df.shape
    print(f"Filas: {filas}")
    print(f"Columnas: {columnas}")
    print("\nTipo de dato de cada columna:")
    print(df.dtypes.to_string())
    return filas, columnas


def revisar_nulos_y_duplicados(df):
    """Cuenta los valores nulos y las filas que están repetidas."""
    titulo("2. Valores nulos y filas duplicadas")
    # isna() marca True en cada celda vacía; el primer sum() suma por columna
    # y el segundo suma todas las columnas.
    total_nulos = int(df.isna().sum().sum())
    # duplicated() marca True en cada fila idéntica a una anterior;
    # al sumar booleanos, cada True cuenta como 1.
    duplicados = int(df.duplicated().sum())
    print(f"Valores nulos en total: {total_nulos}")
    print(f"Filas duplicadas: {duplicados}")
    print(f"Filas que quedarían sin duplicados: {len(df) - duplicados}")
    return total_nulos, duplicados


def estadisticas_descriptivas(df):
    """Muestra media, mediana, desviación estándar, mínimo y máximo de cada variable."""
    titulo("3. Estadísticas descriptivas")
    # describe() calcula las estadísticas por columna; .T la voltea para que
    # cada variable quede en una fila y se lea mejor.
    resumen = df.describe().T[["mean", "50%", "std", "min", "max"]]
    resumen.columns = ["media", "mediana", "desv_std", "minimo", "maximo"]
    print(resumen.round(3).to_string())
    return resumen


def analizar_quality(df):
    """Cuenta cuántos lotes hay de cada calificación y qué porcentaje representan."""
    titulo("4. Distribución de la variable objetivo quality")
    # value_counts() ordena por frecuencia; sort_index() lo ordena por calificación.
    conteo = df["quality"].value_counts().sort_index()
    # normalize=True devuelve proporciones (0 a 1) en lugar de conteos.
    porcentaje = df["quality"].value_counts(normalize=True).sort_index() * 100
    tabla = pd.DataFrame({"lotes": conteo, "porcentaje": porcentaje.round(2)})
    print(tabla.to_string())
    pct_5_y_6 = porcentaje.loc[[5, 6]].sum()
    print(f"\nLas calificaciones 5 y 6 juntas son el {pct_5_y_6:.2f}% de los lotes")
    return conteo


def graficar_quality(df):
    """Genera la gráfica de barras de quality y la guarda en docs/figuras/."""
    titulo("5. Gráfica de la distribución de quality")
    RUTA_FIGURA.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 5))
    # saturation=1 evita que seaborn aclare el color y respeta el #722F37 exacto.
    sns.countplot(data=df, x="quality", color=COLOR_VINO, saturation=1, ax=ax)

    # Escribe encima de cada barra el número de lotes y su porcentaje.
    total = len(df)
    for barra in ax.patches:
        alto = int(barra.get_height())
        x_centro = barra.get_x() + barra.get_width() / 2
        ax.annotate(f"{alto}\n({alto / total:.1%})", (x_centro, alto),
                    ha="center", va="bottom", fontsize=9)

    ax.set_title("Distribución de la calidad del vino tinto (dataset original)")
    ax.set_xlabel("Calificación de calidad (quality)")
    ax.set_ylabel("Número de lotes")
    ax.set_ylim(0, df["quality"].value_counts().max() * 1.15)
    fig.tight_layout()

    # Se guarda ANTES de cerrar: si se muestra o se cierra primero,
    # en algunos entornos la imagen queda vacía.
    fig.savefig(RUTA_FIGURA, dpi=150)
    plt.close(fig)
    print(f"Figura guardada en: {RUTA_FIGURA.relative_to(RAIZ)}")


def main():
    df = pd.read_csv(RUTA_CSV)
    print(f"Archivo leído: {RUTA_CSV.relative_to(RAIZ)}")

    filas, columnas = describir_estructura(df)
    total_nulos, duplicados = revisar_nulos_y_duplicados(df)
    estadisticas_descriptivas(df)
    conteo = analizar_quality(df)
    graficar_quality(df)


if __name__ == "__main__":
    main()
