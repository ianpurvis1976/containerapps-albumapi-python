# Album API - Essential curl Commands

## Base URL
```bash
# Local development
BASE_URL="http://localhost:8080"

# Azure Container Apps (update with your actual URL)
BASE_URL="https://album-api.livelymushroom-3c5b5516.uksouth.azurecontainerapps.io/"
```

## 📋 Quick Reference Commands

### Get All Albums
```bash
curl -X GET "${BASE_URL}/albums"
```

### Get Specific Album
```bash
curl -X GET "${BASE_URL}/albums/1"
```

### Create New Album
```bash
curl -X POST "${BASE_URL}/albums" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Cloud Native Rocks",
    "artist": "The DevOps Band", 
    "price": 16.99,
    "image_url": "https://example.com/rock.jpg"
  }'
```

### Search Albums
```bash
curl -X GET "${BASE_URL}/albums/search?q=KEDA"
curl -X GET "${BASE_URL}/albums/search?q=Container"
```

### Update Album (Partial)
```bash
curl -X PUT "${BASE_URL}/albums/1" \
  -H "Content-Type: application/json" \
  -d '{"price": 14.99}'
```

### Delete Album
```bash
curl -X DELETE "${BASE_URL}/albums/1"
```

### Get Statistics
```bash
curl -X GET "${BASE_URL}/stats"
```

### Health Check
```bash
curl -X GET "${BASE_URL}/health"
```

## 🎯 Sample Albums to Create

### Rock Album
```bash
curl -X POST "${BASE_URL}/albums" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Cloud Native Rocks",
    "artist": "The DevOps Band",
    "price": 16.99,
    "image_url": "https://example.com/rock.jpg"
  }'
```

### Jazz Album
```bash
curl -X POST "${BASE_URL}/albums" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Microservices in B Minor",
    "artist": "Container Jazz Ensemble",
    "price": 18.50,
    "image_url": "https://example.com/jazz.jpg"
  }'
```

### Electronic Album
```bash
curl -X POST "${BASE_URL}/albums" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Kubernetes Beats",
    "artist": "DJ Orchestrator",
    "price": 12.99,
    "image_url": "https://example.com/electronic.jpg"
  }'
```

### Hip-Hop Album
```bash
curl -X POST "${BASE_URL}/albums" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Distributed Systems Flow",
    "artist": "MC LoadBalancer",
    "price": 15.75,
    "image_url": "https://example.com/hiphop.jpg"
  }'
```

## 🔥 Advanced Testing Commands

### Test Error Handling
```bash
# Try to get non-existent album
curl -X GET "${BASE_URL}/albums/999"

# Try empty search
curl -X GET "${BASE_URL}/albums/search?q="

# Try invalid album update
curl -X PUT "${BASE_URL}/albums/999" \
  -H "Content-Type: application/json" \
  -d '{"price": 10.00}'
```

### Performance Testing
```bash
# Multiple rapid requests
for i in {1..10}; do
  curl -s -X GET "${BASE_URL}/albums" > /dev/null && echo "Request $i: OK"
done
```

### Pretty JSON Output (with jq)
```bash
curl -X GET "${BASE_URL}/stats" | jq .
curl -X GET "${BASE_URL}/albums" | jq '.albums[] | {id, title, artist, price}'
```

## 🐕 Datadog-Friendly Testing
These commands will generate rich logs for your Datadog monitoring:

```bash
# Generate search analytics
curl -X GET "${BASE_URL}/albums/search?q=KEDA"
curl -X GET "${BASE_URL}/albums/search?q=Container" 
curl -X GET "${BASE_URL}/albums/search?q=DevOps"

# Generate CRUD operation logs
curl -X POST "${BASE_URL}/albums" -H "Content-Type: application/json" -d '{"title":"Test Album","artist":"Test Artist","price":9.99,"image_url":"https://test.com"}'
curl -X PUT "${BASE_URL}/albums/7" -H "Content-Type: application/json" -d '{"price": 8.99}'
curl -X DELETE "${BASE_URL}/albums/7"

# Generate error logs for monitoring
curl -X GET "${BASE_URL}/albums/999"  # 404 error
curl -X GET "${BASE_URL}/albums/search?q="  # 400 error
```