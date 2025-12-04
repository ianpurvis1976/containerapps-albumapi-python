# Album API - Enhanced Edition

A comprehensive FastAPI application for managing music albums with full CRUD operations, search functionality, and detailed logging.

## 🚀 New Features Added

### ✅ Full CRUD Operations
- **GET** `/albums` - List all albums with count
- **GET** `/albums/{id}` - Get specific album by ID
- **POST** `/albums` - Create new album
- **PUT** `/albums/{id}` - Update existing album
- **DELETE** `/albums/{id}` - Delete album

### 🔍 Search & Analytics
- **GET** `/albums/search?q={query}` - Search albums by title or artist
- **GET** `/stats` - Get comprehensive statistics about albums and artists
- **GET** `/health` - Health check endpoint

### 📊 Enhanced API Information
- **GET** `/` - Interactive API documentation with all available endpoints
- Pydantic models for request/response validation
- Comprehensive error handling with proper HTTP status codes

### 📝 Comprehensive Logging
- Request/response logging with timing
- Detailed operation logging for all CRUD operations
- Startup/shutdown event logging
- Search and error logging

## 🏃‍♂️ Quick Start

### Local Development
```bash
cd src
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload
```

### Docker Build & Run
```bash
cd src
docker build -t album-api .
docker run -p 8080:8080 album-api
```

### Deploy to Azure Container Apps
```bash
cd src
az containerapp up \
  --name $API_NAME \
  --resource-group $RESOURCE_GROUP \
  --location $LOCATION \
  --environment $ENVIRONMENT \
  --source .
```

## 📋 API Examples

### Create Album
```bash
curl -X POST "http://localhost:8080/albums" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My New Album",
    "artist": "Amazing Artist",
    "price": 15.99,
    "image_url": "https://example.com/image.jpg"
  }'
```

### Search Albums
```bash
curl "http://localhost:8080/albums/search?q=KEDA"
```

### Get Statistics
```bash
curl "http://localhost:8080/stats"
```

### Update Album
```bash
curl -X PUT "http://localhost:8080/albums/1" \
  -H "Content-Type: application/json" \
  -d '{"price": 9.99}'
```

## 🐳 Docker Configuration

The Dockerfile now uses the `$PORT` environment variable for maximum flexibility:
- Defaults to port 8080 for local development
- Azure Container Apps can override with `PORT` environment variable
- Supports any port configuration your cloud platform requires

## 📈 Logging Features

The app now provides comprehensive logging:
- **Request Timing**: Every request is logged with duration
- **CRUD Operations**: All create, read, update, delete operations are logged
- **Search Analytics**: Search queries and result counts are tracked
- **Error Tracking**: 404s and validation errors are logged
- **Health Monitoring**: Startup/shutdown events and health checks

## 🔧 Environment Variables

- `PORT`: Server port (default: 8080)
- `LOG_LEVEL`: Logging level (default: INFO)

## 📊 Sample Log Output

```
2025-12-04 10:30:15,123 - app.main - INFO - Album API starting up...
2025-12-04 10:30:15,124 - app.main - INFO - Loaded 6 initial albums
2025-12-04 10:30:20,456 - app.main - INFO - Incoming request: GET http://localhost:8080/albums
2025-12-04 10:30:20,458 - app.main - INFO - Retrieving all albums. Total count: 6
2025-12-04 10:30:20,459 - app.main - INFO - Request completed: GET http://localhost:8080/albums - Status: 200 - Time: 0.0032s
```

## 🎯 Ready for Production

This enhanced API includes:
- ✅ Proper error handling
- ✅ Request validation with Pydantic
- ✅ Comprehensive logging
- ✅ Health checks
- ✅ Docker port flexibility
- ✅ CORS configuration
- ✅ API documentation