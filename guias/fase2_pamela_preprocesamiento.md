# Guía fase 2: Preprocesamiento

| | |
|---|---|
| **Responsable** | Pamela |
| **Rama** | `pamela-fase2-preprocesamiento` |
| **Puedes empezar** | Desde el inicio: el CSV crudo ya está en el repositorio |
| **Dependes de** | Nadie (puedes leer los hallazgos de Mateo cuando los suba, pero no tienes que esperarlos) |
| **Dependen de ti** | Braulio y Octavio necesitan tu CSV limpio para la versión final del modelo |
| **Revisa tu PR** | Braulio |
| **Tus archivos** | `scripts/fase2_preprocesamiento.py`, `data/processed/winequality-red-limpio.csv`, `docs/fase2_preprocesamiento.md`, `docs/figuras/fase2_*.png` |

> Esta guía no te da el código. Te da el contexto, los conceptos, la documentación y pistas para que lo resuelvas tú. Las pistas están ocultas: ábrelas solo si te atoras, empezando por la primera.

---

## 1. Contexto

Los datos del mundo real casi nunca están listos para un modelo. El preprocesamiento convierte el CSV crudo en un dataset limpio y consistente, y tiene que hacerlo de forma **reproducible**: cualquier persona del equipo debe poder ejecutar tu script y obtener exactamente el mismo archivo.

