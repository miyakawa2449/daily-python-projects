# 💰 シンプル家計簿アプリ (Household CSV Manager)

Python の pandas ライブラリを活用したシンプルで実用的な家計簿管理アプリケーションです。CSV形式でのデータ永続化・pandas による集計分析・直感的なコンソールインターフェースを組み合わせ、データ処理技術・ファイル操作・実用ツール開発の重要な技術要素を実践的に学べるプロジェクトです。

## 📝 アプリケーション概要

**主な機能**:
- **データ追加**: 日付・項目・金額の家計データ登録
- **集計表示**: 全データ一覧・合計金額・項目別集計
- **CSV管理**: データの永続化・自動ファイル初期化
- **バリデーション**: 入力データの検証・エラーハンドリング
- **ユーザビリティ**: 日付省略・直感的メニュー操作

**学習ポイント**:
- **pandas データ処理**: DataFrame操作・集計分析の実践
- **CSV ファイル操作**: 読み書き・追記モード・データ永続化
- **エラーハンドリング**: 型変換・入力バリデーション
- **実用アプリ設計**: メニュー駆動・ユーザビリティ考慮
- **データ分析基盤**: 実用的な集計・可視化の基礎

## 📁 ファイル構成

```
day80-household-csv/
├── main.py          # メインプログラム（家計簿機能）
├── README.md        # このファイル
├── requirements.txt # 依存関係
└── household.csv    # データファイル（自動生成）
```

### 🎯 **main.py の構造**

#### **1. 初期設定・自動ファイル作成**
```python
FILENAME = "household.csv"

# 初回起動時の自動セットアップ
if not os.path.exists(FILENAME):
    df_init = pd.DataFrame(columns=["日付", "項目", "金額"])
    df_init.to_csv(FILENAME, index=False)
```

#### **2. データ追加機能（add_record）**
```python
def add_record():
    # 日付入力の柔軟性（省略で今日の日付）
    date_str = input("日付を入力（YYYY-MM-DD、省略で今日）: ").strip()
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")
    
    # 金額入力のバリデーション
    try:
        amount = int(input("金額を入力（整数）: ").strip())
    except ValueError:
        print("❌ 数字で入力してください")
        return
    
    # CSV追記保存
    new_data = pd.DataFrame([[date_str, item, amount]], columns=["日付", "項目", "金額"])
    new_data.to_csv(FILENAME, mode='a', header=False, index=False)
```

#### **3. 集計分析機能（show_summary）**
```python
def show_summary():
    df = pd.read_csv(FILENAME)
    print("\n📋 全データ:")
    print(df)
    
    print("\n💰 合計金額:", df["金額"].sum(), "円")
    
    print("\n📊 項目別の合計:")
    print(df.groupby("項目")["金額"].sum())
```

#### **4. メインループ・UI制御**
```python
while True:
    print("\n=== シンプル家計簿 ===")
    print("1. データを追加")
    print("2. 集計を表示")
    print("3. 終了")
    
    choice = input("番号を選んでください: ").strip()
```

## 🚀 実行方法

### 📦 **必要なライブラリのインストール**

```bash
# pandas ライブラリをインストール
pip install pandas

# または requirements.txt を使用
pip install -r requirements.txt
```

#### **requirements.txt の内容**
```text
pandas==2.1.4
```

### 💻 **プログラム実行**

```bash
# day80-household-csvディレクトリに移動
cd day80-household-csv

# 家計簿アプリを起動
python main.py
```

### ✅ **環境確認**

```bash
# pandas インストール確認
python -c "import pandas; print('✅ pandas installed')"
```

## 💡 使い方

### 🎯 **基本的な操作手順**

#### **1. アプリケーション起動**
```bash
$ python main.py

=== シンプル家計簿 ===
1. データを追加
2. 集計を表示
3. 終了
番号を選んでください: 
```

#### **2. データ追加（選択肢: 1）**
```bash
番号を選んでください: 1

日付を入力（YYYY-MM-DD、省略で今日）: 
項目を入力: 昼食
金額を入力（整数）: 800
✅ データを追加しました。
```

**入力のコツ**:
- **日付省略**: 空エンターで自動的に今日の日付
- **項目例**: 食費、交通費、光熱費、娯楽費など
- **金額**: 整数のみ（小数点不可）

#### **3. 集計表示（選択肢: 2）**
```bash
番号を選んでください: 2

📋 全データ:
        日付    項目    金額
0  2025-01-18   昼食   800
1  2025-01-18   交通費  200
2  2025-01-18   コーヒー 300

💰 合計金額: 1300 円

📊 項目別の合計:
項目
コーヒー    300
交通費     200
昼食      800
Name: 金額, dtype: int64
```

#### **4. アプリケーション終了（選択肢: 3）**
```bash
番号を選んでください: 3
👋 終了します。
```

### 📊 **実用的な使用例**

#### **日常的な家計管理**
```bash
# 朝の通勤
日付: （空エンター = 今日）
項目: 交通費
金額: 300

# ランチ
日付: （空エンター = 今日）
項目: 昼食
金額: 850

# 夕方のコーヒー
日付: （空エンター = 今日）
項目: コーヒー
金額: 400

# 夜の買い物
日付: （空エンター = 今日）
項目: 食材
金額: 1200
```

#### **過去データの登録**
```bash
日付: 2025-01-15
項目: 書籍
金額: 2800

日付: 2025-01-16
項目: 映画
金額: 1800
```

## 🔧 **重要な技術ポイント解説**

### 📊 **1. CSV ファイル管理の自動化**

#### **初期設定の自動化**
```python
# アプリ初回起動時の自動処理
if not os.path.exists(FILENAME):
    df_init = pd.DataFrame(columns=["日付", "項目", "金額"])
    df_init.to_csv(FILENAME, index=False)
```

**技術ポイント**:
- **ファイル存在チェック**: `os.path.exists()` による確認
- **自動初期化**: ヘッダー付きCSVファイルの作成
- **エラー防止**: 「ファイルが見つかりません」エラーの予防

