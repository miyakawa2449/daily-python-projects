# ⏰ Timer App

## 🚀 実行方法
```bash
cd day58-timer
python main.py
```

## 💡 使い方

時間を以下の形式で入力できます：
- `1h30m` - 1時間30分
- `2m` - 2分
- `45s` - 45秒
- `1h30m45s` - 1時間30分45秒

実行中は **Ctrl+C** でキャンセル可能です。

## 📖 学んだことや今後の改善案（学習ログ）

### 🔧 parse_time_string 関数の詳細解説

```python
def parse_time_string(time_str):
    pattern = r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?"
    cleaned = time_str.strip().lower().replace(" ", "")
    match = re.fullmatch(pattern, cleaned)
    if not match:
        return None

    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = int(match.group(3)) if match.group(3) else 0

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds if total_seconds > 0 else None
```

#### 🎯 この関数の役割
ユーザーが入力した時間文字列（例：`"1h30m"`）を秒数に変換する

#### 📋 処理の流れ

1. **正規表現パターンの定義**
   ```python
   pattern = r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?"
   ```
   
   まず、**正規表現とは「文字列のパターンを表現する方法」**です。
   
   **🔍 この正規表現を分解してみましょう：**
   
   ```
   (?:(\d+)h)?  (?:(\d+)m)?  (?:(\d+)s)?
   ↑時間部分    ↑分部分     ↑秒部分
   ```
   
   **📝 各記号の意味：**
   - **`\d`** = 数字1文字（0〜9のどれか）
   - **`\d+`** = 数字が1文字以上連続（例：`1`, `12`, `345`）
   - **`h`** = 文字通りの "h"
   - **`(...)`** = 括弧内をグループ化（後で取り出せる）
   - **`(?:...)`** = グループ化するが番号を付けない
   - **`?`** = 直前の要素が「あってもなくてもOK」
   
   **🎯 具体例で理解しよう：**
   
   | 入力例 | マッチする部分 | 説明 |
   |--------|----------------|------|
   | `"1h30m"` | `1h` + `30m` | 時間と分がマッチ |
   | `"45s"` | `45s` | 秒だけマッチ |
   | `"2h"` | `2h` | 時間だけマッチ |
   | `"1h30m45s"` | `1h` + `30m` + `45s` | 全部マッチ |
   | `"abc"` | マッチしない | 数字+単位の形式ではない |
   
   **🔧 なぜこの形になっているか：**
   ```python
   (?:(\d+)h)?  # 時間部分：「数字 + h」があってもなくてもOK
   (?:(\d+)m)?  # 分部分：「数字 + m」があってもなくてもOK  
   (?:(\d+)s)?  # 秒部分：「数字 + s」があってもなくてもOK
   ```
   
   **💡 キャプチャグループの仕組み：**
   ```python
   pattern = r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?"
                  ↑1番目    ↑2番目    ↑3番目
   ```
   - **`(\d+)`** の部分だけが「キャプチャ」される（数字を取り出せる）
   - `"1h30m"` → `group(1)="1"`, `group(2)="30"`, `group(3)=None`
   
   **🎨 もしも正規表現を使わずに書いたら...**
   ```python
   # こんな複雑なコードになってしまいます！
   def parse_time_without_regex(time_str):
       time_str = time_str.strip().lower().replace(" ", "")
       hours = 0
       minutes = 0
       seconds = 0
       
       # hを探す
       if 'h' in time_str:
           h_pos = time_str.find('h')
           hours = int(time_str[:h_pos])
           time_str = time_str[h_pos+1:]
       
       # mを探す
       if 'm' in time_str:
           m_pos = time_str.find('m')
           minutes = int(time_str[:m_pos])
           time_str = time_str[m_pos+1:]
       
       # sを探す
       if 's' in time_str:
           s_pos = time_str.find('s')
           seconds = int(time_str[:s_pos])
       
       return hours * 3600 + minutes * 60 + seconds
   ```
   
   **✨ 正規表現の威力**
   - 1行で複雑なパターンを表現
   - エラーチェックも自動
   - 可読性が高い（慣れれば）

