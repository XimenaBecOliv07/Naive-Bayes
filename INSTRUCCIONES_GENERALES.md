# 🛠️ Instrucciones Generales: Orden de Trabajo, Entorno (Jupyter / Spyder) y Git

Este documento es la guía base para los **6 integrantes del equipo (Xime, Mateo, Pame, Brau, Tavo y Fátima)**. Léelo completo antes de abrir la guía individual que te toca en la carpeta [`guias/`](./guias/).

---

## ⏳ 1. Orden de Trabajo: ¿Quién tiene que acabar para que empiece el otro?

Como estamos haciendo el proyecto **desde cero y por nuestra cuenta**, los datos pasan de mano en mano como en una línea de producción. Sin embargo, **nadie tiene que esperar sin hacer nada**:

### Etapa 1: Arranque inmediato (Pueden empezar YA en paralelo)
- **Xime (`xime-repositorio-readme`):** Configura las reglas del repositorio en GitHub y supervisa la estructura.
- **Mateo (`mateo-origen-datos`):** El archivo original `data/raw/winequality-red.csv` ya está en el repositorio. Mateo ya puede cargarlo en Spyder o Jupyter, analizar sus columnas, contar filas/valores y redactar `docs/fase1_origen_datos.md`.
- **Pame (`pame-preprocesamiento`):** Como `data/raw/winequality-red.csv` ya está disponible, Pame **también puede empezar desde el primer día** a programar `scripts/preprocesamiento.py` para limpiar los duplicados, crear las columnas `calidad_bin` y `calidad_3`, y generar **`data/processed/winequality-red-limpio.csv`**.

### Etapa 2: Depende de que Pame termine
- **Brau (`brau-modelo-naive-bayes`):**
  - **¿Qué necesita de Pame?** Necesita el archivo `data/processed/winequality-red-limpio.csv` que Pame sube a `main`.
  - **¿Cómo puede adelantar mientras Pame termina?** Puede ir escribiendo su script `scripts/modelo_nb.py` y su Notebook probando temporalmente con `data/raw/winequality-red.csv`. En cuanto Pame suba el archivo limpio a `main`, Brau solo hace `git pull origin main`, cambia la ruta a `winequality-red-limpio.csv`, lo ejecuta y exporta **`data/processed/predicciones.csv`** y **`data/processed/metricas_modelo.csv`**.

### Etapa 3: Dependen de que Brau termine
- **Tavo (`octavio` / `tavo-dashboard-bi`):**
  - **¿Qué necesita de Brau?** Necesita `data/processed/predicciones.csv` y `data/processed/metricas_modelo.csv` para conectarlos a Power BI Desktop.
  - **¿Cómo puede adelantar mientras Brau termina?** Puede instalar Power BI Desktop, preparar la plantilla visual con la paleta de colores vino (`#722F37`, `#C98B92`, `#F7EFE5`), y redactar las fórmulas DAX en `docs/dashboard/guia_power_bi.md`.
- **Fátima (`fatima-presentacion-defensa`):**
  - **¿Qué necesita del equipo?** Las cifras de Mateo y Pame, los resultados del modelo de Brau y las capturas del dashboard de Tavo.
  - **¿Cómo puede adelantar desde el Día 1?** Puede crear la estructura de las 12 diapositivas en PowerPoint (portada, problemática de negocio, marco teórico de Naive Bayes y estructura del guion en `docs/presentacion/guion.md`).

---

## 💻 2. Cómo Preparar tu Entorno en Spyder o Jupyter Notebook

Para que a todos nos corra el código exactamente igual y sin errores de *"ModuleNotFoundError"* o *"FileNotFoundError"*, sigue estos pasos según el programa que uses:

### Opción A: Si usas Anaconda (Spyder o Jupyter Notebook) — *Recomendado*

