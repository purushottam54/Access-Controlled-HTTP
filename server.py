import http.server
import socketserver
import threading
import time
from collections import defaultdict

# Define port
PORT = 8000

# Security Configurations
RATE_LIMIT = 5  # Max requests per minute per IP
WHITELISTED_IPS = ["127.0.0.1"]  # Only allow these IPs if enabled
ENABLE_WHITELIST = False  # Set to True to enforce IP filtering
REQUEST_TIMEOUT = 10  # Seconds before auto-denying access

# Track request counts per IP
request_counts = defaultdict(lambda: {"count": 0, "timestamp": time.time()})


class SecureAccessHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]

        # IP Whitelisting Check
        if ENABLE_WHITELIST and client_ip not in WHITELISTED_IPS:
            print(f"❌ Access denied to {client_ip} (Not whitelisted)")
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Access Denied - IP Not Whitelisted")
            return

        # Rate Limiting Check
        current_time = time.time()
        if (
            current_time - request_counts[client_ip]["timestamp"] < 60
            and request_counts[client_ip]["count"] >= RATE_LIMIT
        ):
            print(f"⛔ Too many requests from {client_ip}. Access Denied!")
            self.send_response(429)  # Too Many Requests
            self.end_headers()
            self.wfile.write(b"Too many requests. Try again later.")
            return

        # Update request count
        if current_time - request_counts[client_ip]["timestamp"] >= 60:
            request_counts[client_ip] = {"count": 1, "timestamp": current_time}
        else:
            request_counts[client_ip]["count"] += 1

        # Log incoming request
        print(f"🔓 Incoming request from: {client_ip} for {self.path}")

        # User Approval with Timeout
        def get_permission():
            return input(f"Grant access to {client_ip}? (y/n): ").strip().lower()

        permission = None
        timer = threading.Thread(target=lambda: time.sleep(REQUEST_TIMEOUT))
        timer.start()

        try:
            permission = get_permission()
        except Exception:
            print("⚠️ Input timeout. Access denied by default.")

        if permission == "y":
            print(f"✅ Access granted to {client_ip}")
            super().do_GET()
        else:
            print(f"⛔ Access denied to {client_ip}")
            self.send_response(403)
            self.end_headers()
            self.wfile.write(b"Access Denied")


# Run server in a separate thread
def run_server():
    with socketserver.TCPServer(("", PORT), SecureAccessHandler) as httpd:
        print(f"🚀 Secure server running on port {PORT}")
        httpd.serve_forever()


run_server()
