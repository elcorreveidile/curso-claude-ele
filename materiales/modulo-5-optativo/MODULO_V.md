# MÓDULO V — Claude avanzado *(optativo)*
## Curso: «Claude para la enseñanza: domina la herramienta»
### Javier Benítez Láinez · laclasedigital.com · claude.laclasedigital.com

---

## NOTA SOBRE ESTE MÓDULO

Este módulo es optativo. Está diseñado para participantes
que quieren ir más allá del uso docente habitual
y explorar las capacidades más técnicas de Claude.
No es necesario completarlo para obtener el certificado
de aprovechamiento del curso.

Si no tienes experiencia técnica previa, no te preocupes.
Este módulo está escrito para docentes, no para programadores.
Todo lo que se explica aquí es accesible con curiosidad
y disposición a experimentar.

---

## VÍDEO V.1 — Claude con herramientas externas

**Duración:** ~7 minutos
**Formato:** Grabación de pantalla en directo
**Subtítulos:** Sí (español)

---

### GUION

«Claude en claude.ai es muy potente. Pero tiene
una limitación: solo sabe lo que le dices tú
o lo que está en sus datos de entrenamiento.
No puede acceder a internet, no puede leer
tu Google Drive, no puede ver tu calendario.

Las herramientas externas eliminan esas limitaciones.

En la interfaz de claude.ai, cuando escribes «/»
se abre un menú de herramientas — las skills —
que Claude puede usar dentro de la conversación.
Según tu configuración y tu plan, puedes conectar:
búsqueda web en tiempo real, Google Drive,
Google Calendar y otras integraciones.

Para un docente eso significa cosas concretas:
buscar noticias de actualidad para una actividad
de hoy, leer un documento de tu Drive sin descargarlo,
o pedirle a Claude que genere un plan de trabajo
teniendo en cuenta tus eventos del calendario.

Vamos a verlo en directo.»

*(Demo en pantalla — búsqueda web + Google Drive)*

---

## VÍDEO V.2 — Introducción a la API de Claude

**Duración:** ~8 minutos
**Formato:** Grabación de pantalla — demo sencilla
**Subtítulos:** Sí (español)

---

### GUION

«La API de Claude es la forma de usar Claude
desde fuera de claude.ai — desde tus propias
aplicaciones, scripts o automatizaciones.

Sé lo que estás pensando: «yo no soy programador/a».
No hace falta serlo para entender qué es la API
y para qué sirve a un docente.

La API te permite tres cosas que la interfaz web no puede:
automatizar tareas repetitivas que haces a mano,
integrar Claude en herramientas que ya usas,
y procesar grandes volúmenes de texto
de forma sistemática.

Para un docente eso puede significar:
generar automáticamente 30 variantes de un ejercicio
con un solo clic, procesar las respuestas de toda
la clase a un cuestionario y extraer patrones,
o crear un bot sencillo que responda preguntas
frecuentes de tu alumnado.

No necesitas saber programar para entender esto.
Necesitas entender qué es posible para poder pedírselo
a alguien que sí sabe — o para usarlo con Claude Code,
que vemos a continuación.

Vamos.»

*(Demo en pantalla — llamada básica a la API
desde el playground de Anthropic)*

---

## VÍDEO V.3 — Claude Code para docentes

**Duración:** ~6 minutos
**Formato:** Grabación de pantalla en directo
**Subtítulos:** Sí (español)

---

### GUION

«Claude Code es una herramienta de línea de comandos
que convierte a Claude en un agente que puede
ejecutar código, gestionar archivos y automatizar
tareas en tu ordenador.

Para un docente sin experiencia técnica eso suena
intimidante. Pero en la práctica, usar Claude Code
es tan sencillo como decirle en lenguaje natural
lo que quieres que haga.

Tres ejemplos concretos para docentes:

Uno: tienes 30 composiciones de tus alumnos
en archivos de texto separados. Con Claude Code
puedes pedirle que las lea todas, extraiga
los errores más frecuentes y genere un informe
del grupo en cinco minutos.

