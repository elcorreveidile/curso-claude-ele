FROM python:3.11-slim

WORKDIR /app

# Copiar requirements primero para caché
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar resto del backend
COPY backend/ .

# Exponer puerto
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
