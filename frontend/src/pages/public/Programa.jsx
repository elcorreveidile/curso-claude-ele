import React from 'react';
import Navbar from '../../components/Navbar';
import Footer from '../../components/Footer';
import PageHero from '../../components/PageHero';
import ModuleCard from '../../components/ModuleCard';
import { useScrollReveal } from '../../lib/hooks';

const MODULES = [
  {
    id: 'modulo-0',
    num: '0',
    title: 'Bienvenida y punto de partida',
    subtitle: 'Qué es Claude, cómo funciona, cómo empezar',
    hours: 1,
    optional: false,
    locked: false,
    videos: [
      { id: 'v0-1', title: 'Vídeo de bienvenida', duration: '4 min' },
    ],
    readings: [
      { id: 'r0-1', title: 'Claude: qué es, de dónde viene y por qué importa' },
    ],
    activities: [
      { id: 'a0-1', title: 'Mi primera conversación con Claude', duration: '20-30 min', requires_submission: false },
    ],
  },
  {
    id: 'modulo-1',
    num: 'I',
    title: 'Conversar con Claude',
    subtitle: 'Prompts, FRAME y análisis de documentos',
    hours: 4,
    optional: false,
    locked: true,
    videos: [
      { id: 'v1-1', title: 'Cómo piensa Claude', duration: '5 min' },
      { id: 'v1-2', title: 'El marco FRAME aplicado a Claude', duration: '8 min' },
    ],
    readings: [
      { id: 'r1-1', title: 'Conversar vs pedir: la diferencia que lo cambia todo' },
      { id: 'r1-2', title: 'Análisis de documentos: PDFs, imágenes y textos largos' },
    ],
    activities: [
      { id: 'a1-1', title: 'Tu primera conversación compleja', duration: '30-40 min', requires_submission: true },
      { id: 'a1-2', title: 'Análisis de un documento real', duration: '20-30 min', requires_submission: false },
    ],
  },
  {
    id: 'modulo-2',
    num: 'II',
    title: 'Projects y memoria',
    subtitle: 'Instrucciones permanentes, documentos y configuración',
    hours: 3,
    optional: false,
    locked: true,
    videos: [
      { id: 'v2-1', title: 'Qué son los Projects y para qué sirven', duration: '6 min' },
      { id: 'v2-2', title: 'Configurar tu Project: instrucciones y documentos', duration: '7 min' },
    ],
    readings: [
      { id: 'r2-1', title: 'Projects: la memoria permanente de Claude' },
      { id: 'r2-2', title: 'Instrucciones que funcionan: cómo configurar tu Project' },
    ],
    activities: [
      { id: 'a2-1', title: 'Configura tu primer Project', duration: '30-40 min', requires_submission: true },
      { id: 'a2-2', title: 'Gestiona múltiples Projects', duration: '20 min', requires_submission: false },
    ],
  },
  {
    id: 'modulo-3',
    num: 'III',
    title: 'Artefactos',
    subtitle: 'Fichas, planes de clase, ejercicios interactivos HTML',
    hours: 3,
    optional: false,
    locked: true,
    videos: [
      { id: 'v3-1', title: 'Qué son los artefactos y cómo activarlos', duration: '5 min' },
      { id: 'v3-2', title: 'Artefactos para docentes: los tipos que más te interesan', duration: '8 min' },
    ],
    readings: [
      { id: 'r3-1', title: 'Artefactos de texto: fichas, planes y rúbricas' },
      { id: 'r3-2', title: 'Artefactos HTML: ejercicios interactivos para el aula' },
    ],
    activities: [
      { id: 'a3-1', title: 'Genera tres artefactos para tu próxima unidad', duration: '45-60 min', requires_submission: true },
      { id: 'a3-2', title: 'Edita y mejora un artefacto en conversación', duration: '20 min', requires_submission: false },
    ],
  },
  {
    id: 'modulo-4',
    num: 'IV',
    title: 'Claude en el aula',
    subtitle: 'Actividades para el alumnado, evaluación formativa y diversidad',
    hours: 5,
    optional: false,
    locked: true,
    videos: [
      { id: 'v4-1', title: 'Claude como herramienta del alumnado', duration: '6 min' },
      { id: 'v4-2', title: 'Evaluación formativa con Claude', duration: '7 min' },
    ],
    readings: [
      { id: 'r4-1', title: 'Diseñar actividades donde el alumno usa Claude' },
      { id: 'r4-2', title: 'Evaluación formativa con Claude' },
    ],
    activities: [
      { id: 'a4-1', title: 'Diseña una actividad para que tu alumnado use Claude', duration: '40-50 min', requires_submission: true },
      { id: 'a4-2', title: 'Corrección y feedback con Claude', duration: '30-40 min', requires_submission: true },
    ],
  },
  {
    id: 'modulo-5',
    num: 'V',
    title: 'Claude avanzado',
    subtitle: 'Herramientas externas, API y Claude Code',
    hours: 3,
    optional: true,
    locked: true,
    badge: 'Optativo',
    videos: [
      { id: 'v5-1', title: 'Claude con herramientas externas', duration: '7 min' },
      { id: 'v5-2', title: 'Introducción a la API de Claude', duration: '8 min' },
      { id: 'v5-3', title: 'Claude Code para docentes', duration: '6 min' },
    ],
    readings: [
      { id: 'r5-1', title: 'Búsqueda web y Google Drive' },
      { id: 'r5-2', title: 'La API de Claude: qué es y para qué sirve a un docente' },
      { id: 'r5-3', title: 'Claude Code: automatizar sin saber programar' },
    ],
    activities: [
      { id: 'a5-1', title: 'Conecta una herramienta externa', duration: '20-30 min', requires_submission: false },
      { id: 'a5-2', title: 'Explora el Playground de la API', duration: '30 min', requires_submission: false },
      { id: 'a5-3', title: 'Primera tarea con Claude Code', duration: '45-60 min', requires_submission: false, badge: 'Para los más valientes' },
    ],
  },
  {
    id: 'modulo-6',
    num: 'VI',
    title: 'Proyecto final y cierre',
    subtitle: 'Unidad didáctica completa + reflexión + certificado',
    hours: 1,
    optional: false,
    locked: true,
    videos: [
      { id: 'v6-1', title: 'El proyecto final: qué es y cómo abordarlo', duration: '5 min' },
      { id: 'v6-2', title: 'Cierre del curso', duration: '4 min' },
    ],
    readings: [
      { id: 'r6-1', title: 'El proyecto final: instrucciones completas' },
      { id: 'r6-2', title: 'Cómo abordar el proyecto sin bloquearse' },
    ],
    activities: [
      { id: 'a6-1', title: 'Proyecto final', duration: 'Variable', requires_submission: true, is_final_project: true },
    ],
  },
];

export default function Programa() {
  useScrollReveal();

  return (
    <>
      <Navbar />
      <div className="inner-page">
        <PageHero
          tag="Contenidos"
          title="Programa por módulos"
          desc="Siete módulos progresivos que van de la primera conversación con Claude hasta la API y Claude Code."
        />
        <div className="inner-content">
          <div className="modules-grid">
            {MODULES.map((m) => (
              <div key={m.id} className="reveal">
                <ModuleCard module={m} />
              </div>
            ))}
          </div>
        </div>
      </div>
      <Footer />
    </>
  );
}
