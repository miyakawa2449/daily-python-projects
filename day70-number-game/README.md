# 🔢 数当てゲーム (Number Guessing Game)

Python の `random` モジュールを活用したシンプルで楽しい数当てゲームです。コンピューターが生成した1〜100の数字を予想して当てる、プログラミング学習に最適な対話型ゲームです。

## 📝 アプリケーション概要

**主な機能**:
- **ランダム数生成**: `random.randint(1, 100)` による1〜100の整数生成
- **対話型ゲーム**: ユーザー入力による予想システム
- **ヒント機能**: 「もっと大きい」「もっと小さい」の誘導メッセージ
- **試行回数カウント**: 何回で正解したかの記録
- **エラーハンドリング**: 数字以外の入力に対する適切な対応

**学習ポイント**:
- `random.randint()` の基本的な使用方法
- while ループと break による制御構造
- try-except によるエラーハンドリング
- ユーザー入力処理（input() と int() の組み合わせ）
- 条件分岐（if-elif-else）の実践的活用

## 📁 ファイル構成

```
day70-number-game/
├── main.py          # メインゲームプログラム
└── README.md        # このファイル
```

### 🎯 **main.py の構造**

```python
import random

def number_game():
    answer = random.randint(1, 100)    # 正解となる数字を生成
    tries = 0                          # 試行回数のカウンター
    
    # ゲームメインループ
    while True:
        try:
            guess = int(input("あなたの予想: "))
            tries += 1
            
            # 比較ロジック
            if guess < answer:
                print("もっと大きい数です。")
            elif guess > answer:
                print("もっと小さい数です。")
            else:
                print(f"🎉 正解！{tries} 回で当てました！")
                break
                
        except ValueError:
            print("⚠️ 数字を入力してください。")
```

## 🚀 実行方法

### 💻 **基本的な実行**

```bash
# day70-number-gameディレクトリに移動
cd day70-number-game

# ゲームを開始
python main.py
```

### 🎮 **実行結果の例**

```
🔢 数当てゲームへようこそ！
1から100の中から正解を当ててください。

あなたの予想: 50
もっと大きい数です。

あなたの予想: 75
もっと小さい数です。

あなたの予想: 63
もっと大きい数です。

あなたの予想: 69
もっと小さい数です。

あなたの予想: 66
もっと大きい数です。

あなたの予想: 67
🎉 正解！6 回で当てました！
```

## 💡 使い方

### 🎯 **基本的な遊び方**

1. **ゲーム開始**: `python main.py` でゲームスタート
2. **数字入力**: 1〜100の間で予想した数字を入力
3. **ヒント確認**: 「もっと大きい」「もっと小さい」のヒントを参考に次の予想
4. **正解**: 正確な数字を当てるとゲーム終了、試行回数が表示される

### 🧠 **効率的な攻略戦略**

#### **二分探索法**
```python
# 効率的な予想パターン
# 1回目: 50  (中央値から開始)
# 2回目: 75  (50-100の中央値) または 25 (1-50の中央値)
# 3回目: さらに範囲を半分に絞る
# 理論上の最大試行回数: log₂(100) ≈ 7回
```

#### **各種戦略の比較**
- **ランダム予想**: 運次第（1〜99回）
- **順次探索**: 最悪99回、平均50回
- **二分探索**: 最悪7回、平均6回 ← **最効率**

### ⚠️ **エラー対応**

```python
# 数字以外を入力した場合
あなたの予想: abc
⚠️ 数字を入力してください。

# 範囲外でも動作（ヒントで誘導）
あなたの予想: 200
もっと小さい数です。
```

## 🎲 **randomモジュールの豊富な機能**

### 📊 **主要メソッド一覧**

