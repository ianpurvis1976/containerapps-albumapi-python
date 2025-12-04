#!/bin/bash

# Album API - Comprehensive curl Testing Script
# This script demonstrates all the enhanced API endpoints

# Set your API base URL (update when deployed to Azure)
BASE_URL="http://localhost:8080"
# For Azure Container Apps, use: BASE_URL="https://your-app-name.region.azurecontainerapps.io"

echo "🎵 Album API - curl Testing Commands"
echo "======================================"
echo

# Test 1: Get API information
echo "1️⃣  Get API Information:"
echo "curl -X GET \"${BASE_URL}/\""
curl -X GET "${BASE_URL}/" | jq .
echo
echo

# Test 2: Get all albums
echo "2️⃣  Get All Albums:"
echo "curl -X GET \"${BASE_URL}/albums\""
curl -X GET "${BASE_URL}/albums" | jq .
echo
echo

# Test 3: Get specific album
echo "3️⃣  Get Specific Album (ID: 1):"
echo "curl -X GET \"${BASE_URL}/albums/1\""
curl -X GET "${BASE_URL}/albums/1" | jq .
echo
echo

# Test 4: Create new albums
echo "4️⃣  Create New Albums:"

echo "📀 Creating Album 1: Rock Album"
echo "curl -X POST \"${BASE_URL}/albums\" \\"
echo "  -H \"Content-Type: application/json\" \\"
echo "  -d '{\"title\": \"Cloud Native Rocks\", \"artist\": \"The DevOps Band\", \"price\": 16.99, \"image_url\": \"https://example.com/rock.jpg\"}'"

curl -X POST "${BASE_URL}/albums" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Cloud Native Rocks", 
    "artist": "The DevOps Band", 
    "price": 16.99, 
    "image_url": "https://example.com/rock.jpg"
  }' | jq .
echo
echo

echo "📀 Creating Album 2: Jazz Album"
echo "curl -X POST \"${BASE_URL}/albums\" \\"
echo "  -H \"Content-Type: application/json\" \\"
echo "  -d '{\"title\": \"Microservices in B Minor\", \"artist\": \"Container Jazz Ensemble\", \"price\": 18.50, \"image_url\": \"https://example.com/jazz.jpg\"}'"

curl -X POST "${BASE_URL}/albums" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Microservices in B Minor", 
    "artist": "Container Jazz Ensemble", 
    "price": 18.50, 
    "image_url": "https://example.com/jazz.jpg"
  }' | jq .
echo
echo

echo "📀 Creating Album 3: Electronic Album"
echo "curl -X POST \"${BASE_URL}/albums\" \\"
echo "  -H \"Content-Type: application/json\" \\"
echo "  -d '{\"title\": \"Kubernetes Beats\", \"artist\": \"DJ Orchestrator\", \"price\": 12.99, \"image_url\": \"https://example.com/electronic.jpg\"}'"

curl -X POST "${BASE_URL}/albums" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Kubernetes Beats", 
    "artist": "DJ Orchestrator", 
    "price": 12.99, 
    "image_url": "https://example.com/electronic.jpg"
  }' | jq .
echo
echo

# Test 5: Search albums
echo "5️⃣  Search Albums:"

echo "🔍 Search for 'KEDA':"
echo "curl -X GET \"${BASE_URL}/albums/search?q=KEDA\""
curl -X GET "${BASE_URL}/albums/search?q=KEDA" | jq .
echo
echo

echo "🔍 Search for 'Container':"
echo "curl -X GET \"${BASE_URL}/albums/search?q=Container\""
curl -X GET "${BASE_URL}/albums/search?q=Container" | jq .
echo
echo

echo "🔍 Search for 'Kubernetes':"
echo "curl -X GET \"${BASE_URL}/albums/search?q=Kubernetes\""
curl -X GET "${BASE_URL}/albums/search?q=Kubernetes" | jq .
echo
echo

# Test 6: Update album
echo "6️⃣  Update Album (Partial Update):"
echo "curl -X PUT \"${BASE_URL}/albums/7\" \\"
echo "  -H \"Content-Type: application/json\" \\"
echo "  -d '{\"price\": 14.99}'"

curl -X PUT "${BASE_URL}/albums/7" \
  -H "Content-Type: application/json" \
  -d '{"price": 14.99}' | jq .
echo
echo

# Test 7: Get updated albums list
echo "7️⃣  Get Updated Albums List:"
echo "curl -X GET \"${BASE_URL}/albums\""
curl -X GET "${BASE_URL}/albums" | jq .
echo
echo

# Test 8: Get statistics
echo "8️⃣  Get API Statistics:"
echo "curl -X GET \"${BASE_URL}/stats\""
curl -X GET "${BASE_URL}/stats" | jq .
echo
echo

# Test 9: Health check
echo "9️⃣  Health Check:"
echo "curl -X GET \"${BASE_URL}/health\""
curl -X GET "${BASE_URL}/health" | jq .
echo
echo

# Test 10: Error handling - Get non-existent album
echo "🔟 Error Handling - Get Non-Existent Album:"
echo "curl -X GET \"${BASE_URL}/albums/999\""
curl -X GET "${BASE_URL}/albums/999" | jq .
echo
echo

# Test 11: Delete album
echo "1️⃣1️⃣ Delete Album (ID: 8):"
echo "curl -X DELETE \"${BASE_URL}/albums/8\""
curl -X DELETE "${BASE_URL}/albums/8" | jq .
echo
echo

# Test 12: Verify deletion
echo "1️⃣2️⃣ Verify Deletion - Get Albums List:"
echo "curl -X GET \"${BASE_URL}/albums\""
curl -X GET "${BASE_URL}/albums" | jq .
echo
echo

echo "✅ Testing Complete!"
echo
echo "🚀 Azure Container Apps URL:"
echo "   Update BASE_URL to your Azure Container Apps URL when deployed"
echo "   Example: https://album-api--abc123.kindwater-12345678.uksouth.azurecontainerapps.io"