# Fase 3A: Entrenamiento del Modelo Gaussian Naive Bayes

**Responsable:** Braulio Herrera Peña  
**Rama:** `braulio-fase3-entrenamiento`  
**Archivos generados:** `scripts/fase3_entrenamiento.py`, `data/processed/predicciones.csv`, `docs/fase3_entrenamiento.md`

## 1. Fundamento teórico: Teorema de Bayes

El clasificador Naive Bayes estima la probabilidad de que un lote de vino pertenezca a una clase de calidad $C_k$ (por ejemplo, `bueno` o `malo`) a partir de su vector de propiedades fisicoquímicas $\mathbf{x} = (x_1, x_2, \dots, x_d)$, aplicando el teorema de Bayes:

$$P(C_k \mid \mathbf{x}) = \frac{P(C_k) \, P(\mathbf{x} \mid C_k)}{P(\mathbf{x})}$$

Cada componente tiene una interpretación directa en la bodega:
- **Probabilidad a priori $P(C_k)$:** Es la frecuencia histórica de cada clase en los datos de entrenamiento antes de observar el análisis químico del lote (en los 1,359 lotes limpios: 52.9 % `bueno` y 47.1 % `malo`).
- **Verosimilitud $P(\mathbf{x} \mid C_k)$:** Mide qué tan probable es observar esa combinación específica de acidez, alcohol, sulfatos y demás variables asumiendo que el lote pertenece a la clase $C_k$.
- **Evidencia $P(\mathbf{x})$:** Factor de normalización constante para todas las clases, que garantiza que las probabilidades sumen 1.
- **Probabilidad a posteriori $P(C_k \mid \mathbf{x})$:** Probabilidad final que entrega el modelo (`prob_bueno`) para decidir si el lote está en riesgo o no.

## 2. El supuesto "ingenuo" de independencia condicional

Estimar la distribución conjunta $P(x_1, x_2, \dots, x_d \mid C_k)$ requeriría una cantidad exponencial de datos. Naive Bayes simplifica este cálculo asumiendo que todas las variables fisicoquímicas son **condicionalmente independientes entre sí** dada la clase $C_k$:

$$P(\mathbf{x} \mid C_k) = \prod_{j=1}^{d} P(x_j \mid C_k)$$

**¿Se cumple este supuesto en el vino tinto?**  
No se cumple estrictamente. En química enológica existen colinealidades naturales:
- `fixed_acidity`, `citric_acid`, `density` y `ph` están estrechamente relacionadas por el equilibrio ácido-base y la densidad del mosto.
- `free_sulfur_dioxide` es una fracción directa de `total_sulfur_dioxide`.

Cuando existen variables fuertemente correlacionadas, Naive Bayes pondera dos veces la misma señal química y distorsiona las probabilidades. Por ello, seleccionar un subconjunto de variables sin redundancia en el Experimento 3 mejora el desempeño del clasificador.

## 3. Elección de `GaussianNB` y parámetros aprendidos

Dentro de las variantes de Naive Bayes disponibles en `scikit-learn`, se seleccionó `GaussianNB` por la naturaleza matemática de los datos:
- **`GaussianNB`:** Diseñado para variables continuas reales (como `alcohol`, `ph`, `density`, `volatile_acidity`).
- **`MultinomialNB`:** Diseñado para conteos discretos (como frecuencias de palabras en texto); no admite valores continuos estandarizados con números negativos.
- **`BernoulliNB`:** Diseñado para indicadores binarios (presencia/ausencia 0 o 1), lo que destruiría la información cuantitativa del laboratorio.

Durante el método `fit`, `GaussianNB` asume que cada variable $x_j$ dentro de cada clase $C_k$ sigue una distribución normal (campana de Gauss) y aprende únicamente **dos parámetros por variable y clase**: la media muestral ($\mu_{jk}$) y la varianza muestral ($\sigma^2_{jk}$):

$$P(x_j \mid C_k) = \frac{1}{\sqrt{2\pi\sigma^2_{jk}}} \exp\left(-\frac{(x_j - \mu_{jk})^2}{2\sigma^2_{jk}}\right)$$

El hiperparámetro `var_smoothing` suma una fracción de la mayor varianza observada a todas las varianzas ($\sigma^2_{jk} + \epsilon$) para garantizar estabilidad numérica y suavizar las fronteras de decisión.

## 4. Diseño del Pipeline y prevención de fuga de datos

