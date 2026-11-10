# 👩‍💻 Guía 6 · Fátima: Fases 5 y 6 (Conclusiones de Negocio, Presentación y Defensa)

- **Integrante:** Fátima
- **Rama asignada:** `fatima-presentacion-defensa`
- **¿Cuándo puedes empezar?:** **Desde el Día 1** puedes armar el esqueleto de las 12 diapositivas, el diseño visual y el guion base; conforme Mateo, Pame, Brau y Tavo suban sus gráficas y capturas a `main`, las integras en las diapositivas.
- **Archivos que debes crear y subir:**
  - `docs/presentacion/guion.md` (guion cronometrado de 30 minutos + conclusiones de negocio + banco de preguntas y respuestas)
  - `docs/presentacion/Presentacion_Naive_Bayes.pptx` (la presentación ejecutiva del equipo)

---

## 🎯 1. ¿Cuál es tu objetivo en el proyecto?
Eres la responsable de las **Fases 5 y 6: Interpretación de Resultados, Presentación Ejecutiva y Coordinación de la Defensa**. Tu trabajo une todo el esfuerzo del equipo en una narrativa clara para el profesor **Ing. Rafael Hernández López**:
1. Redactar las **conclusiones de negocio** (cómo usa la bodega el modelo en la vida real), las **limitaciones técnicas** de Naive Bayes y las propuestas de **trabajo futuro**.
2. Construir la presentación en PowerPoint (`docs/presentacion/Presentacion_Naive_Bayes.pptx`) con 12 diapositivas limpias (poco texto, gráficas grandes y colores vino `#722F37`).
3. Elaborar el guion de tiempos (`docs/presentacion/guion.md`) y el **Banco de Preguntas de Defensa** para que los 6 integrantes sepan responder cualquier pregunta del profesor.

---

## 🛠️ 2. Paso a Paso: Cómo construir el Guion y la Presentación desde cero

### Paso 1: Clonar el repositorio y crear tu rama
```bash
git clone https://github.com/XimenaBecOliv07/Naive-Bayes.git
cd Naive-Bayes
git checkout main
git pull origin main
git checkout -b fatima-presentacion-defensa
```

---

### Paso 2: Estructura de las 12 Diapositivas en PowerPoint (`Presentacion_Naive_Bayes.pptx`)
Crea una presentación limpia en PowerPoint o Canva (exportada a `.pptx`) siguiendo exactamente este orden para los 30 minutos de defensa:

| Diapositiva | Título sugerido | Quién expone | Tiempo | Qué debe incluir (visuales y puntos clave) |
| :---: | :--- | :---: | :---: | :--- |
| **1** | **Portada:** Predicción de la Calidad del Vino Tinto con Naive Bayes | Xime | 0:00 - 1:00 | Nombres de los 6 integrantes, Grupo 219900, Ing. Rafael Hernández López. |
| **2** | **Problemática de Negocio y Objetivo** | Xime | 1:00 - 3:00 | Costo de catas tardías vs. predicción temprana con 11 variables de laboratorio. |
| **3** | **Fase 1: Origen del Dataset (UCI Wine Quality)** | Mateo | 3:00 - 5:30 | 1,599 registros originales, 12 columnas (Cortez et al., 2009), tabla resumen de las variables químicas. |
| **4** | **Distribución de la Calidad (`quality`)** | Mateo | 5:30 - 8:00 | Gráfica `docs/distribucion_quality.png` mostrando que 82 % de los lotes son calidad 5 o 6 (desbalance en extremos). |
| **5** | **Fase 2: Limpieza y Preprocesamiento** | Pame | 8:00 - 10:30 | Flujo: 0 nulos $\rightarrow$ eliminación de 240 duplicados $\rightarrow$ 1,359 lotes únicos $\rightarrow$ corte binario (`bueno` $\ge 6$, `malo` $\le 5$). |
| **6** | **Hallazgos Químicos y Correlaciones** | Pame | 10:30 - 13:00 | Por qué se conservan los *outliers* y las 3 variables más correlacionadas: Alcohol (+), Sulfatos (+) y Acidez Volátil (-). |
| **7** | **Fase 3: Fundamento de Gaussian Naive Bayes** | Brau | 13:00 - 15:00 | Fórmula del Teorema de Bayes, uso de `StandardScaler` dentro de `Pipeline` (sin fuga de datos) y Validación Cruzada (5 pliegues). |
| **8** | **Comparativa de Experimentos** | Brau | 15:00 - 17:30 | Tabla comparativa: Línea base (0.53) vs. 3 Clases (0.58) vs. Binario 11 vars (0.74) vs. **Binario 3 vars (0.75)**. |
| **9** | **Matriz de Confusión del Modelo Final** | Brau | 17:30 - 20:00 | Imagen `docs/modelo_final.png` explicando aciertos (204 de 272 lotes en prueba) y balance entre falsos positivos y negativos. |
| **10** | **Fase 4: Dashboard Interactivo en Power BI** | Tavo | 20:00 - 25:00 | Capturas de respaldo de las 4 páginas del Dashboard mientras Tavo hace la **Demo en Vivo**. |
| **11** | **Fase 5: Conclusiones de Negocio, Limitaciones y Trabajo Futuro** | Fátima | 25:00 - 28:00 | Tus conclusiones estratégicas (ver sección abajo). |
| **12** | **Defensa y Sesión de Preguntas** | Todos | 28:00 - 30:00 | Resumen final de cierre y apertura a preguntas del docente. |