2. **入力文字列の正規化**
   ```python
   cleaned = time_str.strip().lower().replace(" ", "")
   ```
   - `strip()` : 前後の空白を削除
   - `lower()` : 大文字を小文字に変換（`"1H30M"` → `"1h30m"`）
   - `replace(" ", "")` : 空白を削除（`"1h 30m"` → `"1h30m"`）

3. **パターンマッチング**
   ```python
   match = re.fullmatch(pattern, cleaned)
   ```
   
   **🔍 重要な理解ポイント：**
   
   ここでは**2つの変数を同時に処理しているのではありません**！
   
   **実際の処理の流れ：**
   1. **`pattern`** = 「どんな形式を受け入れるか」のルール（設計図）
   2. **`cleaned`** = ユーザーが入力した文字列を綺麗にした実際のデータ
   3. **`re.fullmatch()`** = patternのルールでcleanedをチェック
   4. **`match`** = チェックの結果（マッチしたかどうか + 抽出した数字）
   
   **🎯 具体例で理解しよう：**
   
   ```python
   # 例1: "1h30m" を入力した場合
   pattern = r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?"  # ルール（固定）
   cleaned = "1h30m"                                # 入力データ
   match = re.fullmatch(pattern, cleaned)           # ルールでデータをチェック
   # → match には「1」と「30」が格納される
   
   # 例2: "abc" を入力した場合  
   pattern = r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?"  # ルール（同じ）
   cleaned = "abc"                                  # 入力データ
   match = re.fullmatch(pattern, cleaned)           # ルールでデータをチェック
   # → match は None（マッチしない）
   ```
   
   **💡 `pattern` vs `cleaned` の関係：**
   
   | 変数 | 役割 | 例 |
   |------|------|-----|
   | **`pattern`** | **判定ルール**（固定） | `r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?"` |
   | **`cleaned`** | **実際の入力データ** | `"1h30m"`, `"45s"`, `"abc"`など |
   | **`match`** | **判定結果** | マッチした場合は数字を含む、しなければ`None` |
   
   **🔧 2つのケースに分かれることはありません：**
   
   - **ケース1**: `cleaned`が`pattern`にマッチ → `match`に結果が入る ✅
   - **ケース2**: `cleaned`が`pattern`にマッチしない → `match`は`None` ❌
   
   **📝 実際の動作例：**
   ```python
   # 成功例
   pattern = r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?"
   cleaned = "1h30m"
   match = re.fullmatch(pattern, cleaned)
   print(match.group(1))  # "1"
   print(match.group(2))  # "30" 
   print(match.group(3))  # None
   
   # 失敗例
   pattern = r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?"
   cleaned = "hello"
   match = re.fullmatch(pattern, cleaned)
   print(match)  # None
   # match.group(1) # エラー！matchがNoneなのでgroupメソッドは使えない
   ```
   
   **🎨 料理のレシピに例えると：**
   - **`pattern`** = レシピ（「小麦粉100g + 卵1個 + 牛乳200ml」）
   - **`cleaned`** = 実際の材料（「小麦粉150g + 卵2個」）
   - **`match`** = レシピと材料の照合結果（「小麦粉OK、卵OK、牛乳なし」）
   
   つまり、`re.fullmatch()`は「ルール」と「データ」を照合して、**1つの結果**を返すだけです！

4. **数値の抽出**
   ```python
   hours = int(match.group(1)) if match.group(1) else 0
   minutes = int(match.group(2)) if match.group(2) else 0
   seconds = int(match.group(3)) if match.group(3) else 0
   ```
   - `match.group(n)` : n番目のキャプチャグループから数字を取得
   - **三項演算子**でNoneの場合は0を代入
   - 例：`"1h30m"` → `group(1)="1"`, `group(2)="30"`, `group(3)=None`

5. **秒数への変換**
   ```python
   total_seconds = hours * 3600 + minutes * 60 + seconds
   ```
   - 1時間 = 3600秒、1分 = 60秒として計算

6. **結果の検証と返却**
   ```python
   return total_seconds if total_seconds > 0 else None
   ```
   - 0以下の場合はNoneを返して無効入力として扱う

