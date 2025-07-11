# 📱 QRコード生成器 (QR Code Maker)

Pythonの`qrcode`ライブラリを使用したシンプルで実用的なQRコード生成アプリケーションです。テキストやURLを入力するだけで、高品質なQRコード画像を簡単に作成できます。オブジェクト指向プログラミングの基本概念を実践的に学べるプロジェクトです。

## 📝 アプリケーション概要

**主な機能**:
- **テキスト→QRコード変換**: 任意の文字列をQRコードに変換
- **URL対応**: WebサイトURLのQRコード生成
- **高品質出力**: PNG形式での画像保存
- **カスタマイズ設定**: サイズ、色、誤り訂正レベルの調整
- **簡単操作**: コマンドライン入力だけで完結

**学習ポイント**:
- **外部ライブラリ活用**: `qrcode`と`Pillow`の実践的使用
- **オブジェクト指向理解**: クラスとインスタンスの関係体験
- **段階的処理**: データ設定→構造生成→画像化→保存の流れ
- **メソッドチェーン**: オブジェクトのメソッド連続呼び出し
- **ライブラリインストール**: `pip install`による依存関係管理

## 📁 ファイル構成

```
day73-qr-maker/
├── main.py          # メインプログラム（QRコード生成機能）
├── README.md        # このファイル
└── qrcode.png       # 生成されるQRコード画像（実行後）
```

### 🎯 **main.py の構造**

#### **1. ライブラリインポート**
```python
import qrcode  # QRコード生成ライブラリ
```

#### **2. QRコード生成関数**
```python
def generate_qr(data, filename="qrcode.png"):
    """QRコードを生成して保存"""
    
    # QRCodeオブジェクト作成（設計図からインスタンス生成）
    qr = qrcode.QRCode(
        version=1,                                    # サイズ（1〜40）
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 誤り訂正レベル
        box_size=10,                                  # 1ボックスのピクセルサイズ
        border=4                                      # 白い枠のサイズ
    )
    
    # 段階的な処理フロー
    qr.add_data(data)                    # データ設定
    qr.make(fit=True)                    # QRコード構造生成
    img = qr.make_image(...)             # 画像として実体化
    img.save(filename)                   # ファイルに保存
```

#### **3. メイン実行部**
```python
if __name__ == "__main__":
    text = input("QRコードにする文字列やURLを入力してください: ")
    generate_qr(text.strip())  # 前後の空白削除して関数に渡す
```

## 🚀 実行方法

### 📦 **必要なライブラリのインストール**

```bash
# qrcodeライブラリをインストール（Pillowも同時インストール）
pip install qrcode[pil]

# または個別にインストール
pip install qrcode
pip install pillow
```

### 💻 **基本的な実行**

```bash
# day73-qr-makerディレクトリに移動
cd day73-qr-maker

# QRコード生成器を起動
python main.py
```

### ✅ **インストール確認**

```bash
# インストールされたライブラリを確認
pip list | grep qrcode
pip list | grep Pillow
```

## 💡 使い方

### 🎯 **基本的な使用手順**

#### **1. プログラム起動**
```bash
python main.py
```

#### **2. データ入力**
```
QRコードにする文字列やURLを入力してください: 
```

#### **3. 様々な入力例**

##### **テキスト入力**
```
入力: Hello World!
結果: "Hello World!"のQRコードが生成される
```

##### **URL入力**
```
入力: https://github.com
結果: GitHubサイトへのQRコードが生成される
```

##### **日本語入力**
```
入力: こんにちは世界
結果: 日本語テキストのQRコードが生成される
```

##### **連絡先情報**
```
入力: TEL:090-1234-5678
結果: 電話番号のQRコードが生成される
```

#### **4. 結果確認**
```
✅ QRコードを qrcode.png に保存しました！
```

生成された`qrcode.png`ファイルをスマートフォンのQRコードリーダーでスキャンして動作確認。

### 📊 **生成されるQRコードの特徴**

```
設定値:
- サイズ: version=1（21x21マス）
- 誤り訂正: ERROR_CORRECT_L（約7%のエラー訂正）
- ボックスサイズ: 10ピクセル
- 余白: 4マス
- 色: 黒（QRコード）× 白（背景）
```

## 🔧 **重要な技術要素の詳細解説**

### 📚 **オブジェクト指向プログラミングの実践**

#### **1. クラスとオブジェクト（インスタンス）の関係**

```python
# クラス = 設計図
qrcode.QRCode  # QRコードを生成するための設計図

# オブジェクト = 設計図から作られた実際の製品
qr = qrcode.QRCode(...)  # 設計図から実際のQRコード生成器を作成
```

#### **2. オブジェクトの状態とメソッド**

