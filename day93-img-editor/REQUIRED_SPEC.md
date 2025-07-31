# day93-img-editor 要求定義書

## 📋 **プロジェクト概要**
**ブラウザ画像エディタ - Flask + Pillow統合システム**

Webブラウザ上で画像をアップロードし、リアルタイムで編集・変換できるWebアプリケーションを開発します。

---

## 🎯 **学習目標**

### **主要技術習得**
- ✅ **Flask**: ファイルアップロード処理
- ✅ **Pillow**: 画像処理・変換技術
- ✅ **JavaScript**: フロントエンド画像プレビュー
- ✅ **HTML5**: File API活用
- ✅ **CSS**: 画像エディタUI設計

### **実践的スキル**
- ✅ **ファイル管理**: アップロード・一時保存・削除
- ✅ **画像処理**: フィルタ・リサイズ・回転・明度調整
- ✅ **UI/UX**: 直感的な操作インターフェース
- ✅ **エラーハンドリング**: ファイル形式・サイズ検証

---

## 🎨 **機能要件**

### **🔧 基本機能（必須実装）**

#### **1. 画像アップロード**
```
- 対応形式: JPG, PNG, GIF, WEBP
- 最大ファイルサイズ: 10MB
- ドラッグ&ドロップ対応
- プレビュー表示機能
```

#### **2. 基本編集機能**
```
- リサイズ: 幅・高さ指定、比率維持
- 回転: 90°, 180°, 270°
- 反転: 水平・垂直
- トリミング: 矩形選択
```

#### **3. フィルタ・エフェクト**
```
- 明度調整: -100 ～ +100
- コントラスト調整: 0.5 ～ 2.0
- 彩度調整: 0 ～ 2.0
- ぼかし効果: 0 ～ 10px
- シャープ化: 軽・中・強
```

#### **4. 出力・ダウンロード**
```
- 形式選択: JPG, PNG, WEBP
- 品質設定: 1-100%
- ファイル名指定
- 即座ダウンロード
```

### **🌟 追加機能（チャレンジ要素）**

#### **5. 高度な編集**
```
- グレースケール変換
- セピア調変換
- エッジ検出
- エンボス効果
- 色調反転（ネガティブ）
```

#### **6. 複数画像対応**
```
- 一括アップロード
- 同一設定の一括適用
- ZIP形式での一括ダウンロード
```

---

## 🗂️ **ファイル構成**

```
day93-img-editor/
├── app.py                      # Flaskメインアプリ
├── static/
│   ├── css/
│   │   └── style.css          # エディタUI
│   ├── js/
│   │   └── editor.js          # 画像プレビュー・操作
│   └── uploads/               # 一時アップロード
├── templates/
│   └── index.html             # メイン画面
├── utils/
│   └── image_processor.py     # Pillow処理関数
├── requirements.txt           # 依存関係
├── REQUIRED_SPEC.md           # この要求定義書
└── README.md                  # プロジェクト説明
```

---

## 🛠️ **技術仕様**

### **バックエンド（Flask + Pillow）**

#### **主要エンドポイント**
```python
POST /upload          # 画像アップロード
POST /edit            # 画像編集処理
GET  /download/<id>   # 編集済み画像ダウンロード
GET  /preview/<id>    # プレビュー表示
DELETE /delete/<id>   # 一時ファイル削除
```

#### **Pillow処理例**
```python
from PIL import Image, ImageEnhance, ImageFilter

def resize_image(image, width, height, keep_ratio=True):
    """画像リサイズ"""
    
def rotate_image(image, angle):
    """画像回転"""
    
def adjust_brightness(image, factor):
    """明度調整"""
    
def apply_blur(image, radius):
    """ぼかし効果"""
```

### **フロントエンド（HTML5 + CSS + JS）**

#### **HTML5 File API**
```javascript
// ファイルドロップ処理
dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    const files = e.dataTransfer.files;
    handleFiles(files);
});

// プレビュー表示
function previewImage(file) {
    const reader = new FileReader();
    reader.onload = (e) => {
        previewImg.src = e.target.result;
    };
    reader.readAsDataURL(file);
}
```

#### **リアルタイム編集プレビュー**
```javascript
// CSS Filter でリアルタイムプレビュー
function updatePreview() {
    const brightness = document.getElementById('brightness').value;
    const contrast = document.getElementById('contrast').value;
    
    previewImg.style.filter = 
        `brightness(${brightness}%) contrast(${contrast}%)`;
}
```

---

## 📱 **UI/UXデザイン要件**

### **レイアウト構成**
```
┌─────────────────────────────────────┐
│           Header & Title            │
├─────────────┬───────────────────────┤
│             │                       │
│   Control   │                       │
│   Panel     │    Image Preview      │
│             │       Canvas          │
│   - Size    │                       │
│   - Rotate  │                       │
│   - Filter  │                       │
│   - Export  │                       │
│             │                       │
└─────────────┴───────────────────────┘
```

### **操作フロー**
```
1. 画像選択/ドロップ
   ↓
2. プレビュー表示
   ↓
3. 編集パネルで調整
   ↓
4. リアルタイムプレビュー確認
   ↓
5. 適用ボタンでサーバー処理
   ↓
6. 結果をダウンロード
```

