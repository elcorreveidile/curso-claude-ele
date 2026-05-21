# BRIEFING COMPLETO — «Claude para la enseñanza: domina la herramienta»
## Para Claude Code · Repositorio: elcorreveidile/curso-claude-ele

Pega este archivo completo al inicio de tu sesión con Claude Code.
Lee todo antes de escribir una sola línea de código.

---

## 1. CONTEXTO DEL PROYECTO

Este briefing describe la construcción completa de un segundo curso
de formación docente en el subdominio `claude.laclasedigital.com`.

**Repositorio anterior (referencia):** `elcorreveidile/curso-ia-ele`
**Repositorio nuevo:** `elcorreveidile/curso-claude-ele`
**Subdominio:** `claude.laclasedigital.com`

### Relación con el curso anterior
El curso anterior («IA para la enseñanza de ELE») vive en
`laclasedigital.com` y está dirigido a docentes de ELE.
Este nuevo curso («Claude para la enseñanza») es independiente,
vive en su propio subdominio, y aunque comparte la identidad
de marca [|] y la paleta de color, tiene su propio stack
y su propio despliegue en Vercel.

---

## 2. DESCRIPCIÓN DEL CURSO

**Nombre:** Claude para la enseñanza: domina la herramienta
**Subtítulo:** Formación docente intensiva · 20 horas
**Precio:** 149 € · Precio fijo · Sin precio fundador
**Formato:** Asíncrono + 3 videotutorías en directo por Zoom
**Certificado:** Aprovechamiento · 20 horas
**Público:** Docentes de cualquier materia
  (especialmente ELE, pero aplicable a otros perfiles)
**Nivel de entrada:** Sin experiencia previa con Claude

---

## 3. STACK TÉCNICO

- **Frontend:** React (Create React App + craco) · Tailwind CSS
- **Routing:** React Router v6
- **Backend:** FastAPI (Python)
- **Base de datos:** Supabase (PostgreSQL)
- **Pagos:** Stripe (Checkout + Webhooks)
- **Emails:** Resend
- **Autenticación:** Magic links + JWT (sin contraseñas)
- **Despliegue frontend:** Vercel · subdominio `claude.laclasedigital.com`
- **Identidad de marca:** símbolo [|] · misma paleta que curso anterior

### Paleta de color
```
--blue:      #0F4C81
--amber:     #F5A623
--ink:       #1A2535
--canvas:    #F4F7FA
--dark-bg:   #0A1628
--blue-lt:   #D6E8F7
--blue-bg:   #EDF4FB
--amber-lt:  #FEF3DC
--green:     #1A7A52
--green-lt:  #E8F5EC
```

---

## 4. LO QUE HAY QUE LEER ANTES DE TOCAR NADA

Clonar el repositorio anterior como referencia:
```bash
git clone https://github.com/elcorreveidile/curso-ia-ele.git referencia
```

Leer estos archivos del repositorio de referencia:
```
referencia/frontend/src/App.js
referencia/frontend/src/components/Navbar.jsx
referencia/frontend/src/components/Footer.jsx
referencia/frontend/src/components/PageHero.jsx
referencia/frontend/src/pages/public/Home.jsx
referencia/frontend/src/pages/public/Programa.jsx
referencia/frontend/src/pages/public/Precios.jsx
referencia/frontend/src/index.css
referencia/backend/server.py
referencia/backend/core.py
referencia/backend/models.py
```

---

## 5. ESTRUCTURA DEL REPOSITORIO NUEVO