```python
# オブジェクト = データ（状態） + 機能（メソッド）
qr = qrcode.QRCode(
    version=1,           # 状態: サイズ設定
    box_size=10,         # 状態: ピクセルサイズ
    border=4             # 状態: 余白設定
)

# メソッド = オブジェクトができること
qr.add_data(data)        # 機能: データを追加する
qr.make(fit=True)        # 機能: QRコード構造を生成する
qr.make_image(...)       # 機能: 画像オブジェクトを作る
```

#### **3. オブジェクト間の連携**

```python
# QRCodeオブジェクト → PIL.Imageオブジェクトの生成
qr = qrcode.QRCode(...)     # QRコード生成器オブジェクト
img = qr.make_image(...)    # 画像オブジェクト

# 各オブジェクトが独自の機能を持つ
qr.add_data()               # QRCodeオブジェクトの機能
img.save()                  # PIL.Imageオブジェクトの機能
```

### 🔄 **段階的処理フローの理解**

#### **データから画像ファイルまでの変換プロセス**

```python
# 1. ユーザー入力処理
text = input("...")                    # 例: "https://github.com   \n"
clean_text = text.strip()              # "https://github.com"

# 2. QRコード構造の生成
qr = qrcode.QRCode(...)               # 生成器の準備
qr.add_data(clean_text)               # データ設定
qr.make(fit=True)                     # 数学的パターン計算完了

# 3. 画像として実体化
img = qr.make_image(                  # 抽象的パターン → 具体的画像
    fill_color="black",               # QRコードの色
    back_color="white"                # 背景の色
)

# 4. ファイル保存
img.save("qrcode.png")                # メモリ上の画像 → ディスク上のファイル
```

#### **重要な概念: 「理論上の完成」vs「実体化」**

```python
# 理論上の完成（データ構造として存在）
qr.make(fit=True)           # QRコードのパターンが数学的に計算済み
                           # まだ「見える形」にはなっていない

# 実体化（人間が見える形に変換）
img = qr.make_image(...)    # パターン → 画像データ変換
                           # これで初めて「見える」QRコードになる
```

### 🎨 **外部ライブラリの効果的活用**

#### **1. 依存関係の理解**

```python
# qrcodeライブラリの内部依存
qrcode              # メインのQRコード生成機能
  └── Pillow (PIL)  # 画像生成・保存機能

# インストール時の適切な指定
pip install qrcode[pil]  # 必要な依存関係を一括インストール
```

#### **2. ライブラリAPIの理解**

```python
# qrcodeライブラリのAPI設計
qrcode.QRCode(          # コンストラクタ（初期設定）
    version=1,          # パラメータ: サイズ制御
    error_correction=..., # パラメータ: 品質制御
    box_size=10,        # パラメータ: 表示制御
    border=4            # パラメータ: レイアウト制御
)

# メソッドチェーンの活用可能性
qr.add_data(data).make(fit=True)  # （実際には未対応だが概念として）
```

### 🛡️ **エラーハンドリングと品質管理**

#### **1. 誤り訂正レベルの意味**

```python
# 誤り訂正レベルの選択肢
ERROR_CORRECT_L  # 約7%  - 最小サイズ、基本的な用途
ERROR_CORRECT_M  # 約15% - 標準的な選択
ERROR_CORRECT_Q  # 約25% - 高品質が必要な場合
ERROR_CORRECT_H  # 約30% - 最高品質、印刷物など
```

#### **2. 入力データの前処理**

```python
text = input("...")
clean_text = text.strip()  # 前後の空白・改行削除

# なぜstrip()が重要か
"https://example.com   \n"  # ユーザーの入力（余分な文字含む）
        ↓ strip()
"https://example.com"       # 正確なURL（QRコード読み取り時に問題なし）
```

### 🎯 **カスタマイズ可能な要素**

#### **1. サイズ調整**

```python
# version パラメータによるサイズ制御
version=1   # 21x21 マス（最小）
version=5   # 37x37 マス（中サイズ）
version=10  # 57x57 マス（大サイズ）
version=40  # 177x177 マス（最大）

# box_size パラメータによるピクセルサイズ制御
box_size=5   # 小さい画像
box_size=10  # 標準サイズ（現在の設定）
box_size=20  # 大きい画像
```

#### **2. 色のカスタマイズ**

```python
# 色の組み合わせ例
img = qr.make_image(fill_color="black", back_color="white")    # 標準
img = qr.make_image(fill_color="blue", back_color="yellow")    # カラフル
img = qr.make_image(fill_color="#333333", back_color="#FFFFFF") # HEXコード
```

## 📖 学んだことや今後の改善案（学習ログ）

### 🔧 主要な学習ポイント

#### 1️⃣ **オブジェクト指向プログラミングの実感**

**久しぶりのオブジェクト指向体験**:
```python
# 「物」として扱える感覚の体験
qr = qrcode.QRCode(...)     # QRコード生成器という「物」を作る
qr.add_data("Hello")        # その「物」にデータを教える
qr.make(fit=True)           # その「物」に作業を
