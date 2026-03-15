from datetime import datetime, timedelta
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

import os

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def check_slot_available(service, event_time, calendar_service):

    end_time = event_time + timedelta(minutes=30)

    events = calendar_service.events().list(
        calendarId='primary',
        timeMin=event_time.isoformat() + 'Z',
        timeMax=end_time.isoformat() + 'Z',
        singleEvents=True
    ).execute()

    return len(events.get("items", [])) == 0

def create_calendar_event(summary, start_time):

    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)

    end_time = start_time + timedelta(minutes=30)

    event = {
        "summary": summary,
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "Asia/Kolkata"
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "Asia/Kolkata"
        }
    }

    event = service.events().insert(
        calendarId="primary",
        body=event
    ).execute()

    return "Appointment successfully booked in Google Calendar!"