import React from 'react';
import { Link } from 'react-router-dom';
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';
import { useScrollReveal } from '../../lib/hooks';

export default function Home() {
  useScrollReveal();

  return (
    <>
      <Navbar />
      <div className="home-hero">
        <div className="home-body">
          <p className="home-eyebrow reveal">Formación Docente · 20 horas · 149 €</p>
          <h1 className="home-title reveal reveal--delay-1">
            <em>Claude para la enseñanza:</em><br />domina la herramienta
          </h1>
          <p className="home-subtitle reveal reveal--delay-2">
            El primer curso de formación docente dedicado íntegramente a Claude. De la primera conversación a los artefactos, los Projects, la evaluación formativa y la API. Para docentes que quieren llegar a todo.
          </p>

          <div className="test-card reveal reveal--delay-3">
            <span className="test-card__badge">⭐ Precio fijo · 149 €</span>
            <h2 className="test-card__title">Formación intensiva · 3 videotutorías en directo</h2>
            <p className="test-card__desc">
              Desde cero hasta nivel avanzado. Aprende a usar Claude con criterio pedagógico en tu práctica docente. 20 horas de formación, certificado de aprovechamiento y feedback personalizado.
            </p>
            <Link to="/precios" className="test-card__btn">
              Inscribirme ahora →
            </Link>
          </div>

          <div className="home-divider">
            <div className="home-divider__line" />
            <span className="home-divider__text">Más información sobre el curso</span>
            <div className="home-divider__line" />
          </div>

          <div className="home-links">
            <Link to="/programa">Ver programa</Link>
            <Link to="/precios">Precios e inscripción</Link>
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}
