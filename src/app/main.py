from typing import Optional
import logging
import time
from datetime import datetime
import uuid
import os
import sys

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import ddtrace for automatic instrumentation
from ddtrace import patch_all

# Auto-instrument FastAPI and other libraries
patch_all()

# Datadog logging configuration (from official docs)
LOG_FILE = "/LogFiles/app.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
        '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
        '- %(message)s')

logging.basicConfig(
    level=logging.INFO,
    format=FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)
logger.level = logging.INFO

logger.info('Album API starting with Datadog integration!')

app = FastAPI(
    title="Album API",
    description="A sample album API with CRUD operations and logging",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"]
)

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    # Generate request ID for tracing
    request_id = str(uuid.uuid4())[:8]
    
    # Log request start
    logger.info(f"Request started: {request.method} {request.url.path}")
    
    response = await call_next(request)
    
    # Calculate duration
    duration_ms = round((time.time() - start_time) * 1000, 2)
    
    # Log request completion
    logger.info(f"Request completed: {request.method} {request.url.path} - Status: {response.status_code} - Duration: {duration_ms}ms")
    
    return response

class Album():
    def __init__(self, id, title, artist, price, image_url):
         self.id = id
         self.title = title
         self.artist = artist
         self.price = price
         self.image_url = image_url

# Pydantic models for request/response
class AlbumCreate(BaseModel):
    title: str
    artist: str
    price: float
    image_url: str

class AlbumUpdate(BaseModel):
    title: Optional[str] = None
    artist: Optional[str] = None
    price: Optional[float] = None
    image_url: Optional[str] = None

albums = [ 
    Album(1, "You, Me and an App Id", "Daprize", 10.99, "https://aka.ms/albums-daprlogo"),
    Album(2, "Seven Revision Army", "The Blue-Green Stripes", 13.99, "https://aka.ms/albums-containerappslogo"),
    Album(3, "Scale It Up", "KEDA Club", 13.99, "https://aka.ms/albums-kedalogo"),
    Album(4, "Lost in Translation", "MegaDNS", 12.99,"https://aka.ms/albums-envoylogo"),
    Album(5, "Lock Down Your Love", "V is for VNET", 12.99, "https://aka.ms/albums-vnetlogo"),
    Album(6, "Sweet Container O' Mine", "Guns N Probeses", 14.99, "https://aka.ms/albums-containerappslogo")
]

# Simple in-memory counter for new album IDs
next_id = 7

@app.on_event("startup")
async def startup_event():
    logger.info("Album API starting up...")
    logger.info(f"Loaded {len(albums)} initial albums")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Album API shutting down...")

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {
        "message": "Welcome to Album API",
        "endpoints": {
            "albums": "GET /albums - List all albums",
            "album_by_id": "GET /albums/{id} - Get album by ID",
            "create_album": "POST /albums - Create new album",
            "update_album": "PUT /albums/{id} - Update album",
            "delete_album": "DELETE /albums/{id} - Delete album",
            "search": "GET /albums/search?q={query} - Search albums",
            "stats": "GET /stats - API statistics",
            "health": "GET /health - Health check"
        },
        "timestamp": datetime.now().isoformat()
    }


@app.get("/albums")
def get_albums():
    logger.info(f"Retrieving all albums. Total count: {len(albums)}")
    return {"albums": albums, "total": len(albums)}


@app.get("/albums/{album_id}")
def get_album(album_id: int):
    logger.info(f"Retrieving album with ID: {album_id}")
    
    album = next((album for album in albums if album.id == album_id), None)
    if not album:
        logger.warning(f"Album with ID {album_id} not found")
        raise HTTPException(status_code=404, detail="Album not found")
    
    logger.info(f"Found album: {album.title} by {album.artist}")
    return album


@app.post("/albums")
def create_album(album_data: AlbumCreate):
    global next_id
    
    logger.info(f"Creating new album: {album_data.title} by {album_data.artist}")
    
    new_album = Album(
        id=next_id,
        title=album_data.title,
        artist=album_data.artist,
        price=album_data.price,
        image_url=album_data.image_url
    )
    
    albums.append(new_album)
    next_id += 1
    
    logger.info(f"Successfully created album with ID: {new_album.id}")
    return {"message": "Album created successfully", "album": new_album}


@app.put("/albums/{album_id}")
def update_album(album_id: int, album_data: AlbumUpdate):
    logger.info(f"Updating album with ID: {album_id}")
    
    album = next((album for album in albums if album.id == album_id), None)
    if not album:
        logger.warning(f"Album with ID {album_id} not found for update")
        raise HTTPException(status_code=404, detail="Album not found")
    
    updated_fields = []
    if album_data.title is not None:
        album.title = album_data.title
        updated_fields.append("title")
    if album_data.artist is not None:
        album.artist = album_data.artist
        updated_fields.append("artist")
    if album_data.price is not None:
        album.price = album_data.price
        updated_fields.append("price")
    if album_data.image_url is not None:
        album.image_url = album_data.image_url
        updated_fields.append("image_url")
    
    logger.info(f"Updated album {album_id}. Fields updated: {', '.join(updated_fields)}")
    return {"message": "Album updated successfully", "album": album, "updated_fields": updated_fields}


@app.delete("/albums/{album_id}")
def delete_album(album_id: int):
    logger.info(f"Attempting to delete album with ID: {album_id}")
    
    album_index = next((i for i, album in enumerate(albums) if album.id == album_id), None)
    if album_index is None:
        logger.warning(f"Album with ID {album_id} not found for deletion")
        raise HTTPException(status_code=404, detail="Album not found")
    
    deleted_album = albums.pop(album_index)
    logger.info(f"Successfully deleted album: {deleted_album.title} by {deleted_album.artist}")
    return {"message": "Album deleted successfully", "deleted_album": deleted_album}


@app.get("/albums/search")
def search_albums(q: str):
    logger.info(f"Searching albums with query: '{q}'")
    
    if not q.strip():
        logger.warning("Empty search query provided")
        raise HTTPException(status_code=400, detail="Search query cannot be empty")
    
    query_lower = q.lower()
    matching_albums = [
        album for album in albums 
        if query_lower in album.title.lower() or query_lower in album.artist.lower()
    ]
    
    logger.info(f"Search for '{q}' returned {len(matching_albums)} results")
    return {"query": q, "results": matching_albums, "total": len(matching_albums)}


@app.get("/stats")
def get_stats():
    logger.info("Retrieving API statistics")
    
    total_albums = len(albums)
    artists = list(set(album.artist for album in albums))
    avg_price = sum(album.price for album in albums) / total_albums if total_albums > 0 else 0
    most_expensive = max(albums, key=lambda x: x.price) if albums else None
    cheapest = min(albums, key=lambda x: x.price) if albums else None
    
    stats = {
        "total_albums": total_albums,
        "unique_artists": len(artists),
        "artists": artists,
        "average_price": round(avg_price, 2),
        "most_expensive_album": {
            "title": most_expensive.title,
            "artist": most_expensive.artist,
            "price": most_expensive.price
        } if most_expensive else None,
        "cheapest_album": {
            "title": cheapest.title,
            "artist": cheapest.artist,
            "price": cheapest.price
        } if cheapest else None,
        "timestamp": datetime.now().isoformat()
    }
    
    logger.info(f"Stats generated: {total_albums} albums, {len(artists)} artists, avg price ${avg_price:.2f}")
    return stats


@app.get("/health")
def health_check():
    logger.info("Health check requested")
    return {
        "status": "healthy",
        "service": "Album API",
        "timestamp": datetime.now().isoformat(),
        "albums_count": len(albums)
    }