Para asegurar una evaluación honesta y reproducible en conjunto con la Fase 3B, se aplicaron tres controles:
1. **División estratificada 80/20 (`random_state=42`):** Separa los 1,359 lotes en **1,087 de entrenamiento** y **272 de prueba**. El parámetro `stratify=y` garantiza que ambos subconjuntos conserven exactamente la misma proporción de clases que el dataset completo.
2. **Exclusión de variables objetivo en `X`:** Se retiraron `quality`, `calidad_bin` y `calidad_3` de la matriz predictora para evitar que el modelo lea la respuesta directamente.
3. **Encapsulamiento en `Pipeline([("scaler", StandardScaler()), ("nb", GaussianNB())])`:** Si se estandarizara todo el dataset antes de dividir, la media y desviación estándar de `StandardScaler` incluirían información del conjunto de prueba (*data leakage*). Dentro del `Pipeline`, `StandardScaler` calcula sus parámetros exclusivamente sobre `X_train` al entrenar y solo transforma `X_test` al evaluar (además de hacer lo mismo dentro de cada pliegue de la validación cruzada).

## 5. Resultados de los experimentos de entrenamiento

| Experimento | Variable objetivo | Variables predictoras | `var_smoothing` | Accuracy (prueba) | F1 Macro (prueba) |
|---|---|---|---:|---:|---:|
| 1. Tres clases | `calidad_3` (`baja`, `media`, `alta`) | 11 fisicoquímicas | `1e-9` | 0.5809 | 0.5596 |
| 2. Binario completo | `calidad_bin` (`bueno`, `malo`) | 11 fisicoquímicas | `1e-9` | 0.7353 | 0.7346 |
| 3. Binario final | `calidad_bin` (`bueno`, `malo`) | 3 (`alcohol`, `volatile_acidity`, `sulphates`) | `1.0` | **0.7500** | **0.7493** |

**Interpretación técnica:**
- En el **Experimento 1 (3 clases)** el desempeño cae a `0.5809` de accuracy y `0.5596` de F1 macro porque la clase `media` (`quality == 6`, 107 lotes en prueba) comparte propiedades químicas intermedias con `baja` y `alta`, mientras que `alta` (`quality >= 7`, solo 37 lotes en prueba) sufre un fuerte desbalance que limita su F1 a `0.4932`.
- En el **Experimento 2 (binario con 11 variables)**, al plantear el problema de negocio como detección de lotes en riesgo (`malo` $\le 5$ vs. `bueno` $\ge 6$), el accuracy sube a `0.7353` y el F1 macro a `0.7346`, equilibrando el desempeño entre ambas clases.
- En el **Experimento 3 (binario final con configuración de Fase 3B)**, al conservar únicamente las 3 variables más informativas y con menor colinealidad (`alcohol`, `volatile_acidity`, `sulphates`) junto con `var_smoothing=1.0`, el desempeño alcanza **0.7500 de accuracy** y **0.7493 de F1 macro**, confirmando que eliminar variables redundantes ayuda a respetar el supuesto de independencia de Naive Bayes.

## 6. Generación de predicciones honestas para el Dashboard (`predicciones.csv`)

El dashboard de Power BI (Fase 4) requiere una predicción (`y_pred`) y una probabilidad (`prob_bueno`) para cada uno de los **1,359 lotes**. Entrenar un modelo con los 1,359 lotes y predecir sobre esos mismos lotes produciría métricas artificialmente infladas porque el modelo evaluaría datos que ya memorizó.

Para evitarlo, se utilizó `cross_val_predict` con `StratifiedKFold(n_splits=5, shuffle=True, random_state=42)` y `method="predict_proba"` sobre el modelo final (3 variables y `var_smoothing=1.0`):
- El dataset se divide en 5 pliegues estratificados; cada lote es predicho únicamente por el pipeline entrenado con los 4 pliegues restantes.
- Se identificó el índice de la clase `"bueno"` mediante el atributo `classes_` del clasificador para extraer `prob_bueno` y se asignó `y_pred` a la clase con mayor probabilidad (`np.argmax`).
- Se exportó `data/processed/predicciones.csv` con **1,359 filas y 20 columnas** (las 14 del CSV limpio más `id_lote`, `y_real`, `y_pred`, `prob_bueno`, `acierto` y `lote_en_riesgo`), obteniendo un accuracy global de validación cruzada de **0.7292** y **676 lotes detectados en riesgo**.
