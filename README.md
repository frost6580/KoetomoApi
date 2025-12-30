# KoetomoApi

KoetomoApiは、声ともの内部APIにアクセスするPythonクラスです。
ユーザー認証、フィード投稿、コメント、いいね、フォロー、通話などの操作をサポートします。

## 必要モジュール

- config : APIエンドポイントやアプリ情報を設定
- requests : HTTPリクエスト用
- uuid : デバイスUID生成用

## クラス: Koetomo

### 初期化
koe = Koetomo()
- requests.Sessionを初期化し、共通ヘッダーを設定
- 認証トークンやユーザーIDはlogin後にセット

### login(email, passwd)
- メールアドレスとパスワードでログイン
- 成功するとtokenとuseridがセットされ、post_arrival()が呼ばれる
- 戻り値: JSON

### post_arrival()
- ログイン後に到着通知をサーバーに送信
- 戻り値: なし

### get_feed(count=50)
- フィードを取得
- 戻り値: JSON

### post_feed(text)
- フィードを投稿
- 戻り値: JSON

### delete_feed(id)
- 指定IDのフィードを削除
- 戻り値: JSON

### post_comment(id, text)
- フィードにコメント投稿

### post_like(id)
- フィードに「いいね」を送信

### can_send(id)
- 指定ユーザーにメッセージ送信可能か確認
- 戻り値: JSON

### post_follow(id)
- ユーザーをフォロー

### post_call(id)
- Skyway通話をリクエスト

### post_messages(id)
- 指定ユーザーにテキストメッセージを送信
- 内容は "テスト" に固定
