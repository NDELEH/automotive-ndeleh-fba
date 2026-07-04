# 🚗 Automotive Ndeleh-FBA Network

An open-source, edge-to-cloud diagnostic engine that uses the **Ndeleh Fishbone Algorithm (Ndeleh-FBA)** to trace vehicle system anomalies back to their root causes before a warning light ever turns on. 

This system monitors fuel delivery, electrical infrastructure, and EV battery systems to extract the core **Causal Spine** of a vehicle failure.

---

## 🛠️ System Architecture

1. **Edge Telematics (`edge_telematics/`)**: Lightweight scripts running inside the vehicle's onboard computer to read the CAN-bus and stream active vehicle data packages.
2. **Central Cloud Hub (`cloud_aggregator/`)**: A native HTTP telemetry gateway that collects data packets from millions of active vehicles and exposes a real-time data API.
3. **Predictive UI (`dashboard_ui/`)**: A dynamic web interface running an inline browser-based Ndeleh inference engine to visually map out upcoming failures and secondary microspines.
4. **Automated Deployment (`.github/workflows/`)**: A continuous integration pipeline that handles Over-The-Air (OTA) updates to push new diagnostic logic to the active fleet.

---

## 📁 Repository Structure

```text
automotive-ndeleh-fba/
├── .github/workflows/
│   └── deploy-edge.yml        # Fleet-wide OTA update pipeline
├── cloud_aggregator/
│   └── telemetry_server.py    # Multi-vehicle API server & data hub
├── edge_telematics/
│   ├── obd_streamer.py        # Live CAN-bus broadcast simulator
│   └── local_reasoner.py      # Local Ndeleh Spine Extraction engine
├── dashboard_ui/
│   └── index.html             # Dynamic fleet management dashboard (Live UI)
└── requirements.txt           # Environment dependencies
```

---

## 🎬 How to Run the Full Live Play Loop

To watch the live network communicate, process metrics, and extract causal graphs in real time, run the modules locally on your machine following these steps:

### 1. Download the Project
* Click the green **`<> Code`** button at the top right of this repository.
* Click **Download ZIP** and extract the files to your computer.

### 2. Boot up the Telemetry Server Hub
Open your terminal or command prompt inside the project folder and run the central aggregator:
```bash
python cloud_aggregator/telemetry_server.py
```
*This launches the API gateway on port 8080 to route data between vehicles and the interface.*

### 3. Start the In-Vehicle Sensor Streamer
Open a **second, separate terminal window** in the same project folder and run the vehicle transmitter:
```bash
python edge_telematics/obd_streamer.py
```
*The vehicle will immediately begin packaging and broadcasting real-time fuel, EV battery, and voltage logs to the server.*

### 4. Launch the Predictive Interface
* Open your computer's file explorer, navigate to the `dashboard_ui/` folder, and double-click `index.html`.
* The dashboard will open instantly in your web browser.

---

## 🦴 Live Diagnostic Behavior

Once running, the web browser panel queries the telemetry hub every 2000ms:
* **🟢 NOMINAL**: The vehicle systems are running safely within balanced thresholds.
* **🟡 WARNING / 🔴 CRITICAL**: The moment the streaming vehicle data introduces voltage dips or fuel line dropouts, the Ndeleh-FBA engine instantly isolates the mathematical **Causal Spine**, telling the user exactly *why* a failure is looming before a driver gets stranded.

---

## 🛰️ Fleet Deployment via GitHub Actions
Every time you push code updates to the `main` branch, the included GitHub Workflow (`deploy-edge.yml`) automatically executes. It packages your code into an optimized vehicle layout and simulates a live cellular Over-The-Air broadcast update across the entire connected vehicle fleet.
