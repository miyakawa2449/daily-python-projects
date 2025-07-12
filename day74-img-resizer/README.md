# 🖼️ 画像リサイズツール (Image Resizer)

Pythonの`PIL`（Pillow）ライブラリを使用したシンプルで実用的な画像リサイズアプリケーションです。任意の画像ファイルを指定したサイズに変換して保存できます。画像処理の基本概念とファイル操作を実践的に学べるプロジェクトです。

## 📝 アプリケーション概要

**主な機能**:
- **画像リサイズ**: 任意のサイズに画像を変更
- **フォーマット対応**: JPEG、PNG、GIF等の主要形式サポート
- **簡単操作**: コマンドライン入力だけで完結
- **高品質出力**: Pillowライブラリによる高品質な画像変換
- **ファイル保存**: 指定した名前でリサイズ後の画像を保存

**学習ポイント**:
- **PIL/Pillow活用**: Python標準的な画像処理ライブラリの使用
- **with文**: ファイルの適切なリソース管理
- **ユーザー入力処理**: input()による対話的インターフェース
- **型変換**: 文字列→整数の変換処理
- **例外処理**: 画像ファイル操作における安全性

## 📁 ファイル構成

```
day74-img-resizer/
├── main.py          # メインプログラム（画像リサイズ機能）
├── README.md        # このファイル
├── [元画像ファイル]  # リサイズ対象の画像（ユーザーが準備）
└── [出力画像ファイル] # リサイズ後の画像（実行後生成）
```

### 🎯 **main.py の構造**

#### **1. ライブラリインポート**
```python
from PIL import Image  # Python Imaging Library (Pillow)
```

#### **2. 画像リサイズ関数**
```python
def resize_image(input_path, output_path, width, height):
    """画像を指定サイズにリサイズして保存"""
    with Image.open(input_path) as img:    # ファイルを安全に開く
        resized_img = img.resize((width, height))  # サイズ変更
        resized_img.save(output_path)      # 新しいファイルに保存
        print(f"✅ {output_path} に保存しました！")  # 成功メッセージ
```

#### **3. ユーザー入力処理**
```python
if __name__ == "__main__":
    input_file = input("変換する画像ファイル名を入力してください: ").strip()
    width = int(input("幅(px)を入力してください: "))
    height = int(input("高さ(px)を入力してください: "))
    output_file = input("保存するファイル名を入力してください: ").strip()
    
    resize_image(input_file, output_file, width, height)
```

## 🚀 実行方法

### 📦 **必要なライブラリのインストール**

```bash
# Pillowライブラリをインストール
pip install Pillow
```

### ✅ **インストール確認**

```bash
# Pillowの動作確認
python -c "from PIL import Image; print('Pillow is working!')"
```

### 💻 **基本的な実行**

```bash
# day74-img-resizerディレクトリに移動
cd day74-img-resizer

# 画像リサイズツールを起動
python main.py
```

## 💡 使い方

### 🎯 **基本的な使用手順**

#### **1. 画像ファイルの準備**
```bash
# リサイズしたい画像をプロジェクトディレクトリに配置
# 例: photo.jpg, image.png, picture.gif など
```

#### **2. プログラム起動**
```bash
python main.py
```

#### **3. 対話的な入力**

##### **入力ファイル名の指定**
```
変換する画像ファイル名を入力してください: photo.jpg
```

##### **リサイズサイズの指定**
```
幅(px)を入力してください: 800
高さ(px)を入力してください: 600
```

##### **出力ファイル名の指定**
```
保存するファイル名を入力してください: resized_photo.jpg
```

#### **4. 実行結果**
```
✅ resized_photo.jpg に保存しました！
```

### 📊 **実用的な使用例**

#### **例1: Webサイト用画像の作成**
```
変換する画像ファイル名を入力してください: high_res_photo.jpg
幅(px)を入力してください: 1920
高さ(px)を入力してください: 1080
保存するファイル名を入力してください: web_banner.jpg
```

#### **例2: SNS投稿用正方形画像**
```
変換する画像ファイル名を入力してください: portrait.png
幅(px)を入力してください: 1080
高さ(px)を入力してください: 1080
保存するファイル名を入力してください: instagram_post.png
```