| メソッド | 機能 | 用途 | 使用例 |
|---------|------|------|--------|
| `randint(a, b)` | a〜b の整数 | ゲーム、抽選 | `random.randint(1, 6)` # サイコロ |
| `random()` | 0.0〜1.0の浮動小数点 | 確率判定 | `random.random() < 0.3` # 30%の確率 |
| `uniform(a, b)` | a〜b の浮動小数点 | 連続値生成 | `random.uniform(0.0, 100.0)` # 温度 |
| `choice(seq)` | シーケンスから1つ選択 | ランダム選択 | `random.choice(['赤','青','緑'])` |
| `choices(seq, k=n)` | 重複ありでn個選択 | 重み付き抽選 | `random.choices(items, weights=[1,2,3], k=2)` |
| `sample(seq, k)` | 重複なしでk個選択 | ロト、サンプリング | `random.sample(range(1,46), 6)` # ロト6 |
| `shuffle(list)` | リストをシャッフル | カード、配列混在 | `random.shuffle(cards)` |
| `seed(n)` | 乱数シード設定 | テスト、再現性 | `random.seed(42)` # 同じ結果を再現 |

### 🎮 **実用的な活用例**

#### **1. 確率システム**
```python
# ガチャシステム（重み付き）
items = ["レア", "ノーマル", "コモン"]
weights = [1, 3, 6]  # レア10%, ノーマル30%, コモン60%
result = random.choices(items, weights=weights)[0]
print(f"ガチャ結果: {result}")
```

#### **2. ゲーム要素**
```python
# RPGの敵エンカウント
if random.random() < 0.3:  # 30%の確率で敵出現
    enemies = ["スライム", "ゴブリン", "ドラゴン"]
    enemy = random.choice(enemies)
    hp = random.randint(50, 200)
    print(f"{enemy}が現れた！ HP: {hp}")

# じゃんけん
hands = ["グー", "チョキ", "パー"]
computer = random.choice(hands)
print(f"コンピューター: {computer}")
```

#### **3. データ生成**
```python
# テストデータ生成
test_scores = [random.randint(0, 100) for _ in range(30)]
user_names = random.sample(["田中", "佐藤", "鈴木", "高橋"], 3)

# ランダムパスワード生成
import string
chars = string.ascii_letters + string.digits
password = ''.join(random.choices(chars, k=12))
```

#### **4. シミュレーション**
```python
# A/Bテストシミュレーション
def ab_test(success_rate_a=0.15, success_rate_b=0.18):
    results_a = [random.random() < success_rate_a for _ in range(1000)]
    results_b = [random.random() < success_rate_b for _ in range(1000)]
    
    print(f"A群成功率: {sum(results_a)/1000:.1%}")
    print(f"B群成功率: {sum(results_b)/1000:.1%}")
```

## 📖 学んだことや今後の改善案（学習ログ）

### 🔧 主要な学習ポイント

#### 1️⃣ **random.randint() の威力**

**基本的な使用方法**:
```python
answer = random.randint(1, 100)
# ↓ この1行で実現される処理
# 1. 1から100までの整数範囲を設定
# 2. 各数字が等確率（1/100）で選択される
# 3. 毎回異なる結果が生成される（真の乱数に近い）
```

**重要な特徴**:
- **両端含む**: `randint(1, 100)` は1と100の両方を含む
- **等確率**: すべての整数が同じ確率で選ばれる
- **簡潔性**: 複雑な乱数生成ロジックを1行で実現

#### 2️⃣ **ゲームロジックの構築**

**核心となる比較処理**:
```python
if guess < answer:       # ユーザーの予想が小さすぎる
    print("もっと大きい数です。")
elif guess > answer:     # ユーザーの予想が大きすぎる
    print("もっと小さい数です。")
else:                    # 正解
    print(f"🎉 正解！{tries} 回で当てました！")
    break               # ゲーム終了
```

**学習成果**:
- **三分岐の美しさ**: <, >, == の3つの状態を完全にカバー
- **ユーザビリティ**: 分かりやすいヒントでゲーム体験向上
- **ループ制御**: break による自然なゲーム終了

#### 3️⃣ **エラーハンドリングの実践**

**堅牢な入力処理**:
```python
try:
    guess = int(input("あなたの予想: "))
    # 正常な数値変換
except ValueError:
    print("⚠️ 数字を入力してください。")
    # 文字列や空入力に対する適切な対応
```

**重要な気づき**:
- **ユーザー体験**: エラーでクラッシュしない親切な設計
- **継続性**: エラーが発生してもゲームが続行される
- **実用性**: 実際のアプリケーションで必須の技術

#### 4️⃣ **制御構造の理解深化**

