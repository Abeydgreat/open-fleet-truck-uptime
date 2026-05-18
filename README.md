# Open Fleet Truck Uptime (OFTU) 🚛 Engine v1.0.0

[![License: MIT](https://shields.io)](https://opensource.org)
[![Build Status](https://shields.io)]()
[![Uptime Target](https://shields.io)]()

OFTU is an open-source, data-driven fleet management system and financial modeling engine. It is specifically engineered to maximize the operational uptime of commercial heavy vehicles (18-wheeled configurations) to 98.7% over a 10-year compounding cycle.

## 🚀 Core Architectural Pillars

*   **`/predictive-maintenance`**: Real-time telemetry ingestion algorithms mapping J1939 CAN bus data to an automated 80% component wear-threshold warning matrix.
*   **`/financial-models`**: Dynamic algorithmic equations calculating variable Cost-Per-Kilometre (CPK) metrics, inflation adjustments, and automated fleet growth intervals.
*   **`/driver-telematics`**: A gamified, dual-driver hours logging system designed to optimize vehicle utilization while protecting operator wellness.

## 📁 Repository Structure

```text
open-fleet-truck-uptime/
├── .github/
│   ├── workflows/             # GitHub Actions automation scripts
│   └── ISSUE_TEMPLATE/        # Bug and telemetry failure forms
├── driver-telematics/         # Hours logging and driver performance code
├── financial-models/          # CPK calculator and fleet scaling scripts
└── predictive-maintenance/    # J1939 CAN bus JSON schemas and IoT processing
```

## 📦 Quick Start Deployment (Local Simulation)

### Prerequisites
* Python 3.10+
* Docker (for telemetry database containerization)

### Installation
```bash
git clone github.com
cd open-fleet-truck-uptime
pip install -r requirements.txt
```

### Run the CPK Financial Model
```bash
python financial-models/cpk_calculator.py --purchase_price 500000 --currency ZAR --inflation 0.035
```

## 📈 Monetization & Enterprise Extensions
Commercial operators requiring custom SAP/Oracle ERP hooks or specialized local infrastructure configurations can access our **Enterprise Support Layer** via GitHub Sponsors or contact `abiodunimoukhedeme@gmail.com`.
