from __future__ import print_function
import os.path
import json
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

# YouTube Data API のスコープ
SCOPES = ["https://www.googleapis.com/auth/youtube"]

def get_authenticated_service():
    """YouTube Data API用のOAuth認証を行い、認証済みクライアントを返す"""
    creds = None
    token_path = "token.json"
    credentials_path = "credentials.json"

    # トークンが存在すれば読み込み
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    # トークンがない、または期限切れの場合は再認証
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("🔁 トークンをリフレッシュしています...")
            creds.refresh(Request())
        else:
            print("🌐 新規OAuth認証を開始します...")
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)  # ローカルブラウザで認証フロー開始

        # 認証情報を保存
        with open(token_path, "w") as token:
            token.write(creds.to_json())
            print("✅ token.json に保存しました。")

    return creds


if __name__ == "__main__":
    creds = get_authenticated_service()
    print("\n🎉 OAuth認証が完了しました！token.jsonを確認してください。")

