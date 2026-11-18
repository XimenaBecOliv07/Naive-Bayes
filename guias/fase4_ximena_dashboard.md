# Guía fase 4: Dashboard de Business Intelligence

| | |
|---|---|
| **Responsable** | Ximena |
| **Rama** | `ximena-fase4-dashboard` |
| **Puedes empezar** | Desde el inicio: diseño, paleta y páginas 1 y 2 con el CSV crudo |
| **Dependes de** | Braulio (`predicciones.csv`) y Octavio (`metricas_modelo.csv`) |
| **Dependen de ti** | Fátima necesita las capturas para la presentación |
| **Revisa tu PR** | Fátima |
| **Tus archivos** | Todo lo que va en `docs/dashboard/`: `dashboard_vino.pbix`, capturas `pagina1_resumen.png` a `pagina4_explorador.png` y `guia_power_bi.md` |
| **Requisito** | Power BI Desktop (solo funciona en Windows) |

> Esta guía no te da las fórmulas resueltas. Te da el contexto, los conceptos, la documentación y pistas para que lo resuelvas tú. Las pistas están ocultas: ábrelas solo si te atoras, empezando por la primera.

---

## 1. Contexto

Un modelo que vive en un notebook no le sirve a la bodega: el jefe de calidad no programa en Python. Tu fase convierte las predicciones en una herramienta visual que responde preguntas de negocio: cuántos lotes están en riesgo, qué variables químicas los delatan, qué tanto confiar en el modelo y qué lotes mandar primero a cata.

La regla de oro del diseño de dashboards: **cada página responde una pregunta**, y su título dice la conclusión, no el nombre del gráfico. Por ejemplo, "Los lotes buenos tienen más alcohol" en lugar de "Gráfico de barras de alcohol".

## 2. Objetivo general

Construir en Power BI un dashboard interactivo de cuatro páginas que permita a la bodega identificar y priorizar los lotes con riesgo de baja calidad.

## 3. Objetivos específicos

1. Cargar los CSV de predicciones y métricas con los tipos de datos correctos.
2. Programar medidas DAX para los indicadores de negocio y de desempeño del modelo.
3. Diseñar cuatro páginas: resumen ejecutivo, perfil fisicoquímico, desempeño del modelo y explorador de lotes.
4. Documentar las medidas, las páginas y la forma de uso del tablero.

## 4. Entradas y salidas

| | Archivo |
|---|---|
| **Entrada** | `data/processed/predicciones.csv` (Braulio): tabla principal, una fila por lote |
| **Entrada** | `data/processed/metricas_modelo.csv` (Octavio): métricas del modelo final |
| **Salida** | `docs/dashboard/dashboard_vino.pbix` |
| **Salida** | `docs/dashboard/pagina1_resumen.png`, `pagina2_quimico.png`, `pagina3_modelo.png`, `pagina4_explorador.png` |
| **Salida** | `docs/dashboard/guia_power_bi.md`: medidas DAX, páginas y cómo usar el tablero |

