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

import pandas as pd

# Las rutas se calculan a partir de la ubicación de este archivo
# (scripts/ -> parents[1] es la raíz), así el script funciona sin importar
# desde qué carpeta se ejecute ni en qué computadora.
RAIZ = Path(__file__).resolve().parents[1]
RUTA_CSV = RAIZ / "data" / "raw" / "winequality-red.csv"


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


def main():
    df = pd.read_csv(RUTA_CSV)
    print(f"Archivo leído: {RUTA_CSV.relative_to(RAIZ)}")

    filas, columnas = describir_estructura(df)
    total_nulos, duplicados = revisar_nulos_y_duplicados(df)


if __name__ == "__main__":
    main()
