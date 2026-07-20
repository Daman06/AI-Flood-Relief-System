from models.state import RescueState
from geopy.distance import geodesic
from database.connection import volunteers_collection


def resource_allocation_agent(state: RescueState):

    print("===== RESOURCE ALLOCATION =====")
    print("Searching for location:", state["location"])

    all_volunteers = list(volunteers_collection.find())
    print("Volunteers in DB:")
    for v in all_volunteers:
        print(v)

    print("==============================")

    available_volunteers = list(
        volunteers_collection.find({"available": True})
    )

    volunteer = None
    nearest_distance = float("inf")

    for v in available_volunteers:

        volunteer_location = (
            v["latitude"],
            v["longitude"]
        )

        user_location = (
            state["latitude"],
            state["longitude"]
        )

        distance = geodesic(user_location, volunteer_location).km

        print(f'{v["name"]} is {distance:.2f} km away')

        if distance < nearest_distance:
            nearest_distance = distance
            volunteer = v

    if volunteer:

        state["assigned_volunteer"] = volunteer["name"]
       
        state["mission_status"] = "Assigned"

        volunteers_collection.update_one(
            {"_id": volunteer["_id"]},
            {
                "$set": {
                    "available": False
                }
            }
        )

    else:

        state["assigned_volunteer"] = None
        
        state["mission_status"] = "No Volunteer Available"

    return state