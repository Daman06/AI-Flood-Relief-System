from typing import TypedDict, Optional


class RescueState(TypedDict):
    """
    Shared state used by all LangGraph agents.
    """

    # Victim Information
    victim_name: Optional[str]
    phone_number: Optional[str]
    location: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    emergency_message: Optional[str]

    # Flood Verification
    flood_verified: Optional[bool]

    # Emergency Assessment
    priority: Optional[str]
    priority_reason:Optional[str]
    # Volunteer Assignment
    assigned_volunteer: Optional[str]
  
    volunteer_status: Optional[str]

    # Mission Tracking
    mission_status: Optional[str]
    risk_level: Optional[str]
    verification_reason: Optional[str]