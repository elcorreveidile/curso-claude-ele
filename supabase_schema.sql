-- Script SQL para crear las tablas en Supabase
-- Curso: Claude para la enseñanza: domina la herramienta
-- Fecha: 2026-05-22

-- ============================================
-- TABLA: enrollments (Inscripciones)
-- ============================================
CREATE TABLE IF NOT EXISTS enrollments (
  id                uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  email             text NOT NULL UNIQUE,
  name              text,
  stripe_payment_id text,
  amount_paid       integer DEFAULT 14900, -- 149 € en céntimos
  status            text DEFAULT 'active', -- 'pending' | 'active' | 'completed' | 'cancelled'
  enrolled_at       timestamptz DEFAULT now(),
  completed_at      timestamptz,
  certificate_code  text UNIQUE,
  last_seen_at      timestamptz,
  role              text DEFAULT 'student' -- 'student' | 'admin'
);

-- Índices para optimizar búsquedas comunes
CREATE INDEX IF NOT EXISTS idx_enrollments_email ON enrollments(email);
CREATE INDEX IF NOT EXISTS idx_enrollments_status ON enrollments(status);
CREATE INDEX IF NOT EXISTS idx_enrollments_created_at ON enrollments(enrolled_at DESC);

-- ============================================
-- TABLA: module_progress (Progreso de módulos)
-- ============================================
CREATE TABLE IF NOT EXISTS module_progress (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  enrollment_id uuid NOT NULL REFERENCES enrollments(id) ON DELETE CASCADE,
  module_id     text NOT NULL,
  status        text DEFAULT 'locked', -- 'locked' | 'available' | 'in_progress' | 'completed'
  unlocked_at   timestamptz,
  completed_at  timestamptz,
  created_at    timestamptz DEFAULT now(),
  UNIQUE(enrollment_id, module_id)
);

-- Índices para optimizar búsquedas comunes
CREATE INDEX IF NOT EXISTS idx_module_progress_enrollment ON module_progress(enrollment_id);
CREATE INDEX IF NOT EXISTS idx_module_progress_status ON module_progress(status);
CREATE INDEX IF NOT EXISTS idx_module_progress_module ON module_progress(module_id);

-- ============================================
-- TABLA: task_submissions (Entregas de tareas)
-- ============================================
CREATE TABLE IF NOT EXISTS task_submissions (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  enrollment_id uuid NOT NULL REFERENCES enrollments(id) ON DELETE CASCADE,
  activity_id   text NOT NULL,
  module_id     text NOT NULL,
  content       text,
  file_url      text, -- Para futuros uploads de archivos
  submitted_at  timestamptz DEFAULT now(),
  feedback      text,
  feedback_at   timestamptz,
  UNIQUE(enrollment_id, activity_id)
);

-- Índices para optimizar búsquedas comunes
CREATE INDEX IF NOT EXISTS idx_task_submissions_enrollment ON task_submissions(enrollment_id);
CREATE INDEX IF NOT EXISTS idx_task_submissions_activity ON task_submissions(activity_id);
CREATE INDEX IF NOT EXISTS idx_task_submissions_feedback ON task_submissions(feedback) WHERE feedback IS NULL;

-- ============================================
-- TABLA: live_sessions (Videotutorías en directo)
-- ============================================
CREATE TABLE IF NOT EXISTS live_sessions (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  session_num   integer NOT NULL, -- 1, 2 o 3
  title         text NOT NULL,
  description   text,
  scheduled_at  timestamptz,
  zoom_link     text,
  recording_url text,
  status        text DEFAULT 'scheduled', -- 'scheduled' | 'completed' | 'cancelled'
  created_at    timestamptz DEFAULT now(),
  updated_at    timestamptz DEFAULT now()
);

-- Índices para optimizar búsquedas comunes
CREATE INDEX IF NOT EXISTS idx_live_sessions_num ON live_sessions(session_num);
CREATE INDEX IF NOT EXISTS idx_live_sessions_status ON live_sessions(status);
CREATE INDEX IF NOT EXISTS idx_live_sessions_scheduled ON live_sessions(scheduled_at);

