# Decisiones Técnicas - Curso Claude para la Enseñanza

## Decisiones del Proyecto (2026-05-22)

### Arquitectura General
- **Subdominio independiente:** claude.laclasedigital.com
- **Repositorio separado** del curso de IA para ELE
- **Stack:** React + FastAPI + Supabase + Stripe + Resend
- **Despliegue:** Vercel (frontend) + Railway/Render (backend)

### Características del Curso
- **20 horas · 3 videotutorías · 149 €** precio fijo (sin tiers)
- **Módulo V optativo** (3 horas) con badge ámbar especial
- **Sin GitHub** en el contenido (a diferencia del curso anterior)
- **Público objetivo:** Docentes de cualquier materia, no solo ELE

## Decisiones Técnicas Específicas

### Frontend - React + Tailwind

#### Componentes Base
- **Navbar.jsx** - Navegación condicional (público vs autenticado vs admin)
- **Footer.jsx** - 3 columnas con marca [|], links y contacto
- **PageHero.jsx** - Hero reutilizable para páginas interiores
- **ModuleCard.jsx** - Tarjetas de módulos con número romano y badge optativo
- **Protected.jsx** - HOC para rutas privadas que verifica JWT

#### Páginas Públicas
- **Home.jsx** - Landing con hero oscuro, razones, para quién es
- **Programa.jsx** - Grid de módulos con contenido dinámico del backend
- **Precios.jsx** - Precio único 149€, FAQ, lista de incluidos/no incluidos
- **Login.jsx** - Campo de email para magic link
- **CheckEmail.jsx** - Confirmación "Revisa tu email"
- **Inscripcion.jsx** - Formulario + Stripe Checkout

#### Páginas Privadas
- **Dashboard.jsx** - Progreso general, lista de módulos con estado
- **Modulo.jsx** - Vídeos, lecturas, actividades de un módulo
- **Tarea.jsx** - Descripción, formulario de entrega, feedback
- **Certificado.jsx** - Vista previa + descarga PDF + código verificación

#### Páginas Admin
- **AdminDashboard.jsx** - Stats, enlaces a secciones
- **AdminParticipantes.jsx** - Tabla de estudiantes con progreso
- **AdminSesiones.jsx** - Gestión de 3 videotutorías + desbloqueo de módulos

#### Gestión de Estado
- **Context API** para autenticación (AuthProvider)
- **localStorage** para persistencia de JWT
- **React Query** podría añadirse en futuro para cache

### Backend - FastAPI + Supabase

#### Estructura de Rutas
- **/auth** - Magic links + JWT (login, verify, me)
- **/payments** - Stripe Checkout + webhooks
- **/modules** - Contenido de módulos + progreso
- **/tasks** - Actividades, entregas, feedback
- **/admin** - Stats, participantes, sesiones, certificados

#### Autenticación
- **Magic links** enviados por email (sin contraseñas)
- **JWT** con expiración de 30 días
- **Tokens de un solo uso** para magic links (nonce)
- **Dos secrets diferentes:** JWT_SECRET y MAGIC_LINK_SECRET

#### Base de Datos (Supabase PostgreSQL)

**Tablas creadas:**
1. **enrollments** - Datos de inscripción (email, name, stripe_payment_id, status, certificate_code)
2. **module_progress** - Progreso por módulo (enrollment_id, module_id, status: locked/available/in_progress/completed)
3. **task_submissions** - Entregas (content, feedback, feedback_at)
4. **live_sessions** - 3 videotutorías (session_num, title, scheduled_at, zoom_link, recording_url, status)
5. **certificates** - Códigos de verificación únicos (enrollment_id, name, verification_code)

**Relaciones:**
- enrollments → module_progress (1:N)
- enrollments → task_submissions (1:N)
- enrollments → certificates (1:1)
- live_sessions (entidades independientes)

#### Lógica de Desbloqueo de Módulos
```
Módulo 0: always_open (siempre disponible)
Módulos 1-2: on_enrollment (automático al inscribirse)
Módulo 3: after_videotutoria_1 (admin marca sesión 1 como completada)
Módulos 4-5: after_videotutoria_2 (admin marca sesión 2 como completada)
Módulo 6: after_videotutoria_3 (admin marca sesión 3 como completada)
```

#### Sistema de Pagos (Stripe)
- **Stripe Checkout Session** (no Elements) para simplicidad
- **Webhooks** para confirmación asíncrona de pagos
- **Precio único:** 149€ (configurado en STRIPE_PRICE_ID_CURSO_CLAUDE)
- **Flujo completo:** Usuario → Checkout → Webhook → Crear enrollment → Enviar email welcome

### Emails Transaccionales (Resend)

**Tipos implementados:**
1. **Bienvenida** - Tras pago exitoso con magic link de acceso
2. **Nueva inscripción** - Copia al formador (ADMIN_EMAIL)
3. **Magic link** - Para login
4. **Módulo desbloqueado** - Cuando admin marca videotutoría como completada
5. **Feedback disponible** - Cuando formador escribe feedback en tarea
6. **Certificado disponible** - Al completar curso

**Templates:**
- **wrap_email()** function para estructura HTML común
- **Footer con marca** [|] en todos los emails
- **Viewport meta tag** para correcto rendering en móvil
- **Mobile-friendly** con media queries

## Pendiente de Implementación

### Configuración Requerida
- **Stripe Price ID** - Por configurar en Stripe Dashboard
- **Fechas de videotutorías** - Por determinar (admin las configura)
- **Plataforma grupo privado** - Por decidir (WhatsApp/Telegram/Discord)
- **Grabación de vídeos** - Por producir (placeholders en sistema)

### Mejoras Futuras
- **React Query** para cache de datos y sincronización optimista
- **Upload de archivos** en entregas de tareas (PDFs, docs)
- **Generación de PDF** para certificados con diseño personalizado
- **Sistema de notificaciones** in-app para feedback nuevo
- **Foro/discusiones** por módulo
- **Analytics** de progreso y engagement
- **Tests** unitarios y de integración

## Variables de Entorno Requeridas

```bash
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

**Fecha:** 2026-05-22
**Proyecto:** Claude para la enseñanza: domina la herramienta
**Stack:** React + FastAPI + Supabase + Stripe + Resend
**Autoría:** Claude Code + Javier Benítez Láinez
