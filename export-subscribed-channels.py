from googleapiclient.discovery import build
from auth import get_authenticated_service
import json

def export_subscriptions():
    creds = get_authenticated_service()
    youtube = build("youtube", "v3", credentials=creds)

    subs = []
    next_page_token = None

    print("📦 登録チャンネルを取得中...")

    while True:
        res = youtube.subscriptions().list(
            part="snippet",
            mine=True,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in res.get("items", []):
            ch_id = item["snippet"]["resourceId"]["channelId"]
            title = item["snippet"]["title"]
            subs.append({"id": ch_id, "title": title})
            print(f"✅ {title}")

        next_page_token = res.get("nextPageToken")
        if not next_page_token:
            break

    with open("subscriptions.json", "w", encoding="utf-8") as f:
        json.dump(subs, f, indent=2, ensure_ascii=False)

    print(f"\n💾 {len(subs)} 件の購読チャンネルを 'subscriptions.json' に保存しました。")

if __name__ == "__main__":
    export_subscriptions()

