import React, { useEffect, useState } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { useAuth } from '../lib/auth';

const publicLinks = [
  { to: '/programa', label: 'Programa' },
  { to: '/precios', label: 'Precios' },
];

export default function Navbar() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    const on = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', on);
    return () => window.removeEventListener('scroll', on);
  }, []);

  const close = () => setOpen(false);

  return (
    <nav className={`inner-nav${scrolled ? ' scrolled' : ''}`}>
      <NavLink to="/" className="inner-nav__logo" onClick={close}>
        <span className="pipe">[|]</span>Claude<span className="brand-chip">Curso</span>
      </NavLink>
      <div className={`inner-nav__links${open ? ' open' : ''}`}>
        {publicLinks.map((l) => (
          <NavLink
            key={l.to}
            to={l.to}
            onClick={close}
            className={({ isActive }) => (isActive ? 'active' : '')}
          >
            {l.label}
          </NavLink>
        ))}
        {user ? (
          <>
            <NavLink to="/dashboard" onClick={close}>Mi área</NavLink>
            {user.role === 'admin' && (
              <NavLink to="/admin" onClick={close}>Admin</NavLink>
            )}
            <button
              className="linkish"
              onClick={() => { close(); logout(); navigate('/'); }}
            >
              Salir
            </button>
          </>
        ) : (
          <NavLink to="/login" onClick={close} className="inner-nav__cta">
            Acceder
          </NavLink>
        )}
      </div>
      <button
        className={`inner-nav__burger${open ? ' open' : ''}`}
        onClick={() => setOpen(!open)}
        aria-label="Menú"
      >
        <span></span><span></span><span></span>
      </button>
    </nav>
  );
}
