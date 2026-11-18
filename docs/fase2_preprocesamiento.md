# Fase 2: Preprocesamiento

| | |
|---|---|
| **Responsable** | Pamela |
| **Rama** | `pamela-fase2-preprocesamiento` |
| **Script** | `scripts/fase2_preprocesamiento.py` |
| **Entrada** | `data/raw/winequality-red.csv` (solo lectura) |
| **Salida** | `data/processed/winequality-red-limpio.csv` (1,359 filas y 14 columnas) |
| **Figuras** | `docs/figuras/fase2_atipicos.png`, `docs/figuras/fase2_correlaciones.png` |

## 1. Objetivo

Convertir el CSV crudo en un dataset limpio, consistente y listo para modelar, mediante un script que cualquier integrante del equipo pueda ejecutar y obtener exactamente el mismo archivo.

Para reproducirlo, desde la raíz del proyecto:

```bash
python scripts/fase2_preprocesamiento.py
```

La limpieza va en un script y no se hace a mano en Excel porque un script deja el proceso documentado, se puede repetir y se puede revisar. Una edición manual no deja rastro y no se puede reproducir.

## 2. Resumen del proceso

| Orden | Paso | Resultado |
|:---:|---|---|
| 1 | Carga del CSV crudo | 1,599 filas y 12 columnas |
| 2 | Homogeneizar nombres y tipos | Nombres en minúsculas con guion bajo; `quality` entero, el resto decimal |
| 3 | Verificar nulos | 0 nulos |
| 4 | Eliminar duplicados | 240 eliminados, quedan 1,359 filas |
| 5 | Analizar atípicos | Se detectan y se conservan |
| 6 | Analizar correlaciones | Alcohol y acidez volátil son las más relacionadas con la calidad |
| 7 | Crear variables objetivo | `calidad_bin` y `calidad_3` |
| 8 | Exportar | 1,359 filas y 14 columnas, sin estandarizar |

## 3. Decisiones y justificación

### 3.1 Formato homogéneo

Los nombres originales tenían espacios y mayúsculas (`fixed acidity`, `pH`). Se convirtieron al formato del contrato de datos del equipo (`fixed_acidity`, `ph`), con `strip`, `lower` y `replace(" ", "_")`. Así todas las fases usan los mismos nombres y no se rompen consultas ni medidas posteriores (por ejemplo, en Power BI).

Se aseguró que `quality` sea entero y que las 11 variables fisicoquímicas sean decimales.

### 3.2 Valores nulos

El dataset no tiene valores nulos (0 de 1,599 filas). Aun así, la revisión queda en el script y se imprime en consola, para que quede documentada y para que, si el archivo cambiara, el script lo detecte.

### 3.3 Duplicados

Se eliminaron **240 registros duplicados** (15 % del archivo), y quedaron **1,359 filas**. Se usó `drop_duplicates()` y después `reset_index(drop=True)`.

**Por qué importa.** Si un registro duplicado cae una vez en entrenamiento y otra en prueba, el modelo "reconoce" una fila que ya vio y el accuracy sale inflado. Eliminar los duplicados permite evaluar el modelo de forma honesta.

### 3.4 Valores atípicos

Se identificaron con la regla del rango intercuartílico (valores fuera de Q1 - 1.5·IQR y Q3 + 1.5·IQR) y se graficaron en `docs/figuras/fase2_atipicos.png`.

| Variable | Atípicos |
|---|:---:|
| residual_sugar | 126 |
| chlorides | 87 |
| sulphates | 55 |
| total_sulfur_dioxide | 45 |
| fixed_acidity | 41 |
| density | 35 |
| ph | 28 |
| free_sulfur_dioxide | 26 |
| volatile_acidity | 19 |
| alcohol | 12 |
| citric_acid | 1 |

**Decisión: se conservan todos.**

- Los valores están dentro de rangos químicamente posibles (por ejemplo, pH entre 2.74 y 4.01, alcohol entre 8.4 y 14.9). No hay señales de errores de captura.
- La bodega quiere detectar lotes con propiedades fuera de lo normal. Un lote con acidez volátil o sulfatos extremos es justo el tipo de lote que el modelo debe aprender a reconocer. Eliminarlos le quitaría información valiosa.
- Eliminarlos recortaría el dataset y haría que el modelo funcione peor justo en los casos que importan al negocio.

### 3.5 Correlaciones

Se calculó la correlación de Pearson entre todas las variables y con `quality` (`docs/figuras/fase2_correlaciones.png`).

**Con la calidad:**

