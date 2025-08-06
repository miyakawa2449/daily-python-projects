# Day 99: ログイン認証付きアプリ - Flask-Login + セッション管理

Flask-Loginを使用したユーザー認証システムのサンプルアプリケーションです。

## 機能

- ユーザー登録（ユーザー名、メールアドレス、パスワード）
- ログイン/ログアウト機能
- セッション管理（Remember Me機能付き）
- パスワードのハッシュ化（Werkzeug使用）
- ログイン必須ページの保護
- フラッシュメッセージによるフィードバック

## セットアップ

1. 仮想環境をアクティベート:
```bash
conda activate daily-python
```

2. プロジェクトディレクトリに移動:
```bash
cd day99-account-login
```

3. 必要なパッケージをインストール:
```bash
pip install -r requirements.txt
```

## 実行方法

```bash
python app.py
```

ブラウザで `http://localhost:5000` にアクセスしてください。

## 使い方

1. **新規登録**: 
   - トップページの「新規登録」ボタンをクリック
   - ユーザー名、メールアドレス、パスワードを入力
   - 登録完了後、ログインページにリダイレクト

2. **ログイン**:
   - 登録したメールアドレスとパスワードでログイン
   - 「ログイン状態を保持」にチェックを入れると、ブラウザを閉じても一定期間ログイン状態が維持されます

3. **ダッシュボード**:
   - ログイン後にアクセス可能
   - ユーザー情報の確認が可能

4. **プロフィール**:
   - ユーザーの詳細情報を表示
   - 登録日時などを確認可能

5. **ログアウト**:
   - ナビゲーションバーの「ログアウト」をクリック

## 技術仕様

- **Flask**: Webフレームワーク
- **Flask-Login**: ユーザー認証管理
- **Flask-SQLAlchemy**: データベースORM
- **Flask-WTF**: フォーム処理とCSRF保護
- **SQLite**: ユーザーデータの保存
- **Werkzeug**: パスワードのハッシュ化
- **Bootstrap 5**: UIデザイン

## ファイル構成

```
day99-account-login/
├── app.py              # メインアプリケーション
├── requirements.txt    # 依存パッケージ
├── users.db           # SQLiteデータベース（自動生成）
├── templates/         # HTMLテンプレート
│   ├── base.html      # ベーステンプレート
│   ├── index.html     # トップページ
│   ├── register.html  # 登録ページ
│   ├── login.html     # ログインページ
│   ├── dashboard.html # ダッシュボード
│   └── profile.html   # プロフィールページ
└── README.md          # このファイル
```

## セキュリティ機能

- パスワードは`werkzeug.security`を使用してハッシュ化
- CSRF保護（Flask-WTF）
- セッション管理（Flask-Login）
- ログイン必須ページの自動保護（`@login_required`デコレータ）