import json

from models.state import RescueState
from prompts.emergency_prompt import EMERGENCY_PROMPT
from tools.llm import llm


def emergency_assessment_agent(state: RescueState) -> RescueState:

    message = state.get("emergency_message", "")

    prompt = f"""
{EMERGENCY_PROMPT}

Emergency Message:
{message}
"""

    response = llm.invoke(prompt)

    print("===== AI RESPONSE =====")
    print(response.content)
    print("=======================")

    try:
        cleaned_response = response.content.replace("```json", "").replace("```", "").strip()

        result = json.loads(cleaned_response)
       
        state["priority"] = result.get("priority", "Medium")
        state["priority_reason"] = result.get(
    "reason",
    "AI could not determine priority."
)
        
    except Exception as e:
        print("Emergency Assessment Error:", e)
   
        state["priority"] = "Medium"
        state["priority_reason"] = "AI response could not be parsed."

    return state