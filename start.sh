#!/bin/sh
set -e

echo "=== STARTUP CHECK ==="
echo "PORT=${PORT:-'(not set, defaulting to 8000)'}"
echo "SUPABASE_URL is ${SUPABASE_URL:+set (${#SUPABASE_URL} chars)}"
echo "SUPABASE_SERVICE_KEY is ${SUPABASE_SERVICE_KEY:+set (${#SUPABASE_SERVICE_KEY} chars)}"
echo "JWT_SECRET is ${JWT_SECRET:+set}"
echo "MAGIC_LINK_SECRET is ${MAGIC_LINK_SECRET:+set}"
echo "FRONTEND_ORIGIN=${FRONTEND_ORIGIN:-'(not set)'}"
echo "====================="

exec uvicorn server:app --host 0.0.0.0 --port "${PORT:-8000}"
