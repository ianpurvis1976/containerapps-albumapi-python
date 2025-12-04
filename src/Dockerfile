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



Good question! The `DD_SOURCE=python` environment variable needs to be set in the Datadog sidecar container, not your main application container. Since you used `datadog-ci` to set up the sidecar, we need to check if it's already configured or add it manually.

Let me first check the current sidecar configuration: 

Ran terminal command: az containerapp revision show --name album-api --resource-group rg-datadogcontainerapp-uks-sbox --revision $(az containerapp revision list --name album-api --resource-group rg-datadogcontainerapp-uks-sbox --query "[0].name" -o tsv) --query "properties.template.containers[?name=='datadog-sidecar'].env" -o table

I can see the sidecar has many environment variables but `DD_SOURCE=python` is missing. Let's add it by updating the Container App configuration. We need to modify the sidecar container's environment variables: 

Ran terminal command: az containerapp revision copy \
  --name album-api \
  --resource-group rg-datadogcontainerapp-uks-sbox \
  --from-revision $(az containerapp revision list --name album-api --resource-group rg-datadogcontainerapp-uks-sbox --query "[0].name" -o tsv) \
  --yaml /dev/stdin << 'EOF'
properties:
  template:
    containers:
    - name: album-api
      image: cac3517b1377acr.azurecr.io/album-api:cli-containerapp-20251204135358286510
      env:
      - name: DD_API_KEY
        secretRef: dd-api-key
    - name: datadog-sidecar
      image: index.docker.io/datadog/serverless-init:latest
      env:
      - name: DD_SITE
        value: datadoghq.com
      - name: DD_LOGS_INJECTION
        value: "true"
      - name: DD_TRACE_ENABLED
        value: "true"
      - name: DD_HEALTH_PORT
        value: "5555"
      - name: DD_API_KEY
        secretRef: dd-api-key
      - name: DD_SERVICE
        value: album-api
      - name: DD_AZURE_SUBSCRIPTION_ID
        value: 4f6a8ac7-c366-40b2-a005-ae02bfbadf2f
      - name: DD_AZURE_RESOURCE_GROUP
        value: rg-datadogcontainerapp-uks-sbox
      - name: DD_SERVERLESS_LOG_PATH
        value: "/shared-volume/logs/*.log"
      - name: DD_SOURCE
        value: python
EOF