#### **例3: サムネイル画像の作成**
```
変換する画像ファイル名を入力してください: original.jpg
幅(px)を入力してください: 150
高さ(px)を入力してください: 150
保存するファイル名を入力してください: thumbnail.jpg
```

### 🎨 **対応フォーマット**

#### **入力対応形式**
- **JPEG**: .jpg, .jpeg
- **PNG**: .png（透明度保持）
- **GIF**: .gif
- **BMP**: .bmp
- **TIFF**: .tiff, .tif
- **WebP**: .webp

#### **出力形式**
出力ファイル名の拡張子によって自動的に形式が決定されます：
```python
# 例
"output.jpg"  → JPEG形式で保存
"output.png"  → PNG形式で保存
"output.gif"  → GIF形式で保存
```

## 🔧 **重要な技術要素の詳細解説**

### 📚 **PIL/Pillowライブラリの活用**

#### **1. 画像ファイルの安全な読み込み**
```python
with Image.open(input_path) as img:
    # withブロック内で画像を処理
    # ブロックを抜ける時に自動的にファイルがクローズされる
```

**重要ポイント**:
- **with文**: リソースの自動管理
- **例外安全**: ファイルオープンエラーでも適切にクローズ
- **メモリ効率**: 不要なファイルハンドルの解放

#### **2. 画像リサイズ処理**
```python
resized_img = img.resize((width, height))
```

**処理の詳細**:
- **アスペクト比**: 指定サイズに強制変換（比率は保持されない）
- **リサンプリング**: 高品質なアルゴリズムで画質を維持
- **新しいオブジェクト**: 元画像は変更せず新しい画像オブジェクトを作成

#### **3. 画像保存処理**
```python
resized_img.save(output_path)
```

**自動処理される内容**:
- **フォーマット判定**: 拡張子から保存形式を自動決定
- **品質最適化**: 各形式に適した圧縮設定
- **メタデータ処理**: 必要に応じてEXIF情報等の処理

### 🎯 **ユーザーインターフェース設計**

#### **1. 対話的入力システム**
```python
input_file = input("変換する画像ファイル名を入力してください: ").strip()
width = int(input("幅(px)を入力してください: "))
height = int(input("高さ(px)を入力してください: "))
output_file = input("保存するファイル名を入力してください: ").strip()
```

**設計思想**:
- **段階的入力**: 1つずつ明確に入力項目を提示
- **strip()処理**: 前後の空白削除でユーザーミスを防止
- **型変換**: int()による文字列→数値変換
- **分かりやすいプロンプト**: 何を入力すべきか明確に表示

#### **2. フィードバック設計**
```python
print(f"✅ {output_path} に保存しました！")
```

**ユーザビリティ**:
- **成功の明確な表示**: ✅絵文字による視覚的フィードバック
- **具体的な情報**: 保存先ファイル名の確認
- **処理完了の確認**: 操作が成功したことの明確な通知

### 💡 **シンプル設計の美学**

#### **「ちょっと乱暴だけど動く」設計の価値**

```python
# シンプルで直接的なアプローチ
def resize_image(input_path, output_path, width, height):
    with Image.open(input_path) as img:
        resized_img = img.resize((width, height))
        resized_img.save(output_path)
        print(f"✅ {output_path} に保存しました！")

# 複雑な設定や例外処理は省略
# 最小限のコードで最大の機能を実現
```

**このアプローチの利点**:
- **学習効率**: 核心的な機能に集中できる
- **理解しやすさ**: コードの意図が明確
- **実用性**: 基本的な用途には十分
- **拡張基盤**: 将来の機能追加の土台となる

## 📖 学んだことや今後の改善案（学習ログ）

### 🔧 主要な学習ポイント

#### 1️⃣ **PIL/Pillowライブラリの実践的活用**

**画像処理の基本操作習得**:
```python
# 画像処理の基本パターン
with Image.open(input_path) as img:    # 読み込み
    processed = img.resize((w, h))     # 処理
    processed.save(output_path)        # 保存
```

**重要な学習内容**:
- **リソース管理**: with文による安全なファイル操作
- **オブジェクト指向**: Imageオブジェクトのメソッド活用
- **フォーマット自動処理**: 拡張子による形式自動判定
- **高品質処理**: Pillowの内部アルゴリズムによる品質維持

