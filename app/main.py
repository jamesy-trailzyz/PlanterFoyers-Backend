from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.routes import users, rooms, bookings, payments, cms, auth

app = FastAPI(title="PFResort Booking System", debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
def welcome_dashboard():
    return """
    <html>
        <head>
            <title>🏝️ PFResort Booking Dashboard</title>
            <style>
                body { font-family:'Segoe UI', Arial, sans-serif; margin:0; padding:0; background:#f5f7fa; color:#333; }
                header { background:url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e') center/cover no-repeat; height:300px; display:flex; align-items:center; justify-content:center; color:white; text-shadow:1px 1px 6px rgba(0,0,0,0.7); }
                header h1 { font-size:3rem; }
                main { max-width:1000px; margin:-50px auto 40px; background:white; padding:30px; border-radius:12px; box-shadow:0 6px 20px rgba(0,0,0,0.1); }
                h2 { text-align:center; margin-bottom:20px; font-size:1.8rem; }
                .grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(250px,1fr)); gap:20px; }
                .card { background:#f8f9fa; border-radius:12px; padding:20px; text-align:center; box-shadow:0 2px 8px rgba(0,0,0,0.05); transition: transform 0.2s, box-shadow 0.2s; }
                .card:hover { transform:translateY(-5px); box-shadow:0 4px 12px rgba(0,0,0,0.15); }
                .card h3 { margin-bottom:8px; }
                .card p { font-size:0.95rem; margin-bottom:12px; }
                .btn { display:inline-block; margin:4px 2px; padding:8px 12px; background:#007bff; color:white; border-radius:6px; text-decoration:none; font-weight:bold; font-size:0.9rem; }
                .btn:hover { background:#0056b3; }
                footer { text-align:center; padding:15px; background:#007bff; color:white; border-top:4px solid #0056b3; }
                footer a { color:#fff; text-decoration:underline; }
            </style>
        </head>
        <body>
            <header>
                <h1>🏨 PFResort Booking Dashboard</h1>
            </header>
            <main>
                <h2>Manage Modules</h2>
                <div class="grid">

                    <!-- Auth Module -->
                    <div class="card">
                        <h3>Auth</h3>
                        <p>Secure login & authentication</p>
                        <a class="btn" href="/auth/login">🔑 Login</a>
                        <a class="btn" href="/auth/register">📝 Register</a>
                    </div>

                    <!-- Users Module -->
                    <div class="card">
                        <h3>Users</h3>
                        <p>Manage user accounts</p>
                        <a class="btn" href="/users/">👤 List Users</a>
                        <a class="btn" href="/users/create">➕ Create User</a>
                        <a class="btn" href="/users/update">✏️ Update User</a>
                        <a class="btn" href="/users/delete">🗑️ Delete User</a>
                    </div>

                    <!-- Rooms Module -->
                    <div class="card">
                        <h3>Rooms</h3>
                        <p>Manage rooms & availability</p>
                        <a class="btn" href="/rooms/">🛏️ List Rooms</a>
                        <a class="btn" href="/rooms/create">➕ Add Room</a>
                        <a class="btn" href="/rooms/update">✏️ Update Room</a>
                        <a class="btn" href="/rooms/delete">🗑️ Delete Room</a>
                    </div>

                    <!-- Bookings Module -->
                    <div class="card">
                        <h3>Bookings</h3>
                        <p>Track reservations</p>
                        <a class="btn" href="/bookings/">📅 List Bookings</a>
                        <a class="btn" href="/bookings/create">➕ Create Booking</a>
                        <a class="btn" href="/bookings/update">✏️ Update Booking</a>
                        <a class="btn" href="/bookings/delete">🗑️ Cancel Booking</a>
                    </div>

                    <!-- Payments Module -->
                    <div class="card">
                        <h3>Payments</h3>
                        <p>Track payments & transactions</p>
                        <a class="btn" href="/payments/">💳 List Payments</a>
                        <a class="btn" href="/payments/create">➕ Add Payment</a>
                        <a class="btn" href="/payments/update">✏️ Update Payment</a>
                        <a class="btn" href="/payments/delete">🗑️ Delete Payment</a>
                    </div>

                    <!-- CMS Module -->
                    <div class="card">
                        <h3>CMS</h3>
                        <p>Manage resort content</p>
                        <a class="btn" href="/cms/">📰 List Content</a>
                        <a class="btn" href="/cms/create">➕ Add Content</a>
                        <a class="btn" href="/cms/update">✏️ Update Content</a>
                        <a class="btn" href="/cms/delete">🗑️ Delete Content</a>
                    </div>

                </div>

                <hr style="margin:30px 0;">
                <div style="text-align:center;">
                    <a href="/docs" style="padding:12px 20px; background:#28a745; color:white; border-radius:8px; text-decoration:none; font-weight:bold;">
                        📖 Full API Docs
                    </a>
                </div>
            </main>
            <footer>
                © 2025 PFResort Booking System | Built with <a href="/docs">FastAPI</a>
            </footer>
        </body>
    </html>
    """



# Routers with prefixes
app.include_router(auth.router, tags=["Auth"])
app.include_router(users.router, tags=["Users"])
app.include_router(rooms.router, tags=["Rooms"])
app.include_router(bookings.router, tags=["Bookings"])
app.include_router(payments.router, tags=["Payments"])
app.include_router(cms.router, tags=["CMS"])