**無限ループ + 条件付き脱出**:
```python
while True:              # 無限ループ開始
    # ユーザー入力処理
    # 比較処理
    if guess == answer:  # 正解条件
        break            # ループ脱出
```

**設計の美しさ**:
- **明確な終了条件**: 正解時のみゲーム終了
- **継続的体験**: 間違いは即座にヒントで次の挑戦へ
- **カウンター管理**: tries += 1 による試行回数の正確な記録

#### 5️⃣ **randomモジュールの豊富な可能性**

**今回使用した機能**:
```python
random.randint(1, 100)  # 整数範囲指定
```

**学習で発見した他の強力な機能**:
```python
# 確率判定
if random.random() < 0.3:  # 30%の確率

# 選択系
random.choice(["A", "B", "C"])           # 1つ選択
random.sample([1,2,3,4,5], 3)           # 重複なし複数選択
random.choices(items, weights=[1,2,3])   # 重み付き選択

# 操作系
random.shuffle(my_list)   # リストシャッフル
random.seed(42)          # 再現可能な乱数
```

#### 6️⃣ **プログラムの設計思想**

**シンプルさの中の完成度**:
```python
# たった25行程度のコードに含まれる要素
- 関数定義 (def)
- 変数管理 (answer, tries, guess)
- 制御構造 (while, if-elif-else)
- エラーハンドリング (try-except)
- ユーザーインターフェース (print, input)
- 外部ライブラリ (random)
```

**学習価値**:
- **基本要素の完全活用**: Pythonの主要文法を実践的に使用
- **ユーザー体験**: 技術だけでなく使いやすさも考慮
- **拡張性**: 今後の改良・機能追加の基盤として活用可能

### 🚀 今後の改善・発展アイデア

#### 📈 **機能拡張案**

##### 1️⃣ **難易度システム**
```python
def select_difficulty():
    difficulties = {
        "1": {"range": (1, 50), "name": "簡単"},
        "2": {"range": (1, 100), "name": "普通"},
        "3": {"range": (1, 200), "name": "難しい"}
    }
    
    choice = input("難易度を選択 (1:簡単/2:普通/3:難しい): ")
    return difficulties.get(choice, difficulties["2"])
```

##### 2️⃣ **ヒントシステム強化**
```python
def enhanced_hints(guess, answer, tries):
    diff = abs(guess - answer)
    
    if diff <= 5:
        print("🔥 とても近い！")
    elif diff <= 10:
        print("🌡️ 近い！")
    elif diff <= 20:
        print("📍 まあまあ近い")
    
    # 特別ヒント（5回目以降）
    if tries >= 5:
        if answer % 2 == 0:
            print("💡 ヒント: 答えは偶数です")
        else:
            print("💡 ヒント: 答えは奇数です")
```

##### 3️⃣ **スコアシステム**
```python
def calculate_score(tries, max_range):
    # 試行回数が少ないほど高得点
    max_possible_tries = max_range.bit_length()  # log₂(max_range)
    score = max(0, 1000 - (tries - 1) * 100)
    
    if tries <= max_possible_tries:
        score += 500  # ボーナス
    
    return score
```

##### 4️⃣ **統計機能**
```python
def game_statistics():
    games_played = 0
    total_tries = 0
    best_score = 0
    
    # ゲーム履歴をファイルに保存
    with open("game_stats.txt", "a") as f:
        f.write(f"Game {games_played}: {tries} tries\n")
    
    # 統計表示
    avg_tries = total_tries / games_played if games_played > 0 else 0
    print(f"📊 平均試行回数: {avg_tries:.1f}")
    print(f"🏆 最少記録: {best_score} 回")
```

##### 5️⃣ **マルチプレイヤー対応**
```python
def multiplayer_mode():
    players = ["プレイヤー1", "プレイヤー2"]
    scores = {player: 0 for player in players}
    
    for round_num in range(1, 4):  # 3ラウンド制
        print(f"\n🎮 ラウンド {round_num}")
        answer = random.randint(1, 100)
        
        for player in players:
            tries = play_single_round(player, answer)
            scores[player] += calculate_score(tries, 100)
    
    # 勝者決定
    winner = max(scores, key=scores.get)
    print(f"🏆 優勝: {winner}")
```

