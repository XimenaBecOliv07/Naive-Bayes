# Guion Integral de Exposición Oral: Predicción de la Calidad del Vino Tinto con Naive Bayes

* **Materia:** Ingeniería del Conocimiento — Proyecto Final
* **Grupo:** 219900
* **Docente:** Ing. Rafael Hernández López
* **Fecha:** 26 de noviembre de 2026
* **Duración total:** 30 minutos (33 diapositivas)

## Integrantes del Equipo (6 Expositores)

* Octavio Becerril Olivares (`23281543`)
* Ximena Becerril Olivares (`22280357`)
* Fatima Monserrat Hernandez Tovar (`23281198`)
* Braulio Herrera Peña (`22280384`)
* Carlos Mateo Zamudio Mondragón (`23281532`)
* Pamela Espinoza Montiel (`22280354`)

---

## 1. Cronograma y Distribución de Tiempos (30 Minutos Totales)

| Bloque / Sección | Diapositivas | Tiempo Asignado | Acumulado | Enfoque Principal |
| :--- | :---: | :---: | :---: | :--- |
| **Apertura: Portada e Índice** | Diaps. 1 – 2 | 1 min 00 seg | 01:00 | Presentación del equipo, tema y ruta de exposición. |
| **01. Contexto Teórico** | Diaps. 3 – 7 | 3 min 00 seg | 04:00 | Introducción, problemática en bodega, objetivo general y 6 específicos. |
| **02. Origen del Dataset y Negocio** | Diaps. 8 – 13 | 4 min 00 seg | 08:00 | Dataset Vinho Verde, química del vino, auditoría (1,599 $\rightarrow$ 1,359) y balanceo. |
| **03. Procesamiento** | Diaps. 14 – 19 | 5 min 00 seg | 13:00 | Pipeline ETL, eliminación de duplicados, conservación de outliers y correlaciones. |
| **04. Modelo Naive Bayes, Entrenamiento** | Diaps. 20 – 23 | 4 min 30 seg | 17:30 | Teorema de Bayes, `GaussianNB`, pipeline anti-fuga, 3 experimentos y CV. |
| **05. Evaluación y Optimización** | Diaps. 24 – 27 | 5 min 00 seg | 22:30 | `DummyClassifier`, selección Top 3 variables, `var_smoothing`, matriz y límites. |
| **06. Dashboard Business Intelligence** | Diaps. 28 – 31 | 6 min 00 seg | 28:30 | Recorrido por las 4 vistas interactivas de Power BI y triaje operativo. |
| **07. Conclusión y Cierre** | Diaps. 32 – 33 | 1 min 30 seg | 30:00 | Síntesis ejecutiva de impacto analítico, operativo y cierre formal. |

---

## Apertura: Portada e Índice General
**Tiempo asignado:** 1 min 00 seg

### Diapositiva 1: Portada del Proyecto `[35 seg]`
* **Apoyo visual:** Título principal, nombres de los 6 integrantes, grupo `219900` y docente Ing. Rafael Hernández López.

> **Diálogo:**
> "Buenos días a todos y buen día, profesor Ing. Rafael Hernández López. Somos el equipo del grupo 219900 y hoy presentaremos nuestro proyecto final de Ingeniería del Conocimiento titulado: *'Predicción de la calidad del vino tinto con Naive Bayes'*."

### Diapositiva 2: Índice de la Presentación `[25 seg]`
* **Apoyo visual:** Ruta numerada del 01 al 07 (Contexto, Dataset, Procesamiento, Entrenamiento, Evaluación, Dashboard BI y Conclusión).

> **Diálogo:**
> "Para estructurar nuestra exposición de 30 minutos, dividimos el trabajo en siete bloques: comenzaremos con el contexto teórico y el problema de negocio; pasaremos por el origen y preprocesamiento de los datos; profundizaremos en el entrenamiento y optimización del modelo Naive Bayes; y cerraremos demostrando su aplicación en un tablero interactivo de Power BI junto con nuestras conclusiones."
>
> *(Nota de transición: Cede la palabra al expositor encargado del Bloque 01).*

