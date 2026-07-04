import time
import random
import json

class VehicleSensorStreamer:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def read_can_bus(self):
        """Simulates reading raw OBD-II, EV powertrain, and fuel sensors."""
        return {
            "vehicle_id": self.vehicle_id,
            "timestamp": time.time(),
            "fuel_rail_pressure_psi": random.uniform(35, 55),
            "ev_battery_temp_c": random.uniform(25, 48),
            "alternator_voltage": random.uniform(11.8, 14.2),
            "engine_misfire_count": random.randint(0, 5),
            "miles_driven": 42000
        }

if __name__ == "__main__":
    streamer = VehicleSensorStreamer(vehicle_id="VIN-TRUCK-2026-X")
    print("Streaming vehicle telematics... Press Ctrl+C to stop.")
    while True:
        print(json.dumps(streamer.read_can_bus(), indent=2))
        time.sleep(1)
