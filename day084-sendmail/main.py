import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()  # .env から環境変数を読み込む

def send_email(subject, body, to_email):
    # 環境変数から設定を取得
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = os.getenv("GMAIL_ADDRESS")
    app_password = os.getenv("GMAIL_APP_PASSWORD")

    if not sender_email or not app_password:
        print("❌ 環境変数 GMAIL_ADDRESS または GMAIL_APP_PASSWORD が未設定です")
        return

    # メール本文の構築
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    try:
        print("📡 メールサーバに接続中...")
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # TLSによる暗号化
            server.login(sender_email, app_password)
            server.send_message(msg)
            print("✅ メール送信完了！")
    except Exception as e:
        print(f"❌ メール送信エラー: {e}")

if __name__ == "__main__":
    subject = "テストメール"
    body = "こんにちは！これはPythonから送ったメールです。"
    to_email = input("送信先メールアドレスを入力してください: ").strip()
    send_email(subject, body, to_email)