---

## Bloque 01: Contexto Teórico
**Tiempo asignado:** 3 min 00 seg

### Diapositiva 3: Portada de Sección — Contexto Teórico `[10 seg]`
* **Apoyo visual:** Separador visual `01 Contexto teórico`.

> **Diálogo:**
> "Iniciamos con el primer bloque: el contexto teórico y la motivación industrial detrás de esta solución."

### Diapositiva 4: Introducción `[55 seg]`
* **Apoyo visual:** Texto introductorio e imagen de copa de vino en viñedo.

> **Diálogo:**
> "En la industria vitivinícola, evaluar la calidad de un lote mediante catas sensoriales tradicionales resulta altamente subjetivo, costoso y, sobre todo, tardío, ya que ocurre cuando el vino prácticamente está terminado. Sin embargo, durante la fermentación se realizan análisis fisicoquímicos rutinarios —como la acidez, el grado alcohólico o el pH— que contienen señales tempranas del resultado final.
>
> Por ello, en este proyecto desarrollamos un modelo predictivo basado en Gaussian Naive Bayes integrado directamente en un dashboard de Power BI, permitiendo que cualquier enólogo o responsable de calidad detecte lotes en riesgo sin necesidad de saber programar."

### Diapositiva 5: Problemática en la Bodega `[50 seg]`
* **Apoyo visual:** Descripción de pérdidas por variabilidad de calidad e imagen de barricas en bodega.

> **Diálogo:**
> "El problema concreto que resolvemos se sitúa en una bodega de vino tinto que enfrenta pérdidas económicas recurrentes debido a la variabilidad en la calidad de sus lotes tras la fermentación. Al depender únicamente de evaluaciones manuales posteriores, la bodega no logra detectar a tiempo las desviaciones químicas que originan lotes defectuosos, perdiendo la oportunidad de corregirlos antes del embotellado."

### Diapositiva 6: Objetivo General `[25 seg]`
* **Apoyo visual:** Enunciado central del objetivo del clasificador `Gaussian Naive Bayes` en Power BI.

> **Diálogo:**
> "Nuestro objetivo general es desarrollar un clasificador Gaussian Naive Bayes a partir de 11 variables fisicoquímicas, desplegado en Power BI, para detectar lotes de vino tinto en riesgo antes de su distribución."

### Diapositiva 7: Objetivos Específicos (1 al 6) `[40 seg]`
* **Apoyo visual:** Lista numerada de las 6 etapas metodológicas: Comprender, Preparar, Modelar, Evaluar, Visualizar y Comunicar.

> **Diálogo:**
> "Para lograrlo, establecimos seis objetivos específicos que guían todo el ciclo de vida del proyecto: primero, comprender y auditar las 12 variables del dataset; segundo, preparar y limpiar los datos definiendo clases reproducibles; tercero, entrenar y comparar distintas configuraciones de `GaussianNB`; cuarto, evaluar su desempeño sin fuga de datos frente a una línea base; quinto, visualizar indicadores accionables en Power BI; y sexto, comunicar tanto sus hallazgos como sus limitaciones."
>
> *(Nota de transición: Da paso al Bloque 02 sobre el dataset y el enfoque de negocio).*

---

## Bloque 02: Origen del Dataset y Problema de Negocio
**Tiempo asignado:** 4 min 00 seg

### Diapositiva 8: Portada de Sección — Origen del Dataset y Problema de Negocio `[10 seg]`
* **Apoyo visual:** Separador visual `02 Origen del Dataset y Problema de Negocio`.

> **Diálogo:**
> "Pasamos ahora al bloque dos, donde analizamos la fuente de información y cómo tradujimos el problema enológico a un problema de aprendizaje automático."

