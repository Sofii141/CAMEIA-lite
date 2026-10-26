# Estilo del proyecto: "Macarons"

Todos los documentos (PDF) y las diapositivas del proyecto usan esta paleta y esta tipografía. Muestra: `paleta.png`. La foto original (`paleta_macarons.jpg`) se queda solo en local porque es una imagen de terceros y el repo es público.

## Paleta
| Color | Hex | Uso |
|---|---|---|
| Matcha Powder | `#BCC86F` | Listo, verificado, éxito, números de pasos |
| Semolina Pudding | `#F5CB99` | Fondos suaves, filas de tabla, etiquetas informativas |
| Strawberry Milk | `#FFABA9` | Casos difíciles, avisos suaves |
| Tea Rose | `#F68578` | Acento principal: números de sección, pendientes, alertas |
| Peanut Butter | `#B9794A` | Texto secundario, bordes, pies de página |
| Milk Chocolate | `#79371D` | Títulos, portada, encabezados de tabla |
| Crema (derivado) | `#FFF8EF` | Texto sobre chocolate (portada) y fondos de diapositiva. Las páginas del PDF van en blanco para que los márgenes no queden de otro color |

**Semáforo de estado** (en todos los documentos): 🟢 Matcha = listo · 🟠 Tea Rose = pendiente · 🩷 Strawberry = difícil/riesgo · 🟡 Semolina = informativo.

## Tipografía (Google Fonts, gratis)
- **Títulos:** Fraunces (serif suave y "retro", parecida a la de la paleta), con peso 800.
- **Texto:** Nunito Sans 10,5 pt.
- **Código:** JetBrains Mono.

## Cómo hacer un documento nuevo
1. Copiar `plantilla_documento.html`, cambiarle el nombre con la convención `DDMMAAAA_NN_Nombre_vX.html` y escribir el contenido.
2. Generar el PDF:
   ```bash
   python _Estilo/html_a_pdf.py "ruta/al/documento.html"
   ```
   Usa Microsoft Edge en modo invisible: no hay que instalar nada. Las fuentes están en `_Estilo/fuentes` (licencia OFL), así que funciona sin internet.
3. Los componentes disponibles están en `estilo.css`: portada, `h2 .num`, tablas, `.chip` (ok/pend/dif/info/s/m/l), `.caja` (nota/ok/alerta), `.tarjetas`, `ol.pasos`, `.tiempo` y `.pie`.

## Diapositivas
Usar la misma paleta: fondo Crema o Chocolate, títulos en Fraunces y acento Tea Rose. La primera y la última diapositiva van en Chocolate, como la portada del PDF.