#### 💻 動作例
```python
parse_time_string("1H30M")     # → 5400秒 (1.5時間)
parse_time_string("2m")        # → 120秒
parse_time_string("45s")       # → 45秒
parse_time_string("0s")        # → None (無効)
parse_time_string("abc")       # → None (無効)
parse_time_string("1h 30m")    # → 5400秒 (空白除去後処理)
```

### ⏱️ countdown 関数の詳細解説

```python
def countdown(seconds):
    try:
        for i in range(seconds, 0, -1):
            # カーソルを行の先頭に戻して上書き表示
            print(f"\r残り {i:02d} 秒", end="", flush=True)
            time.sleep(1)
        print("\r時間になりました！" + " " * 10)  # 余分な文字を消去
    except KeyboardInterrupt:
        print("\n\nタイマーをキャンセルしました。")
```

#### 🎯 この関数の役割
デジタル時計のような表示でカウントダウンを実行する

#### 📋 処理の流れ

1. **カウントダウンループ**
   ```python
   for i in range(seconds, 0, -1):
   ```
   - `range(seconds, 0, -1)` で逆順カウント
   - 例：`range(5, 0, -1)` → `[5, 4, 3, 2, 1]`

2. **デジタル時計風表示**
   ```python
   print(f"\r残り {i:02d} 秒", end="", flush=True)
   ```
   - **`\r`** : カーソルを行の先頭に戻す（改行しない）
   - **`{i:02d}`** : 2桁表示（`05`, `04`, `03`...）
   - **`end=""`** : 改行を抑制
   - **`flush=True`** : バッファを即座に出力（リアルタイム表示）

3. **1秒待機**
   ```python
   time.sleep(1)
   ```

4. **完了メッセージ**
   ```python
   print("\r時間になりました！" + " " * 10)
   ```
   - 余分な文字を空白で消去

5. **キャンセル処理**
   ```python
   except KeyboardInterrupt:
       print("\n\nタイマーをキャンセルしました。")
   ```
   - **Ctrl+C** でいつでもキャンセル可能

#### 💡 デジタル表示の仕組み

**通常のprint()の場合**:
```
残り 05秒
残り 04秒  
残り 03秒
```
↑ 縦に積み重なる

**`\r + end="" + flush=True`の場合**:
```
残り 01秒  ← 同じ場所で数字だけ変わる
```
↑ デジタル時計のような更新

### 🎓 今日の重要な学習ポイント

| テーマ | 学習内容 |
|--------|----------|
| 🔤 **正規表現** | `re.fullmatch()`, キャプチャグループ `(\d+)`, オプション `?` |
| 🎨 **文字列処理** | `strip()`, `lower()`, `replace()` |
| 🔄 **三項演算子** | `値 = A if 条件 else B` |
| 🖥️ **ターミナル制御** | `\r`（カーソル制御）, `end=""`, `flush=True` |
| ⚠️ **例外処理** | `KeyboardInterrupt` でCtrl+Cをキャッチ |
| 🔢 **時間計算** | 時・分・秒から総秒数への変換 |

### 🔧 技術的なポイント

#### 標準ライブラリだけでデジタル表示を実現
- **追加ライブラリ不要** 📦
- **軽量で高速** ⚡
- **どの環境でも動作** 🌍

#### エラーハンドリングの充実
- 無効な入力形式の検出
- ゼロ以下の時間の排除
- ユーザーによるキャンセル操作

#### ユーザビリティの向上
- 大文字小文字を問わない入力
- 空白を含む入力にも対応
- 直感的なキャンセル操作（Ctrl+C）

## 🚀 今後の改善・発展アイデア

### 💡 機能拡張のポイント

#### 🖥️ GUI化（Tkinter）
```python
import tkinter as tk
from tkinter import ttk
import threading

class TimerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Timer App")
        
        # 入力フィールド
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack()
        
        # 開始ボタン
        self.start_button = tk.Button(self.root, text="開始", command=self.start_timer)
        self.start_button.pack()
        
        # 表示ラベル
        self.display_label = tk.Label(self.root, text="00:00", font=("Arial", 20))
        self.display_label.pack()
```