### Diapositiva 9: Origen de los Datos y Objetivo Analítico `[55 seg]`
* **Apoyo visual:** 3 tarjetas (*Entradas: 11 variables*, *Variable objetivo: quality 0–10*, *Valor para la bodega*) y dato base *Vinho Verde (Portugal)*.

> **Diálogo:**
> "Trabajamos con el dataset clásico de vino tinto Vinho Verde de Portugal, compuesto originalmente por 1,599 lotes evaluados. Como variables de entrada contamos con 11 mediciones fisicoquímicas objetivas de laboratorio —acidez, azúcares, sulfatos, alcohol, pH y densidad—. La variable objetivo, llamada `quality`, corresponde a la mediana de las calificaciones sensoriales otorgadas por catadores expertos en una escala de 0 a 10.
>
> El valor analítico para la bodega radica en anticipar esa nota sensorial usando únicamente la química del laboratorio."

### Diapositiva 10: ¿Qué miden las variables y cómo afectan al vino? `[55 seg]`
* **Apoyo visual:** Tres columnas: *Potenciadores de calidad*, *Indicadores de defecto/riesgo* y *Balance estructural*.

> **Diálogo:**
> "Desde el punto de vista enológico, agrupamos las 11 variables en tres roles: primero, los potenciadores de calidad, donde destacan el alcohol —que aporta cuerpo y estructura—, los sulfatos como conservantes antimicrobianos y el ácido cítrico que brinda frescura. Segundo, los indicadores de defecto, encabezados por la acidez volátil, que en exceso produce un olor y sabor avinagrado, junto con el exceso de cloruros o dióxido de azufre total. Y tercero, las variables de balance estructural como la acidez fija, el pH, el azúcar residual y la densidad."

### Diapositiva 11: Auditoría Inicial del Dataset `[45 seg]`
* **Apoyo visual:** 4 métricas grandes: `1,599` registros iniciales, `0` valores nulos, `240` filas duplicadas (`15%`) y `1,359` lotes únicos.

> **Diálogo:**
> "Al auditar la calidad de los datos crudos descubrimos cuatro hallazgos clave: el archivo contiene 1,599 registros y 12 columnas; tiene un 100 % de integridad sin valores nulos; sin embargo, detectamos 240 filas exactamente duplicadas, equivalentes al 15 % del total. Al depurarlas, nos quedamos con 1,359 lotes únicos reales sobre los cuales construimos nuestro análisis."

### Diapositiva 12: Desbalance de Clases y Decisión de Modelado `[1 min 00 seg]`
* **Apoyo visual:** Gráfico de barras de distribución original de `quality` (3 a 8) y reglas de reagrupación (`calidad_bin` y `calidad_3`).

> **Diálogo:**
> "Como muestra la gráfica de barras, la variable objetivo original presenta un fuerte desbalance: el 82.5 % de los vinos se concentra en las calificaciones intermedias 5 y 6, mientras que las clases extremas, como calidad 3 con 0.6 % y calidad 8 con 1.1 %, están prácticamente vacías, lo que impide entrenar un clasificador multiclase directo de seis niveles.
>
> Para resolverlo de forma alineada al negocio, definimos dos enfoques: una agrupación binaria llamada `calidad_bin` —dividiendo lotes malos de 5 o menos frente a buenos de 6 o más, logrando un balance casi perfecto de 47 % contra 53 %— y una agrupación de tres niveles llamada `calidad_3` para comparar el rendimiento."

### Diapositiva 13: Tabla Comparativa de Resultados por Enfoque (Vista Previa) `[15 seg]`
* **Apoyo visual:** Tabla resumen comparando Línea Base, 3 clases y enfoques Binarios.

> **Diálogo:**
> "Esta tabla adelanta cómo dicha decisión de reagrupación binaria resultó determinante para elevar la exactitud del modelo hasta el 75 %, como veremos a detalle en la etapa de modelado."
>
> *(Nota de transición: Cede la palabra al responsable del Bloque 03 — Procesamiento).*