---

### Paso 3: Redactar tus Conclusiones (Fase 5) y el Guion en `docs/presentacion/guion.md`
Crea el archivo **`docs/presentacion/guion.md`** incluyendo:

1. **Tus 3 Conclusiones de Negocio (lo que tú expondrás en la Diapositiva 11):**
   - **Impacto operativo:** Con solo **3 mediciones rutinarias de laboratorio (`alcohol`, `volatile_acidity` y `sulphates`)**, la bodega puede anticipar correctamente la calidad en **3 de cada 4 lotes (75 % Accuracy)** antes de pasar a embotellado.
   - **El modelo prioriza, no reemplaza al enólogo:** El clasificador sirve como un "semáforo de alerta temprana" para que los catadores revisen primero los lotes marcados como `lote_en_riesgo` y corrijan procesos de fermentación (por ejemplo, cuando sube el ácido acético).
   - **Limitaciones honestas y trabajo futuro:**
     1. *Supuesto de independencia:* Naive Bayes asume que las variables son independientes, lo cual en química del vino solo se cumple parcialmente (por eso seleccionar 3 variables funcionó mejor que meter las 11).
     2. *Subjetividad de la etiqueta:* La variable `quality` proviene de catadores humanos y no incluye variables de aroma, tipo de uva o barrica.
     3. *Trabajo futuro:* Comparar contra ensambles no lineales (*Random Forest* o *XGBoost*) y conectar el modelo en tiempo real a los sensores de los tanques de fermentación.

2. **El Banco de Preguntas de Defensa (para que estudien los 6):**
   Incluye en `docs/presentacion/guion.md` estas preguntas con su respuesta técnica:
   - *¿Por qué usaron `GaussianNB` y no `MultinomialNB` o `BernoulliNB`?* $\rightarrow$ Porque las 11 variables fisicoquímicas son continuas (números reales), no conteos de palabras ni variables binarias 0/1.
   - *¿Qué pasa si dos variables están muy correlacionadas en Naive Bayes?* $\rightarrow$ El modelo "cuenta doble" la misma información y sobreestima las probabilidades; lo resolvimos quedándonos con las 3 variables clave (`alcohol`, `volatile_acidity`, `sulphates`).
   - *¿Cómo evitaron la fuga de datos (data leakage)?* $\rightarrow$ Dividimos primero en entrenamiento (80 %) y prueba (20 %), y metimos `StandardScaler()` dentro de un `Pipeline` para que la media y desviación estándar se calculen únicamente con los datos de entrenamiento.
   - *¿Por qué convirtieron `quality` en 2 clases (`bueno` $\ge 6$, `malo` $\le 5$)?* $\rightarrow$ Porque en la escala original casi no existen vinos con calificación 3, 4 u 8; al binarizar en $\ge 6$, el dataset queda balanceado (53 % buenos vs 47 % malos) y el Accuracy sube de 0.58 a 0.75.

---

### Paso 4: Subir tu trabajo a GitHub
```bash
git status
git add docs/presentacion/guion.md
git commit -m "docs: redactar conclusiones de negocio, guion de 30 min y banco de preguntas"

git add docs/presentacion/Presentacion_Naive_Bayes.pptx
git commit -m "docs: subir presentacion ejecutiva de 12 diapositivas para la defensa"

git push -u origin fatima-presentacion-defensa
```
Entra a GitHub y abre tu **Pull Request** hacia `main`.

---

## 👔 3. Checklist Logístico para el Día de la Defensa (26 de Noviembre)
Como coordinadora de las Fases 5 y 6, recuérdale a todo el equipo el día anterior:
- **Vestimenta:** Traje formal completo los **6 integrantes** (la rúbrica penaliza a todo el equipo si un integrante no va formal).
- **Respaldo técnico:** Llevar en una memoria USB el Notebook ya ejecutado, el archivo `.pbix` de Power BI, el `.pptx` y las capturas del dashboard en imagen por si falla el internet o Power BI.
- **Ensayo con cronómetro:** Hacer al menos un ensayo en llamada donde cada quien respete su bloque de tiempo para no pasarse de los 30 minutos.
