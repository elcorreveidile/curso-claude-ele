# MÓDULO I — Conversar con Claude
## Curso: «Claude para la enseñanza: domina la herramienta»
### Javier Benítez Láinez · laclasedigital.com · claude.laclasedigital.com

---

## VÍDEO I.1 — Cómo piensa Claude

**Duración:** ~5 minutos
**Formato:** Locución con pantalla compartida
**Subtítulos:** Sí (español)

---

### GUION

«Antes de escribir tu primer prompt, quiero explicarte
algo que cambia completamente cómo usas Claude:
Claude no busca — razona.

Google busca información que ya existe y te la devuelve.
Claude construye una respuesta a partir de lo que sabe,
de lo que le dices y del contexto de la conversación.

Eso tiene una consecuencia importante: cuanto más contexto
le das, mejor razona. Y cuanto más le explicas cómo quieres
que piense, más útil es el resultado.

La segunda cosa que distingue a Claude es que trabaja mejor
en conversación que en prompts de una sola vez.
No le hagas una pregunta y esperes la respuesta perfecta.
Habla con él. Corrígele. Pídele que lo reformule.
Dile qué no te ha gustado y por qué.

Y la tercera: Claude muestra su razonamiento si se lo pides.
Eso es extraordinariamente útil para un docente —
puedes ver por qué tomó una decisión pedagógica
y decidir si la compartes o no.

En este módulo vamos a aprender a aprovechar estas tres
características. Empezamos.»

---

## VÍDEO I.2 — El marco FRAME aplicado a Claude

**Duración:** ~8 minutos
**Formato:** Locución con pantalla compartida — demo en directo
**Subtítulos:** Sí (español)

---

### GUION

«Ya conoces el marco FRAME del curso anterior —
o lo vas a conocer ahora si es la primera vez.

FRAME son seis componentes que convierten un prompt vago
en una instrucción precisa:
Formato · Rol · Audiencia · Meta · Especificaciones · Ejemplo.

En este módulo añadimos una capa específica para Claude
que otros modelos aprovechan menos.

Claude responde especialmente bien a tres elementos extra:

**Primero — el rol extendido.**
No solo «actúa como especialista en ELE».
Sé más específico: «actúa como especialista en ELE
con 15 años de experiencia en grupos de inmersión,
que conoce el MCER en profundidad y que adapta siempre
los materiales al perfil cultural del alumnado».
Cuanto más detallado el rol, más calibrada la respuesta.

**Segundo — las instrucciones en negativo.**
Dile explícitamente qué no debe hacer.
«No uses metalenguaje técnico. No generes listas
si no te las pido. No repitas el enunciado antes
de responder.»
Claude sigue estas instrucciones con mucha precisión
— más que otros modelos.

**Tercero — el razonamiento explícito.**
Añade al final del prompt: «Antes de responder,
explica en dos frases qué decisiones pedagógicas
has tomado y por qué.»
Eso te da acceso al proceso de Claude, no solo al resultado,
y te permite corregir antes de usar el material.

Vamos a verlo en directo.»

*(Demo en pantalla — construir un prompt FRAME + capa Claude)*

---

## LECTURA I.1 — Conversar vs pedir: la diferencia que lo cambia todo

---

### El error más común con la IA

La mayoría de docentes usan la IA como si fuera
un formulario: escriben una instrucción, reciben
una respuesta, la copian o la descartan.

Ese uso produce resultados mediocres. No porque la IA
sea mala sino porque no estás aprovechando lo que
la hace poderosa: su capacidad de mantener contexto
a lo largo de una conversación y de ajustar sus respuestas
en función de lo que le dices.

Una conversación bien construida con Claude puede
producir en 20 minutos lo que tardarías dos horas
en hacer solo — y con una calidad que ningún prompt
de una sola vez puede alcanzar.

---

### Cómo funciona el contexto en Claude

Cada vez que escribes un mensaje, Claude lee toda
la conversación desde el principio antes de responder.
Eso significa que puede recordar lo que le dijiste
hace diez mensajes y tenerlo en cuenta ahora.

Pero hay un límite: la ventana de contexto.
Claude Sonnet puede procesar aproximadamente 200.000
tokens en una conversación — lo equivalente a unas
150.000 palabras. Para una sesión de trabajo docente
normal es más que suficiente.

Cuando la conversación llega al límite, Claude empieza
a «olvidar» los mensajes más antiguos. La solución
es usar Projects — que veremos en el Módulo II —
para mantener contexto entre conversaciones distintas.

---

### La estructura de una conversación eficaz con Claude

Una conversación bien estructurada con Claude para
generar materiales docentes tiene cinco momentos:

**1. Contexto inicial:**
Explica quién eres, para quién trabajas y qué estás
haciendo. Una o dos frases es suficiente.
«Soy docente de español para extranjeros. Estoy preparando
una unidad sobre el pretérito perfecto para un grupo
de nivel B1, adultos universitarios anglófonos.»

