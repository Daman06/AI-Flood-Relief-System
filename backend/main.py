from fastapi.middleware.cors import CORSMiddleware
from database.connection import rescue_requests_collection
from fastapi import FastAPI
from models.state import RescueState
from graph.rescue_graph import graph
from services.weather_service import get_weather
from bson import ObjectId
from database.connection import rescue_requests_collection
from bson import ObjectId
from database.connection import rescue_requests_collection,volunteers_collection
from fastapi import Body
from agents.flood_alert_agent import flood_alert_agent

   

app = FastAPI(title="Flood Relief AI API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Flood Relief AI API is running!"}


@app.post("/rescue")
def create_rescue_request(request: RescueState):

    print("✅ Request reached main.py")
    print("===== REQUEST RECEIVED =====")
    print(request)
    print("============================")
    result = graph.invoke(request)

    return result
@app.get("/requests")
def get_requests():
    requests = list(rescue_requests_collection.find())

    for request in requests:
        request["_id"] = str(request["_id"])

    return requests
@app.put("/accept/{request_id}")
def accept_request(request_id: str, data: dict = Body(...)):

    latitude = data.get("latitude")
    longitude = data.get("longitude")

    rescue_requests_collection.update_one(
        {"_id": ObjectId(request_id)},
        {
            "$set": {
                "mission_status": "In Progress",
                "volunteer_latitude": latitude,
                "volunteer_longitude": longitude,
            }
        },
    )

    return {
        "message": "Mission Accepted"
    }
@app.put("/accept-mission/{request_id}")
def accept_mission(request_id: str):

    rescue_requests_collection.update_one(
        {"_id": ObjectId(request_id)},
        {
            "$set": {
                "mission_status": "In Progress"
            }
        }
    )

    return {
        "message": "Mission Accepted"
    }
@app.get("/dashboard-stats")
def dashboard_stats():

    requests = list(rescue_requests_collection.find())

    total_requests = len(requests)

    high_priority = len(
        [r for r in requests if r.get("priority") == "High"]
    )

    in_progress = len(
        [r for r in requests if r.get("mission_status") == "In Progress"]
    )

    available_volunteers = volunteers_collection.count_documents(
        {"available": True}
    )

    return {
        "total_requests": total_requests,
        "high_priority": high_priority,
        "available_volunteers": available_volunteers,
        "missions_in_progress": in_progress,
    }
@app.get("/flood-alert")
def flood_alert(latitude: float, longitude: float):

    result = flood_alert_agent(latitude, longitude)

    return result