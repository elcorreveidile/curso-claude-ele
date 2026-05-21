"""Contenido de los módulos del curso."""

MODULES = [
    {
        "id": "modulo-0",
        "num": "0",
        "title": "Bienvenida y punto de partida",
        "subtitle": "Qué es Claude, cómo funciona, cómo empezar",
        "hours": 1,
        "optional": False,
        "locked": False,
        "unlock_rule": "always_open",
        "videos": [
            {"id": "v0-1", "title": "Vídeo de bienvenida", "duration": "4 min"},
        ],
        "readings": [
            {"id": "r0-1", "title": "Claude: qué es, de dónde viene y por qué importa"},
        ],
        "activities": [
            {
                "id": "a0-1",
                "title": "Mi primera conversación con Claude",
                "duration": "20-30 min",
                "requires_submission": False,
                "description": "Inicia tu primera conversación con Claude. Preséntate, explica qué materias impartes y qué te gustaría explorar con Claude. No hay respuestas correctas ni incorrectas: el objetivo es que te familiarices con la interfaz.",
            },
        ],
    },
    {
        "id": "modulo-1",
        "num": "I",
        "title": "Conversar con Claude",
        "subtitle": "Prompts, FRAME y análisis de documentos",
        "hours": 4,
        "optional": False,
        "locked": True,
        "unlock_rule": "on_enrollment",
        "videos": [
            {"id": "v1-1", "title": "Cómo piensa Claude", "duration": "5 min"},
            {"id": "v1-2", "title": "El marco FRAME aplicado a Claude", "duration": "8 min"},
        ],
        "readings": [
            {"id": "r1-1", "title": "Conversar vs pedir: la diferencia que lo cambia todo"},
            {"id": "r1-2", "title": "Análisis de documentos: PDFs, imágenes y textos largos"},
        ],
        "activities": [
            {
                "id": "a1-1",
                "title": "Tu primera conversación compleja",
                "duration": "30-40 min",
                "requires_submission": True,
                "description": "Usa el marco FRAME para diseñar una conversación con Claude relacionada con tu práctica docente. Entrega el prompt inicial y un fragmento de la conversación que muestre cómo fue evolucionando.",
            },
            {
                "id": "a1-2",
                "title": "Análisis de un documento real",
                "duration": "20-30 min",
                "requires_submission": False,
                "description": "Sube un documento real de tu práctica (un examen, una unidad didáctica, un artículo) y pide a Claude que lo analice desde una perspectiva pedagógica.",
            },
        ],
    },
    {
        "id": "modulo-2",
        "num": "II",
        "title": "Projects y memoria",
        "subtitle": "Instrucciones permanentes, documentos y configuración",
        "hours": 3,
        "optional": False,
        "locked": True,
        "unlock_rule": "on_enrollment",
        "videos": [
            {"id": "v2-1", "title": "Qué son los Projects y para qué sirven", "duration": "6 min"},
            {"id": "v2-2", "title": "Configurar tu Project: instrucciones y documentos", "duration": "7 min"},
        ],
        "readings": [
            {"id": "r2-1", "title": "Projects: la memoria permanente de Claude"},
            {"id": "r2-2", "title": "Instrucciones que funcionan: cómo configurar tu Project"},
        ],
        "activities": [
            {
                "id": "a2-1",
                "title": "Configura tu primer Project",
                "duration": "30-40 min",
                "requires_submission": True,
                "description": "Crea un Project de Claude para tu práctica docente. Incluye instrucciones permanentes, sube documentos de referencia y configura el contexto. Entrega una captura de pantalla de la configuración.",
            },
            {
                "id": "a2-2",
                "title": "Gestiona múltiples Projects",
                "duration": "20 min",
                "requires_submission": False,
                "description": "Crea un segundo Project para un propósito diferente (por ejemplo, investigación, corrección de textos, generación de materiales). Experimenta con cambiar entre Projects.",
            },
        ],
    },
    {
        "id": "modulo-3",
        "num": "III",
        "title": "Artefactos",
        "subtitle": "Fichas, planes de clase, ejercicios interactivos HTML",
        "hours": 3,
        "optional": False,
        "locked": True,
        "unlock_rule": "after_videotutoria_1",
        "videos": [
            {"id": "v3-1", "title": "Qué son los artefactos y cómo activarlos", "duration": "5 min"},
            {"id": "v3-2", "title": "Artefactos para docentes: los tipos que más te interesan", "duration": "8 min"},
        ],
        "readings": [
            {"id": "r3-1", "title": "Artefactos de texto: fichas, planes y rúbricas"},
            {"id": "r3-2", "title": "Artefactos HTML: ejercicios interactivos para el aula"},
        ],
        "activities": [
            {
                "id": "a3-1",
                "title": "Genera tres artefactos para tu próxima unidad",
                "duration": "45-60 min",
                "requires_submission": True,
                "description": "Usa artefactos de Claude para generar tres materiales distintos para una unidad didáctica real que vayas a impartir: una ficha de presentación, un plan de clase y un ejercicio HTML interactivo. Entrega los tres artefactos.",
            },
            {
                "id": "a3-2",
                "title": "Edita y mejora un artefacto en conversación",
                "duration": "20 min",
                "requires_submission": False,
                "description": "Genera un artefacto y luego, en la misma conversación, pide mejoras específicas (ej: 'simplifica el vocabulario', 'añade más ejemplos', 'adapta para nivel B1'). Observa cómo Claude itera sobre el artefacto.",
            },
        ],
    },
    {
        "id": "modulo-4",
        "num": "IV",
        "title": "Claude en el aula",
        "subtitle": "Actividades para el alumnado, evaluación formativa y diversidad",
        "hours": 5,
        "optional": False,
        "locked": True,
        "unlock_rule": "after_videotutoria_2",
        "videos": [
            {"id": "v4-1", "title": "Claude como herramienta del alumnado", "duration": "6 min"},
            {"id": "v4-2", "title": "Evaluación formativa con Claude", "duration": "7 min"},
        ],
        "readings": [
            {"id": "r4-1", "title": "Diseñar actividades donde el alumno usa Claude"},
            {"id": "r4-2", "title": "Evaluación formativa con Claude"},
        ],
        "activities": [
            {
                "id": "a4-1",
                "title": "Diseña una actividad para que tu alumnado use Claude",
                "duration": "40-50 min",
                "requires_submission": True,
                "description": "Diseña una actividad completa en la que tus estudiantes usen Claude con un propósito pedagógico claro. Incluye objetivos, instrucciones para el alumnado, rúbrica de evaluación y consideraciones éticas.",
            },
            {
                "id": "a4-2",
                "title": "Corrección y feedback con Claude",
                "duration": "30-40 min",
                "requires_submission": True,
                "description": "Experimenta con usar Claude para corregir y dar feedback a producciones de tu alumnado (textos, exposiciones, proyectos). Entrega un ejemplo de corrección y reflexiona sobre las ventajas y limitaciones.",
            },
        ],
    },
    {
        "id": "modulo-5",
        "num": "V",
        "title": "Claude avanzado",
        "subtitle": "Herramientas externas, API y Claude Code",
        "hours": 3,
        "optional": True,
        "locked": True,
        "unlock_rule": "after_videotutoria_2",
        "badge": "Optativo",
        "videos": [
            {"id": "v5-1", "title": "Claude con herramientas externas", "duration": "7 min"},
            {"id": "v5-2", "title": "Introducción a la API de Claude", "duration": "8 min"},
            {"id": "v5-3", "title": "Claude Code para docentes", "duration": "6 min"},
        ],
        "readings": [
            {"id": "r5-1", "title": "Búsqueda web y Google Drive"},
            {"id": "r5-2", "title": "La API de Claude: qué es y para qué sirve a un docente"},
            {"id": "r5-3", "title": "Claude Code: automatizar sin saber programar"},
        ],
        "activities": [
            {
                "id": "a5-1",
                "title": "Conecta una herramienta externa",
                "duration": "20-30 min",
                "requires_submission": False,
                "description": "Si tienes acceso al plan Pro de Claude, experimenta con conectar una herramienta externa (búsqueda web, Google Drive). Si no, lee las documentación y reflexiona sobre posibles usos.",
            },
            {
                "id": "a5-2",
                "title": "Explora el Playground de la API",
                "duration": "30 min",
                "requires_submission": False,
                "description": "Accede al Anthropic Console y experimenta con el Playground de la API. Prueba diferentes prompts y observa cómo las respuestas son idénticas a la interfaz de chat.",
            },
            {
                "id": "a5-3",
                "title": "Primera tarea con Claude Code",
                "duration": "45-60 min",
                "requires_submission": False,
                "badge": "Para los más valientes",
                "description": "Si te atreves, instala Claude Code y automatiza una tarea simple de tu práctica docente: renombrar archivos, generar un índice automáticamente, extraer vocabulario de un texto. Comparte tu experiencia.",
            },
        ],
    },
    {
        "id": "modulo-6",
        "num": "VI",
        "title": "Proyecto final y cierre",
        "subtitle": "Unidad didáctica completa + reflexión + certificado",
        "hours": 1,
        "optional": False,
        "locked": True,
        "unlock_rule": "after_videotutoria_3",
        "videos": [
            {"id": "v6-1", "title": "El proyecto final: qué es y cómo abordarlo", "duration": "5 min"},
            {"id": "v6-2", "title": "Cierre del curso", "duration": "4 min"},
        ],
        "readings": [
            {"id": "r6-1", "title": "El proyecto final: instrucciones completas"},
            {"id": "r6-2", "title": "Cómo abordar el proyecto sin bloquearse"},
        ],
        "activities": [
            {
                "id": "a6-1",
                "title": "Proyecto final",
                "duration": "Variable",
                "requires_submission": True,
                "is_final_project": True,
                "description": "Diseña una unidad didáctica completa que integre Claude de manera coherente y alineada con tu contexto educativo. Debe incluir: objetivos, secuencia de actividades, uso de Claude (por ti y por el alumnado), evaluación y reflexión. Este proyecto es requisito para obtener el certificado.",
            },
        ],
    },
]


MODULE_UNLOCK_RULES = {
    "modulo-0": "always_open",
    "modulo-1": "on_enrollment",
    "modulo-2": "on_enrollment",
    "modulo-3": "after_videotutoria_1",
    "modulo-4": "after_videotutoria_2",
    "modulo-5": "after_videotutoria_2",
    "modulo-6": "after_videotutoria_3",
}
