#!/usr/bin/env python3

# Demo script showing Datadog-optimized JSON logging format

import json
from datetime import datetime

def simulate_datadog_logs():
    print("🐕 Datadog-Optimized JSON Logging Demo\n")
    
    # Sample JSON logs that will appear in Datadog
    sample_logs = [
        {
            "timestamp": "2025-12-04T13:52:44.123Z",
            "level": "INFO",
            "logger": "app.main",
            "message": "Album API starting up...",
            "service": "album-api"
        },
        {
            "timestamp": "2025-12-04T13:52:45.456Z",
            "level": "INFO", 
            "logger": "app.main",
            "message": "Request started",
            "service": "album-api",
            "operation": "request_start",
            "request_id": "a1b2c3d4",
            "method": "GET",
            "path": "/albums"
        },
        {
            "timestamp": "2025-12-04T13:52:45.458Z",
            "level": "INFO",
            "logger": "app.main", 
            "message": "Retrieving all albums. Total count: 6",
            "service": "album-api",
            "operation": "get_albums",
            "album_count": 6
        },
        {
            "timestamp": "2025-12-04T13:52:45.461Z",
            "level": "INFO",
            "logger": "app.main",
            "message": "Request completed", 
            "service": "album-api",
            "operation": "request_complete",
            "request_id": "a1b2c3d4",
            "method": "GET",
            "path": "/albums",
            "status_code": 200,
            "duration": 3.2
        },
        {
            "timestamp": "2025-12-04T13:52:46.101Z",
            "level": "INFO",
            "logger": "app.main",
            "message": "Search requested",
            "service": "album-api", 
            "operation": "search_albums",
            "query": "KEDA"
        },
        {
            "timestamp": "2025-12-04T13:52:46.103Z",
            "level": "INFO",
            "logger": "app.main",
            "message": "Search completed",
            "service": "album-api",
            "operation": "search_complete", 
            "query": "KEDA",
            "results_count": 1
        },
        {
            "timestamp": "2025-12-04T13:52:46.201Z", 
            "level": "WARNING",
            "logger": "app.main",
            "message": "Album not found",
            "service": "album-api",
            "operation": "get_album_error",
            "album_id": 999,
            "error": "not_found"
        }
    ]
    
    print("📋 Sample JSON logs that will appear in Datadog:\n")
    
    for log in sample_logs:
        print(json.dumps(log, indent=2))
        print()
    
    print("🔍 Datadog Benefits:")
    print("✅ Structured data for advanced filtering")
    print("✅ Custom fields (operation, request_id, duration)")
    print("✅ Easy dashboard creation and alerting")
    print("✅ Request tracing via request_id")
    print("✅ Performance monitoring via duration field")
    print("✅ Error tracking with structured error info")

if __name__ == "__main__":
    simulate_datadog_logs()