```
curso-claude-ele/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── PageHero.jsx
│   │   │   ├── ModuleCard.jsx
│   │   │   ├── ProgressBar.jsx
│   │   │   └── VideoEmbed.jsx
│   │   ├── pages/
│   │   │   ├── public/
│   │   │   │   ├── Home.jsx
│   │   │   │   ├── Programa.jsx
│   │   │   │   ├── Precios.jsx
│   │   │   │   ├── Metodologia.jsx
│   │   │   │   ├── SobreMi.jsx
│   │   │   │   ├── Contacto.jsx
│   │   │   │   ├── Inscripcion.jsx
│   │   │   │   ├── Login.jsx
│   │   │   │   └── CheckEmail.jsx
│   │   │   ├── private/
│   │   │   │   ├── Dashboard.jsx
│   │   │   │   ├── Modulo.jsx
│   │   │   │   ├── Tarea.jsx
│   │   │   │   └── Certificado.jsx
│   │   │   └── admin/
│   │   │       ├── AdminDashboard.jsx
│   │   │       ├── AdminParticipantes.jsx
│   │   │       └── AdminSesiones.jsx
│   │   ├── lib/
│   │   │   ├── api.js
│   │   │   ├── auth.js
│   │   │   └── hooks.js
│   │   ├── App.js
│   │   ├── App.css
│   │   ├── index.js
│   │   └── index.css
│   ├── public/
│   │   ├── favicon.ico         ← símbolo [|]
│   │   └── logo.svg
│   ├── package.json
│   ├── craco.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
│
├── backend/
│   ├── server.py
│   ├── core.py
│   ├── models.py
│   ├── scheduler.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── modules.py
│   │   ├── tasks.py
│   │   ├── payments.py
│   │   └── admin.py
│   ├── seed_content/
│   │   └── modules_data.py     ← contenido de los módulos
│   ├── requirements.txt
│   └── tests/
│
├── materiales/
│   ├── modulo-0/
│   ├── modulo-1/
│   ├── modulo-2/
│   ├── modulo-3/
│   ├── modulo-4/
│   ├── modulo-5-optativo/
│   └── modulo-6/
│
├── memory/
│   └── decisions.md
│
└── README.md
```

---

## 6. ESTRUCTURA DE MÓDULOS DEL CURSO

```python
MODULES = [
    {
        "id": "modulo-0",
        "num": "0",
        "title": "Bienvenida y punto de partida",
        "subtitle": "Qué es Claude, cómo funciona, cómo empezar",
        "hours": 1,
        "optional": False,
        "locked": False,  # siempre abierto
        "videos": [
            {
                "id": "v0-1",
                "title": "Vídeo de bienvenida",
                "duration": "4 min",
            }
        ],
        "readings": [
            {
                "id": "r0-1",
                "title": "Claude: qué es, de dónde viene y por qué importa",
            }
        ],
        "activities": [
            {
                "id": "a0-1",
                "title": "Mi primera conversación con Claude",
                "duration": "20-30 min",
                "requires_submission": False,
            }
        ],
    },
    {
        "id": "modulo-1",
        "num": "I",
        "title": "Conversar con Claude",
        "subtitle": "Prompts, FRAME y análisis de documentos",
        "hours": 4,
        "optional": False,
        "locked": True,  # se abre tras inscripción
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
            },
            {
                "id": "a1-2",
                "title": "Análisis de un documento real",
                "duration": "20-30 min",
                "requires_submission": False,
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
            },
            {
                "id": "a2-2",
                "title": "Gestiona múltiples Projects",
                "duration": "20 min",
                "requires_submission": False,
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
            },
            {
                "id": "a3-2",
                "title": "Edita y mejora un artefacto en conversación",
                "duration": "20 min",
                "requires_submission": False,
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
            },
            {
                "id": "a4-2",
                "title": "Corrección y feedback con Claude",
                "duration": "30-40 min",
                "requires_submission": True,
            },
        ],
    },
    {
        "id": "modulo-5",
        "num": "V",
        "title": "Claude avanzado",
        "subtitle": "Herramientas externas, API y Claude Code",
        "hours": 3,
        "optional": True,  # MÓDULO OPTATIVO
        "locked": True,
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
            },
            {
                "id": "a5-2",
                "title": "Explora el Playground de la API",
                "duration": "30 min",
                "requires_submission": False,
            },
            {
                "id": "a5-3",
                "title": "Primera tarea con Claude Code",
                "duration": "45-60 min",
                "requires_submission": False,
                "badge": "Para los más valientes",
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
            }
        ],
    },
]
```

---

## 7. BASE DE DATOS — TABLAS EN SUPABASE

### 7.1 Tabla `enrollments`

```sql
CREATE TABLE enrollments (
  id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  email             text NOT NULL UNIQUE,
  name              text,
  stripe_payment_id text,
  amount_paid       integer DEFAULT 14900, -- 149 € en céntimos
  status            text DEFAULT 'active',
  -- 'pending' | 'active' | 'completed' | 'cancelled'
  enrolled_at       timestamptz DEFAULT now(),
  completed_at      timestamptz,
  certificate_code  text UNIQUE
);
```

### 7.2 Tabla `module_progress`

```sql
CREATE TABLE module_progress (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  enrollment_id uuid REFERENCES enrollments(id),
  module_id     text NOT NULL,
  status        text DEFAULT 'locked',
  -- 'locked' | 'available' | 'in_progress' | 'completed'
  unlocked_at   timestamptz,
  completed_at  timestamptz,
  UNIQUE(enrollment_id, module_id)
);
```

### 7.3 Tabla `task_submissions`