#### **生成されるCSVファイル構造**
```csv
日付,項目,金額
2025-01-18,昼食,800
2025-01-18,交通費,200
2025-01-18,コーヒー,300
```

### 📝 **2. データ入力機能の詳細実装**

#### **日付入力の柔軟性**
```python
date_str = input("日付を入力（YYYY-MM-DD、省略で今日）: ").strip()
if not date_str:
    date_str = datetime.today().strftime("%Y-%m-%d")
```

**技術ポイント**:
- **省略機能**: 空入力時のデフォルト値設定
- **日付形式統一**: YYYY-MM-DD形式での一貫性
- **ユーザビリティ**: 日常使用での入力負荷軽減

#### **金額入力のバリデーション**
```python
try:
    amount = int(input("金額を入力（整数）: ").strip())
except ValueError:
    print("❌ 数字で入力してください")
    return  # 関数を安全に終了
```

**技術ポイント**:
- **型変換**: 文字列→整数の安全な変換
- **例外処理**: ValueError による無効入力の捕捉
- **早期リターン**: エラー時の適切な処理中断

#### **CSV追記保存**
```python
new_data = pd.DataFrame([[date_str, item, amount]], columns=["日付", "項目", "金額"])
new_data.to_csv(FILENAME, mode='a', header=False, index=False)
```

**技術ポイント**:
- **追記モード**: `mode='a'` で既存データを保持
- **ヘッダー制御**: `header=False` で重複ヘッダー防止
- **インデックス除外**: `index=False` で不要な行番号を除去

### 📊 **3. データ分析・集計機能**

#### **全データ表示**
```python
df = pd.read_csv(FILENAME)
print("\n📋 全データ:")
print(df)
```

#### **合計金額計算**
```python
print("\n💰 合計金額:", df["金額"].sum(), "円")
```

#### **項目別集計**
```python
print("\n📊 項目別の合計:")
print(df.groupby("項目")["金額"].sum())
```

**技術ポイント**:
- **pandas DataFrame**: 効率的なデータ操作
- **集計関数**: `sum()` による数値集計
- **グループ化**: `groupby()` によるカテゴリ別分析

### 🔄 **4. ユーザーインターフェース設計**

#### **メニュー駆動型UI**
```python
while True:
    print("\n=== シンプル家計簿 ===")
    print("1. データを追加")
    print("2. 集計を表示")
    print("3. 終了")
    
    choice = input("番号を選んでください: ").strip()
```

**技術ポイント**:
- **無限ループ**: 継続的な操作を可能にする
- **明確な選択肢**: 数値による直感的な操作
- **適切な終了**: ユーザーの意図的な終了制御

#### **入力バリデーション**
```python
if choice == "1":
    add_record()
elif choice == "2":
    show_summary()
elif choice == "3":
    print("👋 終了します。")
    break
else:
    print("❌ 無効な入力です。")
```

**技術ポイント**:
- **分岐制御**: 各選択肢への適切な処理振り分け
- **エラーメッセージ**: 無効入力時の分かりやすい通知
- **ループ継続**: エラー後も操作を継続可能

## 🎨 **カスタマイズ・拡張アイデア**

### 📈 **機能拡張案**

#### **1. 収入・支出の分類**
```python
def add_record():
    record_type = input("収入(1)・支出(2): ").strip()
    amount = int(input("金額を入力: ").strip())
    
    if record_type == "1":
        amount = abs(amount)   # 収入は正の値
    else:
        amount = -abs(amount)  # 支出は負の値
    
    new_data = pd.DataFrame([[date_str, item, amount, record_type]], 
                           columns=["日付", "項目", "金額", "種別"])
```

#### **2. 月別・期間別集計**
```python
def monthly_summary():
    df = pd.read_csv(FILENAME)
    df['日付'] = pd.to_datetime(df['日付'])
    df['年月'] = df['日付'].dt.to_period('M')
    
    monthly = df.groupby('年月')['金額'].sum()
    print("📅 月別集計:")
    for month, amount in monthly.items():
        print(f"  {month}: {amount:,} 円")
    
    # 平均計算
    avg_monthly = monthly.mean()
    print(f"\n📊 月平均: {avg_monthly:,.0f} 円")
```

#### **3. データ削除・編集機能**
```python
def delete_record():
    df = pd.read_csv(FILENAME)
    
    if df.empty:
        print("❌ 削除するデータがありません")
        return
    
    print("\n📋 現在のデータ:")
    print(df.reset_index())
    
    try:
        index = int(input("削除する行番号を入力: "))
        df = df.drop(df.index[index])
        df.to_csv(FILENAME, index=False)
        print("✅ データを削除しました")
    except (ValueError, IndexError):
        print("❌ 無効な行番号です")

def edit_record():
    df = pd.read_csv(FILENAME)
    
    if df.empty:
        print("❌ 編集するデータがありません")
        return
    
    print("\n📋 現在のデータ:")
    print(df.reset_index())
    
    try:
        index = int(input("編集する行番号を入力: "))
        
        new_item = input(f"新しい項目（現在: {df.iloc[index]['項目']}）: ").strip()
        new_amount = int(input(f"新しい金額（現在: {df.iloc[index]['金額']}）: "))
        
        df.iloc[index, df.columns.get_loc('項目')] = new_item
        df.iloc[index, df.columns.get_loc('金額')] = new_amount
        
        df.to_csv(FILENAME, index=False)
        print("✅ データを更新しました")
    except (ValueError, IndexError):
        print("❌ 無効な入力です")
```

