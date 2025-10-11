from googleapiclient.discovery import build
from auth import get_authenticated_service
import json
import time

def import_subscriptions():
    creds = get_authenticated_service()
    youtube = build("youtube", "v3", credentials=creds)

    subs = json.load(open("subscriptions.json", encoding="utf-8"))
    total = len(subs)
    print(f"📥 {total} 件のチャンネルを新アカウントに登録します...")

    for i, sub in enumerate(subs, start=1):
        ch_id = sub["id"]
        title = sub["title"]

        try:
            youtube.subscriptions().insert(
                part="snippet",
                body={
                    "snippet": {
                        "resourceId": {
                            "kind": "youtube#channel",
                            "channelId": ch_id
                        }
                    }
                }
            ).execute()
            print(f"[{i}/{total}] ✅ 登録完了: {title}")
            time.sleep(1)  # スパム防止: 1秒間隔
        except Exception as e:
            print(f"[{i}/{total}] ⚠️ 登録失敗: {title} ({e})")
            time.sleep(2)

    print("\n🎉 全チャンネルの登録処理が完了しました。")

if __name__ == "__main__":
    import_subscriptions()