**2. La solicitud principal con FRAME:**
El prompt completo con los seis componentes más
la capa específica de Claude.

**3. Evaluación y corrección:**
No aceptes el primer resultado si no es exactamente
lo que necesitas. Di qué ha funcionado y qué no.
«El nivel léxico es demasiado alto. Simplifica
el vocabulario pero mantén los ejemplos culturales.»

**4. Refinamiento iterativo:**
Dos o tres rondas de ajuste producen un resultado
que puedes usar directamente. En cada ronda
sé específico sobre qué cambiar.

**5. Cierre y extracción:**
Cuando el resultado es bueno, pide a Claude
que lo consolide en un documento limpio.
«Genera la versión final del material en formato
listo para imprimir, sin comentarios adicionales.»

---

### Cómo pedirle a Claude que razone en voz alta

Esta es la función más infrautilizada de Claude
y la más útil para un docente.

Cuando Claude razona en voz alta puedes:
- Ver si las decisiones pedagógicas son correctas
- Detectar supuestos erróneos sobre tu alumnado
- Aprender cómo piensa un diseñador instruccional experto
- Corregir el rumbo antes de que el material esté terminado

Para activarlo, añade una de estas instrucciones
al final de tu prompt:

«Antes de generar el material, explica en tres frases
qué decisiones didácticas has tomado y por qué.»

«Después de generar el material, señala qué aspectos
has adaptado específicamente para el perfil del alumnado
que te he descrito.»

«Si hay algo del prompt que te genera dudas o que podría
interpretarse de dos formas, pregúntame antes de responder.»

Esta última instrucción es especialmente valiosa:
Claude te pedirá clarificación en lugar de asumir,
lo que produce materiales más ajustados a tu intención.

---

## LECTURA I.2 — Análisis de documentos: PDFs, imágenes y textos largos

---

### Claude como lector experto

Una de las capacidades más potentes de Claude
para docentes es su capacidad de leer y analizar
documentos completos: PDFs, imágenes, transcripciones,
programas de curso, rúbricas, trabajos de alumnado.

No solo los lee — los interpreta, los compara,
los resume y los usa como base para generar nuevos materiales.

---

### Cómo subir documentos a Claude

En la interfaz de claude.ai, junto al campo de texto,
hay un icono de clip. Desde ahí puedes subir:

- **PDFs** — hasta varios cientos de páginas
- **Imágenes** — JPG, PNG, GIF, WebP
- **Archivos de texto** — TXT, MD, CSV
- **Código** — cualquier lenguaje de programación

El plan gratuito permite subir documentos con algunas
limitaciones de tamaño. El plan Pro elimina esas limitaciones.

---

### Usos prácticos para docentes

**Analizar el trabajo de un alumno:**
Sube el trabajo y pide a Claude que lo evalúe
según una rúbrica que tú le describes o que también
subes como documento.

```
Aquí tienes la composición de un alumno de B2
y la rúbrica de evaluación del curso.
Evalúa la composición según cada criterio de la rúbrica.
Señala los tres errores más frecuentes y sugiere
una actividad de refuerzo para cada uno.
No corrijas el texto — solo analiza y sugiere.
```

**Adaptar un recurso auténtico:**
Sube un artículo, una noticia o un texto literario
y pide a Claude que lo adapte a un nivel específico.

**Analizar un programa de curso:**
Sube el programa y pide a Claude que identifique
lagunas, progresiones poco claras o contenidos
que podrían reordenarse.

**Extraer vocabulario de un texto:**
Sube cualquier texto y pide una lista de vocabulario
por niveles, con definiciones en español y ejemplos
en contexto.

**Analizar imágenes para el aula:**
Sube una fotografía y pide a Claude que genere
actividades de descripción, preguntas de comprensión
o tareas comunicativas basadas en la imagen.

---

### Lo que Claude no puede hacer con documentos

- No puede acceder a documentos en URLs externas
  a menos que uses herramientas externas (Módulo V)
- No puede editar el documento original — solo analizarlo
- No recuerda documentos entre conversaciones distintas
  a menos que los subas de nuevo o uses Projects (Módulo II)

---

## ACTIVIDAD I.1 — Tu primera conversación compleja

**Tipo:** Práctica guiada en Claude
**Duración estimada:** 30-40 minutos
**Plan Claude:** Gratuito suficiente

---

### La tarea

Vas a mantener una conversación de al menos ocho
intercambios con Claude para generar un material
didáctico real que puedas usar en tu próxima clase.

---

### Paso 1 · El contexto inicial

Empieza con este mensaje, completando los espacios:

```
Soy docente de [materia]. Trabajo con [descripción
del grupo: nivel, edad, contexto, lengua materna].
Estoy preparando [describe la unidad o el tema].
Necesito un material que trabaje [objetivo comunicativo
o de aprendizaje concreto].
```

