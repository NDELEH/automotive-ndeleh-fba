# 🚗 Automotive Ndeleh-FBA Network

An open-source, edge-to-cloud diagnostic engine that uses the **Ndeleh Fishbone Algorithm (Ndeleh-FBA)** to trace vehicle system anomalies back to their root causes before a warning light ever turns on. 

This system monitors fuel delivery, EV battery systems, electrical voltage, and traditional powertrain sensors to extract the core **Causal Spine** of a vehicle failure.

## 🛠️ System Architecture

1. **Edge Telematics (`edge_telematics/`)**: Lightweight scripts running inside the vehicle's onboard computer to read the CAN-bus and perform instant local root-cause extraction.
2. **Predictive UI (`dashboard_ui/`)**: A fleet operator interface that displays upcoming failures, microspines (contributing factors), and direct maintenance solutions.
3. **Automated Deployment (`.github/workflows/`)**: A continuous integration pipeline that handles Over-The-Air (OTA) updates to push new diagnostic logic to the active fleet.

## 📁 Repository Structure

```text
automotive-ndeleh-fba/
├── .github/workflows/
│   └── deploy-edge.yml        # Fleet-wide OTA update pipeline
├── edge_telematics/
│   ├── obd_streamer.py        # Real-time CAN-bus & sensor simulator
│   └── local_reasoner.py      # Local Ndeleh Spine Extraction engine
├── dashboard_ui/
│   └── index.html             # Predictive fleet management dashboard
└── requirements.txt           # Environment dependencies
```

## 🚀 How to Run Locally

### 1. Stream Vehicle Data
Run the telematics simulator to see mock sensor data representing fuel rail pressure, EV battery temperatures, and system voltages:
```bash
python edge_telematics/obd_streamer.py
```

### 2. Run the Diagnostic Engine
Test how the Ndeleh-FBA processes abnormal sensor data into human-readable root causes:
```bash
python edge_telematics/local_reasoner.py
```

## 🛰️ Fleet Deployment via GitHub Actions
Every time you push code updates to the `main` branch, the included GitHub Workflow (`deploy-edge.yml`) automatically builds a secure package and simulates a live cellular Over-The-Air broadcast to update over 145,000 active connected vehicles simultaneously.
