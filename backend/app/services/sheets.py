import json
import os

import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]

if os.path.exists("credentials/service-account.json"):
    creds = Credentials.from_service_account_file(
        "credentials/service-account.json",
        scopes=SCOPES,
    )
else:
    creds = Credentials.from_service_account_info(
        json.loads(os.getenv("GOOGLE_CREDENTIALS")),
        scopes=SCOPES,
    )

client = gspread.authorize(creds)

sheet = client.open_by_key(
    "1tk4f8yKf3ueR3YaX2XYmy0V6BbUjZtrm-vtrGniaZrU"
).sheet1


def append_activity(
    time_slot: str,
    category: str,
    task: str,
    transcript: str,
    created_at: str,
):
    sheet.append_row(
        [
            time_slot,
            category,
            task,
            transcript,
            created_at,
        ]
    )