from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define the required scopes
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    creds = None

    # Load previously saved credentials (if they exist)
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If no valid credentials available, start login flow
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # 🔥 Add this line exactly here:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)  # <-- 🔥 FIXED PORT

        # Save the new credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Connect to Gmail API
    service = build('gmail', 'v1', credentials=creds)

    # Fetch and display latest email subjects
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])

    if not messages:
        print("📭 No messages found.")
    else:
        print("📥 Latest 5 Email Subjects:\n")
        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id'], format='metadata', metadataHeaders=['Subject']).execute()
            headers = msg_data['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
            print("•", subject)

if __name__ == '__main__':
    main()