---

## Bloque 03: Procesamiento
**Tiempo asignado:** 5 min 00 seg

### Diapositiva 14: Portada de Sección — Procesamiento `[10 seg]`
* **Apoyo visual:** Separador visual `03 Procesamiento`.

> **Diálogo:**
> "Continuamos con el tercer bloque: el preprocesamiento y contrato de datos ejecutado en nuestro pipeline."

### Diapositiva 15: Preprocesamiento y Contrato de Datos (Pipeline Horizontal) `[55 seg]`
* **Apoyo visual:** Flujo horizontal desde `CSV Crudo (1,599 x 12)` hasta `Dataset Limpio (1,359 x 14)` vía `fase2_preprocesamiento.py`.

> **Diálogo:**
> "Todo el flujo de limpieza se automatizó en el script `fase2_preprocesamiento.py` bajo un contrato de datos estricto. Partimos del archivo crudo de 1,599 filas por 12 columnas, estandarizamos los nombres y tipos de datos a formato decimal para las variables químicas y entero para la calidad, depuramos duplicados, conservamos los valores atípicos válidos y generamos las nuevas columnas objetivo, exportando un dataset limpio de 1,359 filas por 14 columnas."

### Diapositiva 16: Limpieza, Esquema y Tratamiento de Duplicados `[55 seg]`
* **Apoyo visual:** Auditoría de esquema, `0` nulos, eliminación de `240` duplicados y alerta roja sobre *Data Leakage*.

> **Diálogo:**
> "Un paso crítico de esta fase fue la eliminación de los 240 registros duplicados. Más allá de limpiar la base, eliminar duplicados es indispensable para evitar fuga de datos o *data leakage*: si un mismo lote duplicado cayera simultáneamente en el conjunto de entrenamiento y en el de prueba, el modelo memorizaría ese registro y nos reportaría una exactitud artificialmente inflada."

### Diapositiva 17: Análisis de Valores Atípicos (Outliers) `[1 min 05 seg]`
* **Apoyo visual:** 11 diagramas de caja (*boxplots*) por variable fisicoquímica y cintillo `SE CONSERVAN TODOS LOS ATÍPICOS`.

> **Diálogo:**
> "Al aplicar la regla estadística del rango intercuartílico en los 11 diagramas de caja, identificamos valores extremos principalmente en azúcar residual, con 126 casos, y cloruros, con 87. Sin embargo, tomamos la decisión fundamentada de conservar todos los valores atípicos por dos razones: primero, desde el criterio químico, todos caen dentro de rangos reales de laboratorio —por ejemplo, un pH entre 2.74 y 4.01—; y segundo, desde el negocio, detectar lotes químicos fuera de lo normal es precisamente el propósito de nuestro sistema de alerta."

### Diapositiva 18: Análisis de Correlaciones e Impacto en Naive Bayes `[1 min 15 seg]`
* **Apoyo visual:** Matriz de correlación de Pearson (*heatmap*), tabla Top 3 correlaciones con `quality` y alerta de colinealidad.

> **Diálogo:**
> "En la matriz de correlación de Pearson observamos dos fenómenos muy importantes. Primero, respecto a la calidad, las tres variables más influyentes son el alcohol con una correlación positiva de `+0.48`, la acidez volátil con una correlación negativa de `-0.40` y los sulfatos con `+0.25`.
>
> Segundo, detectamos correlaciones fuertes entre variables predictoras: por ejemplo, la acidez fija tiene una correlación de `-0.69` con el pH y de `+0.67` con la densidad y el ácido cítrico. Esto nos advierte desde ya sobre las limitaciones del supuesto de independencia de Naive Bayes y justifica filtrar variables redundantes más adelante."

