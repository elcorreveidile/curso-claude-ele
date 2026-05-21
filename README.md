# [|] Claude para la enseñanza: domina la herramienta

Plataforma del curso de formación docente intensiva sobre Claude.
Desarrollada por Javier Benítez Láinez · La Clase Digital.

🌐 **[claude.laclasedigital.com](https://claude.laclasedigital.com)**

---

## Sobre el curso

**Claude para la enseñanza: domina la herramienta** es un curso de formación docente de 20 horas dedicado íntegramente a Claude — desde la primera conversación hasta la API y Claude Code.

- 📅 Primera edición: próximamente
- 👥 Plazas limitadas
- 💶 149 € · Precio fijo
- 🏅 Certificado de aprovechamiento de 20 horas

### Módulos

| Módulo | Contenido | Horas |
|--------|-----------|-------|
| **0** | Bienvenida y punto de partida | 1 h |
| **I** | Conversar con Claude | 4 h |
| **II** | Projects y memoria | 3 h |
| **III** | Artefactos | 3 h |
| **IV** | Claude en el aula | 5 h |
| **V** | Claude avanzado *(optativo)* | 3 h |
| **VI** | Proyecto final y cierre | 1 h |

---

## Stack técnico

### Frontend
- **React** (Create React App + craco)
- **Tailwind CSS**
- **React Router v6**

### Backend
- **FastAPI** (Python)
- **Supabase** (PostgreSQL)
- **Stripe** — pagos y webhooks
- **Resend** — emails transaccionales
- **JWT** + magic links — autenticación sin contraseña

### Despliegue
- Frontend: **Vercel**
- Dominio: **claude.laclasedigital.com**

---

## Estructura del repositorio

```
curso-claude-ele/
│
├── frontend/                  # React app (por construir)
├── backend/                   # FastAPI app (por construir)
├── materiales/                # Contenido de los módulos
│   ├── modulo-0/
│   ├── modulo-1/
│   ├── modulo-2/
│   ├── modulo-3/
│   ├── modulo-4/
│   ├── modulo-5-optativo/
│   └── modulo-6/
├── memory/
└── BRIEFING_CLAUDE_CODE.md    # Briefing completo para Claude Code
```

---

## Desarrollo

El briefing completo para construir la plataforma con Claude Code
está en `BRIEFING_CLAUDE_CODE.md`.

### Variables de entorno necesarias

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

## Relación con el curso anterior

Este curso es independiente de «IA para la enseñanza de ELE»
([laclasedigital.com](https://laclasedigital.com)).
Comparten identidad de marca **[|]** y paleta de color,
pero tienen repositorios y despliegues separados.

---

## Autoría

**Javier Benítez Láinez**
Docente de ELE · Doctor en Computer Science · Formador de Formadores (Instituto Cervantes)
📧 benitezl@go.ugr.es · 🌐 laclasedigital.com

---

*La Clase Digital · 2026*