#### 🔧 **技術的改善案**

##### 1️⃣ **設定管理**
```python
import json

class GameConfig:
    def __init__(self):
        self.min_num = 1
        self.max_num = 100
        self.enable_hints = True
        self.max_hints = 3
    
    def load_from_file(self, filename="config.json"):
        try:
            with open(filename, 'r') as f:
                config = json.load(f)
                self.__dict__.update(config)
        except FileNotFoundError:
            self.save_to_file(filename)  # デフォルト設定を保存
```

##### 2️⃣ **ログシステム**
```python
import datetime

def log_game_result(tries, answer, guesses):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("game_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{timestamp} - 正解:{answer}, 試行回数:{tries}\n")
        f.write(f"予想履歴: {' -> '.join(map(str, guesses))}\n\n")
```

##### 3️⃣ **GUI版への発展**
```python
import tkinter as tk

class NumberGameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("数当てゲーム")
        
        # UI要素作成
        self.setup_ui()
        self.new_game()
    
    def setup_ui(self):
        # 入力フィールド
        self.entry = tk.Entry(self.root, font=("Arial", 16))
        self.entry.pack(pady=10)
        
        # 予想ボタン
        self.guess_button = tk.Button(
            self.root, 
            text="予想する", 
            command=self.make_guess
        )
        self.guess_button.pack(pady=5)
        
        # 結果表示ラベル
        self.result_label = tk.Label(self.root, font=("Arial", 14))
        self.result_label.pack(pady=10)
```

### 💡 **重要な学習成果**

#### 🎯 **技術的理解の深化**

##### 📚 **randomモジュールの真の価値**
- **簡潔性**: `random.randint(1, 100)` - たった1行で複雑な乱数生成
- **信頼性**: 暗号学的には不適切だが、ゲームには十分な品質
- **豊富性**: 8つの主要メソッドで様々な乱数処理に対応
- **実用性**: ゲーム・シミュレーション・テストデータ生成で即戦力

##### 🔧 **プログラム設計の本質理解**
- **ユーザー中心**: エラーハンドリングによる親切な設計
- **拡張性**: シンプルな基盤から複雑な機能への発展可能性
- **完結性**: 25行程度でも完全に動作する美しい構造
- **学習価値**: Pythonの主要文法を実践的に活用

##### 🚀 **ゲーム開発の基礎**
- **ユーザビリティ**: 分かりやすいヒント・メッセージ設計
- **ゲームバランス**: 適度な難易度（二分探索で7回程度）
- **継続性**: エラーでクラッシュしない堅牢な設計

#### 🌟 **「シンプルイズベスト」の実感**

```python
# この1行に込められた価値
answer = random.randint(1, 100)

# 手動実装なら数十行必要な処理
# - 乱数アルゴリズム
# - 範囲制限
# - 均等分布保証
# - エラーハンドリング
```

**今回最大の学習成果**: 「**ライブラリの適切な活用こそが、効率的で美しいプログラミングの基本**」という理解。

**random.randint()** というシンプルなメソッドから始まり、**randomモジュール全体の豊富な機能**、そして**実用的なゲーム開発の基礎**まで一気に学べた、非常に価値の高いプロジェクトでした。

## 🎉 総評

Day 70の数当てゲームは、**「シンプルな中に本質がある」**プログラミングの美学を体現した素晴らしいプロジェクトでした。

### ✅ **特に価値があった学習内容**

1. **random.randint()の威力**: 1行で高品質な乱数生成
2. **制御構造の実践**: while + break による自然なゲームフロー
3. **エラーハンドリング**: ユーザビリティを重視した堅牢な設計
4. **randomモジュールの発見**: 8つの主要メソッドによる豊富な可能性
5. **拡張性の実感**: シンプルな基盤から複雑な機能への発展性

### 🎯 **今後への展開**

このプロジェクトで習得した技術は、**ゲーム開発・データサイエンス・シミュレーション**など様々な分野で活用可能です。特に**randomモジュールの豊富な機能**は、今後のプロジェクトで大きな武器になります。

**25行のシンプルなコード**から**ゲーム開発の基礎**まで学べた、効率的で実用性の高い学習体験でした！🎲✨