---

### Paso 2 · El prompt FRAME con capa Claude

Escribe tu prompt con los seis componentes de FRAME
más las tres instrucciones específicas de Claude:

```
[F] Formato exacto del material que necesitas
[R] Rol extendido y detallado para Claude
[A] Audiencia concreta con todos los detalles relevantes
[M] Meta de aprendizaje en términos de lo que el alumno
    será capaz de hacer
[E] Especificaciones técnicas completas
[E] Ejemplo del estilo o formato deseado

Instrucciones adicionales para Claude:
— No hagas [lo que no quieres]
— Antes de generar el material, explica en dos frases
   qué decisiones pedagógicas has tomado
— Si algo del prompt es ambiguo, pregúntame antes
   de responder
```

---

### Paso 3 · Tres rondas de refinamiento

Después de recibir el primer resultado, haz al menos
tres ajustes. Para cada uno, sé específico:

- «El vocabulario del apartado X es demasiado alto para B1»
- «Las preguntas de comprensión son demasiado literales,
   necesito al menos dos inferenciales»
- «El contexto cultural no encaja con mi grupo —
   cambia los nombres y las referencias a [contexto real]»

---

### Paso 4 · Versión final

Pide a Claude que genere la versión final consolidada:

```
Genera la versión final del material incorporando
todos los ajustes que hemos hecho. Formato limpio,
listo para usar directamente en clase.
Incluye al final una nota breve con las decisiones
pedagógicas principales que has tomado.
```

---

### Reflexión final

Responde estas tres preguntas y guárdalas
para la primera videotutoría:

1. ¿En qué momento de la conversación el material
   dio el salto cualitativo que necesitabas?
2. ¿Qué instrucción específica fue la más determinante
   para el resultado final?
3. ¿Qué cambiarías en tu prompt inicial si lo hicieras
   de nuevo?

---

## ACTIVIDAD I.2 — Análisis de un documento real

**Tipo:** Práctica con documento propio
**Duración estimada:** 20-30 minutos
**Plan Claude:** Gratuito suficiente

---

### La tarea

Sube a Claude un documento real de tu práctica docente
— puede ser un trabajo de un alumno anonimizado,
un texto auténtico que quieras usar en clase,
un programa de curso o cualquier material propio —
y usa una de estas cuatro tareas:

**Opción A — Evaluar un trabajo de alumno:**
```
Aquí tienes un trabajo de un alumno de [nivel].
Evalúalo según estos criterios: [lista tus criterios].
Señala los tres puntos fuertes y los tres aspectos
a mejorar. Sugiere una actividad de refuerzo
para la dificultad principal. No corrijas el texto.
```

**Opción B — Adaptar un recurso auténtico:**
```
Adapta este texto al nivel [nivel MCER] para un grupo
de [descripción del grupo]. Mantén el contenido
y la voz original. Simplifica el vocabulario superior
al nivel indicado. Añade tres preguntas de comprensión
y un glosario de cinco palabras clave con definición
en español.
```

**Opción C — Analizar un programa de curso:**
```
Analiza este programa de curso desde la perspectiva
de la progresión pedagógica. Identifica posibles lagunas,
contenidos que podrían reordenarse y una sugerencia
de actividad integradora que no está contemplada.
```

**Opción D — Generar actividades desde una imagen:**
```
Genera tres actividades comunicativas basadas
en esta imagen para un grupo de [nivel y perfil].
Una actividad de comprensión, una de producción oral
y una de producción escrita. Nivel [nivel MCER].
Instrucciones en español.
```

---

## RECURSOS DEL MÓDULO I

- Guía de prompts de Anthropic:
  docs.anthropic.com/prompt-library
- Documentación de la ventana de contexto:
  docs.anthropic.com/models
- Ejemplos de análisis de documentos:
  disponibles en la plataforma del curso

---

## RESUMEN DEL MÓDULO I

| Elemento | Detalle |
|----------|---------|
| Vídeos | 2 vídeos · ~13 min total |
| Lecturas | 2 textos · ~1.200 palabras total |
| Actividades | 2 actividades · 50-70 min total |
| Entrega | Reflexiones de I.1 para la videotutoría |
| Plan Claude | Gratuito suficiente |

**Al terminar el Módulo I el participante habrá:**
- Entendido cómo piensa Claude y en qué se diferencia
  de un buscador
- Construido un prompt FRAME completo con la capa
  específica de Claude
- Mantenido una conversación compleja de refinamiento
  iterativo
- Analizado un documento real de su práctica docente
- Identificado las instrucciones más determinantes
  para obtener resultados útiles

**Siguiente paso:** Módulo II · Projects y memoria

---

*Curso «Claude para la enseñanza: domina la herramienta»*
*claude.laclasedigital.com · Javier Benítez Láinez · benitezl@go.ugr.es*
*La Clase Digital · 2026*