#### **4. グラフ表示機能**
```python
import matplotlib.pyplot as plt
import seaborn as sns

def show_chart():
    df = pd.read_csv(FILENAME)
    
    if df.empty:
        print("❌ 表示するデータがありません")
        return
    
    # 項目別集計
    item_sum = df.groupby("項目")["金額"].sum().sort_values(ascending=False)
    
    # グラフ作成
    plt.figure(figsize=(12, 6))
    
    # 棒グラフ
    plt.subplot(1, 2, 1)
    item_sum.plot(kind='bar', color='skyblue')
    plt.title('項目別支出（棒グラフ）')
    plt.ylabel('金額（円）')
    plt.xticks(rotation=45)
    
    # 円グラフ
    plt.subplot(1, 2, 2)
    item_sum.plot(kind='pie', autopct='%1.1f%%')
    plt.title('項目別支出（割合）')
    plt.ylabel('')
    
    plt.tight_layout()
    plt.show()

def time_series_chart():
    df = pd.read_csv(FILENAME)
    df['日付'] = pd.to_datetime(df['日付'])
    
    # 日別集計
    daily_sum = df.groupby('日付')['金額'].sum()
    
    plt.figure(figsize=(12, 6))
    daily_sum.plot(kind='line', marker='o')
    plt.title('日別支出推移')
    plt.xlabel('日付')
    plt.ylabel('金額（円）')
    plt.grid(True, alpha=0.3)
    plt.show()
```

#### **5. データエクスポート機能**
```python
import json
from datetime import datetime

def export_data():
    df = pd.read_csv(FILENAME)
    
    print("エクスポート形式を選択:")
    print("1. JSON形式")
    print("2. Excel形式") 
    print("3. 集計レポート（テキスト）")
    
    choice = input("番号を選んでください: ").strip()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if choice == "1":
        # JSON出力
        output_file = f"household_export_{timestamp}.json"
        df.to_json(output_file, orient='records', force_ascii=False, indent=2)
        print(f"✅ JSONファイルを出力: {output_file}")
        
    elif choice == "2":
        # Excel出力
        output_file = f"household_export_{timestamp}.xlsx"
        df.to_excel(output_file, index=False)
        print(f"✅ Excelファイルを出力: {output_file}")
        
    elif choice == "3":
        # 集計レポート
        output_file = f"household_report_{timestamp}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=== 家計簿集計レポート ===\n\n")
            f.write(f"出力日時: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}\n\n")
            
            f.write("📊 全データ:\n")
            f.write(df.to_string(index=False))
            f.write("\n\n")
            
            f.write(f"💰 合計金額: {df['金額'].sum():,} 円\n\n")
            
            f.write("📈 項目別集計:\n")
            item_summary = df.groupby("項目")["金額"].sum().sort_values(ascending=False)
            for item, amount in item_summary.items():
                f.write(f"  {item}: {amount:,} 円\n")
        
        print(f"✅ レポートを出力: {output_file}")
```

#### **6. 設定ファイル対応**
```python
import json

def load_config():
    """設定ファイル読み込み"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # デフォルト設定
        default_config = {
            "csv_filename": "household.csv",
            "date_format": "%Y-%m-%d",
            "currency": "円",
            "default_categories": ["食費", "交通費", "光熱費", "娯楽費", "その他"]
        }
        
        # 設定ファイル作成
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2, ensure_ascii=False)
        
        return default_config

def show_categories():
    """よく使う項目の表示"""
    config = load_config()
    categories = config.get("default_categories", [])
    
    print("\n💡 よく使う項目:")
    for i, category in enumerate(categories, 1):
        print(f"  {i}. {category}")
    
    choice = input("番号で選択（または直接入力）: ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        return categories[int(choice) - 1]
    else:
        return choice if choice else "その他"

# 使用例: add_record関数内で
item = show_categories()
```

### 🔧 **技術的改善案**

#### **1. データバックアップ機能**
```python
import shutil
from datetime import datetime

def backup_data():
    """データファイルのバックアップ作成"""
    if not os.path.exists(FILENAME):
        print("❌ バックアップするデータがありません")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"household_backup_{timestamp}.csv"
    
    shutil.copy2(FILENAME, backup_filename)
    print(f"✅ バックアップを作成: {backup_filename}")

def restore_data():
    """バックアップからのデータ復元"""
    backup_files = [f for f in os.listdir('.') if f.startswith('household_backup_')]
    
    if not backup_files:
        print("❌ バックアップファイルが見つかりません")
        return
    
    print("利用可能なバックアップ:")
    for i, filename in enumerate(backup_files, 1):
        print(f"  {i}. {filename}")
    
    try:
        choice = int(input("復元するバックアップ番号: ")) - 1
        selected_backup = backup_files[choice]
        
        # 現在のデータをバックアップ
        backup_data()
        
        # データ復元
        shutil.copy2(selected_backup, FILENAME)
        print(f"✅ データを復元: {selected_backup}")
        
    except (ValueError, IndexError):
        print("❌ 無効な選択です")
```

#### **2. データ検証・整合性チェック**
```python
def validate_data():
    """データの整合性チェック"""
    try:
        df = pd.read_csv(FILENAME)
        
        print("🔍 データ検証結果:")
        
        # 基本統計
        print(f"  📊 総レコード数: {len(df)}")
        print(f"  📅 データ期間: {df['日付'].min()} ～ {df['日付'].max()}")
        
        # 異常値チェック
        negative_amounts = df[df['金額'] < 0]
        if not negative_amounts.empty:
            print(f"  ⚠️ 負の金額: {len(negative_amounts)} 件")
        
        large_amounts = df[df['金額'] > 50000]  # 5万円以上
        if not large_amounts.empty:
            print(f"  💰 高額取引: {len(large_amounts)} 件")
        
        # 重複チェック
        duplicates = df.duplicated(subset=['日付', '項目', '金額'])
        if duplicates.any():
            print(f"  🔄 重複データ: {duplicates.sum()} 件")
        
        # 空白データチェック
        missing_data = df.isnull().sum()
        if missing_data.any():
            print(f"  ❌ 欠損データ: {missing_data.sum()} 件")
        
        print("✅ データ検証完了")
        
    except Exception as e:
        print(f"❌ 検証エラー: {e}")
```

