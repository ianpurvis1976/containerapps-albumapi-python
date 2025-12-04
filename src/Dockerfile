FROM python:3.11
WORKDIR /code
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

# Copy Datadog configuration
COPY datadog.yaml /etc/datadog/datadog.yaml

# Allow the runtime (eg. Azure) to set the PORT. Default to 8080 for local/dev.
ENV PORT=8080
EXPOSE ${PORT}

# Datadog environment variables
ENV DD_SERVICE=album-api
ENV DD_ENV=production
ENV DD_VERSION=1.0.0
ENV DD_LOGS_INJECTION=true
ENV DD_TRACE_SAMPLE_RATE=1
ENV DD_PROFILING_ENABLED=true

# Use shell form so ${PORT} is expanded from the environment at container start.
# Run with ddtrace for automatic instrumentation
CMD ["sh", "-c", "ddtrace-run uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]