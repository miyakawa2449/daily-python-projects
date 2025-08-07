# 🎮 じゃんけんゲーム (Rock Paper Scissors Game)

Pythonで作成したじゃんけんゲームです。シンプルなコンソール版と、Pygameを使用したグラフィカル版の2つのバージョンを実装しています。

## 📁 ファイル構成

```
day61-janken/
├── main.py           # コンソール版じゃんけんゲーム
├── main_pygame.py    # Pygame版グラフィカルゲーム
├── rock.png          # グー（握りこぶし）の画像
├── paper.png         # パー（開いた手）の画像
├── scissors.png      # チョキ（Vサイン）の画像
└── README.md         # このファイル
```

## 🚀 実行方法

### 📟 **コンソール版**
```bash
cd day61-janken
python main.py
```

### 🎨 **Pygame版**
```bash
# Pygameのインストール（初回のみ）
pip install pygame

# ゲーム実行
python main_pygame.py
```

## 💡 使い方

### 📟 **コンソール版**
```
じゃんけんゲーム（rock/paper/scissors）終了するには 'exit'
あなたの手を入力してください: rock
コンピュータの手: scissors
あなたの勝ち！
あなたの手を入力してください: exit
ゲームを終了します。
```

**操作方法**:
- `rock`, `paper`, `scissors` を入力
- `exit` または `quit` で終了

### 🎨 **Pygame版**
- **マウスでクリック**: 3つの手のボタンから選択
- **VS表示**: あなたとコンピュータの手を左右に表示
- **もう一度ボタン**: 結果画面で次のゲームに進む
- **ウィンドウを閉じる**: ゲーム終了

## ✨ 機能

### 📟 **コンソール版**
- キーボード入力による手の選択
- 入力検証（無効な手の場合は再入力）
- 連続プレイ機能
- 終了コマンド対応

### 🎨 **Pygame版**
- **グラフィカルUI**: 実際の手の画像を使用
- **直感的操作**: マウスクリックで手を選択
- **視覚的フィードバック**: 勝敗に応じた色分け表示
- **日本語対応**: クロスプラットフォーム日本語フォント
- **レスポンシブレイアウト**: 800x600ピクセルの最適化

## 📖 学んだことや今後の改善案（学習ログ）

### 🔧 主要な学習ポイント

#### 1️⃣ **`random.choice()`の理解と活用**

```python
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
```

**重要な発見**:
- **`random.choice()`**: リストからランダムに1つの要素を抽出する関数
- **等確率選択**: 各要素が1/3の確率で選ばれる
- **シンプルな実装**: C言語の`rand() % 3`のような数値変換が不要

**C言語との比較**:
```c
// C言語での実装
int computer_choice = rand() % 3;  // 0, 1, 2のいずれかに丸める
if (computer_choice == 0) {
    printf("グー\n");
} else if (computer_choice == 1) {
    printf("パー\n");
} else {
    printf("チョキ\n");
}
```

```python
# Pythonでの実装
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)  # 直接文字列を選択
print(f"コンピュータの手: {computer_choice}")
```

**Pythonの利点**:
- **直感的**: 意図が明確で読みやすい
- **エラーが少ない**: 配列の範囲外アクセスの心配なし
- **保守しやすい**: 新しい手を追加するのも簡単

#### 2️⃣ **Pygameによるグラフィカルプログラミング**

**プログラミングロジック vs UI設計**の違いを深く理解：

##### 💻 **プログラミングロジック（従来の強み）**
```python
def calculate_result(self):
    """勝敗判定の純粋なロジック"""
    if self.user_choice == self.computer_choice:
        return "あいこ"
    elif (
        (self.user_choice == "rock" and self.computer_choice == "scissors") or
        (self.user_choice == "scissors" and self.computer_choice == "paper") or
        (self.user_choice == "paper" and self.computer_choice == "rock")
    ):
        return "勝ち"
    else:
        return "負け"
```