```sql
CREATE TABLE task_submissions (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  enrollment_id uuid REFERENCES enrollments(id),
  activity_id   text NOT NULL,
  module_id     text NOT NULL,
  content       text,
  file_url      text,
  submitted_at  timestamptz DEFAULT now(),
  feedback      text,
  feedback_at   timestamptz,
  UNIQUE(enrollment_id, activity_id)
);
```

### 7.4 Tabla `live_sessions`

```sql
CREATE TABLE live_sessions (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  session_num   integer NOT NULL, -- 1, 2 o 3
  title         text NOT NULL,
  scheduled_at  timestamptz,
  zoom_link     text,
  recording_url text,
  status        text DEFAULT 'scheduled',
  -- 'scheduled' | 'completed' | 'cancelled'
  created_at    timestamptz DEFAULT now()
);
```

### 7.5 Tabla `certificates`

```sql
CREATE TABLE certificates (
  id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  enrollment_id   uuid REFERENCES enrollments(id) UNIQUE,
  name            text NOT NULL,
  issued_at       timestamptz DEFAULT now(),
  verification_code text UNIQUE DEFAULT
    substring(md5(random()::text), 1, 12)
);
```

---

## 8. LÓGICA DE APERTURA DE MÓDULOS

Los módulos se abren de forma progresiva:

```python
MODULE_UNLOCK_RULES = {
    "modulo-0": "always_open",
    "modulo-1": "on_enrollment",      # se abre al inscribirse
    "modulo-2": "on_enrollment",      # se abre al inscribirse
    "modulo-3": "after_videotutoria_1",  # se abre después de la sesión 1
    "modulo-4": "after_videotutoria_2",  # se abre después de la sesión 2
    "modulo-5": "after_videotutoria_2",  # optativo, mismo momento
    "modulo-6": "after_videotutoria_3",  # se abre después de la sesión 3
}
```

El admin activa el desbloqueo desde el panel
después de cada videotutoría.

---

## 9. PÁGINAS PÚBLICAS — CONTENIDO

### 9.1 Home.jsx — Landing principal

**Hero:**
```jsx
const HERO = {
  tag: 'Formación docente · 20 horas · 149 €',
  title: 'Claude para la enseñanza',
  subtitle: 'Domina la herramienta',
  desc: 'El primer curso de formación docente dedicado íntegramente a Claude. De la primera conversación a los artefactos, los Projects, la evaluación formativa y la API. Para docentes que quieren llegar a todo.',
  cta_primary: { label: 'Inscribirme ahora', to: '/inscripcion' },
  cta_secondary: { label: 'Ver el programa', to: '/programa' },
  badges: ['20 horas', '3 videotutorías en directo', 'Certificado incluido', 'Plazas limitadas'],
};
```

**Por qué este curso:**
```jsx
const REASONS = [
  {
    icon: '🎯',
    title: 'Todo Claude, sin excepciones',
    text: 'Desde la interfaz hasta la API. Desde los prompts hasta Claude Code. El único curso que cubre Claude en profundidad para docentes.',
  },
  {
    icon: '🏗️',
    title: 'Projects y artefactos desde el primer día',
    text: 'No aprenderás a usar Claude — aprenderás a dominarlo. Projects configurados para tu práctica real, artefactos HTML interactivos listos para el aula.',
  },
  {
    icon: '👥',
    title: 'Claude en el aula, no solo en tu mesa',
    text: 'Diseña actividades donde tu alumnado usa Claude con criterio. Evaluación formativa automatizada. Atención a la diversidad con IA.',
  },
  {
    icon: '🔧',
    title: 'Avanzado si quieres llegar más lejos',
    text: 'Módulo optativo con herramientas externas, API y Claude Code para automatizar tareas repetitivas sin saber programar.',
  },
];
```

**Para quién es:**
```jsx
const FOR_WHO = [
  'Docentes de cualquier materia que usan o quieren usar Claude en su práctica',
  'Docentes de ELE que ya han hecho el curso de IA para la enseñanza',
  'Formadores que quieren incorporar IA en sus cursos y talleres',
  'Coordinadores pedagógicos que necesitan entender Claude para asesorar a sus equipos',
];
```

### 9.2 Programa.jsx

Usa el array `MODULES` de la sección 6.
Muestra todos los módulos con sus vídeos, lecturas
y actividades. El módulo V tiene badge «Optativo».

### 9.3 Precios.jsx

