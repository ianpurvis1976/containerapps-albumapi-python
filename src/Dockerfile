FROM python:3.11
WORKDIR /code
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .

# Allow the runtime (eg. Azure) to set the PORT. Default to 8080 for local/dev.
ENV PORT=8080
EXPOSE ${PORT}

# Use shell form so ${PORT} is expanded from the environment at container start.
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT}"]