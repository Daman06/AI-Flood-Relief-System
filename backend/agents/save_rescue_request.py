from datetime import datetime

from database.connection import rescue_requests_collection
from models.state import RescueState


def save_rescue_request_agent(state: RescueState) -> RescueState:

    rescue_request = {
        "victim_name": state["victim_name"],
        "phone_number": state["phone_number"],
        "location": state["location"],
        "emergency_message": state["emergency_message"],
        "flood_verified": state["flood_verified"],
        "priority": state["priority"],
        "priority_reason": state["priority_reason"],
        "assigned_volunteer": state["assigned_volunteer"],
        "mission_status": state["mission_status"],
        "created_at": datetime.utcnow()
    }

    rescue_requests_collection.insert_one(rescue_request)

    print("✅ Rescue request saved to MongoDB.")

    return state