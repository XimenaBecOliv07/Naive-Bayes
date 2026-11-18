# Guía fase 3A: Modelo Naive Bayes, entrenamiento

| | |
|---|---|
| **Responsable** | Braulio |
| **Rama** | `braulio-fase3-entrenamiento` |
| **Puedes empezar** | Desde el inicio, con el CSV crudo y el mismo renombrado de columnas que Pamela |
| **Dependes de** | Pamela (CSV limpio) y Octavio (configuración del modelo final) |
| **Dependen de ti** | Ximena necesita `predicciones.csv` para el dashboard |
| **Trabajas en pareja con** | Octavio (fase 3B): él evalúa y optimiza, tú construyes y entrenas |
| **Revisa tu PR** | Octavio |
| **Tus archivos** | `scripts/fase3_entrenamiento.py`, `data/processed/predicciones.csv`, `docs/fase3_entrenamiento.md` |

> Esta guía no te da el código. Te da el contexto, los conceptos, la documentación y pistas para que lo resuelvas tú. Las pistas están ocultas: ábrelas solo si te atoras, empezando por la primera.

---

## 1. Contexto

Tu fase es el corazón técnico del proyecto: construir el clasificador. Vas a usar **Naive Bayes**, un modelo que aplica el teorema de Bayes para calcular, a partir de las mediciones de un lote, la probabilidad de que sea bueno o malo.

Trabajas en pareja con Octavio. Para que sus resultados sean comparables, **acuerden desde el principio** la misma división de datos: 80 % entrenamiento y 20 % prueba, estratificada, con `random_state=42`. Tú construyes el pipeline y los experimentos; Octavio mide qué tan buenos son y decide la configuración final. Con esa configuración tú generas las predicciones del dashboard.

## 2. Objetivo general

Implementar el clasificador `GaussianNB` dentro de un pipeline reproducible y generar las predicciones de calidad para los 1,359 lotes.

## 3. Objetivos específicos

1. Explicar el teorema de Bayes y el supuesto de independencia condicional de Naive Bayes.
2. Construir un `Pipeline` que estandarice las variables y entrene `GaussianNB` sin fuga de datos.
3. Entrenar tres experimentos: 3 clases con 11 variables, binario con 11 variables y binario con las variables seleccionadas por Octavio.
4. Generar predicciones y probabilidades honestas para todos los lotes y exportar `predicciones.csv`.

## 4. Entradas y salidas