### Diapositiva 19: Variables Objetivo y Regla Anti-Fuga de Datos `[40 seg]`
* **Apoyo visual:** Tabla de reglas de corte (`calidad_bin` y `calidad_3`) y regla crítica de exportación sin estandarizar.

> **Diálogo:**
> "Finalmente, exportamos el archivo limpio respetando una regla metodológica fundamental: los datos salen en sus unidades originales sin estandarizar. La estandarización con `StandardScaler` se aplicará únicamente dentro del Pipeline de entrenamiento en la siguiente fase para evitar cualquier contaminación estadística entre entrenamiento y prueba."
>
> *(Nota de transición: Cede la palabra al expositor del Bloque 04 — Entrenamiento del Modelo).*

---

## Bloque 04: Modelo Naive Bayes, Entrenamiento
**Tiempo asignado:** 4 min 30 seg

### Diapositiva 20: Portada de Sección — Modelo Naive Bayes, Entrenamiento `[10 seg]`
* **Apoyo visual:** Separador visual `04 Modelo Naive Bayes, entrenamiento`.

> **Diálogo:**
> "Entramos al cuarto bloque, dedicado al fundamento matemático y entrenamiento de nuestro clasificador."

### Diapositiva 21: Fundamento del Modelo: Clasificador Naive Bayes `[1 min 30 seg]`
* **Apoyo visual:** Fórmula del Teorema de Bayes $P(C_k \mid \mathbf{x})$, traducción de cada término al negocio y parámetros $(\mu, \sigma^2)$ de `GaussianNB`.

> **Diálogo:**
> "Para predecir la calidad del vino utilizamos el clasificador Naive Bayes, que aplica el teorema de Bayes para calcular la probabilidad a posteriori de que un lote sea bueno o malo dada su composición química. Cada término de la fórmula tiene un significado directo en la bodega: $P(C_k)$ es la frecuencia histórica de vinos buenos y malos; $P(\mathbf{x} \mid C_k)$ es la verosimilitud o perfil químico esperado para cada clase; y $P(C_k \mid \mathbf{x})$ es la probabilidad final que entregamos al usuario.
>
> Elegimos la variante `GaussianNB` porque nuestras variables son mediciones físicas continuas, de modo que el algoritmo aprende únicamente la media y la varianza de cada variable por clase asumiendo una campana de Gauss. Su mayor desafío es el supuesto 'ingenuo' de independencia condicional entre variables, razón por la cual eliminar colinealidades químicas mejora su rendimiento."

### Diapositiva 22: Arquitectura sin Fuga de Datos y Evolución de Experimentos `[1 min 40 seg]`
* **Apoyo visual:** Diagrama de 5 pasos de la arquitectura de entrenamiento y tabla comparativa de los Experimentos 1, 2 y 3.

> **Diálogo:**
> "Para garantizar resultados honestos, implementamos una arquitectura de cinco pasos: partimos de los 1,359 lotes limpios, aplicamos una división estratificada 80/20 dejando 1,087 lotes para entrenamiento y 272 bloqueados para prueba, y encapsulamos el escalamiento y el modelo dentro de un Pipeline para que la media y varianza se calculen exclusivamente sobre entrenamiento.
>
> Evaluamos tres experimentos progresivos: el Experimento 1, multiclase de tres niveles con 11 variables, obtuvo apenas 58.09 % de exactitud porque la clase media se confunde con los extremos. Al replantearlo como clasificación binaria en el Experimento 2, la exactitud saltó a 73.53 %. Finalmente, en el Experimento 3, al conservar únicamente las tres variables más informativas y sin redundancia —alcohol, acidez volátil y sulfatos—, alcanzamos un 75.00 % de exactitud y 74.93 % de F1 macro."

### Diapositiva 23: Salida del Modelo: Alimentando el Tablero de Decisiones `[1 min 10 seg]`
* **Apoyo visual:** KPIs de `predicciones.csv` (`1,359` lotes fuera de muestra, `621` lotes en riesgo, variable `prob_bueno`) y esquema de validación.

