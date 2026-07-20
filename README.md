# 🌊 Flood Relief AI

An AI-powered disaster response system that helps people during floods by providing early flood alerts, verifying rescue requests using AI, prioritizing emergencies, and assigning the nearest available volunteer.

## 🚀 Features

### 👤 User Module
- 📍 Automatic GPS location detection
- 🌧️ AI-powered early flood alerts
- 🚨 Submit rescue requests
- 🧠 AI-based flood verification
- ⚡ AI-based emergency priority detection

### 🚑 Volunteer Module
- View incoming rescue requests
- Accept rescue missions
- Dashboard statistics
- Real-time mission status updates

### 🤖 AI Agents
- Flood Alert Agent
- Flood Verification Agent
- Emergency Assessment Agent
- Resource Allocation Agent

---

## 🛠️ Tech Stack

### Frontend
- React
- Vite
- React Router
- Axios

### Backend
- FastAPI
- Python

### Database
- MongoDB Atlas

### AI
- LangGraph
- LLM-based AI Agents

### APIs
- Open-Meteo Weather API
- OpenStreetMap Nominatim API

---

## 📂 Project Structure

```
FloodRelief/
│
├── backend/
│   ├── agents/
│   ├── database/
│   ├── graph/
│   ├── models/
│   ├── services/
│   ├── tools/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

### Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

Backend runs on:

```
https://ai-flood-relief-system.onrender.com
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## 🧠 Workflow

```
User
   │
   ▼
Location Detection
   │
   ▼
Early Flood Alert
   │
   ▼
Rescue Request
   │
   ▼
Flood Verification AI
   │
   ▼
Emergency Assessment AI
   │
   ▼
Resource Allocation AI
   │
   ▼
MongoDB
   │
   ▼
Volunteer Dashboard
```




## 🌟 Future Improvements

- User Authentication
- Volunteer Authentication
- Live Google Maps Tracking
- Push Notifications
- SMS Alerts
- Real-time ETA using Maps API
- Admin Dashboard
- Mobile Application

---

## 👩‍💻 Author

**Damanpreet Kaur**

B.Tech Computer Science Engineering

---

## 📜 License

This project is developed for educational purposes and hackathon demonstrations.