#### **3. コマンドライン引数対応**
```python
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='シンプル家計簿アプリ')
    parser.add_argument('-f', '--file', default='household.csv', help='データファイル名')
    parser.add_argument('--add', nargs=3, metavar=('DATE', 'ITEM', 'AMOUNT'), 
                       help='データ追加 (日付 項目 金額)')
    parser.add_argument('--summary', action='store_true', help='集計表示のみ')
    parser.add_argument('--backup', action='store_true', help='バックアップ作成')
    
    return parser.parse_args()

# 使用例: python main.py --add 2025-01-18 昼食 800
```

## 🚨 **トラブルシューティング**

### 🔧 **よくあるエラーと解決方法**

#### **1. pandas インストールエラー**
```bash
# エラー例
ModuleNotFoundError: No module named 'pandas'

# 解決方法
pip install pandas

# または仮想環境で
python -m venv household_env
source household_env/bin/activate  # Windows: household_env\Scripts\activate
pip install pandas
```

#### **2. CSVファイル読み込みエラー**
```bash
# エラー例
FileNotFoundError: [Errno 2] No such file or directory: 'household.csv'

# 解決方法
# アプリが自動的にファイルを作成しますが、権限エラーの場合:
# 1. ディレクトリの書き込み権限確認
# 2. 他のアプリでファイルが開かれていないか確認
```

#### **3. 文字化けエラー**
```python
# 問題のあるコード
df = pd.read_csv(FILENAME)  # 文字化け

# 解決方法
df = pd.read_csv(FILENAME, encoding='utf-8')

# さらに安全な方法
try:
    df = pd.read_csv(FILENAME, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(FILENAME, encoding='shift_jis')
```

#### **4. 金額入力エラー**
```python
# エラー防止の改善版
def safe_input_amount():
    while True:
        try:
            amount_str = input("金額を入力（整数）: ").strip()
            amount = int(amount_str)
            
            if amount < 0:
                print("⚠️ 正の数値を入力してください")
                continue
                
            return amount
        except ValueError:
            print("❌ 数字で入力してください")
```

#### **5. データ破損対応**
```python
def repair_csv():
    """破損CSVファイルの修復"""
    try:
        # バックアップ作成
        if os.path.exists(FILENAME):
            shutil.copy2(FILENAME, f"{FILENAME}.backup")
        
        # データ読み込み・修復
        df = pd.read_csv(FILENAME)
        
        # 必要な列の確認・追加
        required_columns = ["日付", "項目", "金額"]
        for col in required_columns:
            if col not in df.columns:
                df[col] = ""
        
        # データ型修正
        df['金額'] = pd.to_numeric(df['金額'], errors='coerce').fillna(0).astype(int)
        
        # 修復したデータを保存
        df.to_csv(FILENAME, index=False)
        print("✅ CSVファイルを修復しました")
        
    except Exception as e:
        print(f"❌ 修復エラー: {e}")
```

## 📖 学んだことや今後の改善案（学習ログ）

### 🎯 **重要な技術習得**

#### **1. pandas データ処理の実践的理解**

**DataFrame操作の基本パターン**:
```python
# データ処理の典型的な流れ
df = pd.read_csv(FILENAME)           # 読み込み
df.groupby("項目")["金額"].sum()     # 集計
df.to_csv(FILENAME, mode='a')        # 保存
```

**重要な発見**:
- **pandas の威力**: 少ないコードで高度な集計処理
- **DataFrame の直感性**: Excelライクな操作感覚
- **集計関数の豊富さ**: sum, mean, count, groupby等

#### **2. CSV ファイル操作・データ永続化**

**追記モードの活用**:
```python
# 既存データを保持しながら新規データ追加
new_data.to_csv(FILENAME, mode='a', header=False, index=False)
```

**学習ポイント**:
- **mode='a'**: 追記モードによるデータ蓄積
- **header=False**: 重複ヘッダーの防止
- **自動初期化**: 初回起動時のファイル作成

#### **3. エラーハンドリング・バリデーション設計**

**型変換の安全な実装**:
```python
try:
    amount = int(input("金額を入力: "))
except ValueError:
    print("❌ 数字で入力してください")
    return  # 早期リターンでエラー伝播防止
```

**設計パターン**:
- **try-except**: 予期される例外の適切な処理
- **早期リターン**: エラー時の処理中断
- **ユーザーフレンドリー**: 分かりやすいエラーメッセージ

#### **4. 実用アプリケーションの設計パターン**

**メニュー駆動型UIの実装**:
```python
while True:                    # 継続的な操作
    choice = input("選択: ")    # ユーザー入力
    
    if choice == "1":
        add_record()           # 機能別関数呼び出し
    elif choice == "3":
        break                  # 適切な終了条件
```

**設計思想**:
- **関数分割**: 機能別の適切な分離
- **継続性**: ループによる連続操作対応
- **直感性**: 数字選択による分かりやすいUI

### 🚀 **実用的な開発スキル向上**

#### **1. データ分析アプリケーション基盤**
- **pandas 活用**: データフレーム操作・集計処理
- **CSV 連携**: ファイルI/O・データ永続化技術
- **可視化準備**: 集計データの構造化・分析準備

#### **2. ユーザビリティを考慮した設計**
- **入力負荷軽減**: デフォルト値・省略機能
- **エラー対応**: 分かりやすいメッセージ・継続可能な処理
- **直感的操作**: メニュー選択・段階的入力

#### **3. 実用ツール開発の基本パターン**
- **データ管理**: CRUD操作（作成・読み取り・更新・削除）
- **集計・分析**: グループ化・統計処理・レポート生成
- **保守性**: 設定分離・バックアップ・データ検証

### 💡 **重要な気づき・学習成果**

#### **1. 「実用性と学習価値の両立」の実現**
```python
# 実際に使える家計簿として機能しながら
# データ処理・ファイル操作の学習も達成

# 日常使用での価値
日々の支出記録 → 月末の集計分析 → 家計改善

# 技術学習での価値  
pandas操作 → CSV処理 → エラーハンドリング
```