Dos: tienes una lista de 200 palabras de vocabulario
en una hoja de cálculo. Con Claude Code puedes
pedirle que genere automáticamente ejercicios
de vocabulario para cada palabra con ejemplos en contexto.

Tres: quieres crear una versión A y una versión B
de un examen con las preguntas en distinto orden.
Claude Code lo hace en segundos.

Vamos a ver cómo se instala y cómo se usa
con un ejemplo real.»

*(Demo en pantalla — instalación básica y primer uso)*

---

## LECTURA V.1 — Claude con herramientas externas: búsqueda web y Google Drive

---

### Por qué las herramientas externas cambian el juego

Claude sin herramientas externas trabaja con
la información que tú le das y con lo que aprendió
durante su entrenamiento. Su conocimiento tiene
una fecha de corte — no sabe qué pasó ayer,
no puede leer un documento que está en tu Drive,
no puede verificar si un dato sigue siendo actual.

Las herramientas externas extienden esas capacidades
de forma significativa para el trabajo docente.

---

### Búsqueda web en tiempo real

Con la búsqueda web activada, Claude puede buscar
información actualizada antes de responderte.

Usos prácticos para docentes:

**Recursos auténticos de actualidad:**
```
Busca una noticia de hoy en español sobre
[tema relevante para la clase]. Nivel de lengua
aproximado B2. Que sea de un medio de comunicación
español o latinoamericano. Después adáptala al nivel B1
manteniendo el contenido esencial.
```

**Verificación de datos:**
```
Verifica si esta información que voy a usar
en clase sigue siendo actual: [información].
Busca la fuente más reciente disponible.
```

**Materiales de cultura contemporánea:**
```
Busca información actualizada sobre [tema cultural:
un festival, un artista, un acontecimiento reciente].
Genera tres preguntas de comprensión cultural
para un grupo de nivel C1.
```

---

### Google Drive

Con Google Drive conectado, Claude puede leer
documentos directamente de tu Drive sin que
tengas que descargarlos y subirlos manualmente.

Usos prácticos:

**Leer el programa del curso directamente:**
```
Lee el documento [nombre del documento] de mi Drive
y genera una secuencia de actividades para la próxima semana
coherente con lo que ya hemos trabajado.
```

**Analizar trabajos del alumnado almacenados en Drive:**
```
Lee los trabajos de mi carpeta [nombre de la carpeta]
y genera un análisis grupal de los errores más frecuentes.
```

**Mantener sincronizados los materiales:**
Los documentos de tu Drive que subes a un Project
se actualizan automáticamente cuando los modificas.
Tu Project siempre trabaja con la versión más reciente
de tu programa, tus rúbricas y tus materiales.

---

### Cómo activar las herramientas externas

En claude.ai, escribe «/» en el campo de texto
para ver las herramientas disponibles en tu cuenta.
Las herramientas que aparecen dependen de tu plan
y de las integraciones que hayas configurado.

Para conectar Google Drive y Google Calendar:
ve a Configuración → Integraciones y sigue
las instrucciones de autorización.

---

## LECTURA V.2 — La API de Claude: qué es y para qué sirve a un docente

---

### Qué es una API

Una API (Application Programming Interface)
es una puerta de acceso a un servicio desde fuera
de su interfaz habitual. La API de Claude te permite
usar Claude desde cualquier aplicación, script
o herramienta que tú construyas o configures —
sin abrir claude.ai.

Para un docente sin experiencia técnica,
lo importante no es entender cómo funciona la API
sino entender qué hace posible.

---

### Qué hace posible la API para un docente

**Automatización de tareas repetitivas:**
Cualquier tarea que haces manualmente una y otra vez
— generar variantes de ejercicios, corregir textos
con el mismo criterio, formatear materiales —
puede automatizarse con la API.

**Procesamiento masivo:**
La interfaz de claude.ai está diseñada para conversaciones.
La API está diseñada para procesar grandes volúmenes.
Si necesitas analizar 50 composiciones, generar
200 ejercicios o procesar los resultados de un cuestionario
de toda la clase, la API es la herramienta adecuada.