#### 2️⃣ **実用的なユーザーインターフェース設計**

**対話的プログラムの基本パターン**:
```python
# 入力 → 処理 → 出力 → フィードバック
input_data = input("プロンプト: ").strip()  # 入力
result = process(input_data)                # 処理  
save(result, output_path)                  # 出力
print("✅ 完了メッセージ")                   # フィードバック
```

**ユーザビリティの配慮**:
- **明確なプロンプト**: 何を入力すべきかが分かりやすい
- **エラー予防**: strip()による前後空白除去
- **段階的入力**: 一度に全て入力させない親切設計
- **成功通知**: 処理完了の明確なフィードバック

#### 3️⃣ **時間制約下での効果的な開発**

**「時間がない時の開発戦略」**:
```python
# 完璧を求めず、動作する最小限の機能に集中
def resize_image(input_path, output_path, width, height):
    # エラーハンドリングは省略
    # 複雑な設定は省略
    # 最低限の機能のみ実装
    with Image.open(input_path) as img:
        resized_img = img.resize((width, height))
        resized_img.save(output_path)
        print(f"✅ {output_path} に保存しました！")
```

**この開発手法の価値**:
- **プロトタイピング**: 素早く動作する版を作成
- **学習効率**: 本質的な機能に集中
- **実用性**: 基本用途には十分対応
- **反復開発**: 後から段階的に改善可能

### 🚀 今後の改善・発展アイデア

#### 📈 **機能拡張案**

##### 1️⃣ **エラーハンドリング強化**
```python
def resize_image_safe(input_path, output_path, width, height):
    """エラー処理付きリサイズ機能"""
    try:
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"ファイルが見つかりません: {input_path}")
        
        if width <= 0 or height <= 0:
            raise ValueError("幅と高さは正の数値を指定してください")
        
        with Image.open(input_path) as img:
            resized_img = img.resize((width, height))
            resized_img.save(output_path)
            print(f"✅ {output_path} に保存しました！")
            
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")
        return False
    
    return True
```

##### 2️⃣ **アスペクト比保持機能**
```python
def resize_keep_aspect(input_path, output_path, max_width, max_height):
    """アスペクト比を保持したリサイズ"""
    with Image.open(input_path) as img:
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        img.save(output_path)
```

##### 3️⃣ **バッチ処理機能**
```python
def batch_resize(input_dir, output_dir, width, height):
    """フォルダ内の全画像を一括リサイズ"""
    import glob
    import os
    
    image_files = glob.glob(os.path.join(input_dir, "*.{jpg,jpeg,png,gif}"))
    
    for input_file in image_files:
        filename = os.path.basename(input_file)
        output_file = os.path.join(output_dir, f"resized_{filename}")
        resize_image(input_file, output_file, width, height)
```

##### 4️⃣ **GUI版の作成**
```python
import tkinter as tk
from tkinter import filedialog, messagebox

def create_gui():
    """tkinterによるGUI版"""
    root = tk.Tk()
    root.title("画像リサイズツール")
    
    # ファイル選択ボタン
    select_btn = tk.Button(root, text="画像を選択", command=select_file)
    
    # サイズ入力欄
    width_entry = tk.Entry(root)
    height_entry = tk.Entry(root)
    
    # リサイズボタン
    resize_btn = tk.Button(root, text="リサイズ実行", command=resize_action)
```

##### 5️⃣ **高度な画像処理機能**
```python
def advanced_resize(input_path, output_path, width, height, **options):
    """高度なリサイズオプション"""
    with Image.open(input_path) as img:
        # リサンプリング方式選択
        resample_method = options.get('resample', Image.Resampling.LANCZOS)
        
        # 品質設定
        quality = options.get('quality', 95)
        
        # シャープネス調整
        if options.get('enhance_sharpness'):
            from PIL import ImageEnhance
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(1.2)
        
        resized_img = img.resize((width, height), resample_method)
        resized_img.save(output_path, quality=quality)
```

#### 🔧 **技術的改善案**

