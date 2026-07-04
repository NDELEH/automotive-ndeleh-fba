import json

class NdelehAutomotiveEngine:
    def __init__(self):
        # Human associative memory weights for engine systems
        self.causal_weights = {
            "Low Alternator Voltage": {"Check Engine Light": 0.8, "Battery Failure": 0.9},
            "Low Fuel Pressure": {"Engine Misfire": 0.75, "Check Engine Light": 0.85},
            "High EV Battery Temp": {"Thermal Throttle": 0.9, "EV System Error": 0.95}
        }

    def analyze_symptoms(self, sensor_data):
        incidents = []
        if sensor_data["alternator_voltage"] < 12.2:
            incidents.append("Low Alternator Voltage")
        if sensor_data["fuel_rail_pressure_psi"] < 38:
            incidents.append("Low Fuel Pressure")
        if sensor_data["ev_battery_temp_c"] > 45:
            incidents.append("High EV Battery Temp")

        diagnostics = {}
        for incident in incidents:
            if incident in self.causal_weights:
                # Find the primary root path (Spine extraction)
                primary_target = max(self.causal_weights[incident], key=self.causal_weights[incident].get)
                influence_score = self.causal_weights[incident][primary_target]
                
                diagnostics[incident] = {
                    "predicted_fault": primary_target,
                    "confidence_spine": influence_score,
                    "status": "Predictive Alert (Pre-CEL)" if influence_score < 0.9 else "Critical Spine Activation"
                }
        return diagnostics

if __name__ == "__main__":
    engine = NdelehAutomotiveEngine()
    test_bad_data = {"alternator_voltage": 11.9, "fuel_rail_pressure_psi": 42, "ev_battery_temp_c": 46}
    print(json.dumps(engine.analyze_symptoms(test_bad_data), indent=4))