**Integración con otras herramientas:**
Puedes conectar Claude a Google Sheets, Notion,
Airtable, o cualquier herramienta que use APIs.
Un flujo típico para docentes: los alumnos envían
sus respuestas a un formulario de Google,
ese formulario las manda a Claude vía API,
Claude las analiza y devuelve el feedback
directamente a una hoja de cálculo.

---

### El Anthropic Console y el Playground

El punto de entrada más sencillo a la API
sin necesidad de código es el **Anthropic Console**
en console.anthropic.com.

El Playground dentro del Console te permite:
- Probar prompts con distintos modelos
- Ajustar parámetros como la temperatura y el contexto
- Ver cómo se construye una llamada a la API
- Exportar el código generado para usarlo en tus scripts

Para docentes que quieren explorar la API sin escribir
código, el Playground es el lugar ideal para empezar.

---

### Costes de la API

La API de Claude tiene un coste por tokens usados
— tanto los tokens de entrada (tu prompt y contexto)
como los de salida (la respuesta de Claude).

Los precios varían según el modelo:
- Claude Haiku: el más económico, ideal para tareas
  masivas sencillas
- Claude Sonnet: equilibrio calidad-coste para
  la mayoría de tareas docentes
- Claude Opus: el más caro, reservar para tareas
  que requieren máxima calidad

Para un docente con uso moderado —
procesar los trabajos de la clase una vez a la semana,
generar materiales por lotes — el coste mensual
de la API suele ser inferior al coste del plan Pro.

---

## LECTURA V.3 — Claude Code: automatizar sin saber programar

---

### Qué es Claude Code

Claude Code es una herramienta de línea de comandos
que instala Claude como agente en tu ordenador.
Desde la terminal, puedes pedirle a Claude
en lenguaje natural que ejecute tareas que involucran
tu sistema de archivos, tu código y tus herramientas.

La diferencia clave con claude.ai: Claude Code
puede actuar, no solo responder. Puede crear archivos,
modificarlos, ejecutar scripts, instalar herramientas
y encadenar varias tareas de forma autónoma.

---

### Instalación básica

```bash
# Requisito: Node.js instalado en tu ordenador
# Descarga desde nodejs.org si no lo tienes

# Instalar Claude Code
npm install -g @anthropic-ai/claude-code

# Verificar instalación
claude --version

# Iniciar Claude Code en una carpeta
cd /ruta/a/tu/carpeta
claude
```

Una vez iniciado, escribes tus instrucciones
en lenguaje natural y Claude Code las ejecuta.

---

### Casos de uso reales para docentes

**Caso 1 — Procesar composiciones del grupo:**

Tienes una carpeta con 25 archivos de texto,
uno por alumno. Quieres un informe de errores frecuentes.

```
Tengo una carpeta llamada "composiciones_grupo_b2"
con 25 archivos de texto. Lee todos los archivos,
identifica los cinco errores gramaticales más frecuentes
en el grupo, cuenta cuántos alumnos cometen cada error
y genera un informe en formato Markdown llamado
"informe_errores_grupo.md".
```

Claude Code lee los 25 archivos, los analiza y genera
el informe. Tiempo: 2-3 minutos en lugar de 2-3 horas.

**Caso 2 — Generar variantes de un ejercicio:**

Tienes un ejercicio de huecos con 10 oraciones.
Necesitas cuatro variantes con las mismas oraciones
en distinto orden para evitar que los alumnos
se copien entre ellos.

```
Tengo el archivo "ejercicio_subjuntivo.txt".
Genera cuatro versiones del mismo ejercicio
con las oraciones en orden aleatorio diferente
en cada versión. Guárdalas como
"version_A.txt", "version_B.txt", etc.
```

**Caso 3 — Crear un banco de vocabulario:**

Tienes una lista de 150 palabras de vocabulario en un CSV.
Necesitas para cada palabra: definición en español,
ejemplo en contexto, nivel MCER aproximado
y una oración para completar.

```
Lee el archivo "vocabulario.csv" que tiene una columna
con 150 palabras en español. Para cada palabra genera:
definición en español simple, un ejemplo en contexto
de nivel B1, el nivel MCER aproximado y una oración
para completar con esa palabra. Guarda el resultado
como "banco_vocabulario_completo.csv".
```

