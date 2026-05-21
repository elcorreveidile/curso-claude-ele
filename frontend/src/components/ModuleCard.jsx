import React from 'react';

export default function ModuleCard({ module }) {
  const { num, title, subtitle, hours, optional, videos, readings, activities } = module;

  return (
    <div className="module-card">
      <div className={`module-card__header module-card__header--${num.replace(/[IVX]/, '').toLowerCase() || num}`}>
        <span className="module-card__roman">{num}</span>
        <h3 className="module-card__htitle">{title}</h3>
        {optional && <span className="module-card__badge">Optativo</span>}
      </div>
      <div className="module-card__body">
        <p style={{ fontSize: '.9rem', color: 'var(--ink-muted)', marginBottom: '1rem' }}>
          {subtitle}
        </p>
        <div className="module-card__items">
          <span style={{ fontSize: '.8rem', fontWeight: 600, color: 'var(--ink)', marginBottom: '.5rem' }}>
            {videos.length} vídeos · {readings.length} lecturas · {activities.length} actividades
          </span>
          <span style={{ fontSize: '.8rem', color: 'var(--ink-muted)' }}>
            Duración: {hours} horas
          </span>
        </div>
      </div>
    </div>
  );
}