```jsx
const PRICING = {
  price: 149,
  currency: 'EUR',
  label: 'Precio único',
  includes: [
    '20 horas de formación (17 obligatorias + 3 optativas)',
    '3 videotutorías en directo por Zoom',
    'Acceso de por vida a los materiales',
    'Certificado de aprovechamiento de 20 horas',
    'Acceso al grupo privado del curso',
    'Plantillas descargables: Project, instrucciones, prompts FRAME',
  ],
  not_included: [
    'Plan Pro de Claude (recomendado a partir del Módulo II · 20 $/mes)',
    'Cuenta en Anthropic Console para el Módulo V (gratuita)',
  ],
  stripe_price_id: 'PENDIENTE_DE_CONFIGURAR',
  faq: [
    {
      q: '¿Necesito experiencia previa con Claude?',
      a: 'No. El curso parte desde cero.',
    },
    {
      q: '¿Necesito el plan Pro de Claude?',
      a: 'El plan gratuito es suficiente para los primeros módulos. A partir del Módulo II recomendamos el plan Pro para sacar el máximo partido.',
    },
    {
      q: '¿El curso es solo para docentes de ELE?',
      a: 'No. Está diseñado para docentes de cualquier materia.',
    },
    {
      q: '¿Qué pasa si no puedo asistir a una videotutoría en directo?',
      a: 'Las videotutorías se graban y están disponibles en la plataforma.',
    },
    {
      q: '¿Cuándo se celebran las videotutorías?',
      a: 'Las fechas se publican en el calendario del curso una vez abierta la inscripción.',
    },
  ],
};
```

---

## 10. SISTEMA DE AUTENTICACIÓN

Igual que el curso anterior: magic links + JWT.

Flujo:
1. Usuario introduce su email en `/login`
2. Backend envía magic link por Resend
3. Usuario hace clic en el enlace
4. Backend valida el token y genera JWT
5. Usuario accede al dashboard

Solo usuarios con `enrollment.status = 'active'`
pueden acceder a las páginas privadas.

---

## 11. EMAILS TRANSACCIONALES (RESEND)

| Evento | Destinatario | Asunto |
|--------|-------------|--------|
| Inscripción completada | Participante | Bienvenido/a al curso · Claude para la enseñanza |
| Inscripción completada | Formador | Nueva inscripción · [nombre] · [email] |
| Magic link | Participante | Tu enlace de acceso al curso |
| Módulo desbloqueado | Participante | Ya puedes acceder al Módulo [N] |
| Videotutoría próxima (24h antes) | Participante | Mañana · Videotutoría [N] · [hora] |
| Feedback disponible | Participante | Tienes feedback nuevo en [actividad] |
| Certificado disponible | Participante | Tu certificado ya está listo |

---

## 12. PANEL DE ADMINISTRACIÓN

Secciones del panel `/admin`:

**Participantes:**
- Lista completa con estado de progreso
- Ver tareas entregadas por participante
- Escribir feedback en tareas
- Generar certificado manualmente

**Módulos:**
- Desbloquear módulo para todos los participantes
- Ver progreso global por módulo

**Videotutorías:**
- Crear/editar sesiones en directo
- Añadir enlace Zoom
- Añadir enlace de grabación
- Marcar como completada (desbloquea el siguiente módulo)

**Certificados:**
- Generar certificados pendientes
- Ver todos los certificados emitidos
- Verificar código de certificado

---

## 13. INSTRUCCIONES ESPECÍFICAS PARA CLAUDE CODE

### Lo que debe hacer

1. Clonar el repositorio de referencia y leer
   los archivos listados en la sección 4.

2. Inicializar el nuevo repositorio con la estructura
   de la sección 5.

3. Crear el frontend React con:
   - Todas las páginas públicas listadas en la sección 9
   - Todas las páginas privadas (Dashboard, Modulo, Tarea, Certificado)
   - El panel de administración
   - Los componentes compartidos

4. Crear el backend FastAPI con:
   - Todas las rutas de autenticación (magic links)
   - Todas las rutas de módulos y progreso
   - Todas las rutas de tareas y feedback
   - Las rutas de pagos con Stripe
   - Las rutas de administración
   - El scheduler para emails automáticos

5. Crear las tablas de Supabase de la sección 7.

6. Configurar los emails de Resend de la sección 11.

7. Crear el README del repositorio.

### Lo que NO debe hacer

- No copiar código del repositorio anterior —
  inspirarse en la arquitectura, no copiar.
- No crear rutas de sesiones individuales o grupales
  (ese sistema es solo del curso anterior).
- No usar localStorage ni sessionStorage.
- No añadir dependencias npm innecesarias.
- No crear el contenido de los módulos en el frontend —
  el contenido viene del backend/Supabase.

### Estilo visual

