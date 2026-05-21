import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';
import api from '../../lib/api';

export default function Login() {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await api.post('/auth/login', { email });
      setSuccess(true);
      setTimeout(() => navigate('/check-email'), 1500);
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al enviar el magic link. Inténtalo de nuevo.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <Navbar />
      <div className="inner-page">
        <div className="auth-card">
          <h1 className="auth-title">Accede al curso</h1>
          <p className="auth-desc">
            Introduce tu email para recibir un enlace de acceso seguro.
          </p>

          {error && (
            <div style={{
              background: '#FEE',
              color: '#C33',
              padding: '.75rem',
              borderRadius: 'var(--r-sm)',
              marginBottom: '1rem',
              fontSize: '.9rem',
            }}>
              {error}
            </div>
          )}

          {success && (
            <div style={{
              background: '#E8F5EC',
              color: 'var(--green)',
              padding: '.75rem',
              borderRadius: 'var(--r-sm)',
              marginBottom: '1rem',
              fontSize: '.9rem',
            }}>
              ✓ ¡Enlace enviado! Revisa tu email.
            </div>
          )}

          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input
                id="email"
                type="email"
                className="auth-input"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                placeholder="tu@email.com"
              />
            </div>
            <button
              type="submit"
              className="btn btn--primary"
              disabled={loading}
              style={{ width: '100%', justifyContent: 'center' }}
            >
              {loading ? 'Enviando...' : 'Enviar enlace de acceso'}
            </button>
          </form>

          <p style={{ fontSize: '.85rem', color: 'var(--ink-muted)', marginTop: '1.5rem', textAlign: 'center' }}>
            Te enviaremos un enlace mágico que te dará acceso directo a tu área.
          </p>
        </div>
      </div>
      <Footer />
    </>
  );
}
