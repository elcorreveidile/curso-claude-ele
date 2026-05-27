import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../../lib/api';

export default function Dashboard() {
  const [modules, setModules] = useState([]);
  const [progress, setProgress] = useState({ total: 0, completed: 0 });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchModules();
  }, []);

  const fetchModules = async () => {
    try {
      const [modulesRes, progressRes] = await Promise.all([
        api.get('/modules'),
        api.get('/modules/progress'),
      ]);
      setModules(modulesRes.data);
      setProgress(progressRes.data);
    } catch (error) {
      console.error('Error fetching dashboard:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div style={{ padding: '2rem', textAlign: 'center' }}>Cargando...</div>;
  }

  const progressPercent = progress.total > 0 ? Math.round((progress.completed / progress.total) * 100) : 0;

  return (
    <div className="inner-page">
        <div className="inner-content">
          <div style={{ marginBottom: '3rem' }}>
            <h1 className="section__title" style={{ fontSize: '2rem', marginBottom: '1rem' }}>
              Mi progreso
            </h1>
            <p style={{ fontSize: '1.1rem', color: 'var(--ink-soft)', marginBottom: '2rem' }}>
              Avanza a tu ritmo por los módulos del curso.
            </p>

            <div style={{
              background: 'var(--surface)',
              borderRadius: 'var(--r-lg)',
              padding: '2rem',
              boxShadow: 'var(--shadow-sm)',
              marginBottom: '2rem',
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
                <span style={{ fontSize: '.9rem', fontWeight: 600, color: 'var(--ink)' }}>
                  Progreso general
                </span>
                <span style={{ fontSize: '.9rem', color: 'var(--blue-mid)', fontWeight: 600 }}>
                  {progress.completed} de {progress.total} módulos completados
                </span>
              </div>
              <div style={{
                height: '8px',
                background: 'var(--canvas-alt)',
                borderRadius: '100px',
                overflow: 'hidden',
              }}>
                <div style={{
                  height: '100%',
                  width: `${progressPercent}%`,
                  background: 'linear-gradient(90deg, var(--blue), var(--amber))',
                  borderRadius: '100px',
                  transition: 'width .4s',
                }} />
              </div>
            </div>
          </div>

          <div>
            <h2 className="section__title" style={{ fontSize: '1.5rem', marginBottom: '1.5rem' }}>
              Módulos
            </h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              {modules.map((module) => (
                <div
                  key={module.id}
                  className={`module-row module-row--${module.status}`}
                  style={{
                    background: 'var(--surface)',
                    borderRadius: 'var(--r-md)',
                    padding: '1.5rem',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '1.5rem',
                    boxShadow: 'var(--shadow-sm)',
                    borderLeft: module.status === 'locked' ? '3px solid var(--canvas-alt)' : '3px solid var(--amber)',
                    opacity: module.status === 'locked' ? 0.6 : 1,
                  }}
                >
                  <div style={{
                    width: '48px',
                    height: '48px',
                    borderRadius: '50%',
                    background: 'var(--blue-light)',
                    color: 'var(--blue)',
                    fontFamily: 'var(--font-display)',
                    fontWeight: 800,
                    fontSize: '1.2rem',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    flexShrink: 0,
                  }}>
                    {module.num}
                  </div>
                  <div style={{ flex: 1 }}>
                    <h3 style={{
                      fontFamily: 'var(--font-display)',
                      fontSize: '1.1rem',
                      fontWeight: 700,
                      color: 'var(--ink)',
                      marginBottom: '.25rem',
                    }}>
                      {module.title}
                    </h3>
                    <p style={{ fontSize: '.85rem', color: 'var(--ink-muted)', marginBottom: '.5rem' }}>
                      {module.subtitle}
                    </p>
                    <p style={{ fontSize: '.8rem', color: 'var(--ink-muted)' }}>
                      {module.hours} horas · {module.videos?.length || 0} vídeos · {module.activities?.length || 0} actividades
                    </p>
                  </div>
                  <div>
                    {module.status === 'locked' && (
                      <span style={{
                        padding: '.4rem 1rem',
                        borderRadius: '100px',
                        background: 'var(--canvas)',
                        color: 'var(--ink-muted)',
                        fontSize: '.8rem',
                        fontWeight: 600,
                      }}>
                        Bloqueado
                      </span>
                    )}
                    {module.status === 'available' && (
                      <Link
                        to={`/modulo/${module.id}`}
                        className="btn btn--primary"
                        style={{ padding: '.6rem 1.5rem' }}
                      >
                        Comenzar →
                      </Link>
                    )}
                    {module.status === 'in_progress' && (
                      <Link
                        to={`/modulo/${module.id}`}
                        className="btn btn--blue"
                        style={{ padding: '.6rem 1.5rem' }}
                      >
                        Continuar →
                      </Link>
                    )}
                    {module.status === 'completed' && (
                      <span style={{
                        padding: '.4rem 1rem',
                        borderRadius: '100px',
                        background: 'var(--green-light)',
                        color: 'var(--green)',
                        fontSize: '.8rem',
                        fontWeight: 600,
                      }}>
                        ✓ Completado
                      </span>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
