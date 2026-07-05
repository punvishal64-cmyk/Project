import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]

creds = Credentials.from_service_account_file(
    "credentials/service-account.json",
    scopes=SCOPES,
)

client = gspread.authorize(creds)

sheet = client.open_by_key("1tk4f8yKf3ueR3YaX2XYmy0V6BbUjZtrm-vtrGniaZrU").sheet1


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