| | Archivo |
|---|---|
| **Entrada** | `data/processed/winequality-red-limpio.csv` (Pamela) |
| **Entrada** | Configuración final del modelo: variables y `var_smoothing` (Octavio, por WhatsApp con `[MODELO]` y en `docs/fase3_evaluacion.md`) |
| **Salida** | `scripts/fase3_entrenamiento.py` |
| **Salida** | `data/processed/predicciones.csv`: columnas según el [contrato de datos](../README.md#6-contrato-de-datos) |
| **Salida** | `docs/fase3_entrenamiento.md`: fundamento teórico y descripción de los experimentos |

## 5. Conceptos que debes investigar

| Concepto | Pregunta que debes poder responder |
|---|---|
| Teorema de Bayes | ¿Qué son la probabilidad a priori, la verosimilitud y la probabilidad a posteriori? |
| Supuesto "ingenuo" | ¿Qué significa independencia condicional y por qué simplifica tanto el cálculo? |
| Variantes de Naive Bayes | ¿Por qué `GaussianNB` y no `MultinomialNB` ni `BernoulliNB` para estos datos? |
| Distribución normal | ¿Qué parámetros aprende `GaussianNB` de cada variable en cada clase? |
| Conjunto de entrenamiento y de prueba | ¿Por qué el modelo nunca debe ver los datos de prueba al entrenar? |
| Estratificación | ¿Qué garantiza `stratify` al dividir los datos? |
| Pipeline | ¿Cómo evita un pipeline la fuga de datos al estandarizar? |
| Predicción por validación cruzada | ¿Por qué no basta con predecir los 1,359 lotes con un modelo entrenado con todos ellos? |

**Fuentes:**
- Guía de Naive Bayes en scikit-learn: https://scikit-learn.org/stable/modules/naive_bayes.html
- Errores comunes y fuga de datos: https://scikit-learn.org/stable/common_pitfalls.html

## 6. Herramientas

| Necesitas... | Investiga |
|---|---|
| Dividir los datos | [`train_test_split`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html): parámetros `test_size`, `stratify`, `random_state` |
| Estandarizar | [`StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) |
| El clasificador | [`GaussianNB`](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html): métodos `fit`, `predict`, `predict_proba`, atributo `classes_`, parámetro `var_smoothing` |
| Encadenar pasos | [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) |
| Predicciones honestas para todos los lotes | [`cross_val_predict`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_predict.html) con [`StratifiedKFold`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html) |
| Reporte rápido de resultados | [`classification_report`](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html) |

## 7. Ruta de trabajo

### Paso 1: Crea tu rama y acuerda la división con Octavio

Sigue la [sección 5 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#5-git-y-github). Antes de programar, confirma con Octavio la división 80/20, estratificada, con `random_state=42`.

### Paso 2: Empieza sin esperar a Pamela

Mientras llega el CSV limpio, carga el crudo y aplica el mismo renombrado de columnas y la misma creación de `calidad_bin` y `calidad_3` (las reglas están en el contrato de datos). Cuando Pamela haga merge, cambias la ruta y borras ese código temporal.

### Paso 3: Construye el pipeline

Arma una función que devuelva un pipeline nuevo con dos pasos: estandarización y `GaussianNB`.

<details>
<summary>Pista 1</summary>

`Pipeline` recibe una lista de tuplas `(nombre, objeto)`. Los nombres los eliges tú y luego sirven para acceder a los parámetros de cada paso.
</details>

<details>
<summary>Pista 2</summary>

¿Por qué una **función** que crea el pipeline y no una sola variable reutilizada? Piensa qué pasa si entrenas el mismo objeto dos veces con datos distintos.
</details>

### Paso 4: Los tres experimentos

| Experimento | Objetivo (`y`) | Variables (`X`) |
|---|---|---|
| 1 | `calidad_3` | Las 11 fisicoquímicas |
| 2 | `calidad_bin` | Las 11 fisicoquímicas |
| 3 (final) | `calidad_bin` | Las que defina Octavio |

Para cada uno: divide, entrena con entrenamiento, predice sobre prueba e imprime un `classification_report`.

<details>
<summary>Pista 1</summary>

`X` debe tener **solo** las 11 variables fisicoquímicas. ¿Qué tres columnas del CSV limpio tienes que quitar? Si dejas alguna, el modelo "hace trampa".
</details>

<details>
<summary>Pista 2</summary>

Escribe una función que reciba `X`, `y` y un nombre de experimento, y que haga todo el proceso. Así la llamas tres veces en lugar de copiar y pegar el código.
</details>

### Paso 5: Predicciones para el dashboard

Ximena necesita una predicción y una probabilidad para **cada uno** de los 1,359 lotes. Si entrenas con todos los lotes y luego los predices, el modelo estaría prediciendo datos que ya vio y los resultados saldrían inflados. Usa validación cruzada para que cada lote lo prediga un modelo que no lo vio al entrenar.

Primero exporta una versión preliminar con las 11 variables. Cuando Octavio comparta la configuración final, vuelve a exportar con ella.

<details>
<summary>Pista 1</summary>

`cross_val_predict` acepta `method="predict_proba"`. El resultado es una matriz con una columna por clase.
</details>

<details>
<summary>Pista 2</summary>

¿Cuál de las columnas de probabilidad corresponde a `bueno`? Revisa el atributo `classes_` del modelo: el orden de las clases es el orden de las columnas.
</details>

<details>
<summary>Pista 3</summary>

Si ya tienes las probabilidades, la clase predicha es la de mayor probabilidad. Investiga `numpy.argmax`.
</details>

### Paso 6: Arma `predicciones.csv`

Parte de una copia del CSV limpio y agrega las columnas del contrato: `id_lote`, `y_real`, `y_pred`, `prob_bueno`, `acierto` y `lote_en_riesgo`.

### Paso 7: Documenta, haz commits y abre el pull request

En `docs/fase3_entrenamiento.md` explica con tus palabras el teorema de Bayes, el supuesto de independencia, por qué `GaussianNB`, el pipeline y los tres experimentos. Al hacer merge, avisa a Ximena con `[MERGE]`.

### Paso 8: Tu sección del notebook (turno 3)

Sigue la [sección 6 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#6-notebook-integrador-por-turnos).

## 8. Criterios de aceptación

Los valores de referencia son aproximados: pueden variar ligeramente según la versión de scikit-learn.

- [ ] El conjunto de prueba tiene **272 lotes** (20 % de 1,359).
- [ ] El experimento 1 (3 clases) da un accuracy cercano a **0.58**.
- [ ] El experimento 2 (binario, 11 variables) da un accuracy cercano a **0.74**.
- [ ] `predicciones.csv` tiene **1,359 filas** y las 20 columnas del contrato de datos.
- [ ] `prob_bueno` está entre 0 y 1, y `lote_en_riesgo` vale 1 exactamente cuando `y_pred` es `malo`.
- [ ] La versión final de `predicciones.csv` usa la configuración que definió Octavio.
- [ ] El script corre sin errores desde la raíz del proyecto.

## 9. Preparación para la defensa (minutos 13 a 17)

Debes poder responder sin leer:
- Escribe y explica el teorema de Bayes con las palabras "a priori", "verosimilitud" y "a posteriori".
- ¿Qué supone Naive Bayes y por qué se le llama "ingenuo"?
- ¿Se cumple ese supuesto en el vino? ¿Qué variables lo rompen?
- ¿Por qué `GaussianNB`?
- ¿Qué hace exactamente el pipeline y cómo evita la fuga de datos?
- ¿Por qué las predicciones del dashboard se generaron con validación cruzada?
