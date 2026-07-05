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

sheet.append_row([
    "09:00-09:30",
    "DSA",
    "Graphs",
    "Solved graph problems",
    "2026-07-04 17:30:00",
])

print("✅ Row added successfully!")