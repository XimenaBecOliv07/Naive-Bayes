# Guía fase 3B: Modelo Naive Bayes, evaluación y optimización

| | |
|---|---|
| **Responsable** | Octavio |
| **Rama** | `octavio-fase3-evaluacion` |
| **Puedes empezar** | Desde el inicio, con el CSV crudo y el mismo renombrado de columnas que Pamela |
| **Dependes de** | Pamela (CSV limpio) |
| **Dependen de ti** | Braulio (configuración final del modelo), Ximena (`metricas_modelo.csv`) y Fátima (resultados para la presentación) |
| **Trabajas en pareja con** | Braulio (fase 3A): él construye y entrena, tú mides y optimizas |
| **Revisa tu PR** | Braulio |
| **Tus archivos** | `scripts/fase3_evaluacion.py`, `data/processed/metricas_modelo.csv`, `docs/fase3_evaluacion.md`, `docs/figuras/fase3_*.png` |

> Esta guía no te da el código. Te da el contexto, los conceptos, la documentación y pistas para que lo resuelvas tú. Las pistas están ocultas: ábrelas solo si te atoras, empezando por la primera.

---

## 1. Contexto

Entrenar un modelo es fácil; saber si de verdad funciona es lo difícil. Un accuracy de 75 % no significa nada si no sabes contra qué compararlo, si lo mediste con datos que el modelo ya había visto o si elegiste la configuración mirando el conjunto de prueba.

Tu fase responde dos preguntas: **¿qué tan bueno es el modelo?** y **¿cómo se mejora sin hacer trampa con los datos?** Para que tus resultados sean comparables con los de Braulio, usen la misma división: 80 % entrenamiento y 20 % prueba, estratificada, con `random_state=42`. Al final decides la configuración del modelo final y se la pasas a Braulio para que genere las predicciones del dashboard.

## 2. Objetivo general

Evaluar y optimizar el clasificador `GaussianNB` con métricas adecuadas, validación cruzada y una línea base, y decidir la configuración del modelo final sin fuga de datos.

## 3. Objetivos específicos

1. Definir una línea base para comprobar que el modelo realmente aprende.
2. Calcular e interpretar accuracy, precision, recall, F1 y la matriz de confusión.
3. Aplicar validación cruzada estratificada de 5 pliegues sobre el conjunto de entrenamiento.
4. Seleccionar variables y ajustar `var_smoothing` usando solo datos de entrenamiento.
5. Comparar las configuraciones, decidir el modelo final y exportar `metricas_modelo.csv`.

## 4. Entradas y salidas

