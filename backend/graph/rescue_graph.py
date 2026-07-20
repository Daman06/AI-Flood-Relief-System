from langgraph.graph import StateGraph, START, END
from agents.resource_allocation import resource_allocation_agent
from agents.save_rescue_request import save_rescue_request_agent
from models.state import RescueState
from agents.flood_verification import flood_verification_agent
from agents.emergency_assessment import emergency_assessment_agent

def route_after_verification(state: RescueState):
    if state.get("flood_verified", False):
        return "verified"
    return "not_verified"

# Create the graph
builder = StateGraph(RescueState)

# Add nodes
builder.add_node(
    "resource_allocation",
    resource_allocation_agent
)
builder.add_node(
    "save_rescue_request",
    save_rescue_request_agent
)
builder.add_node("flood_verification", flood_verification_agent)
builder.add_node("emergency_assessment", emergency_assessment_agent)

# Connect the nodes
builder.add_edge(START, "flood_verification")
builder.add_conditional_edges(
    "flood_verification",
    route_after_verification,
    {
        "verified": "emergency_assessment",
        "not_verified": END,
    },
)
builder.add_edge("emergency_assessment", "resource_allocation")
builder.add_edge("resource_allocation", "save_rescue_request")
builder.add_edge("save_rescue_request", END)

# Compile the graph
graph = builder.compile()