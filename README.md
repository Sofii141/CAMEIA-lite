# CAMEIA-lite

Este es el caso base del proyecto final de Ágiles 2026-2 (tema 3, pair programming). Contiene **24 tareas pequeñas**, cada una basada en una regla real del backlog de CAMEIA. No necesita Docker, Firebase ni base de datos: solo Python 3.10+ y pytest.

## Uso
```bash
pip install pytest
python -m pytest tests/visibles -k t05        # pruebas visibles de una tarea
python -m pytest tests/ocultas -k t05         # pruebas ocultas: SOLO después de declarar "terminado"
```

## Reglas de cada tarea (son las que hacen válida la medición)
1. **Antes de empezar:** anotar cuántos minutos creen que les tomará (pronóstico).
2. **Arrancar el cronómetro** al abrir el enunciado en `TAREAS.md`.
3. **Trabajar** solo con las pruebas de `tests/visibles`.
   - **Línea base:** pareja humana sin IA; uno conduce, el otro navega, y cambian cada 15 min.
   - **Ciclos:** una persona con el agente copiloto, y una fila de bitácora por cada uso.
4. **Declarar "terminado"** cuando pasan las visibles. Parar el cronómetro y hacer commit `tNN: terminado`.
5. **Correr `tests/ocultas`.** Cada prueba que falle es un **error escapado**. Si lo corrigen, el cronómetro sigue aparte como **retrabajo**, con commit `tNN: retrabajo`.
6. **Codewalk de 5 min:** 5 preguntas sin mirar el código, puntuadas de 0 a 5, al autor y al compañero.
7. Llenar la hoja *Medicion por caso* de la bitácora.

> **No abrir `tests/ocultas` antes de terminar.** Ahí está la medición de errores escapados; si se miran antes, el dato no vale. Si alguien las abre por error, se anota con la marca `[C]` y la tarea se descarta.

## Tareas que ya implementó uno de ustedes en CAMEIA
- t10, t11, t12 y t23: las hizo **Juan José**.
- t15: la hizo **Ana Sofía**.

Estas solo se asignan a la condición *con agente* y las hace la **otra persona**, para no medir memoria.

## Asignación por sorteo
```bash
python sorteo.py 30102026
```
El número es la semilla. Anoten en un acta cuál usaron, así cualquiera puede repetir el sorteo y obtener lo mismo.