**メリット**:
- **視覚的に分かりやすい** 👀
- **マウス操作が可能** 🖱️
- **複数タイマーの表示が容易** 📊

#### 🔔 音響アラーム機能
```python
import pygame
import winsound  # Windows
import subprocess  # macOS/Linux

# 方法1: pygame使用
def play_alarm_pygame():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()

# 方法2: playsound使用
from playsound import playsound
def play_alarm_playsound():
    playsound("alarm.wav")

# 方法3: システムビープ
import winsound
def system_beep():
    winsound.Beep(1000, 500)  # 1000Hz, 500ms
```

**実装のポイント**:
- **音声ファイル**: `.mp3`, `.wav`形式をサポート
- **システムビープ**: 音声ファイル不要で簡単
- **ボリューム調整**: ユーザーが音量を設定可能

#### ⏰ 複数タイマー・ポモドーロ機能
```python
class MultiTimer:
    def __init__(self):
        self.timers = []
        
    def add_pomodoro_session(self):
        # ポモドーロ技法: 25分作業 + 5分休憩
        self.timers.append(Timer("作業時間", 25 * 60))
        self.timers.append(Timer("休憩時間", 5 * 60))
        
    def add_custom_timer(self, name, seconds):
        self.timers.append(Timer(name, seconds))
        
class Timer:
    def __init__(self, name, seconds):
        self.name = name
        self.seconds = seconds
        self.remaining = seconds
        self.is_running = False
```

**ポモドーロ技法の実装**:
- **25分作業 → 5分休憩** を自動繰り返し
- **4セット後は長い休憩**（15-30分）
- **進捗トラッキング**機能

### 🎯 段階的な実装プラン

#### フェーズ1: 音響機能追加
```bash
pip install pygame playsound
```
- 現在のCLIタイマーに音を追加
- 複数の音源オプション提供

#### フェーズ2: シンプルGUI化
```python
# 基本的なTkinterウィンドウ
# 時間入力 + 開始ボタン + 表示エリア
```

#### フェーズ3: 複数タイマー対応
```python
# タイマーリスト管理
# 並行実行機能（threading使用）
```

#### フェーズ4: ポモドーロ専用機能
```python
# プリセット設定
# 統計情報表示
# 集中度トラッキング
```

### 🛠️ 必要な技術要素

| フェーズ | 技術 | 学習ポイント |
|----------|------|-------------|
| **音響** | `pygame`, `playsound` | 音声ファイル処理、システム音 |
| **GUI** | `tkinter` | ウィンドウ作成、イベント処理 |
| **並行処理** | `threading` | マルチスレッド、タイマー管理 |
| **データ管理** | `json`, `sqlite3` | 設定保存、履歴管理 |

### 📚 参考実装例

#### 最小限の音付きタイマー
```python
import time
import winsound

def countdown_with_sound(seconds):
    for i in range(seconds, 0, -1):
        print(f"\r残り {i:02d} 秒", end="", flush=True)
        time.sleep(1)
    
    # アラーム音
    for _ in range(3):
        winsound.Beep(1000, 200)
        time.sleep(0.1)
    
    print("\n⏰ 時間です！")
```

#### GUI版の基本構造
```python
import tkinter as tk
import threading

class SimpleTimerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🕐 Timer")
        self.setup_ui()
        
    def setup_ui(self):
        # 時間入力
        tk.Label(self.root, text="時間:").pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        
        # 開始ボタン
        tk.Button(self.root, text="開始", command=self.start).pack()
        
        # 残り時間表示
        self.label = tk.Label(self.root, text="00:00", font=("Arial", 24))
        self.label.pack()
        
    def start(self):
        time_str = self.entry.get()
        seconds = parse_time_string(time_str)
        if seconds:
            # 別スレッドでカウントダウン実行
            threading.Thread(target=self.countdown, args=(seconds,)).start()
            
    def countdown(self, seconds):
        # GUIを更新しながらカウントダウン
        pass
```

これらの機能を段階的に実装することで、シンプルなCLIタイマーから本格的なデスクトップアプリケーションへと発展させることができます！🚀