| Variable | Correlación con `quality` |
|---|:---:|
| alcohol | +0.48 |
| sulphates | +0.25 |
| citric_acid | +0.23 |
| fixed_acidity | +0.12 |
| residual_sugar | +0.01 |
| free_sulfur_dioxide | -0.05 |
| ph | -0.06 |
| chlorides | -0.13 |
| density | -0.18 |
| total_sulfur_dioxide | -0.18 |
| volatile_acidity | -0.40 |

**Interpretación.**

- Los vinos de mayor calidad tienden a tener **más alcohol** (promedio 10.89 en `bueno` contra 9.92 en `malo`).
- Los de menor calidad tienden a tener **más acidez volátil** (0.59 en `malo` contra 0.47 en `bueno`), lo cual es coherente químicamente porque la acidez volátil se asocia con aroma a vinagre.
- `residual_sugar` casi no se relaciona con la calidad (+0.01).
- Las correlaciones son moderadas: ninguna variable por sí sola explica la calidad, y esto anticipa que el modelo tendrá límites.

**Correlaciones entre variables.** Hay pares con relación fuerte:

| Par | Correlación |
|---|:---:|
| fixed_acidity y ph | -0.69 |
| fixed_acidity y density | +0.67 |
| fixed_acidity y citric_acid | +0.67 |
| free_sulfur_dioxide y total_sulfur_dioxide | +0.67 |

Esto importa para Naive Bayes, que supone independencia entre variables. Estas relaciones violan parcialmente ese supuesto. Lo toman en cuenta las fases 3A y 3B.

### 3.6 Variables objetivo

| Columna | Regla | Conteo |
|---|---|---|
| `calidad_bin` | `bueno` si `quality >= 6`; `malo` si `quality <= 5` | 719 `bueno`, 640 `malo` |
| `calidad_3` | `baja` si `quality <= 5`; `media` si `quality == 6`; `alta` si `quality >= 7` | 640 `baja`, 535 `media`, 184 `alta` |

Distribución original de `quality` (ya sin duplicados): 3 → 10, 4 → 53, 5 → 577, 6 → 535, 7 → 167, 8 → 17.

**Por qué el corte en 6.** Con `quality >= 6` el 53 % de los lotes son `bueno` y el 47 % son `malo`, es decir, clases casi balanceadas. Si se cortara en otro punto, una clase dominaría y el modelo podría acertar mucho simplemente prediciendo siempre la clase mayoritaria.

`calidad_3` conserva más detalle, pero la clase `alta` solo tiene 184 lotes (13.5 %), por lo que está desbalanceada.

### 3.7 Sin estandarización

El CSV limpio **no se estandariza**: las variables siguen en sus unidades originales.

Si se estandarizara todo el dataset en esta fase, la media y la desviación estándar se calcularían con datos que luego quedarían en el conjunto de prueba. Eso es **fuga de datos** (*data leakage*) y haría que las métricas salgan mejores de lo real. El escalado se hace en la fase 3, dentro del `Pipeline` (`StandardScaler` + `GaussianNB`), de modo que se ajuste solo con los datos de entrenamiento de cada pliegue.

## 4. Archivo de salida

`data/processed/winequality-red-limpio.csv`: 1,359 filas y 14 columnas, sin índice, en este orden:

```text
fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
free_sulfur_dioxide, total_sulfur_dioxide, density, ph, sulphates, alcohol,
quality, calidad_bin, calidad_3
```

Este orden y estos nombres son el contrato de datos del README, del que dependen las fases 3A, 3B y 4.

## 5. Verificación

| Criterio | Resultado |
|---|---|
| Duplicados eliminados | 240 |
| Filas finales | 1,359 |
| Columnas | 14 |
| `calidad_bin` | 719 `bueno` y 640 `malo` |
| `calidad_3` | 640 `baja`, 535 `media`, 184 `alta` |
| Correlación de `alcohol` con `quality` | +0.48 |
| Correlación de `volatile_acidity` con `quality` | -0.40 |
| El script corre sin errores y regenera el mismo archivo | Sí |
| Datos sin estandarizar | Sí |

## 6. Hallazgos principales

1. Los datos crudos no tenían nulos, pero **15 % de los registros eran duplicados**, que habrían inflado la evaluación del modelo.
2. Hay valores atípicos en todas las variables, pero son químicamente plausibles, así que se conservan.
3. El **alcohol** (+0.48) y la **acidez volátil** (-0.40) son las variables más asociadas con la calidad.
4. El corte binario en 6 produce clases casi balanceadas (53 % y 47 %).
5. Varias variables están correlacionadas entre sí, lo que limita el supuesto de independencia de Naive Bayes.