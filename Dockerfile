FROM python:3.11-slim

WORKDIR /app

# Copiar requirements primero para caché
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar resto del backend
COPY backend/ .

# Copiar entrypoint
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Exponer puerto (Railway inyecta $PORT)
EXPOSE 8000

# Usar $PORT de Railway; si no existe, 8000 como fallback
CMD ["/start.sh"]