---

## ⚡ **技術実装のポイント**

### **🔒 セキュリティ対策**
```python
# ファイル形式検証
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ファイルサイズ制限
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB
```

### **📁 ファイル管理**
```python
import uuid
import os
from datetime import datetime, timedelta

def generate_unique_filename(original_filename):
    """ユニークなファイル名生成"""
    ext = original_filename.rsplit('.', 1)[1].lower()
    unique_id = str(uuid.uuid4())
    return f"{unique_id}.{ext}"

def cleanup_old_files():
    """古い一時ファイルの自動削除"""
    cutoff_time = datetime.now() - timedelta(hours=1)
    # 1時間以上古いファイルを削除
```

### **🎨 画像処理最適化**
```python
def optimize_image_size(image, max_dimension=2000):
    """大きすぎる画像のリサイズ"""
    width, height = image.size
    if max(width, height) > max_dimension:
        ratio = max_dimension / max(width, height)
        new_size = (int(width * ratio), int(height * ratio))
        return image.resize(new_size, Image.Resampling.LANCZOS)
    return image
```

---

## 🧪 **開発・テスト手順**

### **Phase 1: 基本構造**
```bash
# プロジェクト作成
mkdir day93-img-editor
cd day93-img-editor

# 基本ファイル作成
touch app.py requirements.txt
mkdir -p static/{css,js,uploads} templates utils
```

### **Phase 2: アップロード機能**
- [ ] Flask アプリ基本構造
- [ ] ファイルアップロード処理
- [ ] 画像プレビュー表示
- [ ] エラーハンドリング

### **Phase 3: 画像処理**
- [ ] Pillow による基本処理
- [ ] リサイズ・回転機能
- [ ] フィルタ効果実装
- [ ] 処理結果の保存

### **Phase 4: UI改善**
- [ ] CSS によるエディタデザイン
- [ ] JavaScript インタラクション
- [ ] レスポンシブ対応
- [ ] UX最適化

### **Phase 5: 高度機能**
- [ ] 複数フィルタの組み合わせ
- [ ] 処理履歴機能
- [ ] 一括処理対応
- [ ] パフォーマンス最適化

---

## 🎯 **学習チェックポイント**

### **技術理解度確認**
- [ ] **Flask ファイルアップロード**: `request.files` の使い方
- [ ] **Pillow 基本操作**: Image オブジェクトの変換処理
- [ ] **JavaScript File API**: ファイル読み込みとプレビュー
- [ ] **CSS フィルタ**: リアルタイムエフェクト
- [ ] **エラーハンドリング**: ファイル検証とユーザー通知

### **実装品質評価**
- [ ] **ユーザビリティ**: 直感的な操作が可能か
- [ ] **パフォーマンス**: 大きな画像でも快適に動作するか
- [ ] **セキュリティ**: 不正ファイルの適切な処理
- [ ] **保守性**: コードの可読性と拡張性
- [ ] **レスポンシブ**: モバイル対応の品質

---

## 🚀 **今日の成功基準**

### **🎯 最小成功ライン（MVP）**
1. **画像アップロード** → ✅ ドラッグ&ドロップで画像選択
2. **基本編集** → ✅ リサイズ・回転・明度調整が動作
3. **ダウンロード** → ✅ 編集結果をファイルとして取得
4. **UI操作** → ✅ 直感的なエディタインターフェース

### **🌟 理想的な完成度**
1. **高度なフィルタ** → ✅ 複数エフェクトの組み合わせ
2. **リアルタイム** → ✅ CSS プレビューと実処理の連携
3. **複数ファイル** → ✅ 一括処理とZipダウンロード
4. **モバイル対応** → ✅ タッチデバイスでの操作性

---

## 🎊 **day93完了後の達成感**

このプロジェクトを完了すると、あなたは以下を習得します：

✨ **フルスタック画像処理アプリ開発**
✨ **Flask による高度なファイル処理**
✨ **Pillow を使った実用的な画像編集**
✨ **JavaScript によるリッチなUI実装**
✨ **実際に使えるWebツールの制作経験**

**day93は "作って楽しい・使って便利" な実用アプリケーションです！** 🎨📸✨

---

## 📝 **実装開始チェックリスト**

### **環境準備**
- [ ] プロジェクトディレクトリ作成
- [ ] 必要なライブラリインストール (`Flask`, `Pillow`)
- [ ] ディレクトリ構造作成
- [ ] Git初期化

### **基本ファイル作成**
- [ ] `app.py` - Flask アプリケーション
- [ ] `requirements.txt` - 依存関係定義
- [ ] `templates/index.html` - メイン画面
- [ ] `static/css/style.css` - スタイルシート
- [ ] `static/js/editor.js` - JavaScript 操作

### **実装順序**
1. **基本構造**: Flask アプリ + 基本ルーティング
2. **アップロード**: ファイル受信 + 保存機能
3. **プレビュー**: 画像表示 + JavaScript 連携
4. **編集機能**: Pillow による画像処理
5. **UI統合**: エディタインターフェース完成
6. **最適化**: パフォーマンス + UX 改善

**準備ができたら、Phase 1 から始めましょう！** 🚀