#### **2. pandas の実用性の実感**
```python
# 従来のファ# 💰 シンプル家計簿アプリ (Household CSV Manager)

Python の pandas ライブラリを活用したシンプルで実用的な家計簿管理アプリケーションです。CSV形式でのデータ永続化・pandas による集計分析・直感的なコンソールインターフェースを組み合わせ、データ処理技術・ファイル操作・実用ツール開発の重要な技術要素を実践的に学べるプロジェクトです。

## 📝 アプリケーション概要

**主な機能**:
- **データ追加**: 日付・項目・金額の家計データ登録
- **集計表示**: 全データ一覧・合計金額・項目別集計
- **CSV管理**: データの永続化・自動ファイル初期化
- **バリデーション**: 入力データの検証・エラーハンドリング
- **ユーザビリティ**: 日付省略・直感的メニュー操作

**学習ポイント**:
- **pandas データ処理**: DataFrame操作・集計分析の実践
- **CSV ファイル操作**: 読み書き・追記モード・データ永続化
- **エラーハンドリング**: 型変換・入力バリデーション
- **実用アプリ設計**: メニュー駆動・ユーザビリティ考慮
- **データ分析基盤**: 実用的な集計・可視化の基礎

## 📁 ファイル構成

```
day80-household-csv/
├── main.py          # メインプログラム（家計簿機能）
├── README.md        # このファイル
├── requirements.txt # 依存関係
└── household.csv    # データファイル（自動生成）
```

### 🎯 **main.py の構造**

#### **1. 初期設定・自動ファイル作成**
```python
FILENAME = "household.csv"

# 初回起動時の自動セットアップ
if not os.path.exists(FILENAME):
    df_init = pd.DataFrame(columns=["日付", "項目", "金額"])
    df_init.to_csv(FILENAME, index=False)
```

#### **2. データ追加機能（add_record）**
```python
def add_record():
    # 日付入力の柔軟性（省略で今日の日付）
    date_str = input("日付を入力（YYYY-MM-DD、省略で今日）: ").strip()
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")
    
    # 金額入力のバリデーション
    try:
        amount = int(input("金額を入力（整数）: ").strip())
    except ValueError:
        print("❌ 数字で入力してください")
        return
    
    # CSV追記保存
    new_data = pd.DataFrame([[date_str, item, amount]], columns=["日付", "項目", "金額"])
    new_data.to_csv(FILENAME, mode='a', header=False, index=False)
```

#### **3. 集計分析機能（show_summary）**
```python
def show_summary():
    df = pd.read_csv(FILENAME)
    print("\n📋 全データ:")
    print(df)
    
    print("\n💰 合計金額:", df["金額"].sum(), "円")
    
    print("\n📊 項目別の合計:")
    print(df.groupby("項目")["金額"].sum())
```

#### **4. メインループ・UI制御**
```python
while True:
    print("\n=== シンプル家計簿 ===")
    print("1. データを追加")
    print("2. 集計を表示")
    print("3. 終了")
    
    choice = input("番号を選んでください: ").strip()
```

## 🚀 実行方法

### 📦 **必要なライブラリのインストール**

```bash
# pandas ライブラリをインストール
pip install pandas

# または requirements.txt を使用
pip install -r requirements.txt
```

#### **requirements.txt の内容**
```text
pandas==2.1.4
```

### 💻 **プログラム実行**

```bash
# day80-household-csvディレクトリに移動
cd day80-household-csv

# 家計簿アプリを起動
python main.py
```

### ✅ **環境確認**

```bash
# pandas インストール確認
python -c "import pandas; print('✅ pandas installed')"
```

## 💡 使い方

### 🎯 **基本的な操作手順**

#### **1. アプリケーション起動**
```bash
$ python main.py

=== シンプル家計簿 ===
1. データを追加
2. 集計を表示
3. 終了
番号を選んでください: 
```

#### **2. データ追加（選択肢: 1）**
```bash
番号を選んでください: 1

日付を入力（YYYY-MM-DD、省略で今日）: 
項目を入力: 昼食
金額を入力（整数）: 800
✅ データを追加しました。
```

**入力のコツ**:
- **日付省略**: 空エンターで自動的に今日の日付
- **項目例**: 食費、交通費、光熱費、娯楽費など
- **金額**: 整数のみ（小数点不可）

#### **3. 集計表示（選択肢: 2）**
```bash
番号を選んでください: 2

📋 全データ:
        日付    項目    金額
0  2025-01-18   昼食   800
1  2025-01-18   交通費  200
2  2025-01-18   コーヒー 300

💰 合計金額: 1300 円

📊 項目別の合計:
項目
コーヒー    300
交通費     200
昼食      800
Name: 金額, dtype: int64
```

#### **4. アプリケーション終了（選択肢: 3）**
```bash
番号を選んでください: 3
👋 終了します。
```

### 📊 **実用的な使用例**

#### **日常的な家計管理**
```bash
# 朝の通勤
日付: （空エンター = 今日）
項目: 交通費
金額: 300

# ランチ
日付: （空エンター = 今日）
項目: 昼食
金額: 850

# 夕方のコーヒー
日付: （空エンター = 今日）
項目: コーヒー
金額: 400

# 夜の買い物
日付: （空エンター = 今日）
項目: 食材
金額: 1200
```

#### **過去データの登録**
```bash
日付: 2025-01-15
項目: 書籍
金額: 2800

日付: 2025-01-16
項目: 映画
金額: 1800
```

## 🔧 **重要な技術ポイント解説**

### 📊 **1. CSV ファイル管理の自動化**

#### **初期設定の自動化**
```python
# アプリ初回起動時の自動処理
if not os.path.exists(FILENAME):
    df_init = pd.DataFrame(columns=["日付", "項目", "金額"])
    df_init.to_csv(FILENAME, index=False)
