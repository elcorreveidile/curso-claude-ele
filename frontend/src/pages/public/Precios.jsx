import React from 'react';
import { Link } from 'react-router-dom';
import PageHero from '../../components/PageHero';
import { useScrollReveal } from '../../lib/hooks';

export default function Precios() {
  useScrollReveal();

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

  return (
    <div className="inner-page">
      <PageHero
        tag="Inscripción"
        title="Precio e inscripción"
        desc="Formación docente intensiva sobre Claude. 20 horas, 3 videotutorías y certificado de aprovechamiento."
      />
      <div className="inner-content">
        <div style={{ maxWidth: '600px', margin: '0 auto 4rem' }} className="reveal">
          <div style={{
            background: 'var(--surface)',
            borderRadius: 'var(--r-xl)',
            padding: '2.5rem',
            boxShadow: 'var(--shadow-md)',
            border: '2px solid var(--canvas-alt)',
            textAlign: 'center',
          }}>
            <p style={{
              fontSize: '.75rem',
              fontWeight: 700,
              textTransform: 'uppercase',
              letterSpacing: '.1em',
              color: 'var(--ink-muted)',
              marginBottom: '.75rem',
            }}>
              {PRICING.label}
            </p>
            <div style={{
              fontFamily: 'var(--font-display)',
              fontSize: '3.5rem',
              fontWeight: 800,
              color: 'var(--blue)',
              lineHeight: 1,
              marginBottom: '.25rem',
            }}>
              {PRICING.price}
              <span style={{ fontSize: '1.5rem', fontWeight: 400, color: 'var(--ink-muted)' }}> €</span>
            </div>
            <p style={{ fontSize: '.9rem', color: 'var(--ink-muted)', marginBottom: '1.5rem' }}>
              pago único · acceso de por vida · actualizaciones de contenidos mensuales
            </p>

            <ul style={{ listStyle: 'none', marginBottom: '1.75rem', textAlign: 'left' }}>
              {PRICING.includes.map((item, i) => (
                <li key={i} style={{
                  display: 'flex',
                  gap: '.75rem',
                  alignItems: 'flex-start',
                  fontSize: '.9rem',
                  padding: '.5rem 0',
                  borderBottom: '1px solid var(--canvas-alt)',
                  color: 'var(--ink-soft)',
                }}>
                  <span style={{ color: 'var(--blue)', fontWeight: 700 }}>✓</span>
                  {item}
                </li>
              ))}
            </ul>

            <Link
              to="/inscripcion"
              className="btn btn--primary"
              style={{ justifyContent: 'center', width: '100%' }}
            >
              Inscribirme ahora →
            </Link>

            <p style={{ fontSize: '.8rem', color: 'var(--ink-muted)', fontStyle: 'italic', marginTop: '1rem', lineHeight: 1.5 }}>
              El pago se procesa de forma segura con Stripe. Recibirás acceso inmediato tras completar la inscripción.
            </p>
          </div>
        </div>

        <div style={{ marginBottom: '4rem' }} className="reveal reveal--delay-1">
          <p className="section__tag">No incluido</p>
          <h2 className="section__title" style={{ fontSize: '1.8rem', marginBottom: '1.5rem' }}>
            Lo que necesitas aparte del curso
          </h2>
          <div style={{ maxWidth: '720px' }}>
            {PRICING.not_included.map((item, i) => (
              <div key={i} style={{
                background: 'var(--canvas)',
                borderRadius: 'var(--r-md)',
                padding: '1rem 1.5rem',
                marginBottom: '.75rem',
                fontSize: '.95rem',
                color: 'var(--ink-soft)',
              }}>
                {item}
              </div>
            ))}
          </div>
        </div>

        <div style={{ marginBottom: '4rem' }} className="reveal reveal--delay-2">
          <p className="section__tag">Preguntas frecuentes</p>
          <h2 className="section__title" style={{ fontSize: '1.8rem', marginBottom: '1.5rem' }}>
            Dudas sobre la inscripción
          </h2>
          <div style={{ maxWidth: '720px' }}>
            {PRICING.faq.map((item, i) => (
              <div key={i} style={{
                background: 'var(--surface)',
                borderRadius: 'var(--r-md)',
                padding: '1.5rem',
                marginBottom: '.75rem',
                boxShadow: 'var(--shadow-sm)',
              }}>
                <p style={{
                  fontFamily: 'var(--font-display)',
                  fontSize: '.975rem',
                  fontWeight: 700,
                  color: 'var(--ink)',
                  marginBottom: '.5rem',
                }}>
                  {item.q}
                </p>
                <p style={{ fontSize: '.9rem', color: 'var(--ink-soft)', lineHeight: 1.6 }}>
                  {item.a}
                </p>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
