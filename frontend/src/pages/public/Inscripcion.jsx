import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import api from '../../lib/api';

export default function Inscripcion() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      // Crear sesión de Stripe
      const response = await api.post('/payments/create-checkout-session', {
        ...formData,
        origin_url: window.location.origin,
      });
      // Redirigir a Stripe Checkout
      window.location.href = response.data.checkout_url;
    } catch (err) {
      setError(err.response?.data?.detail || 'Error al iniciar el proceso de pago. Inténtalo de nuevo.');
      setLoading(false);
    }
  };

  return (
    <div className="inner-page">
      <div className="auth-card" style={{ maxWidth: '500px' }}>
        <h1 className="auth-title">Inscripción al curso</h1>
        <p className="auth-desc">
          Completa tus datos para acceder al curso "Claude para la enseñanza: domina la herramienta".
        </p>

        <div style={{
          background: 'var(--blue-light)',
          borderRadius: 'var(--r-md)',
          padding: '1rem',
          marginBottom: '1.5rem',
          fontSize: '.9rem',
          color: 'var(--blue)',
        }}>
          <p style={{ marginBottom: '.25rem' }}><strong>Precio: 149 €</strong></p>
          <p style={{ fontSize: '.85rem' }}>Pago único · Acceso de por vida</p>
        </div>

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

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="name">Nombre completo</label>
            <input
              id="name"
              name="name"
              type="text"
              className="auth-input"
              value={formData.name}
              onChange={handleChange}
              required
              placeholder="Juan Pérez García"
            />
          </div>
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              id="email"
              name="email"
              type="email"
              className="auth-input"
              value={formData.email}
              onChange={handleChange}
              required
              placeholder="juan@ejemplo.com"
            />
          </div>
          <button
            type="submit"
            className="btn btn--primary"
            disabled={loading}
            style={{ width: '100%', justifyContent: 'center' }}
          >
            {loading ? 'Procesando...' : 'Continuar al pago →'}
          </button>
        </form>

        <p style={{ fontSize: '.8rem', color: 'var(--ink-muted)', marginTop: '1rem', lineHeight: 1.5 }}>
          El pago se procesa de forma segura a través de Stripe. Al completar el pago recibirás acceso inmediato a la plataforma.
        </p>
      </div>
    </div>
  );
}