1. **Instalar Anaconda:** Si aún no lo tienes, descarga e instala [Anaconda Distribution](https://www.anaconda.com/download) (ya incluye Python, **Spyder**, **Jupyter Notebook**, `pandas`, `numpy`, `scikit-learn` y `matplotlib`).
2. **Verificar que tienes todas las librerías:**
   - Abre **Anaconda Prompt** (en Windows búscalo en el menú Inicio) o tu Terminal (Mac/Linux).
   - Ejecuta este comando para asegurarte de tener todo instalado:
     ```bash
     conda install pandas numpy scikit-learn matplotlib seaborn jupyter -y
     ```
3. **⚠️ PASO CRÍTICO EN SPYDER: Configurar el Directorio de Trabajo (Working Directory)**
   - El error más común en equipo es poner rutas de tu propia computadora como `pd.read_csv("C:/Users/Juan/Desktop/winequality-red.csv")`. **¡NUNCA hagas eso!** Si subes eso a GitHub, a tus compañeros les marcará error porque ellos no tienen tu carpeta `C:/Users/Juan`.
   - **Cómo hacerlo bien en Spyder:**
     1. Abre Spyder.
     2. Mira en la **esquina superior derecha** de Spyder (donde aparece una ruta de carpeta junto a un ícono de carpeta 📂).
     3. Haz clic en ese ícono de carpeta 📂 y selecciona la carpeta raíz del repositorio **`Naive-Bayes`** (donde está este archivo `README.md`).
     4. Ahora siempre podrás leer los archivos usando rutas relativas limpias:
        ```python
        import pandas as pd
        df = pd.read_csv("data/raw/winequality-red.csv")
        ```
4. **Cómo abrir Jupyter Notebook en la carpeta correcta:**
   - Abre **Anaconda Prompt** o tu terminal, entra a la carpeta del proyecto y lanza Jupyter:
     ```bash
     cd ruta/a/tu/carpeta/Naive-Bayes
     jupyter notebook
     ```
   - Se abrirá en tu navegador viendo todas las carpetas del proyecto (`data/`, `notebooks/`, `scripts/`).

---

### Opción B: Si usas VS Code o Terminal con Python puro (`.venv`)

1. Abre la terminal dentro de la carpeta `Naive-Bayes`.
2. Crea un entorno virtual para no mezclar librerías:
   ```bash
   python -m venv .venv
   ```
3. Activa el entorno virtual:
   - **En Windows (PowerShell o CMD):**
     ```bash
     .venv\Scripts\activate
     ```
   - **En Linux o Mac:**
     ```bash
     source .venv/bin/activate
     ```
4. Instala las librerías del proyecto con un solo comando:
   ```bash
   pip install -r requirements.txt
   ```

---

### ✅ Prueba Rápida: Verifica que tu Entorno Funciona
Antes de empezar tu tarea, abre **Spyder** o una celda de **Jupyter Notebook** (ubicado en la raíz de `Naive-Bayes`) y ejecuta estas 8 líneas:

```python
import pandas as pd
import numpy as np
import sklearn
import matplotlib
import seaborn as sns

df = pd.read_csv("data/raw/winequality-red.csv")
print("¡Entorno listo! Filas y columnas cargadas:", df.shape)
```
Si en la consola ves:
`¡Entorno listo! Filas y columnas cargadas: (1599, 12)`
¡Ya tienes tu entorno 100 % configurado para trabajar!

---

## 🌿 3. Guía Paso a Paso de Git y GitHub para Todo el Equipo

La rúbrica evalúa que **los 6 integrantes** tengan su propia rama, sus propios commits descriptivos y su Pull Request en GitHub. Sigue estos 6 pasos:

### Paso 1: Configurar tu nombre y correo en Git (solo la primera vez)
Usa el mismo correo de tu cuenta de GitHub para que tus commits aparezcan con tu foto de perfil:
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo_de_github@ejemplo.com"
```

### Paso 2: Clonar el repositorio en tu computadora
```bash
git clone https://github.com/XimenaBecOliv07/Naive-Bayes.git
cd Naive-Bayes
```

### Paso 3: Crear y cambiarte a TU rama personal
Revisa cuál es el nombre exacto de tu rama y créala a partir de `main`:
```bash
git checkout main
git pull origin main
git checkout -b nombre-de-tu-rama
```
- **Xime:** `git checkout -b xime-repositorio-readme`
- **Mateo:** `git checkout -b mateo-origen-datos`
- **Pame:** `git checkout -b pame-preprocesamiento`
- **Brau:** `git checkout -b brau-modelo-naive-bayes`
- **Tavo:** `git checkout -b octavio` *(o `tavo-dashboard-bi`)*
- **Fátima:** `git checkout -b fatima-presentacion-defensa`

### Paso 4: ¿Cómo traer los archivos cuando el compañero anterior ya terminó?
Por ejemplo, cuando **Pame** termine y sus cambios ya estén en `main`, **Brau** debe ejecutar esto dentro de su rama para recibir el CSV limpio de Pame:
```bash
git pull origin main
```

### Paso 5: Guardar tu avance (Commits) y subirlo a GitHub (Push)
Cada vez que termines un archivo o avance importante en tu guía:
1. Revisa qué archivos modificaste:
   ```bash
   git status
   ```
2. Agrega **únicamente** los archivos que te tocan a ti:
   ```bash
   git add ruta/de/tu/archivo
   ```
3. Crea un commit con un mensaje claro en español:
   - Usa `feat:` para código o análisis nuevo
   - Usa `data:` para archivos CSV de datos
   - Usa `docs:` para documentación, guiones o presentaciones
   ```bash
   git commit -m "feat: descripcion clara de lo que hiciste"
   ```
4. Sube tu rama a GitHub:
   ```bash
   git push -u origin nombre-de-tu-rama
   ```

### Paso 6: Crear tu Pull Request (PR) en GitHub
1. Entra a [https://github.com/XimenaBecOliv07/Naive-Bayes](https://github.com/XimenaBecOliv07/Naive-Bayes) en tu navegador.
2. Verás un botón verde arriba que dice **"Compare & pull request"**. Haz clic ahí.
3. Llena las preguntas breves de la plantilla, crea el Pull Request y avisa por el grupo de WhatsApp para que otro compañero lo revise y le dé **"Merge pull request"** hacia `main`.

---

## 🚫 4. Las 4 Reglas de Oro del Equipo
1. **Prohibido trabajar directo sobre `main`:** Todo el trabajo se hace en tu rama personal y llega a `main` mediante un Pull Request.
2. **Prohibido tocar `data/raw/winequality-red.csv`:** Los datos crudos originales nunca se sobrescriben; cualquier limpieza se guarda en `data/processed/`.
3. **Prohibido usar rutas absolutas (`C:\Users\...`):** Siempre usa rutas relativas desde la raíz del proyecto (`data/raw/...` o `pathlib.Path`).
4. **Cada quien sube solo sus archivos asignados:** Así evitamos conflictos al unir las ramas en GitHub.
