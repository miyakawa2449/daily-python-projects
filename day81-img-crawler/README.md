# 🖼️ day81-img-crawler

## 📋 アプリケーション名
**Bing画像検索クローラー**

## 🎯 アプリケーション概要
Bing画像検索から指定したキーワードの画像を自動的に収集してダウンロードするPythonアプリケーションです。キーワードを入力するだけで、関連する画像を5枚まで自動でローカルに保存します。

## 📁 ファイル構成
```
day81-img-crawler/
├── main.py              # メインスクリプト
├── README.md           # このファイル
└── downloaded_images/   # 画像保存先フォルダ（実行時に自動作成）
    ├── img_0.jpg
    ├── img_1.png
    ├── img_2.gif
    └── ...
```

## 🔧 必要なライブラリ
```bash
pip install requests beautifulsoup4
```

## 🚀 実行方法
```bash
# プロジェクトディレクトリに移動
cd day81-img-crawler

# スクリプトを実行
python main.py
```

## 💻 使い方

### 1️⃣ **プログラムを起動**
```bash
python main.py
```

### 2️⃣ **キーワードを入力**
```
検索キーワードを入力してください（例: 富士山）: 猫
```

### 3️⃣ **自動ダウンロード**
```
🔍 画像URLを収集中...
📥 5 件の画像URLを取得しました。
✅ downloaded_images/img_0.jpg を保存しました
✅ downloaded_images/img_1.png を保存しました
✅ downloaded_images/img_2.gif を保存しました
✅ downloaded_images/img_3.jpg を保存しました
✅ downloaded_images/img_4.webp を保存しました
```

## 🛠️ 機能
- ✅ **キーワード検索**: 任意のキーワードでBing画像検索
- ✅ **自動ダウンロード**: 検索結果の画像を自動でローカル保存
- ✅ **複数フォーマット対応**: JPG、PNG、GIF、WebP等に対応
- ✅ **自動ファイル名生成**: `img_0.jpg`、`img_1.png`等の連番で保存
- ✅ **エラーハンドリング**: ダウンロード失敗時の適切な処理

## ⚙️ 設定可能項目

### 📂 保存先フォルダを変更
```python
# main.py の8行目
SAVE_DIR = "your_custom_folder"
```

### 🔢 ダウンロード枚数を変更
```python
# main.py の55行目
image_urls = fetch_image_urls(query, max_images=10)  # 5→10に変更
```

### 🌐 User-Agentを変更（より詳細に）
```python
# main.py の16〜18行目
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
```

## 📊 使用例

### 🐱 **動物の画像を収集**
```
検索キーワード: 猫
→ downloaded_images/img_0.jpg (可愛い猫の写真)
→ downloaded_images/img_1.png (猫のイラスト)
```

### 🏔️ **風景写真を収集**
```
検索キーワード: 富士山
→ downloaded_images/img_0.jpg (富士山の風景)
→ downloaded_images/img_1.webp (富士山の夕日)
```

### 🍕 **料理写真を収集**
```
検索キーワード: パスタ
→ downloaded_images/img_0.jpg (美味しそうなパスタ)
→ downloaded_images/img_1.png (パスタのレシピ画像)
```

## ⚠️ 注意事項
- 🌐 **インターネット接続必須**: Bing画像検索にアクセスするため
- ⏰ **検索制限**: 短時間での連続実行は制限される可能性があります
- 📝 **著作権**: ダウンロードした画像の著作権にご注意ください
- 🖼️ **画像品質**: 検索結果によりサムネイルサイズの場合があります

## 🐛 トラブルシューティング

### ❌ **画像が見つからない場合**
```
❌ 0 件の画像URLを取得しました。
```
**解決方法**:
- より一般的なキーワードを試す（例: "cat" → "猫"）
- 英語のキーワードを試す
- 時間をおいて再実行する

### ❌ **ダウンロードに失敗する場合**
```
❌ https://example.com/image.jpg のダウンロードに失敗: 404 Client Error
```
**解決方法**:
- インターネット接続を確認
- ファイアウォール設定を確認
- 再実行してみる

## 🔧 技術仕様
- **Python**: 3.6以上
- **主要ライブラリ**: 
  - `requests`: HTTP通信
  - `beautifulsoup4`: HTML解析
  - `mimetypes`: ファイル形式判定
- **対応画像形式**: JPG, JPEG, PNG, GIF, WebP, BMP
- **最大ダウンロード数**: 5枚（設定変更可能）

## 📖 学んだことや今後の改善案（学習ログ）

### ✅ **学んだこと**
- **Web スクレイピング**: BeautifulSoupを使ったHTML解析
- **HTTP通信**: requestsライブラリでのGETリクエスト
- **ファイル操作**: バイナリファイルの読み書き
- **エラーハンドリング**: try-except文での例外処理
- **MIME Type**: Content-Typeヘッダーからファイル拡張子の取得

### 🚀 **今後の改善案**

#### 🔥 **優先度高**
- [ ] **画像品質向上**: JavaScript内のmurl抽出で高解像度画像取得
- [ ] **画像検証**: 壊れた画像ファイルの除外機能
- [ ] **ファイル名重複対応**: 同名ファイルの上書き防止

#### 🌟 **優先度中**
- [ ] **GUI化**: tkinterでユーザーフレンドリーなインターフェース
- [ ] **プログレスバー**: ダウンロード進行状況の可視化
- [ ] **画像フィルタリング**: サイズ・形式での絞り込み機能
- [ ] **バッチ処理**: 複数キーワードの一括処理

#### 💡 **優先度低（発展）**
- [ ] **他検索エンジン対応**: Google Images、Yahoo等
- [ ] **API連携**: 正式なAPI使用への移行
- [ ] **データベース連携**: 検索履歴・画像メタデータの保存
- [ ] **機械学習**: 画像分類・品質評価機能

### 🎯 **技術的課題と解決策**
```
課題: Bingの仕様変更に対する対応
解決策: 複数の抽出手法を並行実装

課題: 画像ファイルの品質・サイズのばらつき  
解決策: Content-Lengthチェック、画像署名検証

課題: レート制限・アクセス制限
解決策: リクエスト間隔制御、User-Agent設定
```

### 📚 **参考になったリソース**
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://docs.python-requests.org/)
- [Python mimetypes module](https://docs.python.org/3/library/mimetypes.html)

---
**🎉 プロジェクト完成日**: 2025年7月19日  
**⚡ 実装時間**: 約2-3時間  
**🛠️ 使用技術**: Python, Web Scraping, HTTP, File I/O