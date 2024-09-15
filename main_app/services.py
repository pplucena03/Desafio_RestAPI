import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]

def create_event(serializer):
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())   

    try:
        service = build("calendar", "v3", credentials=creds)

        event = {
            'summary': serializer['title'],
            'description': serializer['description'],
            'start': {
                'dateTime': f'{serializer['start_date']}T{serializer['start_time']}-03:00',
                'timezone': 'America/Fortaleza',
            },
            'end': {
                'dateTime': f'{serializer['end_date']}T{serializer['end_time']}-03:00',
                'timezone': 'America/Fortaleza',
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
    
    except HttpError as error:
        print(f"Ocorreu um erro: {error}")


def delete_event():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())   

    try:
        service = build("calendar", "v3", credentials=creds)

        service.events().delete(calendarId='primary', eventID='eventID').execute()
    
    except HttpError as error:
        print(f"Ocorreu um erro: {error}")