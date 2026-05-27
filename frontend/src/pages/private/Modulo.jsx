import React, { useState, useEffect } from 'react';
import { useParams, Link } from 'react-router-dom';
import api from '../../lib/api';

export default function Modulo() {
  const { id } = useParams();
  const [module, setModule] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchModule();
  }, [id]);

  const fetchModule = async () => {
    try {
      const response = await api.get(`/modules/${id}`);
      setModule(response.data);
    } catch (error) {
      console.error('Error fetching module:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div style={{ padding: '2rem', textAlign: 'center' }}>Cargando...</div>;
  }

  if (!module) {
    return <div style={{ padding: '2rem', textAlign: 'center' }}>Módulo no encontrado</div>;
  }

  return (
    <div className="inner-page">
        <div className="page-hero">
          <div className="page-hero__inner">
            <p className="page-hero__tag">Módulo {module.num}</p>
            <h1 className="page-hero__title">{module.title}</h1>
            <p className="page-hero__desc">{module.subtitle}</p>
          </div>
        </div>

        <div className="inner-content">
          <div style={{ marginBottom: '3rem' }}>
            <h2 className="section__title" style={{ fontSize: '1.5rem', marginBottom: '1.5rem' }}>
              Vídeos
            </h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.5rem' }}>
              {module.videos?.map((video) => (
                <div
                  key={video.id}
                  style={{
                    background: 'var(--surface)',
                    borderRadius: 'var(--r-md)',
                    padding: '1.5rem',
                    boxShadow: 'var(--shadow-sm)',
                  }}
                >
                  <h3 style={{
                    fontFamily: 'var(--font-display)',
                    fontSize: '1rem',
                    fontWeight: 700,
                    color: 'var(--ink)',
                    marginBottom: '.5rem',
                  }}>
                    {video.title}
                  </h3>
                  <p style={{ fontSize: '.85rem', color: 'var(--ink-muted)' }}>
                    Duración: {video.duration}
                  </p>
                  {module.optional && (
                    <span style={{
                      display: 'inline-block',
                      marginTop: '.75rem',
                      padding: '.2rem .7rem',
                      borderRadius: '100px',
                      background: 'var(--amber-light)',
                      color: 'var(--amber-dark)',
                      fontSize: '.7rem',
                      fontWeight: 700,
                      textTransform: 'uppercase',
                    }}>
                      Optativo
                    </span>
                  )}
                </div>
              ))}
            </div>
          </div>

          <div style={{ marginBottom: '3rem' }}>
            <h2 className="section__title" style={{ fontSize: '1.5rem', marginBottom: '1.5rem' }}>
              Lecturas
            </h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              {module.readings?.map((reading) => (
                <div
                  key={reading.id}
                  style={{
                    background: 'var(--surface)',
                    borderRadius: 'var(--r-md)',
                    padding: '1.25rem 1.5rem',
                    boxShadow: 'var(--shadow-sm)',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '1rem',
                  }}
                >
                  <span style={{ fontSize: '1.5rem' }}>📄</span>
                  <div style={{ flex: 1 }}>
                    <h3 style={{
                      fontFamily: 'var(--font-display)',
                      fontSize: '1rem',
                      fontWeight: 600,
                      color: 'var(--ink)',
                    }}>
                      {reading.title}
                    </h3>
                  </div>
                  <button className="btn btn--outline" style={{ padding: '.5rem 1rem', fontSize: '.85rem' }}>
                    Descargar PDF
                  </button>
                </div>
              ))}
            </div>
          </div>

          <div>
            <h2 className="section__title" style={{ fontSize: '1.5rem', marginBottom: '1.5rem' }}>
              Actividades
            </h2>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              {module.activities?.map((activity) => (
                <div
                  key={activity.id}
                  style={{
                    background: 'var(--surface)',
                    borderRadius: 'var(--r-md)',
                    padding: '1.5rem',
                    boxShadow: 'var(--shadow-sm)',
                    borderLeft: activity.requires_submission ? '3px solid var(--amber)' : '3px solid var(--canvas-alt)',
                  }}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '.75rem' }}>
                    <h3 style={{
                      fontFamily: 'var(--font-display)',
                      fontSize: '1rem',
                      fontWeight: 700,
                      color: 'var(--ink)',
                    }}>
                      {activity.title}
                    </h3>
                    {activity.requires_submission && (
                      <span style={{
                        padding: '.2rem .7rem',
                        borderRadius: '100px',
                        background: 'var(--amber-light)',
                        color: 'var(--amber-dark)',
                        fontSize: '.7rem',
                        fontWeight: 700,
                        textTransform: 'uppercase',
                      }}>
                        Requiere entrega
                      </span>
                    )}
                  </div>
                  <p style={{ fontSize: '.9rem', color: 'var(--ink-muted)', marginBottom: '1rem' }}>
                    Duración estimada: {activity.duration}
                  </p>
                  <Link
                    to={`/tarea/${module.id}/${activity.id}`}
                    className="btn btn--primary"
                    style={{ padding: '.6rem 1.5rem', fontSize: '.9rem' }}
                  >
                    {activity.requires_submission ? 'Entregar actividad →' : 'Ver detalles →'}
                  </Link>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
