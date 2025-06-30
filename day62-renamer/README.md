# 🗂️ ファイル一括リネームツール (Batch File Renamer)

指定したディレクトリ内のファイルを一括でリネームするPythonツールです。ファイル整理や写真の整理などに便利な実用的なアプリケーションです。

## 📁 ファイル構成

```
day62-renamer/
├── main.py           # メインプログラム
└── README.md         # このファイル
```

## 🚀 実行方法

```bash
cd day62-renamer
python main.py
```

## 💡 使い方

### 📋 **実行例**

```bash
python main.py
```

**対話形式で入力**:
```
対象フォルダのパスを入力: .
新しいファイル名の接頭辞を入力: photo
```

**結果**:
```
リネーム対象ファイル: ['IMG_001.jpg', 'IMG_002.jpg', 'IMG_003.jpg', 'document.pdf']
IMG_001.jpg → photo_1.jpg
IMG_002.jpg → photo_2.jpg
IMG_003.jpg → photo_3.jpg
document.pdf → photo_4.pdf
リネームが完了しました！
```

### 🎯 **入力パラメータ**

#### 📂 **対象フォルダのパス**
- **現在のディレクトリ**: `.`
- **相対パス**: `../other-folder`
- **絶対パス**: `/Users/username/Documents/photos`
- **サブディレクトリ**: `test_files`

#### 🔤 **接頭辞（prefix）**
新しいファイル名の先頭に付ける共通の文字列
- **例**: `photo` → `photo_1.jpg`, `photo_2.jpg`
- **例**: `backup` → `backup_1.txt`, `backup_2.txt`
- **例**: `document_2024` → `document_2024_1.pdf`

## ✨ 機能

### ✅ **基本機能**
- **一括リネーム**: 複数ファイルを連番付きで統一
- **拡張子保持**: 元のファイル拡張子を維持
- **フィルタリング**: ディレクトリと隠しファイルを自動除外
- **安全な処理**: 既存ファイルの上書き防止

### 🛡️ **安全機能**
- **ディレクトリスキップ**: フォルダはリネーム対象外
- **隠しファイルスキップ**: `.DS_Store`などを除外
- **事前表示**: リネーム前に対象ファイル一覧を表示

## 🧪 テスト用ファイルの作成

リネームツールをテストするためのサンプルファイル作成：

### 📝 **方法1: ターミナルコマンドで作成**
```bash
# テスト用ディレクトリ作成
mkdir test_files
cd test_files

# サンプルファイル作成
for i in {1..10}; do touch "sample$i.txt"; done

# 確認
ls -la
```

### 🐍 **方法2: Pythonスクリプトで作成**
```python
# create_samples.py
import os

def create_sample_files():
    os.makedirs("test_files", exist_ok=True)
    for i in range(1, 11):
        with open(f"test_files/sample{i}.txt", 'w') as f:
            f.write(f"サンプルファイル{i}の内容\n")
    print("サンプルファイル作成完了")

if __name__ == "__main__":
    create_sample_files()
```

## 📖 学んだことや今後の改善案（学習ログ）

### 🔧 主要な学習ポイント

#### 1️⃣ **`os.listdir()`によるファイル一覧取得**

```python
files = os.listdir(directory)
print(f"リネーム対象ファイル: {files}")
```

**重要な発見**:
- **全アイテム取得**: ファイルもフォルダも隠しファイルも全て含まれる
- **ファイル名のみ**: フルパスではなく、ファイル名だけを返す
- **事前確認の重要性**: ユーザーが何が処理されるかを把握できる

**実際の出力例**:
```python
# ディレクトリ内容: sample1.txt, sample2.txt, __pycache__/, .DS_Store
files = os.listdir(".")
# 結果: ['sample1.txt', 'sample2.txt', '__pycache__', '.DS_Store']
```

**学習**: この段階では**フィルタリング前**なので、後続の処理で不要なファイルを除外する

#### 2️⃣ **パス指定の理解と`.`の意味**

**質問**: 「対象フォルダのパスを入力と表示された場合、プロジェクトのルートフォルダを指定する場合は？ . ですか？」

**回答と学習内容**:
```python
# パス指定の種類
"."           # 現在のディレクトリ（カレントディレクトリ）
".."          # 一つ上のディレクトリ
"./subfolder" # 現在のディレクトリ内のサブフォルダ
"/full/path"  # 絶対パス
```

