from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, rooms, bookings, payments, cms

app = FastAPI(title="PFResort Booking System")

origins = [
    "http://127.0.0.1:8000",   # Swagger docs
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to Angular app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def welcome():
    return """
    <html>
        <head><title>PFResort API</title></head>
        <body style="text-align:center">
            <h1>🏨 PFResort Booking API</h1>
            <p><a href='/docs'>➡ Open API Docs</a></p>
        </body>
    </html>
    """

# register routers
app.include_router(users.router)
app.include_router(rooms.router)
app.include_router(bookings.router)
app.include_router(payments.router)
app.include_router(cms.router)