Las columnas de cada CSV están en el [contrato de datos del README](../README.md#6-contrato-de-datos).

## 5. Conceptos que debes investigar

| Concepto | Pregunta que debes poder responder |
|---|---|
| KPI | ¿Qué hace que un indicador sea útil para tomar una decisión? |
| Power Query | ¿Para qué sirve el paso de "Transformar datos" antes de cargar? |
| Columna calculada y medida | ¿Cuál es la diferencia y cuándo conviene cada una? |
| Contexto de filtro en DAX | ¿Por qué una medida cambia de valor cuando mueves un segmentador? |
| Segmentadores (*slicers*) | ¿Cómo permiten explorar los datos sin modificar el reporte? |
| Formato condicional | ¿Cómo ayuda el color a leer una matriz de confusión? |

**Fuentes (Microsoft Learn):**
- Conectar a un CSV: https://learn.microsoft.com/es-es/power-bi/connect-data/desktop-connect-csv
- Fundamentos de DAX: https://learn.microsoft.com/es-es/power-bi/transform-model/desktop-quickstart-learn-dax-basics
- Crear medidas: https://learn.microsoft.com/es-es/power-bi/transform-model/desktop-measures
- Segmentadores: https://learn.microsoft.com/es-es/power-bi/visuals/power-bi-visualization-slicers
- Visual de matriz: https://learn.microsoft.com/es-es/power-bi/visuals/desktop-matrix-visual
- Formato condicional: https://learn.microsoft.com/es-es/power-bi/create-reports/desktop-conditional-table-formatting

## 6. Herramientas

| Necesitas... | Investiga |
|---|---|
| Contar filas | [`COUNTROWS`](https://learn.microsoft.com/es-es/dax/countrows-function-dax) |
| Contar solo las filas que cumplen una condición | [`CALCULATE`](https://learn.microsoft.com/es-es/dax/calculate-function-dax) |
| Dividir sin errores cuando el denominador es 0 | [`DIVIDE`](https://learn.microsoft.com/es-es/dax/divide-function-dax) |
| Promedios y sumas | [`AVERAGE`](https://learn.microsoft.com/es-es/dax/average-function-dax), [`SUM`](https://learn.microsoft.com/es-es/dax/sum-function-dax) |
| Leer un valor de la tabla de métricas | `CALCULATE` combinado con [`MAX`](https://learn.microsoft.com/es-es/dax/max-function-dax) y un filtro sobre la columna `metrica` |

## 7. Ruta de trabajo

### Paso 1: Crea tu rama

Sigue la [sección 5 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#5-git-y-github).

### Paso 2: Empieza sin esperar el modelo

Mientras llegan los CSV del modelo:
1. Define la paleta: vino `#722F37`, rosa vino `#C98B92` y crema `#F7EFE5`.
2. Carga el CSV crudo y arma un borrador de las páginas 1 y 2 (distribución de calidad y perfil químico). Esas páginas no necesitan predicciones.
3. Cuando Braulio haga merge, ejecuta `git pull origin main` y cambia el origen de datos a `predicciones.csv`.

<details>
<summary>Pista: cambiar el origen sin rehacer todo</summary>

En Power Query, cada consulta empieza con un paso "Origen". Investiga cómo editar ese paso o la opción *Configuración de origen de datos* para apuntar a otro archivo con las mismas columnas.
</details>

### Paso 3: Carga y tipa los datos

Carga `predicciones.csv` como tabla `lotes` y `metricas_modelo.csv` como tabla `metricas`. Revisa en Power Query que cada columna tenga el tipo correcto: decimales, enteros y texto.

<details>
<summary>Pista: los decimales salen mal</summary>

Si tu Windows está configurado en español, Power BI puede esperar coma decimal, pero el CSV usa punto. Investiga la opción *Cambiar tipo > Usando configuración regional* y elige inglés (Estados Unidos).
</details>

### Paso 4: Medidas DAX

Crea medidas para estos indicadores. Tú decides la fórmula:

| Medida | Qué debe calcular |
|---|---|
| Total Lotes | Número de lotes |
| % Lotes Buenos | Proporción de lotes cuya clase real es `bueno` |
| Calidad Media | Promedio de `quality` |
| Alcohol Medio, Acidez Volátil Media, Sulfatos Medios | Promedio de cada variable |
| Lotes en Riesgo | Número de lotes que el modelo marca en riesgo |
| % Lotes en Riesgo | Lotes en riesgo sobre el total |
| Accuracy Prueba, F1 Prueba | Valor leído de la tabla `metricas` |

<details>
<summary>Pista 1</summary>

Una medida puede usar otra medida. Si ya tienes "Total Lotes", úsala como denominador en los porcentajes.
</details>

<details>
<summary>Pista 2</summary>

`lote_en_riesgo` vale 1 o 0. ¿Qué función de agregación te da directamente cuántos lotes valen 1?
</details>

<details>
<summary>Pista 3</summary>

La tabla `metricas` tiene una fila por métrica. Para leer el accuracy tienes que filtrar la fila cuya `metrica` es `accuracy` y devolver su `valor`.
</details>

### Paso 5: Diseña las cuatro páginas

| Página | Pregunta que responde | Elementos sugeridos |
|---|---|---|
| 1. Resumen ejecutivo | ¿Cómo está la calidad de nuestros lotes? | Tarjetas de KPI, distribución por `quality`, proporción bueno/malo |
| 2. Perfil fisicoquímico | ¿Qué distingue a un lote bueno de uno malo? | Promedios por clase, dispersión de alcohol contra acidez volátil, segmentador de `calidad_3` |
| 3. Desempeño del modelo | ¿Cuánto podemos confiar en el modelo? | Tarjetas de accuracy y F1, matriz de confusión, distribución de `prob_bueno` |
| 4. Explorador de lotes | ¿Qué lotes reviso primero? | Segmentadores por alcohol, acidez volátil, sulfatos y predicción; tabla ordenada por `prob_bueno`; tarjeta de lotes en riesgo |

<details>
<summary>Pista: matriz de confusión</summary>

No necesitas un visual especial: usa el visual de **Matriz** con `y_real` en filas, `y_pred` en columnas y el conteo de lotes como valores. El color sale de formato condicional.
</details>

<details>
<summary>Pista: histograma de probabilidades</summary>

Investiga cómo crear **grupos** (*bins*) sobre una columna numérica para agrupar `prob_bueno` en rangos de 0.1.
</details>

### Paso 6: Capturas, documentación y pull request

1. Guarda el `.pbix` en `docs/dashboard/`.
2. Toma una captura de cada página. Son el respaldo si Power BI falla el día de la defensa.
3. Documenta en `docs/dashboard/guia_power_bi.md` cada medida (fórmula y para qué sirve) y cada página.
4. Commits, push y PR. Al hacer merge avisa a Fátima con `[MERGE]`.

### Paso 7: Tu sección del notebook (turno 5)

En el notebook escribe una sección breve: qué archivos alimentan el dashboard, qué KPI tiene y qué pregunta de negocio responde cada página. Sigue la [sección 6 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#6-notebook-integrador-por-turnos).

## 8. Criterios de aceptación

- [ ] El dashboard muestra **1,359 lotes** y alrededor de **53 % de lotes buenos**.
- [ ] Accuracy y F1 coinciden con `metricas_modelo.csv`.
- [ ] La matriz de confusión suma 1,359 lotes (son las predicciones por validación cruzada de todos los lotes).
- [ ] La tarjeta de Lotes en Riesgo cambia al mover los segmentadores.
- [ ] Cada página tiene un título que expresa una conclusión.
- [ ] Las cuatro capturas están en `docs/dashboard/`.

## 9. Preparación para la defensa (minutos 21 a 26)

Prepara una demostración en vivo de 5 minutos y ensáyala con cronómetro. Debes poder responder sin leer:
- ¿Qué decisión puede tomar el jefe de calidad con cada página?
- ¿Qué es una medida DAX y por qué cambia al filtrar?
- ¿Por qué la matriz del dashboard (1,359 lotes) es distinta a la del conjunto de prueba (272 lotes)?
- Si el profesor mueve el segmentador de alcohol, ¿qué espera ver y por qué?
