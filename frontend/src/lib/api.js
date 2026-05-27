import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE,
  withCredentials: true,  // send session_token httpOnly cookie on every request
  headers: {
    'Content-Type': 'application/json',
  },
});

export default api;
