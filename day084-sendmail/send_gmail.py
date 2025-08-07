import os.path
import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# アクセススコープ
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def gmail_authenticate():
    creds = None
    # 保存されているトークンがあれば再利用
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # なければ認証フローを開始
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_838287195545-lo7c5t7it8efta15o4t30h00v2vmskc3.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def create_message(sender, to, subject, body_text):
    message = EmailMessage()
    message.set_content(body_text)
    message['To'] = to
    message['From'] = sender
    message['Subject'] = subject

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_email(service, sender, to, subject, body):
    message = create_message(sender, to, subject, body)
    send_message = service.users().messages().send(userId="me", body=message).execute()
    print(f'✅ メール送信成功! メッセージID: {send_message["id"]}')

if __name__ == '__main__':
    service = gmail_authenticate()
    sender_email = input("📧 送信元メールアドレス（通常自分のGmail）: ")
    recipient_email = input("📨 宛先メールアドレス: ")
    subject = input("📝 件名: ")
    body = input("✏️ 本文: ")
    
    send_email(service, sender_email, recipient_email, subject, body)