##### 🎨 **UI設計（新しい学習領域）**
```python
# 座標とサイズの管理
self.buttons = {
    "rock": pygame.Rect(120, 350, 140, 140),      # x, y, width, height
    "paper": pygame.Rect(330, 350, 140, 140),
    "scissors": pygame.Rect(540, 350, 140, 140)
}

# 視覚的フィードバック
button_color = LIGHT_BLUE if is_selected else WHITE
border_color = BLUE if is_selected else BLACK
```

**重要な気づき**:
- **2つの異なるスキル**: プログラミング技術とデザイン感覚の両方が必要
- **座標管理の重要性**: ピクセル単位での正確な配置
- **ユーザー体験**: 「動作する」だけでなく「使いやすい」ことの重要性

#### 3️⃣ **クロスプラットフォーム対応の実装**

**日本語フォント問題とその解決**:

```python
def get_japanese_font():
    """OS別に日本語フォントを取得"""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        font_paths = [
            "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
            "/System/Library/Fonts/Hiragino Sans GB.ttc"
        ]
    elif system == "Windows":  # Windows
        font_paths = [
            "C:/Windows/Fonts/msgothic.ttc",      # MS ゴシック
            "C:/Windows/Fonts/yugothm.ttc",       # 游ゴシック
            "C:/Windows/Fonts/NotoSansCJK-Regular.ttc"  # Noto CJK
        ]
    elif system == "Linux":  # Linux
        font_paths = [
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
            "/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf"
        ]
```

**学習したポイント**:
- **OS依存の問題**: 各OSで異なるフォントパス
- **フォールバック戦略**: 複数の候補を用意し、順次チェック
- **エラーハンドリング**: フォント読み込み失敗時の対処

#### 4️⃣ **画像処理とリソース管理**

```python
def load_images():
    """画像リソースの読み込みと管理"""
    images = {}
    image_files = {
        "rock": "rock.png",
        "paper": "paper.png", 
        "scissors": "scissors.png"
    }
    
    for choice, filename in image_files.items():
        try:
            image = pygame.image.load(filename)
            image = pygame.transform.scale(image, (120, 120))  # リサイズ
            images[choice] = image
        except pygame.error as e:
            # フォールバック: 灰色の四角形
            fallback_surface = pygame.Surface((120, 120))
            fallback_surface.fill(GRAY)
            images[choice] = fallback_surface
```

**重要な概念**:
- **リソース管理**: 外部ファイルの安全な読み込み
- **統一性**: 画像サイズの自動調整
- **堅牢性**: ファイルが見つからない場合の代替手段

### 🎯 技術的な課題と解決

#### 🐛 **問題1: UI要素の配置ズレ**

**課題**: 文字位置とボタン位置が揃わない

**原因分析**:
```python
# 問題のあったコード
day_header = "  ".join(f"{day:>1}" for day in day_names)    # 1文字幅
week_str = "  ".join(f"{day[0]:2}" if day[0] != 0 else "  " for day in week)  # 2文字幅
```

**解決策**:
```python
# 修正後: 文字幅を統一
day_header = "  ".join(f"{day:>2}" for day in day_names)    # 2文字幅に統一
```

**学習**: UI設計では**一貫性**が最重要

#### 🐛 **問題2: 日本語文字化け**

**課題**: Pygameで日本語が正しく表示されない

**解決アプローチ**:
1. **OS検出**: `platform.system()`でOSを判定
2. **フォントパス探索**: 各OSの標準フォント場所をチェック
3. **段階的フォールバック**: 複数の候補を順次試行

**結果**: Windows、macOS、Linux全てで日本語表示が実現

### 🎨 デザイン思考の学習

#### 📐 **レイアウト設計原則**

**ワイヤーフレーム設計**:
```
┌─────────────────────────────────┐
│           タイトル               │  ← 視覚的ヒエラルキーの頂点
├─────────────────────────────────┤
│     [あなた]    VS   [コンピュータ] │  ← 対戦構図の明確化
│      画像           画像         │
├─────────────────────────────────┤
│           結果表示               │  ← 重要な情報を中央に
├─────────────────────────────────┤
│   [グー]  [パー]  [チョキ]      │  ← 操作要素を下部に配置
└─────────────────────────────────┘
```