```

**技術ポイント**:
- **ファイル存在チェック**: `os.path.exists()` による確認
- **自動初期化**: ヘッダー付きCSVファイルの作成
- **エラー防止**: 「ファイルが見つかりません」エラーの予防

#### **生成されるCSVファイル構造**
```csv
日付,項目,金額
2025-01-18,昼食,800
2025-01-18,交通費,200
2025-01-18,コーヒー,300
```

### 📝 **2. データ入力機能の詳細実装**

#### **日付入力の柔軟性**
```python
date_str = input("日付を入力（YYYY-MM-DD、省略で今日）: ").strip()
if not date_str:
    date_str = datetime.today().strftime("%Y-%m-%d")
```

**技術ポイント**:
- **省略機能**: 空入力時のデフォルト値設定
- **日付形式統一**: YYYY-MM-DD形式での一貫性
- **ユーザビリティ**: 日常使用での入力負荷軽減

#### **金額入力のバリデーション**
```python
try:
    amount = int(input("金額を入力（整数）: ").strip())
except ValueError:
    print("❌ 数字で入力してください")
    return  # 関数を安全に終了
```

**技術ポイント**:
- **型変換**: 文字列→整数の安全な変換
- **例外処理**: ValueError による無効入力の捕捉
- **早期リターン**: エラー時の適切な処理中断

#### **CSV追記保存**
```python
new_data = pd.DataFrame([[date_str, item, amount]], columns=["日付", "項目", "金額"])
new_data.to_csv(FILENAME, mode='a', header=False, index=False)
```

**技術ポイント**:
- **追記モード**: `mode='a'` で既存データを保持
- **ヘッダー制御**: `header=False` で重複ヘッダー防止
- **インデックス除外**: `index=False` で不要な行番号を除去

### 📊 **3. データ分析・集計機能**

#### **全データ表示**
```python
df = pd.read_csv(FILENAME)
print("\n📋 全データ:")
print(df)
```

#### **合計金額計算**
```python
print("\n💰 合計金額:", df["金額"].sum(), "円")
```

#### **項目別集計**
```python
print("\n📊 項目別の合計:")
print(df.groupby("項目")["金額"].sum())
```

**技術ポイント**:
- **pandas DataFrame**: 効率的なデータ操作
- **集計関数**: `sum()` による数値集計
- **グループ化**: `groupby()` によるカテゴリ別分析

### 🔄 **4. ユーザーインターフェース設計**

#### **メニュー駆動型UI**
```python
while True:
    print("\n=== シンプル家計簿 ===")
    print("1. データを追加")
    print("2. 集計を表示")
    print("3. 終了")
    
    choice = input("番号を選んでください: ").strip()
```

**技術ポイント**:
- **無限ループ**: 継続的な操作を可能にする
- **明確な選択肢**: 数値による直感的な操作
- **適切な終了**: ユーザーの意図的な終了制御

#### **入力バリデーション**
```python
if choice == "1":
    add_record()
elif choice == "2":
    show_summary()
elif choice == "3":
    print("👋 終了します。")
    break
else:
    print("❌ 無効な入力です。")
```

**技術ポイント**:
- **分岐制御**: 各選択肢への適切な処理振り分け
- **エラーメッセージ**: 無効入力時の分かりやすい通知
- **ループ継続**: エラー後も操作を継続可能

## 🎨 **カスタマイズ・拡張アイデア**

### 📈 **機能拡張案**

#### **1. 収入・支出の分類**
```python
def add_record():
    record_type = input("収入(1)・支出(2): ").strip()
    amount = int(input("金額を入力: ").strip())
    
    if record_type == "1":
        amount = abs(amount)   # 収入は正の値
    else:
        amount = -abs(amount)  # 支出は負の値
    
    new_data = pd.DataFrame([[date_str, item, amount, record_type]], 
                           columns=["日付", "項目", "金額", "種別"])
```

#### **2. 月別・期間別集計**
```python
def monthly_summary():
    df = pd.read_csv(FILENAME)
    df['日付'] = pd.to_datetime(df['日付'])
    df['年月'] = df['日付'].dt.to_period('M')
    
    monthly = df.groupby('年月')['金額'].sum()
    print("📅 月別集計:")
    for month, amount in monthly.items():
        print(f"  {month}: {amount:,} 円")
    
    # 平均計算
    avg_monthly = monthly.mean()
    print(f"\n📊 月平均: {avg_monthly:,.0f} 円")
```

#### **3. データ削除・編集機能**
```python
def delete_record():
    df = pd.read_csv(FILENAME)
    
    if df.empty:
        print("❌ 削除するデータがありません")
        return
    
    print("\n📋 現在のデータ:")
    print(df.reset_index())
    
    try:
        index = int(input("削除する行番号を入力: "))
        df = df.drop(df.index[index])
        df.to_csv(FILENAME, index=False)
        print("✅ データを削除しました")
    except (ValueError, IndexError):
        print("❌ 無効な行番号です")

def edit_record():
    df = pd.read_csv(FILENAME)
    
    if df.empty:
        print("❌ 編集するデータがありません")
        return
    
    print("\n📋 現在のデータ:")
    print(df.reset_index())
    
    try:
        index = int(input("編集する行番号を入力: "))
        
        new_item = input(f"新しい項目（現在: {df.iloc[index]['項目']}）: ").strip()
        new_amount = int(input(f"新しい金額（現在: {df.iloc[index]['金額']}）: "))
        
        df.iloc[index, df.columns.get_loc('項目')] = new_item
        df.iloc[index, df.columns.get_loc('金額')] = new_amount
        
        df.to_csv(FILENAME, index=False)
        print("✅ データを更新しました")
    except (ValueError, IndexError):
        print("❌ 無効な入力です")
```

#### **4. グラフ表示機能**
```python
import matplotlib.pyplot as plt
import seaborn as sns

def show_chart():
    df = pd.read_csv(FILENAME)
    
    if df.empty:
        print("❌ 表示するデータがありません")
        return
    
    # 項目別集計
    item_sum = df.groupby("項目")["金額"].sum().sort_values(ascending=False)
    
    # グラフ作成
    plt.figure(figsize=(12, 6))
    
    # 棒グラフ
    plt.subplot(1, 2, 1)
    item_sum.plot(kind='bar', color='skyblue')
    plt.title('項目別支出（棒グラフ）')
    plt.ylabel('金額（円）')
    plt.xticks(rotation=45)
    
    # 円グラフ
    plt.subplot(1, 2, 2)
    item_sum.plot(kind='pie', autopct='%1.1f%%')
    plt.title('項目別支出（割合）')
    plt.ylabel('')
    
    plt.tight_layout()
    plt.show()

