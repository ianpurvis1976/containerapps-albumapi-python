#!/usr/bin/env python3

# Demo script showing the enhanced Album API logging capabilities
# This simulates what you'll see when the app runs

import json
from datetime import datetime

def simulate_logs():
    print("🚀 Enhanced Album API - Logging Demo\n")
    
    # Simulate startup logs
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,123')} - app.main - INFO - Album API starting up...")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,124')} - app.main - INFO - Loaded 6 initial albums")
    print()
    
    # Simulate API request logs
    print("📊 Sample API Operations with Logging:\n")
    
    # GET all albums
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,456')} - app.main - INFO - Incoming request: GET /albums")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,457')} - app.main - INFO - Retrieving all albums. Total count: 6")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,459')} - app.main - INFO - Request completed: GET /albums - Status: 200 - Time: 0.0032s")
    print()
    
    # CREATE new album
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,501')} - app.main - INFO - Incoming request: POST /albums")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,502')} - app.main - INFO - Creating new album: My New Song by Cool Artist")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,503')} - app.main - INFO - Successfully created album with ID: 7")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,504')} - app.main - INFO - Request completed: POST /albums - Status: 200 - Time: 0.0045s")
    print()
    
    # SEARCH albums
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,601')} - app.main - INFO - Incoming request: GET /albums/search?q=KEDA")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,602')} - app.main - INFO - Searching albums with query: 'KEDA'")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,603')} - app.main - INFO - Search for 'KEDA' returned 1 results")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,604')} - app.main - INFO - Request completed: GET /albums/search?q=KEDA - Status: 200 - Time: 0.0028s")
    print()
    
    # GET individual album
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,701')} - app.main - INFO - Incoming request: GET /albums/1")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,702')} - app.main - INFO - Retrieving album with ID: 1")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,703')} - app.main - INFO - Found album: You, Me and an App Id by Daprize")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,704')} - app.main - INFO - Request completed: GET /albums/1 - Status: 200 - Time: 0.0019s")
    print()
    
    # UPDATE album
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,801')} - app.main - INFO - Incoming request: PUT /albums/2")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,802')} - app.main - INFO - Updating album with ID: 2")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,803')} - app.main - INFO - Updated album 2. Fields updated: price")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,804')} - app.main - INFO - Request completed: PUT /albums/2 - Status: 200 - Time: 0.0041s")
    print()
    
    # GET statistics
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,901')} - app.main - INFO - Incoming request: GET /stats")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,902')} - app.main - INFO - Retrieving API statistics")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,903')} - app.main - INFO - Stats generated: 7 albums, 7 artists, avg price $13.14")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,904')} - app.main - INFO - Request completed: GET /stats - Status: 200 - Time: 0.0067s")
    print()
    
    # Error case - album not found
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,951')} - app.main - INFO - Incoming request: GET /albums/999")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,952')} - app.main - INFO - Retrieving album with ID: 999")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,953')} - app.main - WARNING - Album with ID 999 not found")
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S,954')} - app.main - INFO - Request completed: GET /albums/999 - Status: 404 - Time: 0.0015s")
    print()

if __name__ == "__main__":
    simulate_logs()
    print("✅ This is what you'll see when your enhanced Album API runs!")
    print("🚀 Deploy to Azure to see these logs in Azure Monitor/Application Insights")