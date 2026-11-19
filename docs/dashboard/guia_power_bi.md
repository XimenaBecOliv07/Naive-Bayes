# Guía de uso del Dashboard Naive Bayes

## 1. Descripción general

El dashboard de Business Intelligence permite analizar la calidad del vino y consultar los resultados del modelo de clasificación Naive Bayes.

Su finalidad es apoyar al área de calidad en la identificación de lotes que podrían presentar baja calidad, analizar sus características fisicoquímicas y consultar el desempeño del modelo de clasificación.

El reporte contiene cinco páginas: una portada y cuatro páginas de análisis.

## 2. Herramientas y archivos de entrada

**Herramienta:** Microsoft Power BI Desktop (Windows).

**Archivos utilizados:**

| Archivo | Descripción |
|---|---|
| `data/processed/predicciones.csv` | Contiene las variables fisicoquímicas, la calidad real, la predicción del modelo, la probabilidad y el indicador de riesgo de cada lote. |
| `data/processed/metricas_modelo.csv` | Contiene las métricas de evaluación del modelo Naive Bayes. |

### Tablas utilizadas en Power BI

| Tabla | Descripción |
|---|---|
| `Vinos` | Contiene información general de los vinos, como calidad y características fisicoquímicas. |
| `predicciones` | Contiene los registros de los lotes utilizados para analizar las predicciones, los aciertos y los riesgos. |
| `metricas_modelo` | Contiene las métricas de evaluación del modelo, como accuracy, precisión, recall y F1. |

## 3. Medidas y cálculos DAX

Las siguientes medidas corresponden a los cálculos identificados en el reporte de Power BI.

### 3.1 Métricas del modelo

Estas medidas consultan los valores almacenados en la tabla `metricas_modelo`.

**Accuracy base**

```DAX
Accuracy base =
CALCULATE(
    MAX(metricas_modelo[valor]),
    metricas_modelo[metrica] = "accuracy_linea_base"
)
```

**Accuracy modelo**

```DAX
Accuracy modelo =
CALCULATE(
    MAX(metricas_modelo[valor]),
    metricas_modelo[metrica] = "accuracy"
)
```

**F1 modelo**

```DAX
F1 modelo =
CALCULATE(
    MAX(metricas_modelo[valor]),
    metricas_modelo[metrica] = "f1_macro"
)
```

**Precision modelo**

```DAX
Precision modelo =
CALCULATE(
    MAX(metricas_modelo[valor]),
    metricas_modelo[metrica] = "precision_macro"
)
```

**Recall modelo**

```DAX
Recall modelo =
CALCULATE(
    MAX(metricas_modelo[valor]),
    metricas_modelo[metrica] = "recall_macro"
)
```

### 3.2 Indicadores generales de calidad

**Calidad promedio**

```DAX
Calidad promedio =
AVERAGE(Vinos[quality])
```

**Lotes buenos**

```DAX
Lotes buenos =
CALCULATE(
    COUNTROWS(Vinos),
    Vinos[quality] >= 6
)
```

**Lotes malos**

```DAX
Lotes malos =
CALCULATE(
    COUNTROWS(Vinos),
    Vinos[quality] <= 5
)
```

**Total de lotes**

```DAX
Total de lotes =
COUNTROWS(Vinos)
```

### 3.3 Exploración de lotes

**Total lotes explorador**

```DAX
Total lotes explorador =
COUNTROWS(predicciones)
```

Esta medida permite contar los registros de la tabla de predicciones. El conjunto contiene 1,359 registros.

**Promedio de Recuento de quality por alcohol**

```DAX
Promedio de Recuento de quality por alcohol =
AVERAGEX(
    KEEPFILTERS(VALUES('Vinos'[alcohol])),
    CALCULATE(COUNTA('Vinos'[quality]))
)
```

Este cálculo permite analizar el recuento de registros de calidad agrupados por los valores de alcohol.

### 3.4 Indicador de riesgo

La tabla `predicciones` contiene la columna `lote_en_riesgo`, que identifica los registros clasificados como lotes en riesgo.

Esta columna se utiliza para analizar y filtrar los lotes que requieren atención.

**Nota:** `lote_en_riesgo` es una columna de datos, no una medida DAX.

## 4. Organización del dashboard

El reporte está organizado en cinco páginas:

### Página 1. Naive Bayes

Es la portada del dashboard. Presenta la identidad del proyecto y sirve como entrada al reporte.

### Página 2. Resumen ejecutivo

Presenta una visión general de los datos de calidad del vino mediante indicadores y visualizaciones que permiten identificar el comportamiento general de los lotes.

### Página 3. Perfil fisicoquímico

Permite explorar las características fisicoquímicas del vino, como alcohol, acidez, densidad y otros componentes relacionados con la calidad.

### Página 4. Desempeño del modelo

Presenta los resultados de evaluación del clasificador Naive Bayes mediante métricas como accuracy, precision, recall y F1.

También permite analizar la diferencia entre el modelo y la línea base.

### Página 5. Explorador de lotes

Permite consultar los registros individuales de las predicciones, analizar la clasificación obtenida y reconocer los lotes identificados como riesgo.

## 5. Resultados de evaluación

De acuerdo con el archivo `metricas_modelo.csv`, los resultados del modelo son:

| Métrica | Resultado |
|---|---:|
| Accuracy base | 52.94 % |
| Accuracy modelo | 75.00 % |
| Precision macro | 74.92 % |
| Recall macro | 74.96 % |
| F1 macro | 74.93 % |

El modelo obtuvo un accuracy de 75.00 %, superior al 52.94 % de la línea base.

**Importante:** las métricas anteriores corresponden a la evaluación del conjunto de prueba. La tabla `predicciones` contiene 1,359 registros de predicciones por validación cruzada, por lo que sus resultados no deben confundirse con las métricas del conjunto de prueba.

## 6. Interacción y uso del reporte

El usuario puede utilizar las visualizaciones y los filtros disponibles en las páginas para explorar la información.

Se recomienda:

1. Consultar primero el resumen ejecutivo para conocer el comportamiento general de los datos.
2. Explorar el perfil fisicoquímico para identificar características relacionadas con la calidad.
3. Revisar las métricas para conocer el desempeño del modelo Naive Bayes.
4. Utilizar el explorador de lotes para consultar las predicciones y los registros identificados como riesgo.

Las tarjetas e indicadores permiten consultar los resultados generales, mientras que las gráficas y tablas facilitan la comparación y exploración de los datos.

## 7. Archivos de entrega y evidencias

Los entregables de esta fase se encuentran en la carpeta `docs/dashboard/`.

| Archivo | Descripción |
|---|---|
| `dashboard_vino.pbix` | Archivo del dashboard de Power BI. |
| `pagina1_resumen.png` | Evidencia de la página de resumen ejecutivo. |
| `pagina2_quimico.png` | Evidencia del perfil fisicoquímico. |
| `pagina3_modelo.png` | Evidencia del desempeño del modelo. |
| `pagina4_explorador.png` | Evidencia del explorador de lotes. |
| `guia_power_bi.md` | Documento con la descripción, medidas y uso del dashboard. |

## 8. Conclusión

El dashboard integra los datos de calidad del vino y los resultados del modelo Naive Bayes en un reporte interactivo de Power BI.

Su implementación permite consultar indicadores generales, explorar las características fisicoquímicas, evaluar el desempeño del clasificador y analizar los lotes identificados como riesgo.

De esta manera, se facilita la interpretación de los resultados del modelo y se proporciona información útil para apoyar el análisis de calidad del vino.