> **Diálogo:**
> "El tablero de Power BI requería una predicción para cada uno de los 1,359 lotes, pero predecir sobre los mismos datos con los que entrenamos inflaría artificialmente las métricas. Para resolverlo, aplicamos validación cruzada estratificada de 5 pliegues mediante `cross_val_predict`, logrando que cada lote fuera evaluado 100 % fuera de muestra.
>
> De este proceso exportamos el archivo `predicciones.csv`, identificando 621 lotes en riesgo y entregando la probabilidad continua `prob_bueno`, que permite priorizar qué lotes deben catarse primero."
>
> *(Nota de transición: Cede la palabra al expositor del Bloque 05 — Evaluación y Optimización).*

---

## Bloque 05: Evaluación y Optimización del Modelo
**Tiempo asignado:** 5 min 00 seg

### Diapositiva 24: Portada de Sección — Evaluación y Optimización `[10 seg]`
* **Apoyo visual:** Separador visual `05 Modelo Naive Bayes, evaluación y optimización`.

> **Diálogo:**
> "En el quinto bloque revisaremos cómo validamos, optimizamos y auditamos los errores del modelo desde la óptica del negocio."

### Diapositiva 25: Optimización Metodológica sin Contaminar la Prueba `[1 min 50 seg]`
* **Apoyo visual:** Gráfico horizontal *Comparación de configuraciones* y puntos clave sobre `DummyClassifier`, selección CV y `var_smoothing`.

> **Diálogo:**
> "Para comprobar que nuestro modelo aporta inteligencia real, lo comparamos contra una línea base ingenua mediante `DummyClassifier`, que siempre predice la clase mayoritaria 'bueno'. Como se observa en la barra inferior del gráfico, esa referencia logra 52.9 % de exactitud pero un F1 macro de apenas 0.35 porque jamás detecta un lote malo. Nuestro modelo supera esa base por más de 22 puntos porcentuales.
>
> Todas las decisiones de ajuste se tomaron usando exclusivamente validación cruzada de 5 pliegues sobre los datos de entrenamiento, sin tocar el conjunto de prueba: evaluamos subconjuntos de 3, 5, 7, 9 y 11 variables, confirmando que el Top 3 maximizó el F1 en validación cruzada; y mediante `GridSearchCV` fijamos el hiperparámetro `var_smoothing` en `1.0` para suavizar las curvas gaussianas frente a valores atípicos, elevando el F1 de validación cruzada a `0.7368`."

### Diapositiva 26: Evaluación de Negocio — Matriz de Confusión `[1 min 55 seg]`
* **Apoyo visual:** Matriz de confusión 2x2 en prueba (`109`, `35`, `33`, `95`) y desglose de costos entre Falso Negativo y Falso Positivo.

> **Diálogo:**
> "Al desbloquear finalmente los 272 lotes de prueba, nuestro modelo acertó en 204 casos —109 vinos buenos y 95 vinos malos—, alcanzando el 75 % de exactitud. Más allá de la cifra global, analizamos el impacto económico de los dos tipos de error:
>
> Los 35 falsos positivos son lotes buenos que el modelo marcó en riesgo; su costo es bajo porque simplemente pasan a una cata de verificación antes de aprobarse. En cambio, los 33 falsos negativos son vinos malos aprobados por error; este es el error más costoso para la bodega porque conlleva riesgo de devoluciones y daño a la reputación de la marca. Por ello, recomendamos usar el modelo como un sistema de triaje en laboratorio para ordenar las catas según la probabilidad `prob_bueno`."

### Diapositiva 27: Alcance del Modelo y Oportunidades de Mejora `[1 min 05 seg]`
* **Apoyo visual:** Tres columnas con iconos: *Subjetividad Sensorial*, *Supuestos Matemáticos* y *Frontera Discretizada*.