| | Archivo |
|---|---|
| **Entrada** | `data/processed/winequality-red-limpio.csv` (Pamela) |
| **Salida** | `scripts/fase3_evaluacion.py` |
| **Salida** | `data/processed/metricas_modelo.csv`: columnas `metrica` y `valor` según el [contrato de datos](../README.md#6-contrato-de-datos) |
| **Salida** | `docs/fase3_evaluacion.md`: métricas, comparación y decisión del modelo final |
| **Salida** | `docs/figuras/fase3_matriz_confusion.png` y `docs/figuras/fase3_comparacion_modelos.png` |
| **Salida** | Mensaje `[MODELO]` por WhatsApp para Braulio con las variables finales y el `var_smoothing` |

## 5. Conceptos que debes investigar

| Concepto | Pregunta que debes poder responder |
|---|---|
| Línea base | ¿Qué accuracy obtiene un modelo "tonto" que siempre predice la clase más frecuente? ¿Por qué hay que superarlo? |
| Matriz de confusión | ¿Qué son los verdaderos y falsos positivos y negativos? ¿Qué error le cuesta más a la bodega? |
| Precision y recall | ¿Cuál es la diferencia? ¿Cuándo importa más cada una? |
| F1 macro | ¿Por qué se usa el promedio *macro* y no solo el accuracy? |
| Validación cruzada | ¿Por qué una sola división train/test puede engañar? |
| Fuga de datos en la selección de variables | ¿Por qué elegir variables mirando el conjunto de prueba invalida el resultado? |
| Hiperparámetros | ¿Qué controla `var_smoothing` en `GaussianNB`? |
| Colinealidad | ¿Por qué quitar variables correlacionadas entre sí puede ayudar a Naive Bayes? |

**Fuentes:**
- Evaluación de modelos en scikit-learn: https://scikit-learn.org/stable/modules/model_evaluation.html
- Validación cruzada: https://scikit-learn.org/stable/modules/cross_validation.html
- Errores comunes y fuga de datos: https://scikit-learn.org/stable/common_pitfalls.html

## 6. Herramientas

| Necesitas... | Investiga |
|---|---|
| Línea base | [`DummyClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.dummy.DummyClassifier.html) con `strategy="most_frequent"` |
| Métricas | [`accuracy_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html), [`precision_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html), [`recall_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html), [`f1_score`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html) (parámetro `average`) |
| Matriz de confusión | [`ConfusionMatrixDisplay.from_predictions`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html) |
| Validación cruzada | [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html) y [`cross_val_score`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html) con `scoring="f1_macro"` |
| Ajuste de hiperparámetros | [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) y [`numpy.logspace`](https://numpy.org/doc/stable/reference/generated/numpy.logspace.html) |
| Tabla comparativa | Un `pandas.DataFrame` construido a partir de diccionarios |

## 7. Ruta de trabajo

### Paso 1: Crea tu rama y acuerda la división con Braulio

Sigue la [sección 5 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#5-git-y-github). Mientras llega el CSV limpio, trabaja con el crudo aplicando el mismo renombrado de columnas y las mismas clases del contrato de datos.

### Paso 2: La línea base

Antes de evaluar Naive Bayes, mide cuánto acierta un clasificador que siempre predice la clase mayoritaria. Ese es el número que hay que superar.

<details>
<summary>Pista</summary>

`DummyClassifier` se entrena y se usa igual que cualquier modelo: `fit` con entrenamiento y `predict` con prueba. Ignora por completo los valores de `X`.
</details>

### Paso 3: Métricas de un modelo

Escribe una función que, dado un objetivo y una lista de variables, divida los datos, entrene el pipeline (estandarización + `GaussianNB`), prediga sobre prueba y devuelva accuracy, precision, recall y F1 macro, además del F1 de validación cruzada sobre entrenamiento.

<details>
<summary>Pista 1</summary>

La validación cruzada se aplica **solo** sobre `X_train` y `y_train`. El conjunto de prueba se reserva para la medición final.
</details>

<details>
<summary>Pista 2</summary>

Haz que la función devuelva un diccionario. Varios diccionarios se convierten fácilmente en un DataFrame para la tabla comparativa.
</details>

### Paso 4: Selección de variables sin trampa

Ordena las variables según qué tan correlacionadas están con `quality`, **calculándolo solo con el conjunto de entrenamiento**. Después prueba quedarte con las mejores 3, 5, 7, 9 y 11, y compara el F1 de validación cruzada de cada opción.

<details>
<summary>Pista 1</summary>

La correlación puede ser negativa y aun así muy informativa (piensa en la acidez volátil). Ordena por el **valor absoluto**.
</details>

<details>
<summary>Pista 2</summary>

Tu `X_train` no incluye `quality`. Para correlacionar necesitas unirla de nuevo usando el índice de `X_train`. Investiga `DataFrame.join` o `df.loc[X_train.index, ...]`.
</details>

<details>
<summary>Pista 3</summary>

Elige el número de variables según el F1 de **validación cruzada**, nunca según el resultado sobre prueba.
</details>

### Paso 5: Ajusta `var_smoothing`

Con las variables elegidas, busca el mejor `var_smoothing` en una cuadrícula de valores, también con validación cruzada sobre entrenamiento.

<details>
<summary>Pista 1</summary>

Para referirte a un parámetro de un paso del pipeline, `GridSearchCV` usa el formato `nombrepaso__parametro`, con doble guion bajo.
</details>

<details>
<summary>Pista 2</summary>

`var_smoothing` se mueve en órdenes de magnitud. Una cuadrícula lineal (0.1, 0.2, 0.3...) no sirve; investiga `numpy.logspace`.
</details>

### Paso 6: Comparación y modelo final

Construye una tabla con la línea base, el modelo de 3 clases, el binario con 11 variables y el binario optimizado. Grafica la matriz de confusión del modelo final y la comparación de configuraciones, y guarda ambas figuras en `docs/figuras/`.

### Paso 7: Comunica y exporta

1. Exporta `metricas_modelo.csv` con las métricas del modelo final sobre prueba y el accuracy de la línea base.
2. Envía a Braulio el mensaje `[MODELO]` con las variables finales y el `var_smoothing`.
3. Documenta en `docs/fase3_evaluacion.md` las métricas, la tabla comparativa, la decisión del modelo final y su interpretación para la bodega.

### Paso 8: Commits y pull request

Al hacer merge, avisa con `[MERGE]` a Ximena y a Fátima.

### Paso 9: Tu sección del notebook (turno 4)

Sigue la [sección 6 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#6-notebook-integrador-por-turnos).

## 8. Criterios de aceptación

Los valores de referencia son aproximados: pueden variar ligeramente según la versión de scikit-learn.

- [ ] La línea base da un accuracy cercano a **0.53**.
- [ ] El modelo final supera claramente a la línea base y queda alrededor de **0.75** de accuracy y F1 macro.
- [ ] La selección de variables y el ajuste de `var_smoothing` usan **solo** datos de entrenamiento.
- [ ] `metricas_modelo.csv` tiene las 5 filas del contrato de datos.
- [ ] Las dos figuras están en `docs/figuras/` con prefijo `fase3_`.
- [ ] Braulio recibió la configuración final y `predicciones.csv` se generó con ella.

## 9. Preparación para la defensa (minutos 17 a 21)

Debes poder responder sin leer:
- ¿Qué es la línea base y por qué superarla demuestra que el modelo aprende?
- Explica la matriz de confusión del modelo final: ¿qué errores comete y cuál es más costoso para la bodega?
- ¿Por qué usaron F1 macro además del accuracy?
- ¿Cómo evitaron la fuga de datos al seleccionar variables y ajustar hiperparámetros?
- ¿Por qué el modelo binario supera al de 3 clases?
- ¿Por qué usar menos variables mejoró (o no empeoró) el modelo?
- ¿Por qué el accuracy no es más alto?