- Misma paleta que el curso anterior (sección 3).
- El símbolo [|] en el favicon, logo y footer.
- Badge «Optativo» en el Módulo V con color ámbar.
- El hero de Home con fondo oscuro (#0A1628) y texto blanco.
- Las tarjetas de módulo con el número romano grande
  en color azul claro como fondo decorativo.
- Los vídeos como placeholders con estructura
  para embeber cualquier plataforma de vídeo.

---

## 14. VARIABLES DE ENTORNO NECESARIAS (BACKEND)

```
SUPABASE_URL=
SUPABASE_SERVICE_KEY=
JWT_SECRET=
MAGIC_LINK_SECRET=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
STRIPE_PRICE_ID_CURSO_CLAUDE=
RESEND_API_KEY=
RESEND_FROM=
FRONTEND_ORIGIN=https://claude.laclasedigital.com
ADMIN_EMAIL=benitezl@go.ugr.es
```

---

## 15. README DEL REPOSITORIO

```markdown
# [|] Claude para la enseñanza: domina la herramienta

Plataforma del curso de formación docente intensiva sobre Claude.
Desarrollada por Javier Benítez Láinez · La Clase Digital.

🌐 claude.laclasedigital.com

## Sobre el curso

20 horas · 3 videotutorías · 149 € · Certificado de aprovechamiento

Formación docente intensiva sobre Claude para docentes
de cualquier materia. Desde la primera conversación
hasta la API y Claude Code.

## Stack

Frontend: React + Tailwind · Backend: FastAPI · DB: Supabase
Pagos: Stripe · Emails: Resend · Despliegue: Vercel

## Módulos

| Módulo | Contenido | Horas |
|--------|-----------|-------|
| 0 | Bienvenida y punto de partida | 1 h |
| I | Conversar con Claude | 4 h |
| II | Projects y memoria | 3 h |
| III | Artefactos | 3 h |
| IV | Claude en el aula | 5 h |
| V | Claude avanzado (optativo) | 3 h |
| VI | Proyecto final y cierre | 1 h |

## Relación con el curso anterior

Este curso es independiente del curso
«IA para la enseñanza de ELE» (laclasedigital.com).
Comparten identidad de marca [|] y paleta de color,
pero tienen repositorios y despliegues separados.

## Autoría

Javier Benítez Láinez · benitezl@go.ugr.es
La Clase Digital · laclasedigital.com · 2026
```

---

## 16. CHECKLIST DE ENTREGA

### Frontend
- [ ] Home.jsx con hero, razones, para quién es y CTA
- [ ] Programa.jsx con todos los módulos y sus contenidos
- [ ] Precios.jsx con FAQ
- [ ] Inscripcion.jsx con formulario y Stripe Checkout
- [ ] Login.jsx con campo de email y magic link
- [ ] CheckEmail.jsx con confirmación
- [ ] Dashboard.jsx con progreso por módulo
- [ ] Modulo.jsx con vídeos, lecturas y actividades
- [ ] Tarea.jsx con formulario de entrega y feedback
- [ ] Certificado.jsx con descarga y código de verificación
- [ ] AdminDashboard.jsx
- [ ] AdminParticipantes.jsx con feedback
- [ ] AdminSesiones.jsx con gestión de videotutorías

### Backend
- [ ] Autenticación con magic links funcional
- [ ] Flujo de inscripción con Stripe completo
- [ ] Sistema de progreso y desbloqueo de módulos
- [ ] Entrega de tareas y feedback del formador
- [ ] Generación de certificados con código único
- [ ] Todos los emails de Resend configurados
- [ ] Panel de admin con todas las funciones

### Base de datos
- [ ] Tabla `enrollments` creada
- [ ] Tabla `module_progress` creada
- [ ] Tabla `task_submissions` creada
- [ ] Tabla `live_sessions` creada
- [ ] Tabla `certificates` creada

### General
- [ ] README del repositorio creado y subido
- [ ] Variables de entorno documentadas en `.env.example`
- [ ] El sitio funciona en local antes de desplegar
- [ ] Sin errores en consola

---

## 17. PENDIENTE — NO IMPLEMENTAR AÚN

- **Stripe Price ID:** pendiente de configurar.
  Usar placeholder `'PENDIENTE_DE_CONFIGURAR'`.
- **URLs de vídeo:** los vídeos no están grabados aún.
  Crear placeholders con estructura para embeber.
- **Fechas de videotutorías:** por determinar.
  El admin las configura desde el panel.
- **Grupo privado del curso:** por determinar la plataforma
  (WhatsApp, Telegram, Discord). No implementar aún.