##### 1️⃣ **設定ファイル対応**
```python
import json

def load_resize_presets():
    """リサイズプリセットをJSONから読み込み"""
    with open('resize_presets.json', 'r') as f:
        return json.load(f)

# resize_presets.json
{
    "web_banner": {"width": 1920, "height": 1080},
    "instagram_post": {"width": 1080, "height": 1080},
    "thumbnail": {"width": 150, "height": 150},
    "mobile_wallpaper": {"width": 1080, "height": 1920}
}
```

##### 2️⃣ **コマンドライン引数対応**
```python
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='画像リサイズツール')
    parser.add_argument('input', help='入力ファイル名')
    parser.add_argument('output', help='出力ファイル名')
    parser.add_argument('-w', '--width', type=int, required=True, help='幅(px)')
    parser.add_argument('-h', '--height', type=int, required=True, help='高さ(px)')
    parser.add_argument('-q', '--quality', type=int, default=95, help='品質(1-100)')
    
    return parser.parse_args()

# 使用例: python main.py input.jpg output.jpg -w 800 -h 600
```

##### 3️⃣ **進捗表示機能**
```python
from tqdm import tqdm
import time

def resize_with_progress(input_path, output_path, width, height):
    """進捗バー付きリサイズ"""
    steps = ['ファイル読み込み', 'リサイズ処理', 'ファイル保存']
    
    with tqdm(total=len(steps), desc="リサイズ中") as pbar:
        # ステップ1: 読み込み
        pbar.set_description("画像を読み込み中...")
        with Image.open(input_path) as img:
            pbar.update(1)
            
            # ステップ2: リサイズ
            pbar.set_description("リサイズ処理中...")
            resized_img = img.resize((width, height))
            pbar.update(1)
            
            # ステップ3: 保存
            pbar.set_description("ファイル保存中...")
            resized_img.save(output_path)
            pbar.update(1)
    
    print("✅ リサイズ完了！")
```

### 💡 **重要な学習成果**

#### 🎯 **実用的ツール開発の体験**

##### 📚 **「動くものを作る」ことの価値**
- **学習効率**: 完璧を求めず、まず動作するものを作る
- **実用性**: 基本機能でも実際に使える価値
- **成功体験**: 短時間で成果を得られる達成感
- **改善基盤**: 動作する版から段階的に改善可能

##### 🔧 **時間制約下での開発スキル**
- **優先順位**: 本質的な機能への集中
- **最小限実装**: 必要最小限の機能で最大の効果
- **プロトタイピング**: 素早く試行錯誤できる開発手法

#### 🚀 **画像処理技術の基礎習得**

##### 💫 **PIL/Pillowライブラリの活用力**
- **基本操作**: 読み込み・リサイズ・保存の基本パターン
- **リソース管理**: with文による安全なファイル操作
- **フォーマット処理**: 各種画像形式への対応

##### 🎨 **今後の応用可能性**
- **Web開発**: アップロード画像の自動リサイズ
- **データ処理**: 機械学習用データセットの前処理
- **業務自動化**: 定期的な画像処理タスクの自動化

#### 🌟 **今後への展開**

このプロジェクトで習得した技術は、**Web アプリケーション・画像処理ツール・データ分析・自動化スクリプト**など様々な分野で活用可能です。特に**シンプルで実用的な設計思想**は、効率的な開発を可能にする重要なスキルです。

## 🎉 総評

Day 74の画像リサイズツールは、**「時間制約がある中でも実用的なツールを素早く開発する」**現実的な開発体験ができた価値あるプロジェクトでした。

### ✅ **特に価値があった学習内容**

1. **PIL/Pillow活用**: Python標準的な画像処理ライブラリの基本操作
2. **リソース管理**: with文による安全なファイル操作
3. **ユーザーインターフェース**: 対話的入力による使いやすい設計
4. **実用性重視**: 完璧でなくても「動く」ものの価値
5. **時間効率**: 短時間で最大の成果を得る開発手法

### 🎯 **今後への展開**

このプロジェクトで習得した技術は、**画像処理アプリケーション・Web サービス・業務自動化ツール**など様々な分野で活用可能です。特に**シンプルで直接的なアプローチ**による開発手法は、プロトタイピングや実用ツール作成で非常に価値があります。

**17行のシンプルなコード**から**実用的な画像リサイズツール**まで構築できた、効率的で実践的な学習体験でした！🖼️✨