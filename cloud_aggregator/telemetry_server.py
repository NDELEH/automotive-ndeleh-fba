import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Thread-safe global telemetry cache storing latest fleet data
LIVE_FLEET_DATA = {
    "VIN-TRUCK-2026-X": {
        "timestamp": 0,
        "fuel_rail_pressure_psi": 45.0,
        "ev_battery_temp_c": 30.0,
        "alternator_voltage": 13.8,
        "engine_misfire_count": 0,
        "miles_driven": 42000
    }
}

class TelemetryRouter(BaseHTTPRequestHandler):
    def end_headers(self):
        # Enable Cross-Origin Resource Sharing (CORS) so the UI can read the data
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        """Serves the live fleet data to the UI Dashboard."""
        if self.path == "/api/telemetry":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(LIVE_FLEET_DATA).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        """Receives incoming telemetry updates from vehicles."""
        if self.path == "/api/update":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                payload = json.loads(post_data.decode("utf-8"))
                vin = payload.get("vehicle_id", "UNKNOWN-VIN")
                LIVE_FLEET_DATA[vin] = payload
                
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "acknowledged"}).encode("utf-8"))
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(str(e).encode("utf-8"))

def launch_network_hub():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, TelemetryRouter)
    print("🛰️ Ndeleh-FBA Telemetry Server live on port 8080...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server safely.")

if __name__ == "__main__":
    launch_network_hub()
