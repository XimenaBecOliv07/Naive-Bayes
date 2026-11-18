# Instrucciones generales: cómo trabajamos como equipo

Este documento no describe el proyecto (eso está en el [`README.md`](./README.md)), sino **la forma en que decidimos organizarnos**: quién es dueño de qué, en qué orden se entrega, cómo usamos Git y GitHub y cómo nos comunicamos.

## Ruta rápida

1. Prepara tu entorno de Python ([sección 4](#4-entorno-de-trabajo)).
2. Clona el repositorio y crea **tu** rama ([sección 5](#5-git-y-github)).
3. Abre la guía de tu fase en [`guias/`](./guias/) y trabaja **solo en tus archivos** ([sección 1](#1-cada-archivo-tiene-un-solo-dueño)).
4. Haz commits pequeños, sube tu rama y abre un pull request cuando algo funcione.
5. Avisa por WhatsApp con el formato de la [sección 7](#7-comunicación-por-whatsapp).

---

## 1. Cada archivo tiene un solo dueño

Si dos personas nunca editan el mismo archivo, no hay conflictos al unir las ramas. Esa es la regla más importante de este documento.

| Integrante | Fase | Archivos a su cargo |
|---|---|---|
| Mateo | 1 | `scripts/fase1_exploracion.py`, `docs/fase1_origen_datos.md`, `docs/figuras/fase1_*.png` |
| Pamela | 2 | `scripts/fase2_preprocesamiento.py`, `data/processed/winequality-red-limpio.csv`, `docs/fase2_preprocesamiento.md`, `docs/figuras/fase2_*.png` |
| Braulio | 3A | `scripts/fase3_entrenamiento.py`, `data/processed/predicciones.csv`, `docs/fase3_entrenamiento.md` |
| Octavio | 3B | `scripts/fase3_evaluacion.py`, `data/processed/metricas_modelo.csv`, `docs/fase3_evaluacion.md`, `docs/figuras/fase3_*.png` |
| Ximena | 4 | Todo lo que va en `docs/dashboard/` |
| Fátima | 5 | Todo lo que va en `docs/presentacion/` |

Archivos de organización (`README.md`, este documento, `guias/`, `.github/`, `requirements.txt`, `.gitignore`): los mantiene Octavio. Si necesitas un cambio en ellos, pídelo por WhatsApp.

El notebook `notebooks/NaiveBayes.ipynb` es **compartido** y se edita por turnos ([sección 6](#6-notebook-integrador-por-turnos)).

## 2. Plan de entrega por hitos

Todos empiezan al mismo tiempo. Nadie se queda esperando sin hacer nada: mientras llega el archivo de otra fase, se avanza con el CSV crudo y con el [contrato de datos](./README.md#6-contrato-de-datos) del README.

| Hito | Qué se cierra | Quién | Desbloquea a |
|:---:|---|---|---|
| H0 | Organización del repositorio en `main` | Octavio | Todos |
| H1 | Exploración de datos (fase 1) en `main` | Mateo | Fátima (cifras de datos) |
| H1 | CSV limpio (fase 2) en `main` | Pamela | Braulio y Octavio |
| H2 | Configuración final del modelo y `metricas_modelo.csv` en `main` | Octavio | Braulio, Ximena y Fátima |
| H2 | `predicciones.csv` con el modelo final en `main` | Braulio | Ximena |
| H3 | Dashboard y capturas en `main` | Ximena | Fátima |
| H4 | Presentación y guion en `main` | Fátima | Cierre |
| H5 | Notebook integrador completo en `main` y resultados en el README | Todos | Entrega |

### Qué hace cada quien mientras espera

| Integrante | Puede avanzar desde el inicio con... | Cuando llega lo que necesita... |
|---|---|---|
| Mateo | El CSV crudo | No depende de nadie |
| Pamela | El CSV crudo | No depende de nadie |
| Braulio | El CSV crudo, aplicando el mismo renombrado de columnas que Pamela | Cambia la ruta al CSV limpio y aplica la configuración final de Octavio |
| Octavio | El CSV crudo, con el mismo renombrado | Cambia la ruta al CSV limpio y vuelve a ejecutar |
| Ximena | El CSV crudo para las páginas 1 y 2, la paleta de colores y el diseño | Cambia el origen de datos en Power Query a `predicciones.csv` y arma las páginas 3 y 4 |
| Fátima | Estructura de la presentación, problemática y marco teórico | Completa cifras, figuras y capturas |

## 3. Reglas del equipo

1. **Nadie trabaja directo sobre `main`.** Todo llega a `main` mediante un pull request.
2. **Nadie modifica `data/raw/winequality-red.csv`.** Cualquier transformación se guarda en `data/processed/`.
3. **Solo rutas relativas** (`data/raw/...` o `pathlib.Path`). Nunca `C:\Users\...` ni `/home/...`.
4. **Cada quien sube solo sus archivos** (tabla de la sección 1).
5. **Si usas IA, que sea para entender, no para copiar.** En la defensa tienes que poder explicar cada línea de tu trabajo.
6. **Si llevas más de 30 minutos trabado, pide ayuda** con un mensaje `[BLOQUEO]`. Es mejor que pierda tiempo una persona y no todo el equipo.

## 4. Entorno de trabajo

### Opción A: Anaconda (Spyder o Jupyter), recomendada

1. Instala [Anaconda Distribution](https://www.anaconda.com/download). Ya incluye Python, Spyder, Jupyter, pandas, numpy, scikit-learn y matplotlib.
2. En *Anaconda Prompt* o en la terminal, verifica que tengas todo:
   ```bash
   conda install pandas numpy scikit-learn matplotlib seaborn jupyter -y
   ```
3. **En Spyder:** en la esquina superior derecha selecciona como directorio de trabajo la carpeta raíz `Naive-Bayes` (donde está el `README.md`). Así funcionan las rutas relativas.
4. **En Jupyter:** abre la terminal en la carpeta del proyecto y ejecuta `jupyter notebook`.

### Opción B: Python con entorno virtual (VS Code o terminal)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Prueba rápida

Desde la raíz del proyecto, ejecuta:

```python
import pandas as pd, numpy, sklearn, matplotlib, seaborn
df = pd.read_csv("data/raw/winequality-red.csv")
print(df.shape)
```

Si ves `(1599, 12)`, tu entorno está listo.

## 5. Git y GitHub

### 5.1 Configuración inicial (una sola vez)

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "correo_de_tu_cuenta_de_github@ejemplo.com"
git clone https://github.com/XimenaBecOliv07/Naive-Bayes.git
cd Naive-Bayes
```

Usa el correo de tu cuenta de GitHub para que tus commits aparezcan a tu nombre. La rúbrica revisa los commits de cada integrante.

### 5.2 Crear tu rama (una sola vez)

El formato de las ramas es `nombre-faseN-tema`:

```bash
git switch main
git pull origin main
git switch -c mateo-fase1-origen-datos      # usa el nombre de tu rama
```

| Integrante | Rama |
|---|---|
| Mateo | `mateo-fase1-origen-datos` |
| Pamela | `pamela-fase2-preprocesamiento` |
| Braulio | `braulio-fase3-entrenamiento` |
| Octavio | `octavio-fase3-evaluacion` |
| Ximena | `ximena-fase4-dashboard` |
| Fátima | `fatima-fase5-presentacion` |

Las ramas viejas (`Braulio_Equipo_4`, `Pamela_Equipo_4`, `octavio`) no tienen trabajo propio y se borrarán. No trabajes en ellas.

### 5.3 Ciclo de trabajo

Repite este ciclo cada vez que algo funcione. No esperes a terminar todo para hacer un solo commit gigante.

```bash
git status                                   # 1. qué cambiaste
git add scripts/fase1_exploracion.py         # 2. agrega SOLO tus archivos
git commit -m "feat(fase1): calcular estadisticas descriptivas"   # 3. commit
git push -u origin mateo-fase1-origen-datos  # 4. sube tu rama (después basta con git push)
```

### 5.4 Formato de los commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/es/v1.0.0/) con la fase como *scope*: `tipo(faseN): descripción en minúsculas`.

| Tipo | Cuándo usarlo | Ejemplo |
|---|---|---|
| `feat` | Código o análisis nuevo | `feat(fase2): eliminar duplicados y crear clases de calidad` |
| `fix` | Corregir algo que estaba mal | `fix(fase3): corregir ruta del csv limpio` |
| `docs` | Documentación, reportes, guion, presentación | `docs(fase1): documentar diccionario de variables` |
| `chore` | Mantenimiento que no cambia resultados | `chore(fase4): agregar capturas del dashboard` |

### 5.5 Traer el trabajo de otros

Cuando alguien avisa por WhatsApp que su fase ya está en `main` y tú la necesitas, ejecuta **dentro de tu rama**:

```bash
git pull origin main
```

Esto mezcla lo nuevo de `main` en tu rama. Como cada quien edita archivos distintos, no debería haber conflictos.

### 5.6 Pull request y revisión

1. Entra al repositorio en GitHub, pulsa **Compare & pull request** y elige `main` como destino.
2. Llena la plantilla del pull request.
3. Avisa por WhatsApp con `[PR]`.
4. El PR lo revisa **quien depende de tu trabajo**. Así cada quien lee a fondo justo lo que va a usar:

| Autor del PR | Revisa |
|---|---|
| Mateo (fase 1) | Pamela |
| Pamela (fase 2) | Braulio |
| Braulio (fase 3A) | Octavio |
| Octavio (fase 3B) | Braulio |
| Ximena (fase 4) | Fátima |
| Fátima (fase 5) | Ximena |
| Organización del repositorio | Ximena |

5. Quien revisa deja comentarios o aprueba, y después hace merge con **Create a merge commit**. **Nunca uses *Squash and merge***, porque borra los commits individuales que evalúa la rúbrica.
6. Quien hizo merge avisa con `[MERGE]`.

## 6. Notebook integrador por turnos

El notebook `notebooks/NaiveBayes.ipynb` lo escribimos entre todos para que cada uno entienda las fases de los demás. El problema es que un `.ipynb` es un archivo JSON con salidas y contadores de ejecución: si dos personas lo editan al mismo tiempo, Git no puede mezclar los cambios.

**Solución: una rama aparte y turnos.**

- El notebook vive en la rama compartida **`notebook-integrador`**, separada de las ramas de cada fase. Si algo sale mal ahí, no afecta el trabajo de nadie más.
- Solo una persona edita a la vez. El turno se pide y se libera por WhatsApp.
- Git también te protege: si alguien subió cambios antes que tú, tu `git push` será rechazado y tendrás que hacer `git pull` primero. Si eso pasa, avisa antes de continuar.

| Turno | Integrante | Sección |
|:---:|---|---|
| 1 | Mateo | Fase 1: origen y exploración |
| 2 | Pamela | Fase 2: preprocesamiento |
| 3 | Braulio | Fase 3A: entrenamiento |
| 4 | Octavio | Fase 3B: evaluación y optimización |
| 5 | Ximena | Fase 4: indicadores y descripción del dashboard |
| 6 | Fátima | Fase 5: conclusiones (y ejecución final completa) |

Tu turno empieza cuando tu fase ya está en `main` y la persona anterior liberó el notebook.

### Pasos de tu turno

1. Avisa por WhatsApp: `[NOTEBOOK] tomo - tu nombre`.
2. Cambia a la rama del notebook y actualízala:
   ```bash
   git switch notebook-integrador
   git pull origin notebook-integrador
   git merge origin/main          # trae los CSV y scripts ya aprobados
   ```
   Si es tu primera vez, antes ejecuta `git fetch origin`.
3. Abre el notebook y **ejecuta y lee todas las secciones anteriores**. Esta es la parte donde aprendes las otras fases: no escribas la tuya sin entender de dónde vienen tus datos.
4. Escribe **solo tu sección**: código y celdas de interpretación con tus palabras.
5. Ejecuta *Kernel > Restart & Run All* y verifica que todo corre sin errores.
6. Sube tus cambios:
   ```bash
   git add notebooks/NaiveBayes.ipynb
   git commit -m "feat(fase2): agregar seccion de preprocesamiento al notebook"
   git push origin notebook-integrador
   ```
7. Avisa por WhatsApp: `[NOTEBOOK] libero - tu nombre`.
8. Regresa a tu rama: `git switch nombre-de-tu-rama`.

Al terminar el turno 6 se abre un pull request de `notebook-integrador` hacia `main`. Lo revisa todo el equipo.

## 7. Comunicación por WhatsApp

Fija en el grupo un mensaje con la tabla de hitos de la sección 2 y márcala conforme se cumpla. Usa estos prefijos para que los mensajes se lean de un vistazo:

| Prefijo | Uso | Ejemplo |
|---|---|---|
| `[INICIO]` | Empiezas a trabajar | `[INICIO] Pamela - fase2 - arranco limpieza` |
| `[PR]` | Abriste un pull request | `[PR] Pamela - fase2 - <link> - listo para revisar` |
| `[MERGE]` | Hiciste merge a `main` | `[MERGE] fase2 en main - Braulio y Octavio hagan pull` |
| `[MODELO]` | Octavio comparte la configuración final | `[MODELO] variables: ... - var_smoothing: ...` |
| `[NOTEBOOK]` | Tomas o liberas el notebook | `[NOTEBOOK] tomo - Mateo` |
| `[BLOQUEO]` | Llevas más de 30 minutos trabado | `[BLOQUEO] Braulio - fase3 - no carga el csv` |
| `[LISTO]` | Terminaste tu fase | `[LISTO] Mateo - fase1` |

## 8. Defensa (26 de noviembre, 30 minutos)

| Minutos | Integrante | Tema |
|---|---|---|
| 0 a 3 | Fátima | Introducción, problemática y objetivos |
| 3 a 8 | Mateo | Fase 1: origen y exploración de datos |
| 8 a 13 | Pamela | Fase 2: preprocesamiento y hallazgos |
| 13 a 17 | Braulio | Fase 3A: fundamento de Naive Bayes y entrenamiento |
| 17 a 21 | Octavio | Fase 3B: evaluación, matriz de confusión y comparación |
| 21 a 26 | Ximena | Fase 4: demostración en vivo del dashboard |
| 26 a 28 | Fátima | Fase 5: conclusiones, limitaciones y trabajo futuro |
| 28 a 30 | Todos | Preguntas |

Los seis integrantes van con traje formal: la rúbrica penaliza a todo el equipo si falta uno.

## 9. Documentación de referencia

- Libro oficial de Git en español: https://git-scm.com/book/es/v2
- Crear un pull request en GitHub: https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
- Conventional Commits: https://www.conventionalcommits.org/es/v1.0.0/
- Documentación de Jupyter: https://docs.jupyter.org/en/latest/