**重要な気づき**:
- **`.` = 現在いる場所**: プロジェクトルートで実行すれば、そのディレクトリが対象
- **相対パスの概念**: 実行場所を基準とした相対的な位置指定
- **安全性の考慮**: 現在のディレクトリを指定すると`main.py`自体もリネーム対象になる可能性

**対策学習**:
```bash
# 安全なテスト方法
mkdir test_files
for i in {1..5}; do touch "test_files/sample$i.txt"; done
# パス入力: test_files
```

#### 3️⃣ **接頭辞（prefix）の概念理解**

**質問**: 「『新しいファイル名の接頭辞を入力』と言われているが、ここでは何を入れればいい？」

**学習した内容**:
```python
# ファイル名の構成
new_filename = f"{prefix}_{i}{ext}"
#                 ↑      ↑  ↑
#              接頭辞  連番 拡張子
```

**実用例**:
```python
# 接頭辞: "photo" の場合
"sample1.jpg" → "photo_1.jpg"
"sample2.jpg" → "photo_2.jpg"

# 接頭辞: "backup_2024" の場合  
"document.pdf" → "backup_2024_1.pdf"
"report.docx" → "backup_2024_2.docx"
```

**用途別接頭辞の例**:
- **写真整理**: `vacation_2024`, `wedding`, `family_photo`
- **文書管理**: `report`, `meeting_notes`, `project_doc`
- **バックアップ**: `backup`, `archive`, `old_version`

#### 4️⃣ **`input().strip()`の重要性**

**質問**: 「inputの後ろについている.strip()は何をしているんですか？使わずにtarget_dirに代入してはいけないんですか？」

**詳細な学習内容**:

##### ❌ **`.strip()` なしの問題**
```python
target_dir = input("対象フォルダのパスを入力: ")
# ユーザー入力: "  .  " (前後にスペース)
files = os.listdir(target_dir)  # Error!
# OSError: [Errno 2] No such file or directory: '  .  '
```

##### ✅ **`.strip()` ありの解決**
```python
target_dir = input("対象フォルダのパスを入力: ").strip()
# ユーザー入力: "  .  " → "." に変換
files = os.listdir(target_dir)  # 正常動作
```

**除去される文字**:
- **半角スペース**: ` `
- **タブ文字**: `\t`
- **改行文字**: `\n`, `\r`

**実際のユーザー入力ミス例**:
```
対象フォルダのパスを入力:  .  ← 前後にスペース
対象フォルダのパスを入力: 	.	 ← 前後にタブ
対象フォルダのパスを入力: ./test_folder
                     ← コピペ時の改行
```

**重要な学習**: **ユーザー入力を扱う際は必ず`.strip()`を使う**ことがベストプラクティス

#### 5️⃣ **プログラム実行フローの理解**

**質問**: 「このブロックの順番で処理しているんですよね？batch_rename(target_dir, prefix)で関数を呼び出してファイル名を一括変換する処理をしていると。」

**完全な処理フロー**:
```python
if __name__ == "__main__":
    # 1️⃣ ユーザーから対象ディレクトリを入力
    target_dir = input("対象フォルダのパスを入力: ").strip()
    
    # 2️⃣ ユーザーから接頭辞を入力  
    prefix = input("新しいファイル名の接頭辞を入力: ").strip()
    
    # 3️⃣ リネーム関数を呼び出し（実際の処理）
    batch_rename(target_dir, prefix)
    
    # 4️⃣ 完了メッセージ表示
    print("リネームが完了しました！")
```

**重要な理解**:
- **メイン処理**: ユーザーインターフェース担当
- **`batch_rename()` 関数**: 実際のファイル操作担当
- **役割分担**: UI処理とビジネスロジックの分離

### 🛠️ コードの技術的詳細

#### 🔄 **enumerate()の活用**
```python
for i, filename in enumerate(files, 1):
#                              ↑
#                        1から開始
```
- **連番生成**: 1, 2, 3... の順序でインデックス作成
- **開始番号指定**: デフォルトは0だが、1から開始に変更

