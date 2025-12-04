FROM python:3.11
WORKDIR /code
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

# Allow the runtime (eg. Azure) to set the PORT. Default to 8080 for local/dev.
ENV PORT=8080
EXPOSE ${PORT}

# Datadog recommended environment variables for main container
ENV PYTHONUNBUFFERED=1
ENV DD_LOGS_INJECTION=true

# Use shell form so ${PORT} is expanded from the environment at container start.
CMD ["sh", "-c", "ddtrace-run uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]

