from ollama_client import ask_ollama
from tools import check_slot_available, create_calendar_event
from datetime import datetime
import json

conversation_history = []

with open("business_info.txt", "r", encoding="utf-8", errors="ignore") as f:
    business_info = f.read()


def detect_intent(message):

    prompt = f"""
Classify the user's intent.

User message:
{message}

Return ONLY JSON like this:

{{
 "intent": "book | services | question | general"
}}
"""

    response = ask_ollama(prompt)

    try:
        data = json.loads(response)
        return data.get("intent", "general")
    except:
        return "general"


def extract_booking_details(message, now):

    prompt = f"""
Current date and time: {now}

Extract booking details from this message.

User message:
{message}

Return ONLY JSON.

Example:
{{
 "service": "haircut",
 "time": "2026-03-10T15:00:00"
}}
"""

    response = ask_ollama(prompt)

    try:
        return json.loads(response)
    except:
        return {}


def process_message(message: str):

    now = datetime.now().strftime("%A, %d %B %Y %I:%M %p")

    intent = detect_intent(message)

    # SERVICES QUESTIONS
    if intent == "services":

        prompt = f"""
You are a friendly salon receptionist.

Business information:
{business_info}

User question:
{message}

Answer clearly and naturally.
"""

        return ask_ollama(prompt)

    # BOOKING REQUEST
    if intent == "book":

        details = extract_booking_details(message, now)

        service = details.get("service")
        time_value = details.get("time")

        if not service:
            return "Sure! What service would you like to book?"

        if not time_value:
            return "What date and time would you prefer?"

        try:
            event_time = datetime.fromisoformat(time_value)
        except:
            return "I couldn't understand the time. Could you repeat it?"

        if not check_slot_available(service, event_time):
            return "That slot is already booked. Please choose another time."

        return create_calendar_event(
            f"{service} appointment",
            event_time
        )

    # GENERAL CONVERSATION
    conversation_history.append(f"User: {message}")

    history_text = "\n".join(conversation_history[-4:])

    prompt = f"""
You are a friendly salon receptionist.

Business information:
{business_info}

Conversation:
{history_text}

Respond naturally like a real receptionist.

IMPORTANT RULES:
• Keep responses SHORT (1–2 sentences).
• Do NOT explain everything.
• Ask one question at a time.
• Be conversational.
"""

    response = ask_ollama(prompt)

    conversation_history.append(f"AI: {response}")

    if len(conversation_history) > 10:
        conversation_history.pop(0)

    return response