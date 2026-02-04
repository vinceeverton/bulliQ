# BullIQ 🎯  
**A darts performance, training, and checkout-intelligence platform**

BullIQ is a DartCounter-adjacent system designed to help darts players **win more legs**, not just record scores.

It focuses on:
- personalized checkout routes
- pressure-based practice
- deep but practical stats
- optional one-camera assist scoring

BullIQ does **not** integrate with or modify DartCounter.  
It runs alongside any scoring app or can be used standalone.

—

## 🧠 Core Features

- 🎯 Checkout Intelligence (player-specific routes)
- 🧪 Practice & pressure drills
- 📊 Stats engine (double %, clutch performance)
- 👥 Team / league ready architecture
- 📸 One-camera assist mode (optional)
- 📱 Mobile-first (iOS / Android via Expo)
- 🐳 Dockerized backend

—

## 🧱 Tech Stack

### Backend
- Python 3.11
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker

### Mobile App
- React Native
- Expo
- TypeScript

### Vision (Optional)
- OpenCV
- Single camera (phone or webcam)

—

## 📁 Repository Structure
bulliq/
├── docker-compose.yml
├── README.md
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── database.py
│       ├── models.py
│       ├── routes.py
│       ├── services/
│       └── data/
├── mobile/
│   ├── package.json
│   ├── app.json
│   └── App.tsx
└── vision/
└── detect_darts.py
—

## ✅ Requirements

### Required
- **Docker** (v20+)
- **Docker Compose**
- **Node.js 18+**
- **npm**
- **Python 3.11+** (only if running vision module)

### Recommended
- macOS / Linux / WSL2
- Phone with Expo Go (for mobile testing)
- 1080p camera for assist mode

—

## 🚀 Installation

### 1️⃣ Clone the repo
```bash
git clone https://github.com/yourusername/bulliq.git
cd bulliq

### 2️⃣ Start Backend + Database

  docker-compose up —build
  
This will start:
	•	FastAPI backend → http://localhost:8000
	•	PostgreSQL database → port 5432

You should see:

Uvicorn running on http://0.0.0.0:8000

3️⃣ Install & Run Mobile App

cd mobile
npm install
npx expo start

Options:
	•	Scan QR code with Expo Go (iOS / Android)
	•	Run in iOS Simulator / Android Emulator

4️⃣ (Optional) Run Camera Assist

cd vision
python detect_darts.py

Press q to exit.

This only verifies camera feed in MVP.
Detection logic will be added later.



🎯 How to Use BullIQ (MVP)

Checkout Intelligence
	1.	Open the mobile app
	2.	Tap Get Checkout
	3.	App requests a route from the backend
	4.	Route is based on:
	•	remaining score
	•	stored double hit tendencies
	
	40 → D20
	
As stats improve, routes adapt.



Practice Mode (Manual)
	•	Enter throws manually
	•	Practice doubles
	•	Run pressure drills (via backend logic)

⸻

Assist Mode (Camera)
	•	Camera suggests dart locations
	•	Player confirms score
	•	Prevents false readings
	•	Suitable for practice & leagues

⸻

📸 One-Camera Setup (Recommended)

Camera Placement
	•	Ceiling-mounted behind the oche or
	•	Above the board, slightly off-center
	•	Camera must NOT move after calibration

Minimum Specs
	•	1080p resolution
	•	30 FPS
	•	Fixed focus
	•	Side lighting (avoid glare)

⸻

🧠 Design Philosophy
	•	Manual confirmation beats false automation
	•	Checkout thinking is the real problem
	•	Pressure practice wins matches
	•	Team data is under-served in darts

BullIQ solves these without competing with existing scoring apps.

⸻

🐛 Troubleshooting

Backend not starting
	•	Make sure Docker is running
	•	Check port 8000 is free
	•	Run:
	
	docker-compose down
docker-compose up —build

Mobile app can’t reach API
	•	Use your local IP, not localhost, on real devices
Example:
http://192.168.1.10:8000

Camera not detected
	•	Try a different camera index:
	
	cv2.VideoCapture(1)
	
🔮 Roadmap

Phase 1 (Current)
	•	Manual scoring
	•	Checkout intelligence
	•	Practice engine
	•	Camera feed

Phase 2
	•	Full checkout table (170 → 2)
	•	Dart tip detection
	•	Calibration UI
	•	Offline sync

Phase 3
	•	Team chemistry
	•	League tools
	•	OBS streaming overlays
	•	Hardware buttons / pedals

⸻

📜 License

MIT (recommended — update if needed)

⸻

🎯 Final Notes

BullIQ is designed to:
	•	run locally
	•	scale cleanly
	•	stay legal & league-friendly
	•	complement DartCounter, not replace it

You can start practicing today and grow this into a serious product.

Good darts 🎯	
—
