import pygame
import random
import sys
import os
import platform

# 初期化
pygame.init()

# 画面設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("じゃんけんゲーム")

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 150, 255)
GREEN = (100, 255, 100)
RED = (255, 100, 100)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)

# 日本語フォント設定（クロスプラットフォーム対応）
def get_japanese_font():
    """OS別に日本語フォントを取得"""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        font_paths = [
            "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
            "/System/Library/Fonts/Hiragino Sans GB.ttc",
            "/Library/Fonts/Arial Unicode MS.ttf",
            "/System/Library/Fonts/Apple Gothic.ttf"
        ]
    elif system == "Windows":  # Windows
        font_paths = [
            "C:/Windows/Fonts/msgothic.ttc",
            "C:/Windows/Fonts/msgothic.ttf",
            "C:/Windows/Fonts/NotoSansCJK-Regular.ttc",
            "C:/Windows/Fonts/yugothm.ttc",
            "C:/Windows/Fonts/yugothb.ttc",
            "C:/Windows/Fonts/BIZ-UDGothicR.ttc"
        ]
    elif system == "Linux":  # Linux
        font_paths = [
            "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
            "/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf",
            "/usr/share/fonts/truetype/fonts-japanese-gothic.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        ]
    else:
        font_paths = []
    
    for font_path in font_paths:
        if os.path.exists(font_path):
            print(f"使用フォント: {font_path}")
            return font_path
    
    print(f"警告: {system}で日本語フォントが見つかりません。")
    return None

def setup_fonts():
    """フォントをセットアップ"""
    japanese_font_path = get_japanese_font()
    
    if japanese_font_path:
        try:
            font_large = pygame.font.Font(japanese_font_path, 48)
            font_medium = pygame.font.Font(japanese_font_path, 36)
            font_small = pygame.font.Font(japanese_font_path, 24)
            return font_large, font_medium, font_small
        except Exception as e:
            print(f"フォント読み込みエラー: {e}")
    
    print("システムデフォルトフォントを使用します。")
    font_large = pygame.font.Font(None, 48)
    font_medium = pygame.font.Font(None, 36)
    font_small = pygame.font.Font(None, 24)
    return font_large, font_medium, font_small

# フォント設定を実行
font_large, font_medium, font_small = setup_fonts()

# 画像読み込み関数
def load_images():
    """じゃんけんの手の画像を読み込み"""
    images = {}
    image_files = {
        "rock": "rock.png",     # グーの画像
        "paper": "paper.png",   # パーの画像  
        "scissors": "scissors.png"  # チョキの画像
    }
    
    for choice, filename in image_files.items():
        try:
            # 画像を読み込み
            image = pygame.image.load(filename)
            # サイズを調整（120x120ピクセル）
            image = pygame.transform.scale(image, (120, 120))
            images[choice] = image
            print(f"画像読み込み成功: {filename}")
        except pygame.error as e:
            print(f"画像読み込み失敗: {filename} - {e}")
            # フォールバック: 四角形で代替
            fallback_surface = pygame.Surface((120, 120))
            fallback_surface.fill(GRAY)
            images[choice] = fallback_surface
    
    return images

class JankenGame:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.choice_jp = {"rock": "グー", "paper": "パー", "scissors": "チョキ"}
        self.user_choice = None
        self.computer_choice = None
        self.result = ""
        self.show_result = False
        
        # 画像を読み込み
        self.images = load_images()
        
        # ボタンの位置とサイズ（画像サイズに合わせて調整）
        self.button_width = 140
        self.button_height = 140
        self.button_y = 350
        
        self.buttons = {
            "rock": pygame.Rect(120, self.button_y, self.button_width, self.button_height),
            "paper": pygame.Rect(330, self.button_y, self.button_width, self.button_height),
            "scissors": pygame.Rect(540, self.button_y, self.button_width, self.button_height)
        }
        
        # リセットボタン
        self.reset_button = pygame.Rect(350, 520, 100, 40)
        
        # 結果表示エリア
        self.result_area = {
            "user": pygame.Rect(150, 150, 140, 140),
            "computer": pygame.Rect(510, 150, 140, 140)
        }
    
    def draw_button(self, choice, rect, is_selected=False):
        """ボタンを描画"""
        # ボタンの背景色
        if is_selected:
            button_color = LIGHT_BLUE
            border_color = BLUE
            border_width = 4
        else:
            button_color = WHITE
            border_color = BLACK
            border_width = 2
        
        # ボタンの枠を描画
        pygame.draw.rect(screen, button_color, rect)
        pygame.draw.rect(screen, border_color, rect, border_width)
        
        # 画像を描画
        image_rect = self.images[choice].get_rect()
        image_rect.center = rect.center
        screen.blit(self.images[choice], image_rect)
        
        # 日本語ラベル
        jp_text = font_small.render(self.choice_jp[choice], True, BLACK)
        jp_rect = jp_text.get_rect(center=(rect.centerx, rect.bottom + 15))
        screen.blit(jp_text, jp_rect)
    
    def draw_result_image(self, choice, rect, label):
        """結果表示用の画像を描画"""
        # 背景
        pygame.draw.rect(screen, WHITE, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)
        
        # 画像を描画
        image_rect = self.images[choice].get_rect()
        image_rect.center = rect.center
        screen.blit(self.images[choice], image_rect)
        
        # ラベル
        label_text = font_medium.render(label, True, BLACK)
        label_rect = label_text.get_rect(center=(rect.centerx, rect.top - 20))
        screen.blit(label_text, label_rect)
        
        # 選択した手の名前
        choice_text = font_small.render(self.choice_jp[choice], True, BLACK)
        choice_rect = choice_text.get_rect(center=(rect.centerx, rect.bottom + 10))
        screen.blit(choice_text, choice_rect)
    
    def handle_click(self, pos):
        """クリック処理"""
        for choice, rect in self.buttons.items():
            if rect.collidepoint(pos):
                self.user_choice = choice
                self.computer_choice = random.choice(self.choices)
                self.calculate_result()
                self.show_result = True
                return
        
        # リセットボタン
        if self.reset_button.collidepoint(pos) and self.show_result:
            self.reset_game()
    
    def calculate_result(self):
        """勝敗判定"""
        if self.user_choice == self.computer_choice:
            self.result = "あいこ！"
        elif (
            (self.user_choice == "rock" and self.computer_choice == "scissors") or
            (self.user_choice == "scissors" and self.computer_choice == "paper") or
            (self.user_choice == "paper" and self.computer_choice == "rock")
        ):
            self.result = "あなたの勝ち！"
        else:
            self.result = "あなたの負け！"
    
    def reset_game(self):
        """ゲームリセット"""
        self.user_choice = None
        self.computer_choice = None
        self.result = ""
        self.show_result = False
    
    def draw(self):
        """画面描画"""
        screen.fill(WHITE)
        
        # タイトル
        title = font_large.render("じゃんけんゲーム", True, BLACK)
        title_rect = title.get_rect(center=(SCREEN_WIDTH//2, 50))
        screen.blit(title, title_rect)
        
        if not self.show_result:
            # 指示文
            instruction = font_medium.render("手を選んでください", True, BLACK)
            instruction_rect = instruction.get_rect(center=(SCREEN_WIDTH//2, 100))
            screen.blit(instruction, instruction_rect)
            
            # ボタンを描画
            for choice, rect in self.buttons.items():
                self.draw_button(choice, rect)
                
        else:
            # 結果画面
            # あなたの手を左側に表示
            self.draw_result_image(self.user_choice, self.result_area["user"], "あなた")
            
            # コンピュータの手を右側に表示
            self.draw_result_image(self.computer_choice, self.result_area["computer"], "コンピュータ")
            
            # VS表示
            vs_text = font_large.render("VS", True, BLACK)
            vs_rect = vs_text.get_rect(center=(SCREEN_WIDTH//2, 220))
            screen.blit(vs_text, vs_rect)
            
            # 結果表示
            result_color = GREEN if "勝ち" in self.result else RED if "負け" in self.result else BLACK
            result_text = font_large.render(self.result, True, result_color)
            result_rect = result_text.get_rect(center=(SCREEN_WIDTH//2, 320))
            screen.blit(result_text, result_rect)
            
            # リセットボタン
            pygame.draw.rect(screen, GRAY, self.reset_button)
            pygame.draw.rect(screen, BLACK, self.reset_button, 2)
            reset_text = font_small.render("もう一度", True, BLACK)
            reset_rect = reset_text.get_rect(center=self.reset_button.center)
            screen.blit(reset_text, reset_rect)

def main():
    clock = pygame.time.Clock()
    game = JankenGame()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 左クリック
                    game.handle_click(event.pos)
        
        game.draw()
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()