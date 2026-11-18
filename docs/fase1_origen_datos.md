# Fase 1: Origen y exploración de datos

| | |
|---|---|
| **Responsable** | Mateo |
| **Proyecto** | Predicción de la calidad del vino tinto con Naive Bayes |
| **Materia** | Ingeniería del Conocimiento, grupo 219900 |
| **Script** | `scripts/fase1_exploracion.py` |
| **Figura** | `docs/figuras/fase1_distribucion_quality.png` |

## 1. Procedencia

| Concepto | Valor |
|---|---|
| Dataset | *Wine Quality*, variante de vino tinto |
| Repositorio | UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/186/wine+quality |
| Autores | Paulo Cortez, António Cerdeira, Fernando Almeida, Telmo Matos y Joaquim Reis |
| Año | 2009 |
| Origen de las muestras | Vino tinto *vinho verde* del norte de Portugal |
| Archivo en el repositorio | `data/raw/winequality-red.csv` (solo lectura) |

Cada fila es un lote de vino. Las primeras 11 columnas son mediciones de laboratorio (pruebas fisicoquímicas) y la última, `quality`, es la calificación sensorial: cada muestra la evaluaron al menos tres catadores expertos en una escala de 0 a 10 y se registró la mediana de sus calificaciones.

**Referencia:**
Cortez, P., Cerdeira, A., Almeida, F., Matos, T., y Reis, J. (2009). Modeling wine preferences by data mining from physicochemical properties. *Decision Support Systems, 47*(4), 547-553. https://doi.org/10.1016/j.dss.2009.05.016

### Por qué estos datos sirven para el problema de la bodega

Las mediciones fisicoquímicas se toman en el laboratorio durante y después de la fermentación, mucho antes de la cata final. Si esas mediciones contienen información sobre la calidad, un modelo puede **anticipar** qué lotes tienen riesgo de salir mal, cuando todavía hay tiempo de revisarlos.

## 2. Resumen técnico

Cifras obtenidas al ejecutar `python scripts/fase1_exploracion.py` desde la raíz del proyecto:

| Concepto | Valor |
|---|---|
| Filas (lotes) | 1,599 |
| Columnas | 12 (11 predictoras + 1 objetivo) |
| Tipos de datos | 11 columnas decimales (`float64`) y `quality` entera (`int64`) |
| Valores nulos | 0 |
| Filas duplicadas | 240 |
| Filas que quedan sin duplicados | 1,359 |

### Distribución de `quality`

| Calificación | Lotes | Porcentaje |
|:---:|---:|---:|
| 3 | 10 | 0.63% |
| 4 | 53 | 3.31% |
| 5 | 681 | 42.59% |
| 6 | 638 | 39.90% |
| 7 | 199 | 12.45% |
| 8 | 18 | 1.13% |
| **Total** | **1,599** | **100%** |

Aunque la escala va de 0 a 10, en los datos solo aparecen calificaciones del 3 al 8. Las calificaciones 5 y 6 juntas suman **1,319 lotes (82.49%)**.

![Distribución de la calidad del vino tinto](figuras/fase1_distribucion_quality.png)

### Estadísticas descriptivas

| Variable | Media | Mediana | Desv. estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|---:|
| fixed acidity | 8.320 | 7.900 | 1.741 | 4.600 | 15.900 |
| volatile acidity | 0.528 | 0.520 | 0.179 | 0.120 | 1.580 |
| citric acid | 0.271 | 0.260 | 0.195 | 0.000 | 1.000 |
| residual sugar | 2.539 | 2.200 | 1.410 | 0.900 | 15.500 |
| chlorides | 0.087 | 0.079 | 0.047 | 0.012 | 0.611 |
| free sulfur dioxide | 15.875 | 14.000 | 10.460 | 1.000 | 72.000 |
| total sulfur dioxide | 46.468 | 38.000 | 32.895 | 6.000 | 289.000 |
| density | 0.997 | 0.997 | 0.002 | 0.990 | 1.004 |
| pH | 3.311 | 3.310 | 0.154 | 2.740 | 4.010 |
| sulphates | 0.658 | 0.620 | 0.170 | 0.330 | 2.000 |
| alcohol | 10.423 | 10.200 | 1.066 | 8.400 | 14.900 |
| quality | 5.636 | 6.000 | 0.808 | 3.000 | 8.000 |

Lo que se lee en esta tabla:
- Las variables están en **escalas muy distintas**: `density` casi no varía (desviación de 0.002), mientras que `total sulfur dioxide` va de 6 a 289.
- En varias variables la media es mayor que la mediana y el máximo está muy lejos del resto (`residual sugar`, `chlorides`, `total sulfur dioxide`, `sulphates`). Eso indica **valores extremos** hacia arriba.