**色彩設計**:
```python
# 情報の重要度を色で表現
TITLE_COLOR = BLACK      # 最も重要
RESULT_WIN = GREEN       # 良い結果
RESULT_LOSE = RED        # 注意が必要な結果
LABEL_COLOR = GRAY       # 補助情報
```

#### 🔄 **相対配置の重要性**

**固定配置の問題**:
```python
# 画面サイズが変わると破綻する
self.buttons = {
    "rock": pygame.Rect(120, 350, 140, 140),  # ハードコーディング
}
```

**相対配置の解決策**:
```python
# 画面サイズに応じて動的に配置
center_x = SCREEN_WIDTH // 2
button_spacing = (SCREEN_WIDTH - total_button_width) // (button_count + 1)
```

### 🚀 今後の改善・発展アイデア

#### 📈 **機能拡張**
- **スコア機能**: 連勝記録、勝率統計
- **難易度設定**: コンピュータの戦略パターン
  - ランダム（現在）
  - プレイヤーの癖を学習
  - 心理的戦略（相手の前回の手を考慮）
- **サウンド**: 効果音、BGM
- **アニメーション**: 手を出すときのカウントダウン

#### 🎨 **視覚的改善**
- **パーティクルエフェクト**: 勝利時の花火演出
- **スムーズトランジション**: 画面切り替えアニメーション
- **テーマ切り替え**: ダークモード、季節テーマ
- **カスタムキャラクター**: プレイヤーアバター

#### 🌐 **技術的発展**
- **ネットワーク対戦**: 複数プレイヤー対応
- **AI対戦**: 機械学習を使った高度なAI
- **モバイル対応**: Kivy、BeeWareでスマートフォン版
- **Web版**: PyScriptでブラウザ実行

#### 📊 **データ分析機能**
```python
# 統計情報の記録・分析
class GameStats:
    def __init__(self):
        self.games_played = 0
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.choice_history = []
        
    def analyze_patterns(self):
        """プレイヤーの選択パターンを分析"""
        # 最も多い手、連続選択パターンなど
```

### 🎓 **この実装から学べる重要な概念**

#### 💻 **プログラミングスキル**
1. **標準ライブラリ活用**: `random.choice()`の効果的な使用
2. **クロスプラットフォーム開発**: OS差異への対応
3. **エラーハンドリング**: 堅牢なアプリケーション設計
4. **リソース管理**: 外部ファイルの安全な取り扱い

#### 🎨 **UI/UX設計**
1. **視覚的ヒエラルキー**: 情報の重要度を視覚的に表現
2. **ユーザビリティ**: 直感的な操作性の実現
3. **レスポンシブデザイン**: 異なる環境での一貫した体験
4. **フィードバック**: ユーザーの行動に対する適切な反応

#### 🔧 **ソフトウェア工学**
1. **段階的開発**: コンソール版→GUI版への発展
2. **モジュール設計**: 機能の分離と再利用性
3. **プラットフォーム抽象化**: OS依存部分の隠蔽
4. **テスト可能性**: ロジックとUIの分離

### 💡 **C言語経験者としての気づき**

**従来のプログラミング（C言語）**:
- 低レベル制御重視
- メモリ管理が明示的
- 効率性を重視した実装

**Pythonでの新しいアプローチ**:
- 高レベル abstraction の活用
- 開発速度と保守性の重視
- ライブラリエコシステムの活用

**統合された学習価値**:
- **基礎理論（C言語）** + **実用性（Python）** = **包括的理解**
- アルゴリズム思考とUI設計思考の両立
- 効率性と開発速度のトレードオフの理解

## 🎉 総評

このじゃんけんゲームプロジェクトは、**シンプルなゲームロジック**から始まり、**グラフィカルUI**、**クロスプラットフォーム対応**まで、現代的なアプリケーション開発に必要な多くの要素を含んだ**包括的な学習体験**となりました。

特に「**プログラミングロジックとUI設計は異なるスキル**」という気づきは、今後のソフトウェア開発において非常に重要な視点です。

**C言語での基礎経験**を活かしながら、**Pythonの柔軟性**と**現代的な開発手法**を学ぶことで、より実用的で保守しやすいアプリケーションを作成する能力が大幅に向上しました！🎊