> **Diálogo:**
> "Con rigor científico, documentamos tres limitaciones que explican por qué el modelo se ubica en 75 % y no en 95 %: primero, la subjetividad sensorial de la variable objetivo, pues los catadores perciben aromas y taninos que no están medidos en las 11 variables químicas; segundo, la persistencia de cierta dependencia química y asimetría en sulfatos respecto a una campana de Gauss ideal; y tercero, el efecto de discretizar una escala continua, donde vinos de calidad 5 y 6 tienen perfiles químicos muy cercanos en la frontera."
>
> *(Nota de transición: Cede la palabra al expositor del Bloque 06 — Dashboard BI).*

---

## Bloque 06: Dashboard de Business Intelligence
**Tiempo asignado:** 6 min 00 seg

### Diapositiva 28: Vista 1 — Resumen Ejecutivo (Panorama General de Calidad) `[1 min 30 seg]`
* **Apoyo visual:** Captura de la pestaña *Resumen ejecutivo* en Power BI (KPIs `1599`, `855`, `744`, `5.64`, barras por calidad y gráfico de anillo).

> **Diálogo:**
> "En el sexto bloque llevamos todo el trabajo analítico a un tablero interactivo en Power BI estructurado en cuatro vistas. La primera pestaña, Resumen Ejecutivo, ofrece a la dirección de la bodega una fotografía inmediata de los 1,599 registros históricos evaluados, mostrando una calidad promedio de 5.64.
>
> El gráfico de anillo refleja el balance operativo —53.47 % de lotes buenos frente a 46.53 % en riesgo—, mientras que el gráfico de barras confirma que más del 80 % de la producción se concentra en las notas 5 y 6. Además, integramos filtros dinámicos para explorar cualquier rango de calidad en tiempo real."

### Diapositiva 29: Vista 2 — Perfil Fisicoquímico por Nivel de Calidad `[1 min 30 seg]`
* **Apoyo visual:** Captura de la pestaña *Perfil fisicoquímico* con 4 gráficos de barras (Alcohol, pH, Acidez volátil y Sulfatos).

> **Diálogo:**
> "La segunda vista, Perfil Fisicoquímico, permite validar visualmente las decisiones del algoritmo. En los gráficos observamos cómo el alcohol asciende hasta el 12 % en los vinos de calidad 8, y cómo los sulfatos crecen de forma sostenida diferenciando claramente los lotes buenos en morado de los malos en turquesa.
>
> Por el contrario, la acidez volátil cae drásticamente de 0.88 a cerca de 0.40 en los mejores vinos, mientras que el pH se mantiene prácticamente plano alrededor de 3.3 en todas las categorías, confirmando visualmente por qué fue descartado por el modelo."

### Diapositiva 30: Vista 3 — Auditoría y Transparencia del Modelo Naive Bayes `[1 min 30 seg]`
* **Apoyo visual:** Captura de la pestaña *Desempeño del modelo* mostrando métricas Holdout (`272`) arriba y Validación Cruzada Global (`1,359`) abajo.

> **Diálogo:**
> "En la tercera pestaña, Desempeño del Modelo, priorizamos la transparencia metodológica. Separamos explícitamente los dos esquemas de evaluación: en la fila superior presentamos las métricas sobre el conjunto de prueba reservado de 272 lotes con el 75 % de exactitud; y en la fila inferior mostramos la validación cruzada global sobre los 1,359 lotes únicos, alcanzando 991 aciertos y 72.92 % de exactitud fuera de muestra, acompañados de su matriz de confusión y una nota explicativa para que ningún usuario confunda ambas mediciones."

### Diapositiva 31: Vista 4 — Explorador de Lotes y Triaje Operativo `[1 min 30 seg]`
* **Apoyo visual:** Captura de la pestaña *Explorador de lotes* (`1,359` lotes, `991` correctas, `368` incorrectas, filtros y tabla lote a lote).