---

### Lo que Claude Code no puede hacer solo

Claude Code es un agente con mucha autonomía,
pero siempre bajo tu supervisión. Antes de ejecutar
acciones que afecten a archivos importantes,
Claude Code te pide confirmación.

Buenas prácticas:
- Trabaja siempre en una carpeta específica,
  no en el escritorio ni en carpetas con documentos importantes
- Revisa siempre el resultado antes de usarlo
- Haz una copia de seguridad de los archivos
  que vayas a procesar por lotes

---

## ACTIVIDAD V.1 — Conecta una herramienta externa

**Tipo:** Configuración y práctica
**Duración estimada:** 20-30 minutos
**Plan Claude:** Pro recomendado

---

### La tarea

Conecta al menos una herramienta externa a Claude —
búsqueda web o Google Drive — y completa
una de estas tareas:

**Opción A — Búsqueda web:**
Genera una actividad de comprensión lectora
basada en una noticia de hoy en español.
Pide a Claude que busque la noticia, la seleccione
según criterios de nivel y temática que tú defines,
y genere la actividad directamente.

**Opción B — Google Drive:**
Sube uno de tus documentos de programación o rúbricas
a tu Project y pide a Claude que genere una actividad
coherente con lo que ya has trabajado según ese documento.

---

## ACTIVIDAD V.2 — Explora el Playground de la API

**Tipo:** Exploración técnica
**Duración estimada:** 30 minutos
**Plan:** Cuenta gratuita en console.anthropic.com

---

### La tarea

1. Crea una cuenta en **console.anthropic.com**
2. Abre el **Workbench** (Playground)
3. Configura un system prompt para tu asistente docente
4. Prueba el mismo prompt con Haiku y con Sonnet
5. Observa las diferencias en calidad y velocidad
6. Exporta el código generado y guárdalo

No necesitas ejecutar el código — solo entender
qué contiene y qué haría.

---

## ACTIVIDAD V.3 — Primera tarea con Claude Code *(para los más valientes)*

**Tipo:** Práctica técnica
**Duración estimada:** 45-60 minutos
**Requisito:** Node.js instalado

---

### La tarea

Instala Claude Code y completa una de estas tareas:

**Opción A:** Procesa una carpeta con al menos cinco
archivos de texto y genera un informe de resumen.

**Opción B:** Genera cuatro variantes de un ejercicio
existente con las preguntas en orden diferente.

**Opción C:** Crea un banco de vocabulario expandido
a partir de una lista simple de palabras.

---

### Reflexión final del módulo optativo

1. ¿Qué herramienta externa te parece más útil
   para tu práctica docente inmediata?
2. ¿Qué tarea repetitiva de tu trabajo docente
   podría automatizarse con Claude Code?
3. ¿Hay algo de este módulo que quieras profundizar
   en la tercera videotutoría?

---

## RECURSOS DEL MÓDULO V

- Anthropic Console: console.anthropic.com
- Documentación de la API: docs.anthropic.com/api
- Claude Code: docs.anthropic.com/claude-code
- Node.js: nodejs.org
- Guía de integraciones de claude.ai:
  docs.anthropic.com/integrations

---

## RESUMEN DEL MÓDULO V

| Elemento | Detalle |
|----------|---------|
| Vídeos | 3 vídeos · ~21 min total |
| Lecturas | 3 textos · ~1.800 palabras total |
| Actividades | 3 actividades · 95-120 min total |
| Entrega | Optativa · reflexión para tercera videotutoría |
| Plan Claude | Pro + cuenta en console.anthropic.com |

**Al terminar el Módulo V el participante habrá:**
- Conectado al menos una herramienta externa a Claude
- Explorado el Playground de la API de Anthropic
- Entendido qué automatizaciones son posibles
  con Claude Code para su práctica docente
- Identificado al menos una tarea repetitiva
  que puede automatizar

**Siguiente paso:** Módulo VI · Proyecto final y cierre

---

*Curso «Claude para la enseñanza: domina la herramienta»*
*claude.laclasedigital.com · Javier Benítez Láinez · benitezl@go.ugr.es*
*La Clase Digital · 2026*
