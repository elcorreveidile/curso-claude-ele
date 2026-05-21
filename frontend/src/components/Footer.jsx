import React from 'react';
import { Link } from 'react-router-dom';

export default function Footer() {
  return (
    <footer>
      <div className="footer-inner">
        <div>
          <div className="footer-brand__logo">
            <span className="pipe">[|]</span>Claude<span className="brand-chip">Curso</span>
          </div>
          <p className="footer-brand__desc">
            Formación docente intensiva sobre Claude para docentes
            de cualquier materia.<br />20 horas · 3 videotutorías · Certificado incluido.
          </p>
        </div>
        <div>
          <p className="footer-col__title">El curso</p>
          <div className="footer-col__links">
            <Link to="/programa">Programa</Link>
            <Link to="/precios">Precios e inscripción</Link>
          </div>
        </div>
        <div>
          <p className="footer-col__title">Contacto</p>
          <p className="footer-contact">
            <strong>Javier Benítez Láinez</strong><br />
            Docente de ELE · Granada (España)
          </p>
        </div>
      </div>
      <div className="footer-bottom">
        <span>© 2026 Javier Benítez Láinez · Formación Docente</span>
        <a href="https://laclasedigital.com" target="_blank" rel="noopener noreferrer">
          laclasedigital.com
        </a>
      </div>
    </footer>
  );
}