def time_series_chart():
    df = pd.read_csv(FILENAME)
    df['日付'] = pd.to_datetime(df['日付'])
    
    # 日別集計
    daily_sum = df.groupby('日付')['金額'].sum()
    
    plt.figure(figsize=(12, 6))
    daily_sum.plot(kind='line', marker='o')
    plt.title('日別支出推移')
    plt.xlabel('日付')
    plt.ylabel('金額（円）')
    plt.grid(True, alpha=0.3)
    plt.show()
```

#### **5. データエクスポート機能**
```python
import json
from datetime import datetime

def export_data():
    df = pd.read_csv(FILENAME)
    
    print("エクスポート形式を選択:")
    print("1. JSON形式")
    print("2. Excel形式") 
    print("3. 集計レポート（テキスト）")
    
    choice = input("番号を選んでください: ").strip()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if choice == "1":
        # JSON出力
        output_file = f"household_export_{timestamp}.json"
        df.to_json(output_file, orient='records', force_ascii=False, indent=2)
        print(f"✅ JSONファイルを出力: {output_file}")
        
    elif choice == "2":
        # Excel出力
        output_file = f"household_export_{timestamp}.xlsx"
        df.to_excel(output_file, index=False)
        print(f"✅ Excelファイルを出力: {output_file}")
        
    elif choice == "3":
        # 集計レポート
        output_file = f"household_report_{timestamp}.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=== 家計簿集計レポート ===\n\n")
            f.write(f"出力日時: {datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}\n\n")
            
            f.write("📊 全データ:\n")
            f.write(df.to_string(index=False))
            f.write("\n\n")
            
            f.write(f"💰 合計金額: {df['金額'].sum():,} 円\n\n")
            
            f.write("📈 項目別集計:\n")
            item_summary = df.groupby("項目")["金額"].sum().sort_values(ascending=False)
            for item, amount in item_summary.items():
                f.write(f"  {item}: {amount:,} 円\n")
        
        print(f"✅ レポートを出力: {output_file}")
```

#### **6. 設定ファイル対応**
```python
import json

