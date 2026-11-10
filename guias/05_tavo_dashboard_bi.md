# 👨‍💻 Guía 5 · Tavo (Octavio): Fase 4 (Dashboard en Power BI)

- **Integrante:** Tavo (Octavio)
- **Rama asignada:** `octavio` *(o `tavo-dashboard-bi`)*
- **¿De quién dependes?:** Necesitas los archivos `data/processed/predicciones.csv` y `data/processed/metricas_modelo.csv` que genera **Brau (Fase 3)**.
- **Archivos que debes crear y subir:**
  - `docs/dashboard/guia_power_bi.md` (documentación de tus medidas DAX y estructura del tablero)
  - `docs/dashboard/dashboard_vino.pbix` (tu archivo de Power BI Desktop)
  - Capturas de pantalla de las 4 páginas del dashboard en `docs/dashboard/` (`pagina1_resumen.png`, `pagina2_quimico.png`, `pagina3_modelo.png`, `pagina4_explorador.png`) para la presentación de Fátima y como respaldo el día de la defensa.

---

## 🎯 1. ¿Cuál es tu objetivo en el proyecto?
Eres el responsable de la **Fase 4: Dashboard de Inteligencia de Negocios en Power BI**. Tu objetivo es transformar las predicciones del modelo Naive Bayes en una herramienta visual interactiva para el jefe de calidad de la bodega, de modo que pueda:
1. Ver cuántos lotes están en riesgo de salir de mala calidad.
2. Entender visualmente cómo el **alcohol**, la **acidez volátil** y los **sulfatos** separan a los vinos buenos de los malos.
3. Evaluar la confiabilidad del modelo (Accuracy del 75 % y Matriz de Confusión).
4. Filtrar lotes individuales con segmentadores interactivos para decidir qué lotes mandar a cata urgente.

---

## 🛠️ 2. Paso a Paso: Cómo construir el Dashboard desde cero en Power BI Desktop

> 💡 **Nota importante:** Power BI Desktop corre en Windows. Cuando Brau haya subido `data/processed/predicciones.csv` y `data/processed/metricas_modelo.csv` a `main`, descarga los cambios con `git pull origin main` y abre Power BI Desktop.

### Paso 1: Actualizar tu rama con los datos de Brau
```bash
git checkout octavio
git pull origin main
```

### Paso 2: Cargar y verificar los tipos de datos en Power BI
1. Abre **Power BI Desktop** $\rightarrow$ **Inicio > Obtener datos > Texto o CSV**.
2. Selecciona `data/processed/predicciones.csv` y haz clic en **Transformar datos** (Power Query):
   - Cambia el nombre de la tabla en el panel derecho a **`lotes`**.
   - Verifica que las columnas numéricas (`alcohol`, `volatile_acidity`, `sulphates`, `prob_bueno`, etc.) tengan el tipo **Número decimal** (si tu Windows usa coma decimal y el CSV usa punto decimal, haz clic derecho en la columna $\rightarrow$ *Cambiar tipo > Usando configuración regional > Número decimal > Inglés (Estados Unidos)*).
   - Verifica que `y_real`, `y_pred`, `calidad_bin` y `calidad_3` sean tipo **Texto**.
   - Verifica que `quality`, `id_lote`, `acierto` y `lote_en_riesgo` sean **Número entero**.
3. En la misma ventana, haz clic en **Nuevo origen > Texto o CSV**, selecciona `data/processed/metricas_modelo.csv` y nómbrala **`metricas`**.
4. Haz clic arriba a la izquierda en **Cerrar y aplicar**.

---

### Paso 3: Crear las 10 Medidas DAX (Pestaña Modelado > Nueva medida)
Selecciona la tabla `lotes` y crea una por una estas medidas DAX:

```dax
Total Lotes = COUNTROWS(lotes)
```
```dax
% Lotes Buenos = DIVIDE(CALCULATE(COUNTROWS(lotes), lotes[y_real] = "bueno"), [Total Lotes])
```
```dax
Calidad Media = AVERAGE(lotes[quality])
```
```dax
Alcohol Medio = AVERAGE(lotes[alcohol])
```
```dax
Acidez Volatil Media = AVERAGE(lotes[volatile_acidity])
```
```dax
Sulfatos Medios = AVERAGE(lotes[sulphates])
```
```dax
Lotes en Riesgo = SUM(lotes[lote_en_riesgo])
```
```dax
% Lotes en Riesgo = DIVIDE([Lotes en Riesgo], [Total Lotes])
```
```dax
Accuracy Prueba = CALCULATE(MAX(metricas[valor]), metricas[metrica] = "accuracy")
```
```dax
F1 Prueba = CALCULATE(MAX(metricas[valor]), metricas[metrica] = "f1_macro")
```
*(Selecciona las medidas de porcentaje `% Lotes Buenos`, `% Lotes en Riesgo`, `Accuracy Prueba` y `F1 Prueba` y en **Herramientas de medición** dales formato de **Porcentaje `%`**).*

---

