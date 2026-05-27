import React, { useState, useEffect } from 'react';
import api from '../../lib/api';

export default function AdminParticipantes() {
  const [participants, setParticipants] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchParticipants();
  }, []);

  const fetchParticipants = async () => {
    try {
      const response = await api.get('/admin/participants');
      setParticipants(response.data);
    } catch (error) {
      console.error('Error fetching participants:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div style={{ padding: '2rem', textAlign: 'center' }}>Cargando...</div>;
  }

  return (
    <div className="inner-page">
        <div className="inner-content">
          <h1 className="section__title" style={{ fontSize: '2rem', marginBottom: '2rem' }}>
            Gestión de Participantes
          </h1>

          <div style={{
            background: 'var(--surface)',
            borderRadius: 'var(--r-lg)',
            boxShadow: 'var(--shadow-sm)',
            overflow: 'hidden',
          }}>
            <table style={{ width: '100%', borderCollapse: 'collapse' }}>
              <thead>
                <tr style={{ background: 'var(--canvas-alt)' }}>
                  <th style={{ padding: '1rem', textAlign: 'left', fontSize: '.8rem', textTransform: 'uppercase', letterSpacing: '1px' }}>
                    Email
                  </th>
                  <th style={{ padding: '1rem', textAlign: 'left', fontSize: '.8rem', textTransform: 'uppercase', letterSpacing: '1px' }}>
                    Nombre
                  </th>
                  <th style={{ padding: '1rem', textAlign: 'left', fontSize: '.8rem', textTransform: 'uppercase', letterSpacing: '1px' }}>
                    Fecha inscripción
                  </th>
                  <th style={{ padding: '1rem', textAlign: 'left', fontSize: '.8rem', textTransform: 'uppercase', letterSpacing: '1px' }}>
                    Progreso
                  </th>
                  <th style={{ padding: '1rem', textAlign: 'left', fontSize: '.8rem', textTransform: 'uppercase', letterSpacing: '1px' }}>
                    Estado
                  </th>
                </tr>
              </thead>
              <tbody>
                {participants.map((participant) => (
                  <tr key={participant.id} style={{ borderBottom: '1px solid var(--canvas-alt)' }}>
                    <td style={{ padding: '1rem', fontSize: '.9rem', color: 'var(--ink-soft)' }}>
                      {participant.email}
                    </td>
                    <td style={{ padding: '1rem', fontSize: '.9rem', color: 'var(--ink)' }}>
                      {participant.name || '-'}
                    </td>
                    <td style={{ padding: '1rem', fontSize: '.9rem', color: 'var(--ink-muted)' }}>
                      {new Date(participant.enrolled_at).toLocaleDateString('es-ES')}
                    </td>
                    <td style={{ padding: '1rem', fontSize: '.9rem', color: 'var(--ink-soft)' }}>
                      {participant.completed_modules || 0}/{participant.total_modules || 0} módulos
                    </td>
                    <td style={{ padding: '1rem' }}>
                      <span style={{
                        padding: '.3rem .8rem',
                        borderRadius: '100px',
                        fontSize: '.75rem',
                        fontWeight: 600,
                        background: participant.status === 'active' ? 'var(--green-light)' : 'var(--canvas-alt)',
                        color: participant.status === 'active' ? 'var(--green)' : 'var(--ink-muted)',
                      }}>
                        {participant.status === 'active' ? 'Activo' : participant.status}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>

            {participants.length === 0 && (
              <div style={{ padding: '3rem', textAlign: 'center', color: 'var(--ink-muted)' }}>
                No hay participantes inscritos aún.
              </div>
            )}
          </div>
        </div>
      </div>
  );
}
