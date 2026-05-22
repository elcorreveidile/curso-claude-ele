import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import './App.css';

// Auth
import { AuthProvider } from './lib/auth';

// Páginas públicas
import Home from './pages/public/Home';
import Programa from './pages/public/Programa';
import Precios from './pages/public/Precios';
import Inscripcion from './pages/public/Inscripcion';
import Login from './pages/public/Login';
import CheckEmail from './pages/public/CheckEmail';

// Páginas privadas
import Dashboard from './pages/private/Dashboard';
import Modulo from './pages/private/Modulo';
import Tarea from './pages/private/Tarea';
import Certificado from './pages/private/Certificado';

// Páginas admin
import AdminDashboard from './pages/admin/AdminDashboard';
import AdminParticipantes from './pages/admin/AdminParticipantes';
import AdminSesiones from './pages/admin/AdminSesiones';

// Componentes
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Protected from './components/Protected';

export default function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Navbar />
        <Routes>
          {/* Public */}
          <Route path="/" element={<Home />} />
          <Route path="/programa" element={<Programa />} />
          <Route path="/precios" element={<Precios />} />
          <Route path="/inscripcion" element={<Inscripcion />} />
          <Route path="/login" element={<Login />} />
          <Route path="/check-email" element={<CheckEmail />} />

          {/* Private */}
          <Route path="/dashboard" element={<Protected><Dashboard /></Protected>} />
          <Route path="/modulo/:id" element={<Protected><Modulo /></Protected>} />
          <Route path="/tarea/:moduleId/:taskId" element={<Protected><Tarea /></Protected>} />
          <Route path="/certificado" element={<Protected><Certificado /></Protected>} />

          {/* Admin */}
          <Route path="/admin" element={<Protected adminOnly><AdminDashboard /></Protected>} />
          <Route path="/admin/participantes" element={<Protected adminOnly><AdminParticipantes /></Protected>} />
          <Route path="/admin/sesiones" element={<Protected adminOnly><AdminSesiones /></Protected>} />

          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
        <Footer />
      </AuthProvider>
    </BrowserRouter>
  );
}
