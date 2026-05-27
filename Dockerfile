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

# EXPOSE 8080 tells Railway to route external traffic to port 8080,
# matching the $PORT value Railway injects (consistently 8080 for this service).
EXPOSE 8080

CMD ["/start.sh"]
