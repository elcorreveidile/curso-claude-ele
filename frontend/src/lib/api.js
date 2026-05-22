import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para añadir JWT a cada request
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('jwt');
  console.log('[API] Request to', config.url, 'token exists:', !!token);
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
    console.log('[API] Authorization header set');
  } else {
    console.log('[API] No token found in localStorage');
  }
  return config;
});

// Interceptor para manejar errores 401
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('[API] Error:', error.response?.status, error.response?.data);
    if (error.response?.status === 401) {
      localStorage.removeItem('jwt');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
