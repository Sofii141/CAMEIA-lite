# Cómo miden los estudios publicados (y qué copiamos de cada uno)

Marcas: **[V]** se abrió el PDF y se comprobó la frase · **[P]** viene de un resumen y hay que comprobarla en el original.

| Estudio (base de datos) | Qué miden y cómo | Qué tomamos para nuestro diseño |
|---|---|---|
| **Hannay et al. 2009**, *Information and Software Technology* 51(7) — **ScienceDirect**, DOI [10.1016/j.infsof.2009.02.001](https://doi.org/10.1016/j.infsof.2009.02.001) | Metaanálisis de 18 experimentos. Tres variables estándar: **calidad**, **duración** (tiempo de calendario hasta terminar) y **esfuerzo** (horas-persona: una pareja cuenta doble). Encontraron un efecto pequeño en calidad, medio en duración y negativo en esfuerzo, y que dependía de la complejidad de la tarea. **[P]** | Usar las mismas tres variables con esos nombres. Reportar **esfuerzo**, no solo duración: la pareja humana gasta 2 personas y el agente 1. |
| **Arisholm et al. 2007**, *IEEE Transactions on Software Engineering* 33(2) — **IEEE Xplore**, DOI [10.1109/TSE.2007.17](https://doi.org/10.1109/TSE.2007.17) | 295 consultores profesionales en tareas de cambio sobre dos sistemas Java. Miden **duración**, **esfuerzo** y **corrección** (si la solución pasa pruebas de aceptación). Los resultados dependieron de la complejidad del sistema y de la experiencia. **[P]** | Clasificar las tareas por complejidad (S/M/L) y analizar por grupo. La "corrección" se mide con pruebas que el desarrollador no ve. |
| **Shihab et al. 2025**, Oregon State (ICER 2025, **ACM**) — PDF en `Articulos/` | Diseño *within-subjects* (cada persona hace tareas con y sin Copilot). Dos variables: **tiempo hasta completar** y **número de pruebas pasadas**. El cronómetro se pausa al leer las instrucciones. Graban la pantalla. **[V]** | **Plantilla directa de nuestro diseño:** cronómetro por tarea, pruebas automáticas como criterio objetivo, grabación de pantalla como evidencia. |
| **Welter et al. 2025**, ASE 2025 (**IEEE/ACM**) — PDF en `Articulos/` | Comparan parejas humanas con una persona + Copilot. Miden la **transferencia de conocimiento** agrupando lo que dicen en *episodios* (cada uno con su tema, largo y si tuvo éxito). Hallazgo: con Copilot se acepta con menos escrutinio. **[V]** | Nuestra métrica de comprensión (*codewalk*) es una versión simple de esto. Además, contar en la bitácora cuántas sugerencias se aceptaron sin modificar. |
| **METR 2025** (arXiv 2507.09089) — PDF en `Articulos/` | RCT con 16 devs y 246 tareas, **asignadas al azar** a "con IA" o "sin IA". Miden el tiempo real y lo comparan con el **pronóstico** y la **percepción** de los mismos devs. **[V]** | Sortear la condición de cada tarea. Antes de cada tarea, anotar cuánto creen que tardarán, y después cuánto creen que les ayudó la IA. Así se mide la "trampa de la sensación de velocidad" que menciona el profe. |
| **Peng et al. 2023** (arXiv 2302.06590) — PDF en `Articulos/` | Experimento controlado con una sola tarea (servidor HTTP en JS): el grupo con Copilot fue un 55,8 % más rápido. **[V]** | Contraste para la exposición: una tarea pequeña y nueva favorece al agente, y un repo maduro conocido no (METR). |
| **Ma et al. 2023** (LLM@AIED, arXiv 2306.05153) — PDF en `Articulos/` | Revisión: las métricas usadas para "pAIr programming" son **menos completas** que las de pair programming humano. **[V]** | Justifica medir también comprensión, y no solo tiempo. |
| **Anthropic 2026** ([web](https://www.anthropic.com/research/AI-assistance-coding-skills)) | RCT con 52 ingenieros: **quiz de comprensión** después de la tarea. Con IA, unos 17 puntos menos; la mayor caída fue en depuración. **[P]** | El *codewalk* incluye una pregunta de depuración ("si falla X, ¿dónde mirarías?"). |

## Cómo buscar más en las bases oficiales (para ampliar las fuentes)
- **ScienceDirect** (Information and Software Technology, Journal of Systems and Software): `"pair programming" AND ("AI assistant" OR Copilot OR LLM)`, filtrado 2023–2026.
- **IEEE Xplore / ACM Digital Library**: `"pair programming" "knowledge transfer"` y `"Copilot" "controlled experiment"`.
- Con correo de Unicauca, entren por el portal de bases de datos de la biblioteca para descargar los PDF de pago (Hannay y Arisholm).

## Las variables que medimos (resumen para el GQM)
| Variable | Definición operacional | Fuente que la respalda |
|---|---|---|
| Duración | Minutos de cronómetro desde leer el enunciado hasta pasar las pruebas visibles | Hannay 2009; Shihab 2025 |
| Esfuerzo | Duración × personas (pareja humana = 2) | Hannay 2009 |
| Corrección / errores escapados | Pruebas **ocultas** que fallan después de declarar "terminado" | Arisholm 2007; Shihab 2025 |
| Retrabajo | Commits o ciclos de corrección después del primer "terminado" | Diseño propio (PDF del profe: "retrabajo") |
| Comprensión | *Codewalk* de 5 preguntas, 0–5, al autor y al compañero | Welter 2025; Anthropic 2026 |
| Percepción | Tiempo pronosticado antes y ayuda percibida después | METR 2025 |
