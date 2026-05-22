import React, { createContext, useContext, useState, useEffect } from 'react';
import api from './api';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check for token in URL fragment (from magic link redirect)
    const hash = window.location.hash;
    console.log('[Auth] Checking for token in URL hash:', hash);
    if (hash && hash.includes('token=')) {
      const token = hash.split('token=')[1];
      console.log('[Auth] Token found in URL, saving to localStorage');
      if (token) {
        localStorage.setItem('jwt', token);
        console.log('[Auth] Token saved, length:', token.length);
        // Clean URL
        window.history.replaceState({}, document.title, window.location.pathname);
        console.log('[Auth] URL cleaned');
      }
    }

    const token = localStorage.getItem('jwt');
    console.log('[Auth] Token from localStorage:', !!token);
    if (token) {
      console.log('[Auth] Fetching user data...');
      fetchUser();
    } else {
      console.log('[Auth] No token found, setting loading to false');
      setLoading(false);
    }
  }, []);

  const fetchUser = async () => {
    try {
      const response = await api.get('/auth/me');
      setUser(response.data);
    } catch (error) {
      console.error('Error fetching user:', error);
      localStorage.removeItem('jwt');
    } finally {
      setLoading(false);
    }
  };

  const login = async (email) => {
    await api.post('/auth/login', { email });
  };

  const logout = () => {
    localStorage.removeItem('jwt');
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, loading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
}
