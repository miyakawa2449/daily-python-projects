# day98-markdown-blog
## アプリケーション名
Markdown対応ブログシステム - FlaskとMySQLを使用したMarkdownブログエンジン

## アプリケーション概要
Markdownファイルを読み込んで管理できるブログシステムです。記事の作成・編集・削除はもちろん、既存のMarkdownファイルをインポートする機能も搭載しています。

## ファイル構成
```
day98-markdown-blog/
├── app.py                    # Flaskアプリケーションのメインファイル
├── templates/               
│   ├── base.html            # ベーステンプレート（共通レイアウト）
│   ├── index.html           # トップページ（記事一覧）
│   ├── post_detail.html     # 記事詳細ページ
│   ├── create_post.html     # 新規投稿フォーム
│   ├── edit_post.html       # 記事編集フォーム
│   └── load_markdown.html   # Markdownファイル読み込みページ
├── .env                     # 環境変数（データベース接続情報）
├── sample_post.md          # サンプル記事（Pythonプログラミング入門）
├── tech_blog.md            # サンプル記事（Web開発トレンド）
├── recipe.md               # サンプル記事（カルボナーラレシピ）
└── README.md               # このファイル
```

## 実行方法
1. 必要なライブラリをインストール：
```bash
conda activate daily-python
pip install Flask Flask-SQLAlchemy PyMySQL python-dotenv markdown
```

2. MySQLデータベースを作成（既に作成済みの場合はスキップ）：
```bash
mysql -u root -p
CREATE DATABASE day98_markdown_blog CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

3. アプリケーションを起動：
```bash
python app.py
```

4. ブラウザで http://127.0.0.1:5000 にアクセス

## 使い方
### 新規記事の作成
1. 「新規投稿」ボタンをクリック
2. タイトルと内容（Markdown形式）を入力
3. 「投稿する」ボタンで保存

### Markdownファイルの読み込み
1. 「Markdown読み込み」ボタンをクリック
2. ファイルパスを入力（例: `./sample_post.md`）
3. 「読み込む」ボタンでインポート

### 記事の編集・削除
- 各記事の「編集」ボタンから内容を修正
- 「削除」ボタンで記事を削除（確認ダイアログあり）

## 📖 学んだことや今後の改善案（学習ログ）

### 学んだこと
1. **Flask-SQLAlchemy**によるORM操作
   - モデル定義とデータベース操作の簡素化
   - リレーションシップの管理

2. **Markdownのパースと表示**
   - `markdown`ライブラリによるHTML変換
   - シンタックスハイライトの実装
   - セキュアなHTML表示（XSS対策）

3. **ファイル操作とエラーハンドリング**
   - 外部ファイルの安全な読み込み
   - 適切なエラーメッセージの表示

4. **Bootstrap 5の活用**
   - レスポンシブデザインの実装
   - モダンなUIコンポーネントの使用

### 今後の改善案
1. **機能追加**
   - タグ・カテゴリー機能
   - 検索機能
   - ページネーション
   - コメント機能

2. **セキュリティ強化**
   - ユーザー認証システム
   - CSRF対策
   - ファイルアップロード時の検証強化

3. **パフォーマンス改善**
   - キャッシング機能
   - 画像の最適化
   - 非同期処理の導入

4. **UI/UX改善**
   - リアルタイムMarkdownプレビュー
   - ドラフト保存機能
   - ダークモード対応
