import React, { useState, useEffect } from 'react';
import api from '../../lib/api';

export default function Certificado() {
  const [certificate, setCertificate] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchCertificate();
  }, []);

  const fetchCertificate = async () => {
    try {
      const response = await api.get('/certificates/my');
      setCertificate(response.data);
    } catch (error) {
      console.error('Error fetching certificate:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleDownload = async () => {
    try {
      const response = await api.get('/certificates/my/download', {
        responseType: 'blob',
      });
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `certificado-curso-claude-${certificate.verification_code}.pdf`);
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      alert('Error al descargar el certificado. Inténtalo de nuevo.');
    }
  };

  if (loading) {
    return <div style={{ padding: '2rem', textAlign: 'center' }}>Cargando...</div>;
  }

  if (!certificate) {
    return (
      <div className="inner-page">
          <div className="inner-content">
            <div style={{
              background: 'var(--surface)',
              borderRadius: 'var(--r-lg)',
              padding: '3rem',
              boxShadow: 'var(--shadow-sm)',
              textAlign: 'center',
              maxWidth: '600px',
              margin: '0 auto',
            }}>
              <div style={{
                width: '80px',
                height: '80px',
                borderRadius: '50%',
                background: 'var(--canvas-alt)',
                color: 'var(--ink-muted)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '2rem',
                margin: '0 auto 1.5rem',
              }}>
                🔒
              </div>
              <h1 style={{
                fontFamily: 'var(--font-display)',
                fontSize: '1.5rem',
                fontWeight: 800,
                color: 'var(--ink)',
                marginBottom: '1rem',
              }}>
                Certificado no disponible
              </h1>
              <p style={{ fontSize: '1rem', color: 'var(--ink-soft)', lineHeight: 1.7, marginBottom: '2rem' }}>
                Aún no has completado todos los módulos del curso. Cuando termines todas las actividades,
                podrás descargar tu certificado de aprovechamiento.
              </p>
              <a href="/dashboard" className="btn btn--blue" style={{ display: 'inline-block' }}>
                Volver al dashboard
              </a>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <>
      <div className="inner-page">
        <div className="inner-content">
          <div style={{ maxWidth: '800px', margin: '0 auto' }}>
            <div style={{
              background: 'linear-gradient(135deg, #0A1628, #0F2744)',
              borderRadius: 'var(--r-xl)',
              padding: '3rem',
              boxShadow: 'var(--shadow-lg)',
              color: 'var(--white)',
              textAlign: 'center',
              marginBottom: '2rem',
            }}>
              <div style={{ marginBottom: '2rem' }}>
                <span style={{
                  fontFamily: 'Georgia, serif',
                  fontSize: '3rem',
                  color: 'var(--amber)',
                  letterSpacing: '-3px',
                }}>
                  [|]
                </span>
              </div>
              <h1 style={{
                fontFamily: 'var(--font-display)',
                fontSize: '2rem',
                fontWeight: 800,
                marginBottom: '1rem',
              }}>
                Certificado de Aprovechamiento
              </h1>
              <p style={{ fontSize: '1.1rem', opacity: 0.9, marginBottom: '2rem' }}>
                Se otorga el presente certificado a
              </p>
              <h2 style={{
                fontFamily: 'var(--font-display)',
                fontSize: '1.8rem',
                fontWeight: 700,
                marginBottom: '1rem',
              }}>
                {certificate.name}
              </h2>
              <p style={{ fontSize: '1rem', opacity: 0.9, marginBottom: '2rem' }}>
                Por haber completado satisfactoriamente el curso
              </p>
              <h3 style={{
                fontFamily: 'var(--font-display)',
                fontSize: '1.4rem',
                fontWeight: 700,
                marginBottom: '0.5rem',
              }}>
                Claude para la enseñanza: domina la herramienta
              </h3>
              <p style={{ fontSize: '1rem', opacity: 0.9, marginBottom: '2rem' }}>
                20 horas de formación · 3 videotutorías
              </p>
              <div style={{
                display: 'flex',
                justifyContent: 'center',
                gap: '2rem',
                fontSize: '0.9rem',
                opacity: 0.8,
                marginBottom: '2rem',
              }}>
                <div>
                  <p style={{ marginBottom: '0.25rem' }}>Fecha de emisión</p>
                  <p style={{ fontWeight: 600 }}>
                    {new Date(certificate.issued_at).toLocaleDateString('es-ES', {
                      year: 'numeric',
                      month: 'long',
                      day: 'numeric',
                    })}
                  </p>
                </div>
                <div>
                  <p style={{ marginBottom: '0.25rem' }}>Código de verificación</p>
                  <p style={{ fontWeight: 600, fontFamily: 'monospace' }}>
                    {certificate.verification_code}
                  </p>
                </div>
              </div>
              <div style={{
                borderTop: '1px solid rgba(255,255,255,0.2)',
                paddingTop: '1.5rem',
                fontSize: '0.85rem',
                opacity: 0.8,
              }}>
                <p style={{ marginBottom: '0.5rem' }}>Javier Benítez Láinez · La Clase Digital</p>
                <p>laclasedigital.com</p>
              </div>
            </div>

            <div style={{
              background: 'var(--surface)',
              borderRadius: 'var(--r-lg)',
              padding: '2rem',
              boxShadow: 'var(--shadow-sm)',
              textAlign: 'center',
            }}>
              <button
                onClick={handleDownload}
                className="btn btn--primary"
                style={{
                  padding: '1rem 2rem',
                  fontSize: '1.1rem',
                  marginBottom: '1rem',
                }}
              >
                📥 Descargar certificado (PDF)
              </button>
              <p style={{ fontSize: '.9rem', color: 'var(--ink-muted)', lineHeight: 1.6 }}>
                Tu certificado incluye un código único de verificación: <strong>{certificate.verification_code}</strong>
              </p>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
