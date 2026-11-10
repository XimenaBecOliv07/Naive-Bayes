# 👩‍💻 Guía 1 · Xime: Líder del Proyecto, Repositorio e Integración

- **Integrante:** Xime
- **Rama asignada:** `xime-repositorio-readme`
- **¿Cuándo puedes empezar?:** **Desde el Día 1** (no dependes de que nadie termine antes).
- **Archivos que están a tu cargo:**
  - `README.md` (actualizar los resultados finales conforme el equipo avance)
  - `.github/pull_request_template.md`
  - `requirements.txt` y `.gitignore`
  - Revisión y aprobación (*Merge*) de los Pull Requests de Mateo, Pame, Brau, Tavo y Fátima.

---

## 🎯 1. ¿Cuál es tu objetivo en el proyecto?
Como líder del repositorio, tu responsabilidad es:
1. Asegurar que todos los integrantes sean **Colaboradores** en GitHub (`Settings > Collaborators > Add people`).
2. Mantener la rama `main` limpia, ordenada y funcionando sin errores.
3. Redactar en el `README.md` el planteamiento del problema de negocio de la bodega de vino tinto y, cuando Brau termine el modelo, actualizar la tabla de resultados finales en el `README.md`.
4. En la defensa oral (primeros 3 minutos), presentar al equipo y explicar **por qué una bodega pierde dinero con catas manuales tardías** y cómo nuestro modelo Naive Bayes resuelve ese problema.

---

## 🛠️ 2. Paso a Paso: Lo que debes hacer desde cero

### Paso 1: Dar acceso al equipo en GitHub
1. Entra a tu repositorio en GitHub: `https://github.com/XimenaBecOliv07/Naive-Bayes`
2. Ve a **Settings** (pestaña superior) $\rightarrow$ **Collaborators** (menú izquierdo) $\rightarrow$ **Add people**.
3. Agrega los usuarios de GitHub de **Mateo, Pame, Brau, Tavo y Fátima** y pídeles que acepten la invitación en su correo.

### Paso 2: Clonar el repositorio y crear tu rama
Abre tu terminal o Git Bash y ejecuta:
```bash
git clone https://github.com/XimenaBecOliv07/Naive-Bayes.git
cd Naive-Bayes
git checkout main
git pull origin main
git checkout -b xime-repositorio-readme
```

### Paso 3: Verificar el entorno base en Spyder o Jupyter
1. Abre Spyder o Jupyter Notebook siguiendo [`INSTRUCCIONES_GENERALES.md`](../INSTRUCCIONES_GENERALES.md).
2. Verifica que el archivo `requirements.txt` tenga todas las librerías que ocuparán Mateo, Pame y Brau (`pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `jupyter`).
3. Revisa y personaliza `.github/pull_request_template.md` y `README.md` (agregando los nombres completos y matrículas de los 6 integrantes en la sección de Equipo).

### Paso 4: Hacer tus commits y subir tu rama
```bash
git status
git add README.md .github/pull_request_template.md
git commit -m "docs: agregar nombres completos del equipo y detallar problematica de negocio"
git push -u origin xime-repositorio-readme
```
Después entra a GitHub, abre tu **Pull Request** de `xime-repositorio-readme` hacia `main` y hazle **Merge**.

---

## 🔄 3. Cómo Coordinar el Orden de los Pull Requests del Equipo

Para que el proyecto avance sin bloqueos, coordina las entregas en este orden:

1. **Primero (Día 1-2):** Revisa y aprueba los Pull Requests de **Mateo** (`mateo-origen-datos`) y **Pame** (`pame-preprocesamiento`).
   - *Qué verificar en el PR de Pame:* Que exista `scripts/preprocesamiento.py` y que haya generado `data/processed/winequality-red-limpio.csv` con **1,359 filas**.
2. **Segundo (Día 3-4):** Avisa a **Brau** que ya está listo el CSV limpio en `main`. Cuando Brau termine, revisa su PR (`brau-modelo-naive-bayes`).
   - *Qué verificar en el PR de Brau:* Que su código use `StandardScaler` y `GaussianNB`, y que haya generado `data/processed/predicciones.csv` y `data/processed/metricas_modelo.csv`.
3. **Tercero (Día 5-6):** Avisa a **Tavo** y **Fátima** que ya están las predicciones en `main` para que terminen el Dashboard en Power BI y la presentación final.
4. **Cierre final:** Cuando Brau tenga las métricas definitivas (Accuracy y F1-Score), vuelve a entrar a tu rama `xime-repositorio-readme`, anota la tabla de resultados finales en `README.md` y haz un segundo commit y PR.

---

## 🎤 4. Qué te toca decir en la Defensa (Minuto 0 al 3)
- **Diapositivas 1 y 2 (Portada y Problemática de Negocio):**
  - Explica qué problema real tiene la bodega: evaluar el vino únicamente con catadores humanos es lento, costoso y ocurre cuando la fermentación ya terminó.
  - Explica cuál es nuestra propuesta: aprovechar las **11 mediciones fisicoquímicas de laboratorio** (acidez, alcohol, sulfatos, pH, etc.) para clasificar automáticamente con **Naive Bayes** si un lote saldrá *bueno* o *malo* y priorizar qué lotes auditar antes de embotellar.