Tu fase es el punto de apoyo de todo el proyecto. Si el CSV limpio tiene un error, ese error llega al modelo, al dashboard y a la presentación. Por eso tu salida sigue el [contrato de datos del README](../README.md#6-contrato-de-datos): Braulio, Octavio y Ximena trabajan desde ya con esos nombres de columnas.

## 2. Objetivo general

Construir un proceso de limpieza reproducible que transforme `winequality-red.csv` en el dataset con el que se entrenará el modelo.

## 3. Objetivos específicos

1. Homogeneizar los nombres de las columnas y los tipos de datos.
2. Verificar los valores nulos y eliminar los registros duplicados.
3. Analizar los valores atípicos (*outliers*) y justificar qué se hace con ellos.
4. Analizar las correlaciones entre variables y con la calidad.
5. Crear las variables objetivo `calidad_bin` y `calidad_3`.
6. Exportar `data/processed/winequality-red-limpio.csv`.

## 4. Entradas y salidas

| | Archivo |
|---|---|
| **Entrada** | `data/raw/winequality-red.csv` (solo lectura) |
| **Salida** | `scripts/fase2_preprocesamiento.py`: script reproducible |
| **Salida** | `data/processed/winequality-red-limpio.csv`: 14 columnas según el contrato de datos |
| **Salida** | `docs/fase2_preprocesamiento.md`: reporte con decisiones y hallazgos |
| **Salida** | `docs/figuras/fase2_atipicos.png` y `docs/figuras/fase2_correlaciones.png` |

## 5. Conceptos que debes investigar

| Concepto | Pregunta que debes poder responder |
|---|---|
| Reproducibilidad | ¿Por qué la limpieza va en un script y no se hace a mano en Excel? |
| Duplicados | ¿Por qué un duplicado que cae a la vez en entrenamiento y en prueba infla el accuracy? |
| Valores atípicos | ¿Cuándo un valor extremo es un error y cuándo es un dato real valioso? |
| Correlación de Pearson | ¿Qué significa una correlación de +0.5, de 0 y de -0.4? |
| Discretización | ¿Cómo se convierte una variable numérica en categorías? |
| Fuga de datos (*data leakage*) | ¿Por qué **no** debes estandarizar el dataset completo en esta fase? |

Lectura recomendada sobre fuga de datos: https://scikit-learn.org/stable/common_pitfalls.html

## 6. Herramientas

| Necesitas... | Investiga |
|---|---|
| Rutas que funcionen en cualquier computadora | [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html), en especial `Path(__file__)` y `.parents` |
| Renombrar columnas | La propiedad `DataFrame.columns` y los métodos de texto de Python (`lower`, `strip`, `replace`) |
| Nulos | [`DataFrame.isna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html), [`DataFrame.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html) |
| Duplicados | [`DataFrame.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html) y `reset_index` |
| Tipos de datos | [`DataFrame.astype`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html) |
| Atípicos | [`seaborn.boxplot`](https://seaborn.pydata.org/generated/seaborn.boxplot.html) |
| Correlaciones | [`DataFrame.corr`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html) y [`seaborn.heatmap`](https://seaborn.pydata.org/generated/seaborn.heatmap.html) |
| Crear categorías | [`pandas.cut`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html) o una comparación booleana con `.map` |
| Exportar | [`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) |

## 7. Ruta de trabajo

### Paso 1: Crea tu rama

Sigue la [sección 5 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#5-git-y-github).

### Paso 2: Rutas reproducibles

Tu script debe funcionar sin importar desde qué carpeta se ejecute ni en qué computadora. Define tres rutas: la raíz del proyecto, el CSV crudo y el CSV de salida.

<details>
<summary>Pista 1</summary>

`Path(__file__)` es la ruta de tu propio script. Si el script está en `scripts/`, ¿cuántos niveles tienes que subir para llegar a la raíz?
</details>

<details>
<summary>Pista 2</summary>

`.resolve()` convierte la ruta en absoluta y `.parents[0]` es la carpeta que contiene al archivo. Prueba en la consola qué devuelven `.parents[0]` y `.parents[1]`.
</details>

### Paso 3: Formato homogéneo

Los nombres originales tienen espacios y mayúsculas (`fixed acidity`, `pH`). Conviértelos al formato del contrato de datos (`fixed_acidity`, `ph`). Asegura además que `quality` sea entero y el resto decimales.

<details>
<summary>Pista</summary>

Puedes recorrer `df.columns` con una *list comprehension* y aplicar a cada nombre varios métodos de texto encadenados.
</details>

### Paso 4: Nulos y duplicados

Revisa los nulos (aunque no haya, la revisión debe quedar documentada) y elimina los duplicados. Imprime en consola cuántos había antes y cuántas filas quedan.

### Paso 5: Atípicos y correlaciones

Genera un diagrama de caja por variable y una matriz de correlación, y guárdalos en `docs/figuras/`. Después decide: ¿eliminas los atípicos o los conservas? Justifícalo pensando en el negocio, no solo en la estadística.

<details>
<summary>Pista 1</summary>

Para muchos diagramas de caja en una sola figura, investiga `plt.subplots(filas, columnas)` y recorre los ejes con `axes.ravel()`.
</details>

<details>
<summary>Pista 2: para decidir sobre los atípicos</summary>

Piensa en lo que quiere detectar la bodega. Un lote con acidez volátil extrema, ¿es un error de captura o justo el tipo de lote defectuoso que el modelo debe aprender a reconocer?
</details>

### Paso 6: Variables objetivo

Crea dos columnas nuevas:

| Columna | Regla |
|---|---|
| `calidad_bin` | `bueno` si `quality >= 6`, `malo` si `quality <= 5` |
| `calidad_3` | `baja` si `quality <= 5`, `media` si `quality == 6`, `alta` si `quality >= 7` |

<details>
<summary>Pista 1</summary>

Para `calidad_bin`, la comparación `df["quality"] >= 6` produce una serie de `True`/`False`. Investiga cómo transformar esos valores en texto con `.map`.
</details>

<details>
<summary>Pista 2</summary>

Para `calidad_3`, `pandas.cut` recibe los límites de los intervalos (`bins`) y sus nombres (`labels`). Fíjate si los intervalos incluyen el límite derecho o el izquierdo.
</details>

### Paso 7: Exporta y documenta

Guarda el CSV sin la columna de índice y redacta `docs/fase2_preprocesamiento.md` con cada decisión y su justificación: nulos, duplicados, atípicos, correlaciones y clases.

### Paso 8: Commits, pull request y aviso

Separa en commits el script, el CSV y el reporte. Cuando hagan merge, avisa con `[MERGE]` para que Braulio y Octavio hagan `git pull origin main`.

### Paso 9: Tu sección del notebook (turno 2)

Cuando el turno de Mateo termine, sigue la [sección 6 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#6-notebook-integrador-por-turnos).

## 8. Criterios de aceptación

- [ ] La consola reporta **240 duplicados eliminados** y **1,359 filas** finales.
- [ ] El CSV limpio tiene **1,359 filas y 14 columnas**, con los nombres exactos del contrato de datos.
- [ ] `calidad_bin`: **719 `bueno`** y **640 `malo`**.
- [ ] `calidad_3`: **640 `baja`**, **535 `media`** y **184 `alta`**.
- [ ] La correlación con `quality` sale aproximadamente en +0.48 para `alcohol` y -0.40 para `volatile_acidity`.
- [ ] `python scripts/fase2_preprocesamiento.py` corre sin errores desde la raíz y vuelve a generar el mismo archivo.
- [ ] El CSV no se estandarizó: los valores siguen en sus unidades originales.

## 9. Preparación para la defensa (minutos 8 a 13)

Debes poder responder sin leer:
- ¿Qué pasos de limpieza aplicaste y en qué orden?
- ¿Por qué eliminar duplicados es importante para evaluar el modelo honestamente?
- ¿Por qué conservaste (o eliminaste) los valores atípicos?
- ¿Por qué el corte binario en `quality >= 6` deja clases casi balanceadas?
- ¿Por qué el escalado no se hace en tu fase y dónde se hace?
- ¿Qué variables se relacionan más con la calidad y qué significa eso químicamente?
