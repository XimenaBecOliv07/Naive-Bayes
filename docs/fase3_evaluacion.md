# Fase 3B: Evaluacion y optimizacion del modelo

**Responsable:** Octavio
**Rama:** `octavio-fase3-evaluacion`
**Script:** `scripts/fase3_evaluacion.py`

## 1. Metodologia

- Division 80/20 estratificada con `random_state=42` (1087 entrenamiento, 272 prueba), igual que la fase 3A.
- Todas las decisiones (variables y `var_smoothing`) se tomaron con validacion cruzada estratificada de 5 pliegues sobre entrenamiento. El conjunto de prueba solo se uso para la medicion final.

## 2. Linea base

`DummyClassifier` que siempre predice la clase mas frecuente: accuracy 0.5294, F1 macro 0.3462.

siempre hay que superarla por un modelo si tiene gran cantidad de un tipo de datos llega un punto en el que se sesga y siempre va a dar la misma predicciony ser tonto

## 3. Seleccion de variables

Correlacion absoluta con `quality`, calculada solo con entrenamiento:

| Variable | abs(r) |
|---|---:|
| alcohol | 0.478 |
| volatile_acidity | 0.401 |
| sulphates | 0.263 |
| citric_acid | 0.217 |
| density | 0.186 |

| Variables | F1 CV | Accuracy prueba | F1 prueba |
|---:|---:|---:|---:|
| 3 | 0.7239 | 0.7537 | 0.7531 |
| 5 | 0.7080 | 0.7426 | 0.7426 |
| 7 | 0.7177 | 0.7426 | 0.7420 |
| 9 | 0.7099 | 0.7500 | 0.7497 |
| 11 | 0.7134 | 0.7353 | 0.7346 |

Se eligieron 3 variables por tener el mayor F1 de validacion cruzada.

Ya que los datos mas variados sirven para poder tener un mejor resultado

## 4. Ajuste de var_smoothing

`GridSearchCV` con `np.logspace(-9, 2, 23)`. Mejor valor: 1.0 (F1 CV 0.7368).

[Que hace var_smoothing y por que se decidio con CV aunque en prueba bajo 1 lote]

## 5. Comparacion de configuraciones

| Modelo | Accuracy | F1 macro |
|---|---:|---:|
| Linea base | 0.5294 | 0.3462 |
| 3 clases, 11 variables | 0.5809 | 0.5596 |
| Binario, 11 variables | 0.7353 | 0.7346 |
| Binario, 3 variables | 0.7537 | 0.7531 |
| Binario optimizado (final) | 0.7500 | 0.7493 |

![Comparacion](figuras/fase3_comparacion_modelos.png)

[Por que el binario supera al de 3 clases]

## 6. Modelo final

- Variables: `alcohol`, `volatile_acidity`, `sulphates`
- `var_smoothing`: 1.0
- Prueba: accuracy 0.7500, precision macro 0.7492, recall macro 0.7496, F1 macro 0.7493

![Matriz de confusion](figuras/fase3_matriz_confusion.png)

|  | Predice bueno | Predice malo |
|---|---:|---:|
| Es bueno | 109 | 35 |
| Es malo | 33 | 95 |

[Que error es mas costoso para la bodega y como deberia usarse el modelo]

## 7. Limitaciones

[Por que el accuracy no es mas alto: piensa en el origen de `quality`, el supuesto de independencia y el tamano del dataset]