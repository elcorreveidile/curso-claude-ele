import React from 'react';
import { Link } from 'react-router-dom';

export default function CheckEmail() {
  return (
    <div className="inner-page">
      <div className="auth-card" style={{ textAlign: 'center' }}>
        <div style={{
          width: '80px',
          height: '80px',
          borderRadius: '50%',
          background: 'var(--amber-light)',
          color: 'var(--amber)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          fontSize: '2.5rem',
          margin: '0 auto 1.5rem',
        }}>
          ✓
        </div>
        <h1 className="auth-title">Revisa tu email</h1>
        <p className="auth-desc">
          Te hemos enviado un enlace de acceso seguro. Si no lo ves en unos minutos, revisa tu carpeta de spam.
        </p>
        <div style={{
          background: 'var(--canvas)',
          borderRadius: 'var(--r-md)',
          padding: '1rem',
          marginTop: '1.5rem',
          fontSize: '.9rem',
          color: 'var(--ink-soft)',
        }}>
          <p style={{ marginBottom: '.5rem' }}><strong>¿No lo has recibido?</strong></p>
          <p>El enlace puede tardar unos minutos en llegar. Si pasado ese tiempo no lo has recibido, inténtalo de nuevo.</p>
        </div>
        <Link
          to="/login"
          className="btn btn--outline"
          style={{ marginTop: '1.5rem', width: '100%', justifyContent: 'center' }}
        >
          Volver a intentar
        </Link>
      </div>
    </div>
  );
}