def load_config():
    """設定ファイル読み込み"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        # デフォルト設定
        default_config = {
            "csv_filename": "household.csv",
            "date_format": "%Y-%m-%d",
            "currency": "円",
            "default_categories": ["食費", "交通費", "光熱費", "娯楽費", "その他"]
        }
        
        # 設定ファイル作成
        with open('config.json', 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=2, ensure_ascii=False)
        
        return default_config

def show_categories():
    """よく使う項目の表示"""
    config = load_config()
    categories = config.get("default_categories", [])
    
    print("\n💡 よく使う項目:")
    for i, category in enumerate(categories, 1):
        print(f"  {i}. {category}")
    
    choice = input("番号で選択（または直接入力）: ").strip()
    
    if choice.isdigit() and 1 <= int(choice) <= len(categories):
        return categories[int(choice) - 1]
    else:
        return choice if choice else "その他"

# 使用例: add_record関数内で
item = show_categories()
```

### 🔧 **技術的改善案**

#### **1. データバックアップ機能**
```python
import shutil
from datetime import datetime

def backup_data():
    """データファイルのバックアップ作成"""
    if not os.path.exists(FILENAME):
        print("❌ バックアップするデータがありません")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"household_backup_{timestamp}.csv"
    
    shutil.copy2(FILENAME, backup_filename)
    print(f"✅ バックアップを作成: {backup_filename}")

def restore_data():
    """バックアップからのデータ復元"""
    backup_files = [f for f in os.listdir('.') if f.startswith('household_backup_')]
    
    if not backup_files:
        print("❌ バックアップファイルが見つかりません")
        return
    
    print("利用可能なバックアップ:")
    for i, filename in enumerate(backup_files, 1):
        print(f"  {i}. {filename}")
    
    try:
        choice = int(input("復元するバックアップ番号: ")) - 1
        selected_backup = backup_files[choice]
        
        # 現在のデータをバックアップ
        backup_data()
        
        # データ復元
        shutil.copy2(selected_backup, FILENAME)
        print(f"✅ データを復元: {selected_backup}")
        
    except (ValueError, IndexError):
        print("❌ 無効な選択です")
```

#### **2. データ検証・整合性チェック**
```python
def validate_data():
    """データの整合性チェック"""
    try:
        df = pd.read_csv(FILENAME)
        
        print("🔍 データ検証結果:")
        
        # 基本統計
        print(f"  📊 総レコード数: {len(df)}")
        print(f"  📅 データ期間: {df['日付'].min()} ～ {df['日付'].max()}")
        
        # 異常値チェック
        negative_amounts = df[df['金額'] < 0]
        if not negative_amounts.empty:
            print(f"  ⚠️ 負の金額: {len(negative_amounts)} 件")
        
        large_amounts = df[df['金額'] > 50000]  # 5万円以上
        if not large_amounts.empty:
            print(f"  💰 高額取引: {len(large_amounts)} 件")
        
        # 重複チェック
        duplicates = df.duplicated(subset=['日付', '項目', '金額'])
        if duplicates.any():
            print(f"  🔄 重複データ: {duplicates.sum()} 件")
        
        # 空白データチェック
        missing_data = df.isnull().sum()
        if missing_data.any():
            print(f"  ❌ 欠損データ: {missing_data.sum()} 件")
        
        print("✅ データ検証完了")
        
    except Exception as e:
        print(f"❌ 検証エラー: {e}")
```

#### **3. コマンドライン引数対応**
```python
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='シンプル家計簿アプリ')
    parser.add_argument('-f', '--file', default='household.csv', help='データファイル名')
    parser.add_argument('--add', nargs=3, metavar=('DATE', 'ITEM', 'AMOUNT'), 
                       help='データ追加 (日付 項目 金額)')
    parser.add_argument('--summary', action='store_true', help='集計表示のみ')
    parser.add_argument('--backup', action='store_true', help='バックアップ作成')
    
    return parser.parse_args()

# 使用例: python main.py --add 2025-01-18 昼食 800
```

## 🚨 **トラブルシューティング**

### 🔧 **よくあるエラーと解決方法**

#### **1. pandas インストールエラー**
```bash
# エラー例
ModuleNotFoundError: No module named 'pandas'

# 解決方法
pip install pandas

# または仮想環境で
python -m venv household_env
source household_env/bin/activate  # Windows: household_env\Scripts\activate
pip install pandas
```

#### **2. CSVファイル読み込みエラー**
```bash
# エラー例
FileNotFoundError: [Errno 2] No such file or directory: 'household.csv'

# 解決方法
# アプリが自動的にファイルを作成しますが、権限エラーの場合:
# 1. ディレクトリの書き込み権限確認
# 2. 他のアプリでファイルが開かれていないか確認
```

#### **3. 文字化けエラー**
```python
# 問題のあるコード
df = pd.read_csv(FILENAME)  # 文字化け

# 解決方法
df = pd.read_csv(FILENAME, encoding='utf-8')

# さらに安全な方法
try:
    df = pd.read_csv(FILENAME, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(FILENAME, encoding='shift_jis')
```

#### **4. 金額入力エラー**
```python
# エラー防止の改善版
def safe_input_amount():
    while True:
        try:
            amount_str = input("金額を入力（整数）: ").strip()
            amount = int(amount_str)
            
            if amount < 0:
                print("⚠️ 正の数値を入力してください")
                continue
                
            return amount
        except ValueError:
            print("❌ 数字で入力してください")
```

#### **5. データ破損対応**
```python
def repair_csv():
    """破損CSVファイルの修復"""
    try:
        # バックアップ作成
        if os.path.exists(FILENAME):
            shutil.copy2(FILENAME, f"{FILENAME}.backup")
        
        # データ読み込み・修復
        df = pd.read_csv(FILENAME)
        
        # 必要な列の確認・追加
        required_columns = ["日付", "項目", "金額"]
        for col in required_columns:
            if col not in df.columns:
                df[col] = ""
        
        # データ型修正
        df['金額'] = pd.to_numeric(df['金額'], errors='coerce').fillna(0).astype(int)
        
        # 修復したデータを保存
        df.to_csv(FILENAME, index=False)
        print("✅ CSVファイルを修復しました")
        
    except Exception as e:
        print(f"❌ 修復エラー: {e}")
```

## 📖 学んだことや今後の改善案（学習ログ）

### 🎯 **重要な技術習得**

#### **1. pandas データ処理の実践的理解**

**DataFrame操作の基本パターン**:
```python
# データ処理の典型的な流れ
df = pd.read_csv(FILENAME)           # 読み込み
df.groupby("項目")["金額"].sum()     # 集計
df.to_csv(FILENAME, mode='a')        # 保存
```

**重要な発見**:
- **pandas の威力**: 少ないコードで高度な集計処理
- **DataFrame の直感性**: Excelライクな操作感覚
- **集計関数の豊富さ**: sum, mean, count, groupby等

#### **2. CSV ファイル操作・データ永続化**

**追記モードの活用**:
```python
# 既存データを保持しながら新規データ追加
new_data.to_csv(FILENAME, mode='a', header=False, index=False)
```

**学習ポイント**:
- **mode='a'**: 追記モードによるデータ蓄積
- **header=False**: 重複ヘッダーの防止
- **自動初期化**: 初回起動時のファイル作成

#### **3. エラーハンドリング・バリデーション設計**

**型変換の安全な実装**:
```python
try:
    amount = int(input("金額を入力: "))
except ValueError:
    print("❌ 数字で入力してください")
    return  # 早期リターンでエラー伝播防止
```

**設計パターン**:
- **try-except**: 予期される例外の適切な処理
- **早期リターン**: エラー時の処理中断
- **ユーザーフレンドリー**: 分かりやすいエラーメッセージ

#### **4. 実用アプリケーションの設計パターン**

**メニュー駆動型UIの実装**:
```python
while True:                    # 継続的な操作
    choice = input("選択: ")    # ユーザー入力
    
    if choice == "1":
        add_record()           # 機能別関数呼び出し
    elif choice == "3":
        break                  # 適切な終了条件
```

**設計思想**:
- **関数分割**: 機能別の適切な分離
- **継続性**: ループによる連続操作対応
- **直感性**: 数字選択による分かりやすいUI

### 🚀 **実用的な開発スキル向上**

#### **1. データ分析アプリケーション基盤**
- **pandas 活用**: データフレーム操作・集計処理
- **CSV 連携**: ファイルI/O・データ永続化技術
- **可視化準備**: 集計データの構造化・分析準備

#### **2. ユーザビリティを考慮した設計**
- **入力負荷軽減**: デフォルト値・省略機能
- **エラー対応**: 分かりやすいメッセージ・継続可能な処理
- **直感的操作**: メニュー選択・段階的入力

#### **3. 実用ツール開発の基本パターン**
- **データ管理**: CRUD操作（作成・読み取り・更新・削除）
- **集計・分析**: グループ化・統計処理・レポート生成
- **保守性**: 設定分離・バックアップ・データ検証

### 💡 **重要な気づき・学習成果**

#### **1. 「実用性と学習価値の両立」の実現**
```python
# 実際に使える家計簿として機能しながら
# データ処理・ファイル操作の学習も達成

# 日常使用での価値
日々の支出記録 → 月末の集計分析 → 家計改善

# 技術学習での価値  
pandas操作 → CSV処理 → エラーハンドリング
```

#### **2. pandas の実用性の実感**
```python
# 従来