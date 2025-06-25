# 📝 CLI ToDo List

## 🚀 実行方法
```bash
cd day057-todo-cli
python main.py
```

## 💡 使い方

```
1: 追加 | 2: 削除 | 3: 終了
選択してください: 
```
操作メニューは1から3のみです。
番号を入力し、作業を行います。

### ➕ 1. 追加
「1」を入力した後、Enterキーを押して、次の行に「タスク」を入力し、もう一度「Enter」キーを押します。

### ❌ 2. 削除
「2」を入力した後、Enterキーを押して、削除するタスクの番号を入力し、もう一度「Enter」キーを押します。

### 🔚 3. 終了
「3」を入力した後、Enterキーを押すとプログラムが終了し、ターミナル画面に戻ります。

## 📖 学んだことや今後の改善案（学習ログ）

### 📦 json と os を使う理由
```python
import json
import os

FILENAME = "todo_data.json"
```
- **json**: ToDoのデータ（リスト）をファイルに保存して、次回実行時にも内容を復元できるようにするため。
- **os**: 保存ファイル（todo_data.json）が存在しているかを確認するため（初回起動時の例外防止）

### 📂 load_tasks 関数について
```python
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []
```
この関数は、保存されているToDoリストのデータをJSONファイルから読み込む処理を行っています。

#### 🔧 処理の詳細
1. **関数定義**: `load_tasks()`
   - パラメータなし、戻り値はToDoリストのデータ（Pythonのリスト形式）

2. **ファイル存在チェック**: `if os.path.exists(FILENAME):`
   - FILENAME（"todo_data.json"）というファイルが存在するかチェック
   - 初回実行時やファイルが削除された場合に備えた安全な処理

3. **ファイル読み込み**:
   ```python
   with open(FILENAME, "r") as f:
       return json.load(f)
   ```
   - ファイルが存在する場合、読み込みモード（"r"）で開く
   - `json.load(f)`でJSONファイルをPythonのリスト形式に変換して返す
   - `with`文でファイルの自動クローズを保証

4. **デフォルト値**: `return []`
   - ファイルが存在しない場合は空のリスト`[]`を返す
   - 初回実行時の状態を表現

#### 💻 実際の動作例
**ケース1**: ファイルが存在し、以下の内容がある場合
```json
[
  "買い物",
  "勉強",
  "運動"
]
```
→ `["買い物", "勉強", "運動"]` というリストを返す

**ケース2**: ファイルが存在しない場合（初回実行など）  
→ `[]` 空のリストを返す

この関数は`main()`関数の最初で呼び出され、前回保存されたToDoリストを復元してプログラムの継続性を保っています。

### 💾 save_tasks 関数について
```python
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)
```

#### 🔧 処理の詳細
1. **関数定義**: `save_tasks(tasks)`
   - `tasks`パラメータ：保存したいToDoリストのデータ（Pythonのリスト形式）

2. **ファイルオープン**: `with open(FILENAME, "w") as f:`
   - FILENAME（"todo_data.json"）というファイルを書き込みモード（"w"）で開く
   - `with`文を使用することで、処理終了時に自動的にファイルを閉じる（リソース管理）

3. **JSON形式で保存**: `json.dump(tasks, f, indent=2)`
   - `tasks`リストをJSON形式でファイル`f`に書き込む
   - `indent=2`：JSONを見やすくインデント（2スペース）で整形

#### 💻 実際の動作例
もしタスクリストが `["買い物", "勉強", "運動"]` だった場合、以下のようなJSONファイルが作成されます：
```json
[
  "買い物",
  "勉強", 
  "運動"
]
```
この関数は、メインループでタスクの追加・削除が行われるたびに呼び出され、常に最新の状態をファイルに保存しています。これにより、プログラムを終了しても次回起動時にデータが保持されます。

### 🎯 main 関数の説明
```python
def main():
    tasks = load_tasks()
    while True:
        print("\nToDoリスト:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print("\n1: 追加 | 2: 削除 | 3: 終了")
        choice = input("選択してください: ")
        if choice == "1":
            task = input("追加するタスク: ")
            tasks.append(task)
        elif choice == "2":
            num = int(input("削除する番号: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
        elif choice == "3":
            break
        else:
            print("無効な入力です。")
        save_tasks(tasks)
```

#### 🔄 処理の流れ
1. **初期化**
   ```python
   tasks = load_tasks()
   ```
   - 保存されているToDoリストを読み込んで初期化

2. **メインループ** (`while True:`)
   - プログラムが終了するまで無限ループで以下を繰り返します

3. **ToDoリスト表示**
   ```python
   print("\nToDoリスト:")
   for i, task in enumerate(tasks):
       print(f"{i+1}. {task}")
   ```
   - 現在のタスク一覧を番号付きで表示
   - `enumerate()`でインデックスと要素を同時に取得
   - `i+1`で1から始まる番号にして表示

4. **メニュー表示とユーザー入力**
   ```python
   print("\n1: 追加 | 2: 削除 | 3: 終了")
   choice = input("選択してください: ")
   ```
   - 操作メニューを表示してユーザーの選択を受け取る

5. **選択に応じた処理**

   **➕ 選択肢1（追加）**:
   ```python
   if choice == "1":
       task = input("追加するタスク: ")
       tasks.append(task)
   ```
   - 新しいタスクを入力してリストの末尾に追加

   **❌ 選択肢2（削除）**:
   ```python
   elif choice == "2":
       num = int(input("削除する番号: ")) - 1
       if 0 <= num < len(tasks):
           tasks.pop(num)
   ```
   - 削除したいタスクの番号を入力
   - 表示番号（1から開始）をリストインデックス（0から開始）に変換（`-1`）
   - 有効な範囲内かチェックしてから削除

   **🔚 選択肢3（終了）**:
   ```python
   elif choice == "3":
       break
   ```
   - ループを終了してプログラム終了

   **⚠️ 無効な入力**:
   ```python
   else:
       print("無効な入力です。")
   ```
   - 1、2、3以外の入力に対するエラーメッセージ

6. **データ保存**
   ```python
   save_tasks(tasks)
   ```
   - 各操作後に変更内容をファイルに保存

#### 💻 実行例
```
ToDoリスト:
1. 買い物
2. 勉強

1: 追加 | 2: 削除 | 3: 終了
選択してください: 1
追加するタスク: 運動

ToDoリスト:
1. 買い物
2. 勉強
3. 運動
```
このようにユーザーフレンドリーなCLIインターフェースでToDoリストの管理ができる仕組みになっています。


## 🎓 学習ポイントまとめ
| テーマ    | 学べること                             |
| -------- | ------------------------------------ |
| 📁 ファイル処理 | `with open()`, `json.load/dump()` |
| 🔀 条件分岐   | `if`/`elif`/`else` の構文              |
| 🔄 ループ処理  | `while`, `for`, `enumerate()`       |
| ⌨️ ユーザー入力 | `input()`, 入力値の加工とエラーハンドリング |
| 💾 データ保存  | プログラム終了後もデータを保持する方法       |
| 🏗️ コード構成  | 関数分割、`main()`関数、`__main__`判定   |
