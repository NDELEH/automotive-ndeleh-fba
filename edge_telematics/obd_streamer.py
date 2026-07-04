import time
import random
import json
import urllib.request

class VehicleSensorStreamer:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def read_can_bus(self):
        """Simulates reading raw OBD-II, EV powertrain, and fuel sensors."""
        return {
            "vehicle_id": self.vehicle_id,
            "timestamp": time.time(),
            "fuel_rail_pressure_psi": random.uniform(34, 52),  # Drops under 38 occasionally
            "ev_battery_temp_c": random.uniform(25, 49),      # Spikes over 45 occasionally
            "alternator_voltage": random.uniform(11.9, 14.2),  # Drops under 12.2 occasionally
            "engine_misfire_count": random.randint(0, 2),
            "miles_driven": 42000
        }

    def broadcast_telemetry(self, data):
        """Sends data payload directly to the network server over HTTP POST."""
        url = "http://localhost:8080/api/update"
        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers={'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=2) as response:
                return response.read().decode("utf-8")
        except Exception as e:
            return f"Network drop: {e}"

if __name__ == "__main__":
    streamer = VehicleSensorStreamer(vehicle_id="VIN-TRUCK-2026-X")
    print("📡 Vehicle Telematics Node active. Broadcasting live data stream...")
    while True:
        sensor_data = streamer.read_can_bus()
        log = streamer.broadcast_telemetry(sensor_data)
        print(f"Uploaded Package at {sensor_data['timestamp']} -> Server response: {log}")
        time.sleep(2)
