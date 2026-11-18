# Guía fase 5: Conclusiones, presentación y defensa

| | |
|---|---|
| **Responsable** | Fátima |
| **Rama** | `fatima-fase5-presentacion` |
| **Puedes empezar** | Desde el inicio: estructura, problemática y marco teórico |
| **Dependes de** | Todos: cifras de Mateo y Pamela, resultados de Braulio y Octavio, capturas de Ximena |
| **Dependen de ti** | Todo el equipo para la defensa del 26 de noviembre |
| **Revisa tu PR** | Ximena |
| **Tus archivos** | Todo lo que va en `docs/presentacion/`: `Presentacion_Naive_Bayes.pptx` y `guion.md` |

> Esta guía no te da la presentación hecha. Te da el contexto, los conceptos, las herramientas y pistas para que la construyas tú. Las pistas están ocultas: ábrelas solo si te atoras.

---

## 1. Contexto

Un buen proyecto mal contado pierde puntos. Tu fase convierte el trabajo técnico de todos en una **historia** que el docente y un directivo de la bodega puedan seguir: hay un problema que cuesta dinero, unos datos que lo pueden anticipar, un modelo que lo resuelve con cierta confianza y una herramienta para usarlo.

También eres la responsable de que el equipo llegue preparado: guion con tiempos, banco de preguntas y logística del día.

## 2. Objetivo general

Comunicar los resultados del proyecto en una presentación ejecutiva de 30 minutos y coordinar la defensa del equipo.

## 3. Objetivos específicos

1. Redactar las conclusiones de negocio, las limitaciones del modelo y el trabajo futuro.
2. Construir la presentación ejecutiva con las cifras, figuras y capturas de cada fase.
3. Elaborar el guion cronometrado de la defensa.
4. Reunir el banco de preguntas de defensa y asegurar que cada integrante sepa responder las de su fase.
5. Coordinar la logística del día de la defensa.

## 4. Entradas y salidas

| | Archivo |
|---|---|
| **Entrada** | `docs/fase1_origen_datos.md` y `docs/figuras/fase1_*.png` (Mateo) |
| **Entrada** | `docs/fase2_preprocesamiento.md` y `docs/figuras/fase2_*.png` (Pamela) |
| **Entrada** | `docs/fase3_entrenamiento.md` (Braulio), `docs/fase3_evaluacion.md` y `docs/figuras/fase3_*.png` (Octavio) |
| **Entrada** | Capturas en `docs/dashboard/` (Ximena) |
| **Salida** | `docs/presentacion/Presentacion_Naive_Bayes.pptx` |
| **Salida** | `docs/presentacion/guion.md`: guion, conclusiones, banco de preguntas y logística |

## 5. Conceptos que debes investigar

| Concepto | Pregunta que debes poder responder |
|---|---|
| Presentación ejecutiva | ¿En qué se diferencia de una presentación técnica? ¿Qué le importa a un directivo? |
| Una idea por diapositiva | ¿Por qué el título de cada diapositiva debe ser una conclusión? |
| Limitaciones de un modelo | ¿Por qué reconocerlas da más credibilidad en lugar de quitarla? |
| Trabajo futuro | ¿Qué alternativas existen a Naive Bayes y qué ventaja tendrían? |
| Narrativa | ¿Cómo se conecta cada fase con la siguiente para que la historia fluya? |

## 6. Herramientas

