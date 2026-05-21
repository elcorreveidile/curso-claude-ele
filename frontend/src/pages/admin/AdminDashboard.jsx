import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';
import api from '../../lib/api';

export default function AdminDashboard() {
  const [stats, setStats] = useState({
    total_enrollments: 0,
    active_students: 0,
    completed_modules: 0,
    pending_feedback: 0,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    try {
      const response = await api.get('/admin/stats');
      setStats(response.data);
    } catch (error) {
      console.error('Error fetching stats:', error);
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
          <h1 className="section__title" style={{ fontSize: '2rem', marginBottom: '2rem' }}>
            Panel de Administración
          </h1>

          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
            gap: '1.5rem',
            marginBottom: '3rem',
          }}>
            <div style={{
              background: 'var(--surface)',
              borderRadius: 'var(--r-lg)',
              padding: '1.5rem',
              boxShadow: 'var(--shadow-sm)',
              borderLeft: '4px solid var(--blue)',
            }}>
              <p style={{ fontSize: '.8rem', color: 'var(--ink-muted)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.5rem' }}>
                Total inscritos
              </p>
              <p style={{ fontSize: '2.5rem', fontWeight: 800, color: 'var(--blue)', lineHeight: 1 }}>
                {stats.total_enrollments}
              </p>
            </div>

            <div style={{
              background: 'var(--surface)',
              borderRadius: 'var(--r-lg)',
              padding: '1.5rem',
              boxShadow: 'var(--shadow-sm)',
              borderLeft: '4px solid var(--green)',
            }}>
              <p style={{ fontSize: '.8rem', color: 'var(--ink-muted)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.5rem' }}>
                Estudiantes activos
              </p>
              <p style={{ fontSize: '2.5rem', fontWeight: 800, color: 'var(--green)', lineHeight: 1 }}>
                {stats.active_students}
              </p>
            </div>

            <div style={{
              background: 'var(--surface)',
              borderRadius: 'var(--r-lg)',
              padding: '1.5rem',
              boxShadow: 'var(--shadow-sm)',
              borderLeft: '4px solid var(--amber)',
            }}>
              <p style={{ fontSize: '.8rem', color: 'var(--ink-muted)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.5rem' }}>
                Módulos completados
              </p>
              <p style={{ fontSize: '2.5rem', fontWeight: 800, color: 'var(--amber)', lineHeight: 1 }}>
                {stats.completed_modules}
              </p>
            </div>

            <div style={{
              background: 'var(--surface)',
              borderRadius: 'var(--r-lg)',
              padding: '1.5rem',
              boxShadow: 'var(--shadow-sm)',
              borderLeft: '4px solid #C33',
            }}>
              <p style={{ fontSize: '.8rem', color: 'var(--ink-muted)', textTransform: 'uppercase', letterSpacing: '1px', marginBottom: '0.5rem' }}>
                Feedback pendiente
              </p>
              <p style={{ fontSize: '2.5rem', fontWeight: 800, color: '#C33', lineHeight: 1 }}>
                {stats.pending_feedback}
              </p>
            </div>
          </div>

          <div>
            <h2 className="section__title" style={{ fontSize: '1.5rem', marginBottom: '1.5rem' }}>
              Gestión del curso
            </h2>
            <div style={{
              display: 'grid',
              gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
              gap: '1.5rem',
            }}>
              <Link
                to="/admin/participantes"
                style={{
                  background: 'var(--surface)',
                  borderRadius: 'var(--r-lg)',
                  padding: '2rem',
                  boxShadow: 'var(--shadow-sm)',
                  textDecoration: 'none',
                  color: 'var(--ink)',
                  transition: 'transform 0.2s, box-shadow 0.2s',
                  border: '2px solid var(--canvas-alt)',
                }}
                onMouseEnter={(e) => {
                  e.target.style.transform = 'translateY(-4px)';
                  e.target.style.boxShadow = 'var(--shadow-md)';
                  e.target.style.borderColor = 'var(--blue)';
                }}
                onMouseLeave={(e) => {
                  e.target.style.transform = 'none';
                  e.target.style.boxShadow = 'var(--shadow-sm)';
                  e.target.style.borderColor = 'var(--canvas-alt)';
                }}
              >
                <h3 style={{
                  fontFamily: 'var(--font-display)',
                  fontSize: '1.2rem',
                  fontWeight: 700,
                  marginBottom: '0.5rem',
                }}>
                  👥 Participantes
                </h3>
                <p style={{ fontSize: '.95rem', color: 'var(--ink-soft)' }}>
                  Gestiona los estudiantes, ver progreso, tareas y certificados.
                </p>
              </Link>

              <Link
                to="/admin/sesiones"
                style={{
                  background: 'var(--surface)',
                  borderRadius: 'var(--r-lg)',
                  padding: '2rem',
                  boxShadow: 'var(--shadow-sm)',
                  textDecoration: 'none',
                  color: 'var(--ink)',
                  transition: 'transform 0.2s, box-shadow 0.2s',
                  border: '2px solid var(--canvas-alt)',
                }}
                onMouseEnter={(e) => {
                  e.target.style.transform = 'translateY(-4px)';
                  e.target.style.boxShadow = 'var(--shadow-md)';
                  e.target.style.borderColor = 'var(--amber)';
                }}
                onMouseLeave={(e) => {
                  e.target.style.transform = 'none';
                  e.target.style.boxShadow = 'var(--shadow-sm)';
                  e.target.style.borderColor = 'var(--canvas-alt)';
                }}
              >
                <h3 style={{
                  fontFamily: 'var(--font-display)',
                  fontSize: '1.2rem',
                  fontWeight: 700,
                  marginBottom: '0.5rem',
                }}>
                  📹 Videotutorías
                </h3>
                <p style={{ fontSize: '.95rem', color: 'var(--ink-soft)' }}>
                  Configura las 3 videotutorías en directo y desbloquea módulos.
                </p>
              </Link>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}
