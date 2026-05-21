import React, { useState, useEffect } from 'react';
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';
import api from '../../lib/api';

export default function AdminSesiones() {
  const [sessions, setSessions] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchSessions();
  }, []);

  const fetchSessions = async () => {
    try {
      const response = await api.get('/admin/sessions');
      setSessions(response.data);
    } catch (error) {
      console.error('Error fetching sessions:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div style={{ padding: '2rem', textAlign: 'center' }}>Cargando...</div>;
  }

  return (
    <>
      <Navbar />
      <div className="inner-page">
        <div className="inner-content">
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
            <h1 className="section__title" style={{ fontSize: '2rem', marginBottom: 0 }}>
              Videotutorías en Directo
            </h1>
            <button className="btn btn--primary">
              + Nueva videotutoría
            </button>
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
            {sessions.map((session) => (
              <div
                key={session.id}
                style={{
                  background: 'var(--surface)',
                  borderRadius: 'var(--r-lg)',
                  padding: '2rem',
                  boxShadow: 'var(--shadow-sm)',
                  borderLeft: session.status === 'completed' ? '4px solid var(--green)' : '4px solid var(--amber)',
                }}
              >
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1rem' }}>
                  <div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '1rem', marginBottom: '0.5rem' }}>
                      <span style={{
                        width: '48px',
                        height: '48px',
                        borderRadius: '50%',
                        background: 'var(--blue)',
                        color: 'var(--white)',
                        fontFamily: 'var(--font-display)',
                        fontWeight: 800,
                        fontSize: '1.2rem',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                      }}>
                        {session.session_num}
                      </span>
                      <h3 style={{
                        fontFamily: 'var(--font-display)',
                        fontSize: '1.3rem',
                        fontWeight: 700,
                        color: 'var(--ink)',
                      }}>
                        {session.title}
                      </h3>
                    </div>
                    {session.scheduled_at && (
                      <p style={{ fontSize: '.95rem', color: 'var(--ink-muted)' }}>
                        📅 {new Date(session.scheduled_at).toLocaleDateString('es-ES', {
                          weekday: 'long',
                          year: 'numeric',
                          month: 'long',
                          day: 'numeric',
                          hour: '2-digit',
                          minute: '2-digit',
                        })}
                      </p>
                    )}
                  </div>
                  <span style={{
                    padding: '.4rem 1rem',
                    borderRadius: '100px',
                    fontSize: '.8rem',
                    fontWeight: 600,
                    background: session.status === 'completed' ? 'var(--green-light)' : 'var(--amber-light)',
                    color: session.status === 'completed' ? 'var(--green)' : 'var(--amber-dark)',
                    textTransform: 'uppercase',
                  }}>
                    {session.status === 'completed' ? 'Completada' : 'Programada'}
                  </span>
                </div>

                {session.zoom_link && (
                  <div style={{ marginBottom: '1rem' }}>
                    <a
                      href={session.zoom_link}
                      target="_blank"
                      rel="noopener noreferrer"
                      style={{
                        display: 'inline-block',
                        padding: '.6rem 1.2rem',
                        borderRadius: 'var(--r-sm)',
                        background: 'var(--blue-light)',
                        color: 'var(--blue)',
                        textDecoration: 'none',
                        fontSize: '.9rem',
                        fontWeight: 600,
                      }}
                    >
                      🔗 Unirse a Zoom
                    </a>
                  </div>
                )}

                {session.recording_url && (
                  <div style={{ marginBottom: '1rem' }}>
                    <a
                      href={session.recording_url}
                      target="_blank"
                      rel="noopener noreferrer"
                      style={{
                        display: 'inline-block',
                        padding: '.6rem 1.2rem',
                        borderRadius: 'var(--r-sm)',
                        background: 'var(--canvas-alt)',
                        color: 'var(--ink-soft)',
                        textDecoration: 'none',
                        fontSize: '.9rem',
                      }}
                    >
                      📺 Ver grabación
                    </a>
                  </div>
                )}

                <div style={{ display: 'flex', gap: '1rem' }}>
                  <button className="btn btn--outline" style={{ padding: '.5rem 1rem', fontSize: '.85rem' }}>
                    Editar
                  </button>
                  {session.status !== 'completed' && (
                    <button className="btn btn--primary" style={{ padding: '.5rem 1rem', fontSize: '.85rem' }}>
                      Marcar como completada
                    </button>
                  )}
                </div>
              </div>
            ))}

            {sessions.length === 0 && (
              <div style={{
                background: 'var(--surface)',
                borderRadius: 'var(--r-lg)',
                padding: '3rem',
                boxShadow: 'var(--shadow-sm)',
                textAlign: 'center',
                color: 'var(--ink-muted)',
              }}>
                <p style={{ fontSize: '1.1rem', marginBottom: '1rem' }}>No hay videotutorías programadas aún.</p>
                <p style={{ fontSize: '.9rem' }}>Crea las 3 videotutorías del curso cuando tengas las fechas confirmadas.</p>
              </div>
            )}
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}