> **Diálogo:**
> "Finalmente, la cuarta vista es el Explorador de Lotes, diseñada para la operación diaria en laboratorio. Aquí descendemos al detalle individual de los 1,359 lotes depurados, permitiendo filtrar por calidad real, predicción o acierto del modelo.
>
> Gracias a la probabilidad `prob_bueno` y al indicador `lote_en_riesgo`, el equipo de control de calidad puede ordenar su agenda diaria: en lugar de catar al azar, revisan prioritariamente los lotes con menor probabilidad de éxito, optimizando recursos y previniendo fallas antes del embotellado."
>
> *(Nota de transición: Cede la palabra para el cierre final — Bloque 07).*

---

## Bloque 07: Conclusión General y Cierre
**Tiempo asignado:** 1 min 30 seg

### Diapositiva 32: Conclusión General: De Datos Fisicoquímicos a Decisiones en Bodega `[1 min 15 seg]`
* **Apoyo visual:** Tres pilares ejecutivos: *Rigor Analítico*, *Impacto Operativo* y *Toma de Decisiones BI*.

> **Diálogo:**
> "Para concluir, este proyecto demuestra cómo la ingeniería del conocimiento y la inteligencia de negocios transforman mediciones rutinarias de laboratorio en una ventaja operativa real para la bodega.
>
> A lo largo de las siete secciones recorridas, partimos de la depuración rigurosa de los datos hasta construir un clasificador Naive Bayes optimizado y libre de fuga de información. Comprobamos que basta monitorear tres indicadores químicos clave —alcohol, acidez volátil y sulfatos— para alcanzar un 75 % de exactitud en la detección temprana de lotes en riesgo, superando por más de 22 puntos porcentuales la línea base.
>
> Al integrar estas probabilidades en Power BI, entregamos una herramienta práctica que no reemplaza el criterio del enólogo, sino que lo potencia: prioriza las catas sensoriales sobre los lotes críticos, optimiza los tiempos de laboratorio y protege la calidad de la marca."

### Diapositiva 33: Cierre Formal — Gracias por su atención `[15 seg]`
* **Apoyo visual:** Diapositiva final *Gracias por su atención*.

> **Diálogo:**
> "Con esto concluimos nuestra presentación. Muchas gracias por su atención, profesor y compañeros; quedamos a su disposición para cualquier pregunta o comentario."

---

## 2. Guía Rápida para Preguntas Frecuentes del Docente / Evaluadores

* **P1: ¿Por qué en la Vista 1 de Power BI aparecen `1,599` lotes y en las Vistas 3 y 4 aparecen `1,359`?**
  > **Respuesta sugerida:** Porque la Vista 1 (*Resumen Ejecutivo*) está conectada al dataset histórico completo capturado en bodega (`1,599` registros), mientras que las Vistas 3 y 4 están conectadas a `predicciones.csv` (`1,359` lotes únicos tras eliminar los `240` duplicados en la Fase 2 para evitar fuga de datos).

* **P2: ¿Por qué se eligió `var_smoothing = 1.0` si en prueba el accuracy pasó de `0.7537` a `0.7500`?**
  > **Respuesta sugerida:** Porque la diferencia en prueba es de apenas 1 lote (`205` vs. `204` aciertos de `272`), mientras que en validación cruzada de 5 pliegues sobre los `1,087` lotes de entrenamiento, `var_smoothing = 1.0` elevó el F1 macro de `0.7239` a `0.7368`. Elegir hiperparámetros con validación cruzada evita el sobreajuste al conjunto de prueba.

* **P3: ¿Por qué no se eliminaron los valores atípicos (*outliers*) detectados en los boxplots?**
  > **Respuesta sugerida:** Porque todos los valores están dentro de rangos químicos reales de laboratorio (por ejemplo, pH entre `2.74` y `4.01`) y representan lotes con desviaciones reales que precisamente el modelo necesita aprender a detectar como *lotes en riesgo*.