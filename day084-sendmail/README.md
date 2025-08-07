# 📧 day84-sendmail

## 📋 アプリケーション名
**Pythonメール送信ツール**

## 🎯 アプリケーション概要
PythonからGmailを使ってメールを送信するツールです。SMTP方式とGmail API方式の2つのアプローチを提供し、日本語メールの送信に完全対応しています。OAuth2認証による安全な認証と、環境変数を使った設定管理で、実用的なメール送信システムを構築できます。

## 📁 ファイル構成
```
day84-sendmail/
├── main.py                    # SMTP方式（アプリパスワード）
├── send_gmail.py             # Gmail API方式（OAuth2）
├── README.md                 # このファイル
├── .env                      # 環境変数（要作成、機密情報）
├── client_secret.json        # Google Cloud認証情報（要取得）
├── token.json               # OAuth2トークン（実行時自動作成）
└── .gitignore               # 機密ファイル除外設定
```

## 🔧 必要な準備

### 📦 **ライブラリのインストール**
```bash
# 必要パッケージのインストール
pip install python-dotenv
pip install google-auth google-auth-oauthlib google-auth-httplib2
pip install google-api-python-client
```

### 🔑 **SMTP方式の準備（main.py）**
```bash
# 1. .envファイル作成
touch .env

# 2. 環境変数設定
echo "GMAIL_ADDRESS=your_email@gmail.com" >> .env
echo "GMAIL_APP_PASSWORD=your_16_character_app_password" >> .env
```

