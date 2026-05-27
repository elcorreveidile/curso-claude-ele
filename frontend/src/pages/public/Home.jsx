import React from 'react';
import { Link } from 'react-router-dom';
import { useScrollReveal } from '../../lib/hooks';

const HERO = {
  tag: 'Formación docente · 20 horas · 149 €',
  title: 'Claude para la enseñanza',
  subtitle: 'Domina la herramienta',
  desc: 'El primer curso de formación docente dedicado íntegramente a Claude. De la primera conversación a los artefactos, los Projects, la evaluación formativa y la API. Para docentes que quieren llegar a todo.',
  badges: ['20 horas', '3 videotutorías en directo', 'Certificado incluido', 'Plazas limitadas'],
};

const REASONS = [
  {
    icon: '🎯',
    title: 'Todo Claude, sin excepciones',
    text: 'Desde la interfaz hasta la API. Desde los prompts hasta Claude Code. El único curso que cubre Claude en profundidad para docentes.',
  },
  {
    icon: '🏗️',
    title: 'Projects y artefactos desde el primer día',
    text: 'No aprenderás a usar Claude — aprenderás a dominarlo. Projects configurados para tu práctica real, artefactos HTML interactivos listos para el aula.',
  },
  {
    icon: '👥',
    title: 'Claude en el aula, no solo en tu mesa',
    text: 'Diseña actividades donde tu alumnado usa Claude con criterio. Evaluación formativa automatizada. Atención a la diversidad con IA.',
  },
  {
    icon: '🔧',
    title: 'Avanzado si quieres llegar más lejos',
    text: 'Módulo optativo con herramientas externas, API y Claude Code para automatizar tareas repetitivas sin saber programar.',
  },
];

const FOR_WHO = [
  'Docentes de cualquier materia que usan o quieren usar Claude en su práctica',
  'Docentes de ELE que ya han hecho el curso de IA para la enseñanza',
  'Formadores que quieren incorporar IA en sus cursos y talleres',
  'Coordinadores pedagógicos que necesitan entender Claude para asesorar a sus equipos',
];

export default function Home() {
  useScrollReveal();

  return (
    <>
      {/* Hero */}
      <div className="home-hero">
        <div className="home-body">
          <p className="home-eyebrow reveal">{HERO.tag}</p>
          <h1 className="home-title reveal reveal--delay-1">
            <em>{HERO.title}:</em><br />{HERO.subtitle}
          </h1>
          <p className="home-subtitle reveal reveal--delay-2">
            {HERO.desc}
          </p>

          <div className="home-badges reveal reveal--delay-3">
            {HERO.badges.map((badge, i) => (
              <span key={i} className="home-badge">{badge}</span>
            ))}
          </div>

          <div className="home-ctas reveal reveal--delay-4">
            <Link to="/inscripcion" className="btn btn--primary" style={{ fontSize: '1.05rem', padding: '.9rem 2rem' }}>
              Inscribirme ahora →
            </Link>
            <Link
              to="/programa"
              className="btn btn--outline"
              style={{
                fontSize: '1.05rem',
                padding: '.9rem 2rem',
                color: 'rgba(255,255,255,.85)',
                borderColor: 'rgba(255,255,255,.3)',
                background: 'transparent',
              }}
            >
              Ver el programa
            </Link>
          </div>
        </div>
      </div>

      {/* Reasons */}
      <section className="inner-content">
        <div style={{ maxWidth: '900px', margin: '0 auto' }}>
          <p className="section__tag reveal">Por qué este curso</p>
          <h2 className="section__title reveal">Formación docente sobre Claude, de verdad.</h2>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(360px, 1fr))',
            gap: '1.5rem',
            marginTop: '2.5rem',
          }}>
            {REASONS.map((reason, i) => (
              <div
                key={i}
                className={`reveal reveal--delay-${i + 1}`}
                style={{
                  background: 'var(--surface)',
                  borderRadius: 'var(--r-lg)',
                  padding: '2rem',
                  boxShadow: 'var(--shadow-sm)',
                  borderLeft: '3px solid var(--amber)',
                }}
              >
                <div style={{ fontSize: '2rem', marginBottom: '1rem' }}>{reason.icon}</div>
                <h3 style={{
                  fontFamily: 'var(--font-display)',
                  fontSize: '1.1rem',
                  fontWeight: 700,
                  color: 'var(--ink)',
                  marginBottom: '.75rem',
                }}>
                  {reason.title}
                </h3>
                <p style={{ fontSize: '.9rem', color: 'var(--ink-soft)', lineHeight: 1.65 }}>
                  {reason.text}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* For who */}
      <section style={{ background: 'var(--dark-bg)', padding: '5rem 2.5rem' }}>
        <div style={{ maxWidth: '760px', margin: '0 auto' }}>
          <p className="section__tag reveal" style={{ color: 'var(--amber)' }}>Para quién es</p>
          <h2 className="section__title reveal" style={{ color: 'var(--white)', marginBottom: '2rem' }}>
            ¿Es este curso para ti?
          </h2>
          <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {FOR_WHO.map((item, i) => (
              <li
                key={i}
                className={`reveal reveal--delay-${i + 1}`}
                style={{
                  display: 'flex',
                  alignItems: 'flex-start',
                  gap: '1rem',
                  padding: '1.2rem 1.5rem',
                  background: 'rgba(255,255,255,.06)',
                  borderRadius: 'var(--r-md)',
                  border: '1px solid rgba(255,255,255,.09)',
                  fontSize: '.95rem',
                  color: 'rgba(255,255,255,.82)',
                  lineHeight: 1.55,
                }}
              >
                <span style={{ color: 'var(--amber)', fontWeight: 700, flexShrink: 0, marginTop: '.15rem' }}>✓</span>
                {item}
              </li>
            ))}
          </ul>
          <div className="reveal" style={{ textAlign: 'center', marginTop: '3rem' }}>
            <Link to="/inscripcion" className="btn btn--primary" style={{ fontSize: '1.05rem', padding: '.9rem 2.5rem' }}>
              Inscribirme ahora · 149 € →
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
