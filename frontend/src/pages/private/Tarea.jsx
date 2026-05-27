import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import api from '../../lib/api';

export default function Tarea() {
  const { moduleId, taskId } = useParams();
  const [task, setTask] = useState(null);
  const [submission, setSubmission] = useState(null);
  const [content, setContent] = useState('');
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    fetchTask();
    fetchSubmission();
  }, [moduleId, taskId]);

  const fetchTask = async () => {
    try {
      const response = await api.get(`/tasks/${taskId}`);
      setTask(response.data);
    } catch (error) {
      console.error('Error fetching task:', error);
    } finally {
      setLoading(false);
    }
  };

  const fetchSubmission = async () => {
    try {
      const response = await api.get(`/tasks/${taskId}/submission`);
      setSubmission(response.data);
      if (response.data?.content) {
        setContent(response.data.content);
      }
    } catch (error) {
      // No hay submission todavía, no hay error
      setSubmission(null);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitting(true);
    try {
      await api.post(`/tasks/${taskId}/submit`, { content });
      await fetchSubmission();
      alert('¡Actividad entregada correctamente!');
    } catch (error) {
      alert('Error al entregar la actividad. Inténtalo de nuevo.');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return <div style={{ padding: '2rem', textAlign: 'center' }}>Cargando...</div>;
  }

  if (!task) {
    return <div style={{ padding: '2rem', textAlign: 'center' }}>Actividad no encontrada</div>;
  }

  return (
    <div className="inner-page">
        <div className="page-hero">
          <div className="page-hero__inner">
            <p className="page-hero__tag">Actividad</p>
            <h1 className="page-hero__title">{task.title}</h1>
            <p className="page-hero__desc">Duración estimada: {task.duration}</p>
          </div>
        </div>

        <div className="inner-content">
          <div style={{ maxWidth: '800px', margin: '0 auto' }}>
            <div style={{
              background: 'var(--surface)',
              borderRadius: 'var(--r-lg)',
              padding: '2rem',
              boxShadow: 'var(--shadow-sm)',
              marginBottom: '2rem',
            }}>
              <h2 style={{
                fontFamily: 'var(--font-display)',
                fontSize: '1.3rem',
                fontWeight: 700,
                color: 'var(--ink)',
                marginBottom: '1rem',
              }}>
                Descripción de la actividad
              </h2>
              <p style={{ fontSize: '1rem', color: 'var(--ink-soft)', lineHeight: 1.7 }}>
                {task.description}
              </p>
            </div>

            {submission?.feedback ? (
              <div style={{
                background: 'var(--green-light)',
                borderRadius: 'var(--r-lg)',
                padding: '2rem',
                boxShadow: 'var(--shadow-sm)',
                marginBottom: '2rem',
                borderLeft: '4px solid var(--green)',
              }}>
                <h3 style={{
                  fontFamily: 'var(--font-display)',
                  fontSize: '1.2rem',
                  fontWeight: 700,
                  color: 'var(--green)',
                  marginBottom: '1rem',
                }}>
                  Feedback del formador
                </h3>
                <p style={{ fontSize: '1rem', color: 'var(--ink-soft)', lineHeight: 1.7, whiteSpace: 'pre-wrap' }}>
                  {submission.feedback}
                </p>
                <p style={{ fontSize: '.85rem', color: 'var(--ink-muted)', marginTop: '1rem' }}>
                  Enviado: {new Date(submission.feedback_at).toLocaleDateString('es-ES', {
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric',
                  })}
                </p>
              </div>
            ) : submission && (
              <div style={{
                background: 'var(--amber-light)',
                borderRadius: 'var(--r-lg)',
                padding: '1.5rem',
                boxShadow: 'var(--shadow-sm)',
                marginBottom: '2rem',
                borderLeft: '4px solid var(--amber)',
              }}>
                <p style={{ fontSize: '.95rem', color: 'var(--ink-soft)' }}>
                  <strong>Estado:</strong> Entregado y pendiente de revisión
                </p>
              </div>
            )}

            <form onSubmit={handleSubmit}>
              <div className="form-group">
                <label htmlFor="content">Tu respuesta</label>
                <textarea
                  id="content"
                  className="form-input"
                  value={content}
                  onChange={(e) => setContent(e.target.value)}
                  required
                  placeholder="Escribe aquí tu respuesta..."
                  style={{ minHeight: '200px' }}
                  disabled={submission}
                />
              </div>
              {submission ? (
                <div style={{
                  background: 'var(--canvas)',
                  borderRadius: 'var(--r-md)',
                  padding: '1rem',
                  textAlign: 'center',
                }}>
                  <p style={{ fontSize: '.9rem', color: 'var(--ink-muted)', marginBottom: '.5rem' }}>
                    Entregado el {new Date(submission.submitted_at).toLocaleDateString('es-ES', {
                      year: 'numeric',
                      month: 'long',
                      day: 'numeric',
                    })}
                  </p>
                  <Link to="/dashboard" className="btn btn--blue" style={{ padding: '.6rem 1.5rem' }}>
                    Volver al dashboard
                  </Link>
                </div>
              ) : (
                <button
                  type="submit"
                  className="btn btn--primary"
                  disabled={submitting}
                  style={{ width: '100%', justifyContent: 'center' }}
                >
                  {submitting ? 'Entregando...' : 'Entregar actividad'}
                </button>
              )}
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}