**Gmailアプリパスワードの取得**:
1. [Google Account](https://myaccount.google.com/) にアクセス
2. 「セキュリティ」→「2段階認証プロセス」
3. 「アプリパスワード」→「メール」を選択
4. 16文字のパスワードを`.env`に設定

### 🌐 **Gmail API方式の準備（send_gmail.py）**
1. [Google Cloud Console](https://console.cloud.google.com/) でプロジェクト作成
2. Gmail API を有効化
3. OAuth 2.0 認証情報を作成
4. `client_secret.json` をダウンロード
5. プロジェクトフォルダに配置

## 🚀 実行方法

### 📧 **SMTP方式（シンプル）**
```bash
# プロジェクトディレクトリに移動
cd day84-sendmail

# SMTP方式で実行
python main.py

# 実行例
送信先メールアドレスを入力してください: recipient@example.com
📡 メールサーバに接続中...
✅ メール送信完了！
```

### 🚀 **Gmail API方式（高機能）**
```bash
# Gmail API方式で実行
python send_gmail.py

# 実行例
📧 送信元メールアドレス（通常自分のGmail）: sender@gmail.com
📨 宛先メールアドレス: recipient@example.com
📝 件名: テストメールです
✏️ 本文: 文字化けせず届きますか？
✅ メール送信成功! メッセージID: 1983139ee4dbcc40
```

## 💻 使い方

### 📝 **基本的なメール送信（SMTP）**
```python
from main import send_email

# シンプル送信
send_email("件名", "本文", "recipient@example.com")
```

### 🎯 **Gmail API経由での送信**
```python
from send_gmail import gmail_authenticate, send_email

# Gmail API使用
service = gmail_authenticate()
send_email(service, "sender@gmail.com", "recipient@example.com", 
          "件名", "本文")
```

### 🔧 **プログラムからの呼び出し例**
```python
# SMTP方式
import os
from dotenv import load_dotenv
from main import send_email

load_dotenv()

# 環境変数から送信者情報を取得
sender = os.getenv("GMAIL_ADDRESS")
password = os.getenv("GMAIL_APP_PASSWORD")

# メール送信
send_email("重要なお知らせ", "システムが正常に動作しています", "admin@company.com")
```

## ⚖️ **2つのアプローチの比較**

### 🥇 **Gmail API方式（推奨）**
| 項目 | 詳細 |
|------|------|
| **認証** | OAuth2（最高レベルのセキュリティ） |
| **設定** | Google Cloud Console |
| **日本語** | 完全対応、文字化けなし |
| **機能** | 豊富（送信、受信、検索、管理） |
| **制限** | 1日100万件（無料枠） |
| **メリット** | 安全、高機能、文字化け対応 |

### 🥈 **SMTP方式**
| 項目 | 詳細 |
|------|------|
| **認証** | アプリパスワード |
| **設定** | .envファイルのみ |
| **日本語** | 基本対応 |
| **機能** | 送信専用 |
| **制限** | 1日500件 |
| **メリット** | 設定簡単、軽量 |

## 🛠️ 機能

### ✅ **共通機能**
- **日本語メール対応**: UTF-8エンコーディング
- **セキュアな認証**: パスワード・トークン管理
- **エラーハンドリング**: 詳細なエラーメッセージ
- **環境変数管理**: 機密情報の安全な管理

### ✅ **Gmail API限定機能**
- **トークン自動管理**: 初回認証後は自動更新
- **高送信制限**: 大量送信対応
- **完全な文字化け対策**: 日本語・絵文字完全対応

### ✅ **実行時の詳細情報**
```bash
# SMTP実行例
📡 メールサーバに接続中...
✅ メール送信完了！

# Gmail API実行例
🔄 保存済みトークンを使用します
📤 メール送信中...
   📧 From: sender@gmail.com
   📨 To: recipient@example.com
   📝 Subject: テストメール
✅ メール送信成功!
📋 メッセージID: 1983139ee4dbcc40
```

## 📊 使用例

### 🔔 **システム通知**
```python
# サーバー監視システム
def send_alert(error_message):
    subject = f"🚨 システムアラート - {datetime.now().strftime('%Y/%m/%d %H:%M')}"
    body = f"""
システムエラーが発生しました。

エラー内容:
{error_message}

確認をお願いします。

-- 自動監視システム
"""
    send_email(subject, body, "admin@company.com")
```

### 📈 **日次レポート**
```python
# 業務レポート自動送信
def send_daily_report():
    subject = f"📊 日次レポート - {date.today()}"
    body = f"""
本日の業績をお知らせします。

売上: ¥1,234,567
訪問者数: 5,678人
新規登録: 123人

詳細は添付ファイルをご確認ください。
"""
    send_email(subject, body, "manager@company.com")
```

### 🎂 **自動リマインダー**
```python
# 誕生日通知システム
def birthday_reminder(name, birthday):
    subject = f"🎉 {name}さんの誕生日です！"
    body = f"""
{name}さん、お誕生日おめでとうございます！🎂

今日という特別な日が、素晴らしい一年の始まりとなりますように。

チーム一同より
"""
    send_email(subject, body, f"{name}@company.com")
```

## ⚠️ 注意事項

### 🔐 **セキュリティ関連**
- **`.env`ファイル**: Gitに含めない（.gitignoreに追加）
- **client_secret.json**: 機密ファイル（公開禁止）
- **アプリパスワード**: 定期的な再生成推奨
- **OAuth2トークン**: 自動管理（token.json）

### 📧 **メール送信関連**
- **送信制限**: Gmail の1日あたりの送信制限を遵守
- **スパム対策**: 大量送信時は間隔を空ける
- **文字エンコーディング**: 日本語はUTF-8で送信

### 🔧 **技術的制約**
- **Gmail専用**: 現在のコードはGmail特化
- **インターネット必須**: オフラインでは動作不可
- **2段階認証**: Gmail側で有効化が必要

## 🐛 トラブルシューティング

### ❌ **アプリパスワードエラー**
```
534, b'5.7.9 Application-specific password required'
```
**解決方法**:
1. Gmail で2段階認証を有効化
2. アプリパスワードを正しく設定
3. `.env`ファイルの内容を確認

### ❌ **OAuth2認証エラー**
```
invalid_client: The OAuth client was not found
```
**解決方法**:
1. `client_secret.json`ファイルの確認
2. Google Cloud Console でAPI有効化確認
3. 認証情報の再ダウンロード

### ❌ **文字化け問題**
```
件名や本文が正しく表示されない
```
**解決方法**:
- Gmail API方式を使用（完全対応）
- UTF-8エンコーディングを明示的に指定

## 🚀 今後の改善案・拡張アイデア

### 🔥 **優先度高**
- [ ] **📎 添付ファイル機能**
  ```python
  def send_email_with_attachment(subject, body, to_email, attachment_path):
      # ファイル添付機能の実装
      with open(attachment_path, 'rb') as f:
          message.add_attachment(f.read(), filename=os.path.basename(attachment_path))
  ```

- [ ] **📁 複数宛先への一斉送信**
  ```python
  def batch_send_email(subject, body, recipient_list):
      # 複数宛先への効率的な一括送信
      for recipient in recipient_list:
          send_email(subject, body, recipient)
          time.sleep(1)  # API制限対策
  ```

### 🌟 **優先度中**
- [ ] **🔁 テンプレートからメール本文を生成**
  ```python
  def send_template_email(template_name, variables, to_email):
      # Jinjaテンプレートエンジンでメール生成
      template = Template(load_template(template_name))
      body = template.render(**variables)
      send_email("通知", body, to_email)
  ```

- [ ] **🕒 予約送信機能**
  ```python
  def schedule_email(subject, body, to_email, send_time):
      # cronやTaskSchedulerとの連携で時間指定送信
      # または、Pythonのschedulerライブラリ使用
      scheduler.add_job(send_email, trigger='date', run_date=send_time,
                       args=[subject, body, to_email])
  ```

### 💡 **優先度低（発展）**
- [ ] **🔐 トークン保存や自動更新の仕組み強化**
  ```python
  class TokenManager:
      def __init__(self):
          self.token_file = 'secure_token.json'
      
      def encrypt_token(self, token_data):
          # トークンの暗号化保存
          pass
      
      def auto_refresh(self):
          # バックグラウンドでの自動更新
          pass
  ```

- [ ] **📊 送信履歴の管理**
  ```python
  def log_email_history(sender, recipient, subject, status):
      # SQLiteやCSVでの送信ログ管理
      pass
  ```

- [ ] **🎨 HTMLメール対応**
  ```python
  def send_html_email(subject, html_body, to_email):
      # リッチテキストメールの送信
      message.add_alternative(html_body, subtype='html')
  ```

- [ ] **🌐 他メールプロバイダー対応**
  ```python
  # Outlook, Yahoo Mail等への拡張
  class EmailProvider:
      def __init__(self, provider_type):
          self.configure_smtp(provider_type)
  ```

### 🔧 **技術的改善**
- [ ] **設定ファイル**: YAML/JSONによる設定外部化
- [ ] **ロギング**: 詳細な実行ログとデバッグ情報
- [ ] **GUI化**: tkinter/PyQtでのグラフィカルインターフェース
- [ ] **Webアプリ化**: Flask/FastAPIでブラウザ対応
- [ ] **Docker化**: コンテナでの簡単デプロイ

## 📖 学んだことや今後の改善案（学習ログ）

### ✅ **学んだこと**

#### 📧 **メール送信プロトコル**
- **SMTP基礎**: メール送信の標準プロトコル
- **TLS暗号化**: `starttls()`による通信の安全化
- **認証方式**: アプリパスワード vs OAuth2の違い
- **MIMEメッセージ**: メール構造の理解（ヘッダー、本文）

#### 🔐 **認証とセキュリティ**
- **OAuth2フロー**: 現代的な認証方式の実装
- **環境変数管理**: `python-dotenv`による機密情報管理
- **トークン管理**: アクセストークンの保存・更新仕組み
- **Googleアプリパスワード**: 2段階認証時の専用認証

#### 🌐 **API連携**
- **Google Gmail API**: RESTfulAPIの実践的利用
- **認証フロー**: `google-auth`ライブラリの活用
- **エラーハンドリング**: APIエラーの適切な処理
- **レート制限**: API使用量の管理

#### 🛠️ **Python標準ライブラリ**
- **smtplib**: SMTP通信の基礎
- **email.mime**: メールメッセージの構造化
- **base64エンコーディング**: バイナリデータの文字列変換
- **os.getenv()**: 環境変数の安全な取得

#### 🔧 **プロジェクト構成**
- **複数アプローチ**: 1つの問題に対する複数の解決策
- **設定ファイル分離**: コードと設定の分離原則
- **エラーハンドリング**: ユーザーフレンドリーなエラー表示

### 🎯 **技術的な発見**

#### 💡 **Gmail API vs SMTP の使い分け**
```python
# SMTP: シンプルな送信専用
# Gmail API: 高機能・高セキュリティ・文字化け完全対応

# 選択基準:
# - 単発送信 → SMTP
# - 大量送信・日本語重視 → Gmail API
# - 高セキュリティ要求 → Gmail API
```

#### 🔍 **文字エンコーディングの重要性**
```python
# 日本語メールの文字化け対策
# UTF-8エンコーディング + 適切なMIME設定が重要
message = EmailMessage()  # Gmail APIは自動処理
msg.attach(MIMEText(body, "plain", "utf-8"))  # SMTP手動指定
```

### 📚 **参考になったリソース**
- [Gmail API Documentation](https://developers.google.com/gmail/api)
- [Python smtplib Documentation](https://docs.python.org/3/library/smtplib.html)
- [Google OAuth2 Flow](https://developers.google.com/identity/protocols/oauth2)
- [Email Security Best Practices](https://support.google.com/mail/answer/7126229)

### 🏆 **プロジェクト成果**
- **コード行数**: 約120行（2つのアプローチ）
- **実装時間**: 約3-4時間
- **対応機能**: SMTP・Gmail API両方式
- **文字化け対策**: 完全対応
- **セキュリティ**: OAuth2・環境変数管理

### 🎯 **実用性の評価**
- ✅ **即座に使える**: 設定すれば実用レベル
- ✅ **拡張しやすい**: モジュール化された構造
- ✅ **学習効果高**: 複数の重要技術を習得
- ✅ **応用範囲広**: 業務自動化に直結

---
**🎉 プロジェクト完成日**: 2025年7月21日  
**⚡ 実装時間**: 約3-4時間  
**🛠️ 使用技術**: Python, Gmail API, SMTP, OAuth2, python-dotenv