### Paso 4: Diseñar las 4 Páginas del Dashboard
Usa una paleta de colores sobria inspirada en vino tinto:
- **Vino tinto oscuro (principal):** `#722F37`
- **Rosa vino suave (secundario):** `#C98B92`
- **Crema claro (fondo de tarjetas):** `#F7EFE5`

#### 📄 Página 1: Resumen Ejecutivo
- **Título superior:** *Panorama General de Calidad en Lotes de Vino Tinto (1,359 Lotes)*
- **4 Tarjetas (Cards) arriba:**
  1. `Total Lotes` (1,359)
  2. `% Lotes Buenos` (52.9 %)
  3. `Calidad Media` (5.62)
  4. `% Lotes en Riesgo`
- **Gráfico de columnas agrupadas:** Eje X = `quality` (3 al 8), Eje Y = `Total Lotes`.
- **Gráfico de anillo (Donut chart):** Leyenda = `y_real` (`bueno` vs `malo`), Valores = `Total Lotes`.

#### 📄 Página 2: Perfil Fisicoquímico
- **Título superior:** *Los lotes buenos se distinguen por mayor alcohol, más sulfatos y menor acidez volátil*
- **Gráfico de barras agrupadas:** Eje = `y_real` (`bueno` vs `malo`), Valores = `Alcohol Medio`, `Acidez Volatil Media`, `Sulfatos Medios`.
- **Gráfico de dispersión (Scatter plot):** Eje X = `alcohol`, Eje Y = `volatile_acidity`, Leyenda = `y_real` (no resumir X ni Y para ver cada lote).
- **Segmentador (Slicer):** `calidad_3` (`baja`, `media`, `alta`).

#### 📄 Página 3: Desempeño del Modelo Naive Bayes
- **Título superior:** *El clasificador Naive Bayes acierta 3 de cada 4 lotes (75 % Accuracy)*
- **3 Tarjetas arriba:** `Accuracy Prueba` (75.0 %), `F1 Prueba` (74.9 %), y `Lotes en Riesgo`.
- **Visual de Matriz (Matriz de Confusión):** Filas = `y_real`, Columnas = `y_pred`, Valores = `Total Lotes` (actívale formato condicional de color de fondo rojo vino).
- **Gráfico de columnas (Distribución de probabilidades):** Eje X = `prob_bueno` (clic derecho en `prob_bueno` $\rightarrow$ *Nuevo grupo > Tamaño de compartimiento = 0.1*), Eje Y = `Total Lotes`.

#### 📄 Página 4: Explorador de Lotes en Riesgo (Para Toma de Decisiones)
- **Título superior:** *Simulador Operativo: Priorización de Lotes para Cata en Bodega*
- **4 Segmentadores (Slicers) a la izquierda:**
  - Rango de `alcohol`
  - Rango de `volatile_acidity`
  - Rango de `sulphates`
  - Botones de `y_pred` (`bueno` / `malo`)
- **Tarjeta destacada:** `Lotes en Riesgo` (cambia dinámicamente al mover las barras de alcohol o acidez).
- **Tabla detallada:** `id_lote`, `alcohol`, `volatile_acidity`, `sulphates`, `y_real`, `y_pred`, `prob_bueno` (ordenada de menor a mayor `prob_bueno` para ver arriba los lotes más críticos).

---

### Paso 5: Guardar, tomar capturas y subir a tu rama `octavio`
1. Guarda el archivo en **`docs/dashboard/dashboard_vino.pbix`**.
2. Toma captura de pantalla de cada una de las 4 páginas y guárdalas en **`docs/dashboard/`**.
3. Documenta tus medidas DAX y cómo usar el tablero en **`docs/dashboard/guia_power_bi.md`**.
4. Sube tus cambios desde la terminal:
```bash
git checkout octavio
git status
git add docs/dashboard/
git commit -m "feat: agregar dashboard interactivo en Power BI, medidas DAX y capturas"
git push -u origin octavio
```
5. Abre tu **Pull Request** en GitHub hacia `main`.

---

## 🎤 3. Qué te toca hacer en la Defensa (Minuto 20 al 25 · Demo en Vivo)
- **Diapositiva 10 (5 minutos de demostración en vivo):**
  1. Muestra la **Página 1**: *"Analizamos 1,359 lotes únicos; el 53 % cumple con el estándar de calidad buena"*.
  2. Pasa a la **Página 2**: Haz clic en la barra de vinos *malos* y muestra cómo automáticamente se observa menor alcohol (< 10 %) y mayor acidez volátil (> 0.6 g/L).
  3. Pasa a la **Página 3**: Señala el Accuracy del 75 % y la matriz de confusión.
  4. Cierra en la **Página 4**: Mueve en vivo el filtro deslizante de `alcohol` hacia abajo (ej. vinos con menos de 10 % de alcohol) y muestra cómo sube el indicador de **Lotes en Riesgo**, explicando: *"Así el jefe de planta sabe exactamente qué lotes mandar a cata urgente hoy mismo"*.
     *(Ten siempre las 4 capturas de pantalla en las diapositivas por si la computadora del salón no tiene Power BI instalado).*