-- ============================================
-- TABLA: certificates (Certificados)
-- ============================================
CREATE TABLE IF NOT EXISTS certificates (
  id              uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  enrollment_id   uuid NOT NULL UNIQUE REFERENCES enrollments(id) ON DELETE CASCADE,
  name            text NOT NULL,
  verification_code text UNIQUE DEFAULT substring(md5(random()::text), 1, 12),
  issued_at       timestamptz DEFAULT now()
);

-- Índices para optimizar búsquedas comunes
CREATE INDEX IF NOT EXISTS idx_certificates_enrollment ON certificates(enrollment_id);
CREATE INDEX IF NOT EXISTS idx_certificates_verification ON certificates(verification_code);

-- ============================================
-- ROW LEVEL SECURITY (RLS) - Opcional pero recomendado
-- ============================================
-- Habilitar RLS en todas las tablas
ALTER TABLE enrollments ENABLE ROW LEVEL SECURITY;
ALTER TABLE module_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE task_submissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE live_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE certificates ENABLE ROW LEVEL SECURITY;

-- Políticas RLS básicas (ajustar según necesidades)
-- Enrollments: usuarios solo pueden ver su propia inscripción
CREATE POLICY "Users can view own enrollment" ON enrollments
  FOR SELECT USING (email = current_email());

-- Module progress: usuarios solo pueden ver su propio progreso
CREATE POLICY "Users can view own progress" ON module_progress
  FOR SELECT USING (
    enrollment_id IN (SELECT id FROM enrollments WHERE email = current_email())
  );

-- Task submissions: usuarios solo pueden ver sus propias submissions
CREATE POLICY "Users can view own submissions" ON task_submissions
  FOR SELECT USING (
    enrollment_id IN (SELECT id FROM enrollments WHERE email = current_email())
  );

-- Certificates: usuarios solo pueden ver su propio certificado
CREATE POLICY "Users can view own certificate" ON certificates
  FOR SELECT USING (
    enrollment_id IN (SELECT id FROM enrollments WHERE email = current_email())
  );

-- Live sessions: todos pueden ver (son públicas para estudiantes)
CREATE POLICY "Everyone can view sessions" ON live_sessions
  FOR SELECT USING (true);

-- ============================================
-- DATOS INICIALES - Sesiones de videotutoría
-- ============================================
INSERT INTO live_sessions (session_num, title, description, status) VALUES
(1, 'Videotutoría 1: Fundamentos de Claude', 'Introducción práctica a Claude y conversación básica.', 'scheduled'),
(2, 'Videotutoría 2: Projects y Artefactos', 'Cómo configurar Projects y usar artefactos en tu práctica.', 'scheduled'),
(3, 'Videotutoría 3: Claude en el aula', 'Evaluación formativa y actividades para estudiantes.', 'scheduled')
ON CONFLICT DO NOTHING;

-- ============================================
-- FUNCIONES HELPER (Opcional)
-- ============================================

-- Función para obtener email actual del usuario JWT
CREATE OR REPLACE FUNCTION current_email()
RETURNS text AS $$
  SELECT NULL::text; -- Esta función debe implementarse según tu auth system
$$ LANGUAGE sql STABLE;

-- ============================================
-- NOTAS
-- ============================================
-- 1. Este script asume que ya has creado el proyecto en Supabase
-- 2. Ajusta los tipos de datos según tus necesidades específicas
-- 3. Las políticas RLS son básicas - personalízalas según tu auth system
-- 4. Los índices optimizan queries comunes del frontend
-- 5. current_email() necesita implementarse según tu auth system
--    (usualmente via JWT token en los headers)

-- ============================================
-- VERIFICACIÓN
-- ============================================
-- Verifica que las tablas se crearon correctamente
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public'
  AND table_name IN ('enrollments', 'module_progress', 'task_submissions', 'live_sessions', 'certificates')
ORDER BY table_name, ordinal_position;