| Necesitas... | Usa |
|---|---|
| Diapositivas | PowerPoint, Google Slides o Canva (exportado a `.pptx`) |
| Paleta del proyecto | Vino `#722F37`, rosa vino `#C98B92`, crema `#F7EFE5` |
| Cifras y figuras | Los reportes `docs/fase*.md` y la carpeta `docs/figuras/` |
| Agenda de la defensa | [Sección 8 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#8-defensa-26-de-noviembre-30-minutos) |

## 7. Ruta de trabajo

### Paso 1: Crea tu rama

Sigue la [sección 5 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#5-git-y-github).

### Paso 2: Esqueleto de la presentación

Desde el inicio, arma la estructura siguiendo la agenda de la defensa. Una sugerencia de bloques: portada, problemática y objetivos, datos, preprocesamiento, fundamento de Naive Bayes, resultados y comparación, matriz de confusión, dashboard, conclusiones, preguntas. Deja marcadores donde irán las cifras y figuras de cada fase.

<details>
<summary>Pista: cuántas diapositivas</summary>

Calcula el tiempo de cada bloque en la agenda. Una diapositiva cada 2 o 3 minutos suele ser un buen ritmo; más diapositivas obligan a correr.
</details>

### Paso 3: Problemática y objetivos

Redacta tus diapositivas de apertura a partir de las secciones 1 a 3 del [README](../README.md). Tú abres la defensa (minutos 0 a 3).

### Paso 4: Integra el trabajo de cada fase

Conforme cada fase llegue a `main` (ejecuta `git pull origin main`), toma sus cifras y figuras. Cada integrante revisa la diapositiva de su fase antes de que la des por terminada.

### Paso 5: Conclusiones, limitaciones y trabajo futuro

Con los resultados de Octavio, redacta:
1. **Conclusiones de negocio:** ¿qué gana la bodega con este modelo y cómo debería usarlo?
2. **Limitaciones:** ¿por qué el modelo no acierta más? Piensa en el origen de la etiqueta `quality`, en el supuesto de independencia y en el tamaño y alcance del dataset.
3. **Trabajo futuro:** ¿qué probarías después?

<details>
<summary>Pista: el papel del modelo</summary>

Pregúntate si el modelo debe **reemplazar** al enólogo o **priorizar** su trabajo. La respuesta define el tono de toda la conclusión.
</details>

### Paso 6: Guion y banco de preguntas

En `docs/presentacion/guion.md` incluye:
1. La agenda con minutos y responsables.
2. Las ideas clave de cada bloque, en puntos, no en texto para leer.
3. El banco de preguntas: reúne las preguntas de la sección 9 de **cada guía** y pide a cada integrante que escriba la respuesta de su fase con sus palabras.
4. La logística del día.

### Paso 7: Ensayo y logística

- Organiza al menos un ensayo completo con cronómetro.
- Respaldo en USB y en la nube: presentación, `.pbix`, capturas del dashboard y notebook ejecutado.
- Recuerda al equipo el traje formal: la rúbrica penaliza a todos si falta uno.

### Paso 8: Commits y pull request

Separa en commits el guion y la presentación.

### Paso 9: Tu sección del notebook (turno 6, el último)

Escribe la sección de conclusiones del notebook y, al final, ejecuta *Kernel > Restart & Run All* para comprobar que el notebook completo corre sin errores. Sigue la [sección 6 de las instrucciones generales](../INSTRUCCIONES_GENERALES.md#6-notebook-integrador-por-turnos).

## 8. Criterios de aceptación

- [ ] La presentación cubre todas las fases en el orden de la agenda.
- [ ] Todas las cifras coinciden con los reportes y el dashboard (sin números inventados ni redondeados de más).
- [ ] Cada diapositiva de fase fue revisada por su responsable.
- [ ] El guion cabe en 30 minutos según el ensayo cronometrado.
- [ ] El banco de preguntas tiene las respuestas de las seis personas.
- [ ] Hay capturas de respaldo del dashboard dentro de la presentación.

## 9. Preparación para la defensa (minutos 0 a 3 y 26 a 28)

Debes poder responder sin leer:
- ¿Cuál es el problema de negocio y por qué importa?
- ¿Qué debería hacer la bodega con los resultados del modelo?
- ¿Cuáles son las tres limitaciones más importantes del proyecto?
- ¿Qué harían diferente con más tiempo o más datos?
