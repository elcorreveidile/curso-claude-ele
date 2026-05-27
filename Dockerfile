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

# Railway inyecta $PORT — no usar EXPOSE fijo para evitar conflicto con el ruteo
CMD ["/start.sh"]