#### 📂 **os.path.join()による安全なパス結合**
```python
old_path = os.path.join(directory, filename)
```
- **クロスプラットフォーム対応**: Windows(`\`) と Unix(`/`) の違いを自動処理
- **パス区切り文字の自動挿入**: 手動で`/`を追加する必要なし

#### 🔍 **ファイル種別判定**
```python
if os.path.isdir(old_path) or filename.startswith('.'):
    continue
```
- **`os.path.isdir()`**: ディレクトリかどうかを判定
- **`filename.startswith('.')`**: 隠しファイル（Unix系）の判定

#### 📋 **拡張子分離**
```python
name, ext = os.path.splitext(filename)
# "sample1.txt" → ("sample1", ".txt")
```
- **拡張子保持**: リネーム後も元の拡張子を維持
- **ファイル種別維持**: 画像、文書など、ファイルタイプが変わらない

### 🚀 今後の改善・発展アイデア

#### 📈 **機能拡張**
- **プレビュー機能**: 実際にリネームする前に結果を表示
- **アンドゥ機能**: リネーム前の状態に戻す
- **設定ファイル**: よく使う接頭辞をプリセット保存
- **バッチ処理**: 複数ディレクトリを一度に処理

#### 🛡️ **エラーハンドリング強化**
```python
# 改善案
def batch_rename_safe(directory, prefix):
    try:
        if not os.path.exists(directory):
            print(f"エラー: '{directory}' が見つかりません")
            return
        
        if not os.path.isdir(directory):
            print(f"エラー: '{directory}' はディレクトリではありません")
            return
            
        # リネーム処理...
        
    except PermissionError:
        print("エラー: ファイルアクセス権限がありません")
    except OSError as e:
        print(f"エラー: {e}")
```

#### 🎨 **ユーザビリティ向上**
- **GUI版**: tkinterやPyQt5での視覚的インターフェース
- **ドラッグ&ドロップ**: ファイルをドラッグしてリネーム
- **プログレスバー**: 大量ファイル処理時の進捗表示
- **フィルター機能**: 特定の拡張子のみを対象

#### 🔧 **技術的発展**
- **正規表現対応**: 複雑なリネームパターン
- **CSV連携**: ファイル名とメタデータの対応表
- **ログ機能**: リネーム履歴の記録
- **設定ファイル**: JSON/YAML形式での設定管理

#### 📊 **高度な機能**
```python
# 発展例: 日付ベースリネーム
def rename_by_date(directory, prefix):
    """ファイルの更新日時に基づいてリネーム"""
    import datetime
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # ファイルの更新日時を取得
            mtime = os.path.getmtime(file_path)
            date_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y%m%d')
            
            name, ext = os.path.splitext(filename)
            new_name = f"{prefix}_{date_str}_{name}{ext}"
            # リネーム処理...
```

### 🎓 **プログラミング学習の成果**

#### 💻 **Pythonスキルの向上**
1. **標準ライブラリ**: `os`モジュールの実用的活用
2. **文字列処理**: `.strip()`, f-string, `.splitext()`
3. **ファイル操作**: パス操作、ディレクトリ処理
4. **エラーハンドリング**: 堅牢なアプリケーション設計

#### 🏗️ **ソフトウェア設計**
1. **関数分離**: UIロジックとビジネスロジックの分離
2. **ユーザビリティ**: 分かりやすいインターフェース設計
3. **安全性**: 意図しない操作の防止
4. **拡張性**: 機能追加しやすい構造

#### 🔍 **問題解決能力**
1. **事前調査**: ファイル一覧の確認
2. **フィルタリング**: 不要なファイルの除外
3. **入力検証**: ユーザー入力の前処理
4. **段階的処理**: 安全で確実な実装

## 🎉 総評

このファイル一括リネームツールは、**実用性の高い日常業務ツール**として完成しました。特に以下の学習価値が高い：

### ✅ **実用的価値**
- **日常業務**: 写真整理、文書管理に即戦力
- **時間短縮**: 手動リネームの大幅効率化
- **ミス防止**: 統一された命名規則

### 📚 **学習価値**
- **ファイル操作**: Pythonでのファイルシステム操作の基礎
- **ユーザー入力処理**: 堅牢な入力検証の実装
- **エラーハンドリング**: 実用アプリケーションの安全性

### 🚀 **発展可能性**
- **GUI化**: より使いやすいインターフェース
- **高度な機能**: 正規表現、メタデータ活用
- **自動化**: バッチ処理、スケジュール実行

**小さなツールから始まって、実用的なアプリケーションへ**: プログラミング学習の理想的なプロジェクトとなりました！🎊