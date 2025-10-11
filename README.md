# このリポジトリは何？

YouTubeの登録チャンネルを旧カウントから新アカウントへ移行するためのスクリプト

#  事前準備

* [Google Cloud Console](https://console.cloud.google.com/apis/credentials) でプロジェクトを作成
* APIとサービス → 有効なAPIとサービス → ライブラリ」で **YouTube Data API v3** を有効化
* 認証情報 → 認証情報を作成 → OAuthクライアントID」
   * アプリケーションの種類：「デスクトップアプリ」
* 生成された **`credentials.json`** をDownload


# 手順

```bash
$ git clone https://github.com/masaharu-suizu/Import-YouTube-subscribed-channels.git 

$ cd Import-YouTube-subscribed-channels

$ uv sync 

$ cp /{path to}/credentiols.json ./

## 古いgoogleアカウントで認証
$ uv run auth.py 
🌐 新規OAuth認証を開始します...
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=***
✅ token.json に保存しました。

🎉 OAuth認証が完了しました！token.jsonを確認してください。

$ uv run export-subscribed-channels.py 
📦 登録チャンネルを取得中...
✅ ***
✅ ***
✅ ***

💾 x 件の購読チャンネルを 'subscriptions.json' に保存しました。

$ rm -i token.json 

## 新しいgoogleアカウントで認証
$ uv run auth.py 
🌐 新規OAuth認証を開始します...
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=***
✅ token.json に保存しました。

🎉 OAuth認証が完了しました！token.jsonを確認してください。

$ uv run import-subscribed-channels.py
📥 x 件のチャンネルを新アカウントに登録します...
[1/x] ✅ 登録完了: ***
[2/x] ✅ 登録完了: ***
[3/x] ✅ 登録完了: ***

🎉 全チャンネルの登録処理が完了しました。
```










