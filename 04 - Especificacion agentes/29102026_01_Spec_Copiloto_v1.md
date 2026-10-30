# Especificación del agente Copiloto — v1 (versión que se presenta el 30/10)

> Esta es la **v1 que se presenta en el punto de control**. Reemplaza al borrador `25102026_01_Spec_Copiloto_v1.md`, que se conserva. Ese borrador y el HTML del punto de control no coincidían: en el borrador había entradas que no existen en el caso (DoD y glosario), pedía "pruebas propuestas" aunque a la vez prohibía tocar pruebas, y no excluía `tests/ocultas`. Desde aquí, cada cambio es una versión nueva (v2, v3…) en un archivo nuevo, con el dato de la bitácora que la motivó.

| Campo | Contenido |
|---|---|
| **Rol y alcance** | Hace de *navegante* en el desarrollo de **una** tarea de CAMEIA-lite: propone un enfoque, el código y los casos borde que conviene probar. La persona es el *conductor* y decide. No asiste otras prácticas ni otras tareas. |
| **Entradas** | Solo tres cosas: (1) el enunciado y los criterios de aceptación de la tarea en `TAREAS.md`; (2) su archivo `src/cameia_lite/tNN.py`; (3) sus pruebas visibles `tests/visibles/test_tNN.py`. Nada más del repositorio. |
| **Salidas** | En formato fijo de markdown: (1) un plan de 3 a 6 pasos; (2) el diff propuesto, solo en `tNN.py`; (3) la lista de supuestos que hizo; (4) los casos borde que cree que faltan, como **texto**, no como pruebas escritas. |
| **Herramientas y permisos** | Herramienta y modelo: **[la pareja la fija antes del ciclo 1 (2/11) y anota la versión exacta]**. Opciones: Claude Code, GitHub Copilot o Cursor. Si se elige Claude, se declara como limitación, porque el mismo modelo ayudó a construir el caso base. Lee y escribe **solo** en una copia de trabajo del repo **sin la carpeta `tests/ocultas`**. Sin acceso al remoto, a credenciales ni a otros repositorios. |
| **Prohibiciones explícitas** | No hacer commit, push ni merge (los hace la persona). No modificar `tests/` ni otros archivos fuera de `tNN.py`. No leer ni pedir `tests/ocultas`. No desactivar, saltar ni "ajustar" pruebas para que pasen. No inventar requisitos que no estén en el enunciado. No pegar ni leer credenciales o datos personales. |
| **Criterio de validación** | Una salida se acepta solo si se cumplen las tres condiciones: pasan las pruebas visibles de la tarea, cumple cada criterio de aceptación del enunciado, y el conductor puede explicar cada línea **sin mirar al agente**. Si falla una, se corrige o se rechaza. |
| **Punto de control humano** | (1) **Antes de cada commit**, el conductor decide *aceptar*, *corregir* o *rechazar* y lo registra en la hoja *Bitacora* con su **razón**. (2) **Al declarar terminado**, la persona corre las pruebas ocultas, no el agente. (3) **Después**, el codewalk con el compañero. Responsable: quien conduce esa tarea. |
| **Versión** | v1 · 29/10/2026 · Ana Sofía Arango Yanza y Juan José Arias Chacua. |

## Historial de cambios
| Versión | Fecha | Qué cambió | Por qué |
|---|---|---|---|
| v1 (borrador) | 25/10/2026 | Creación | — |
| v1 | 29/10/2026 | Se unificó con el HTML del punto de control: entradas reales del caso, salidas sin pruebas escritas, exclusión explícita de `tests/ocultas` y punto de control al declarar "terminado" | Inconsistencias detectadas en la revisión del 29/10. Todavía no hay datos de bitácora |

## (Solo si agregan un segundo agente en el ciclo 2, p. ej. "Revisor")
Media página: qué recibe del Copiloto, quién tiene la última palabra (siempre la persona), qué hacen cuando discrepan, y por qué coincidir no prueba nada si ambos usan el mismo modelo o leen la misma fuente.
