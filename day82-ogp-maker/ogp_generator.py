from PIL import Image, ImageDraw, ImageFont
import os

class OGPGenerator:
    """OGP画像生成クラス"""
    
    def __init__(self):
        # デフォルト設定
        self.width = 1200
        self.height = 630
        self.default_background = "#1e1e1e"
        self.default_text_color = "#ffffff"
        self.default_font_size = 64
        
        # フォントパス（優先順）
        self.font_paths = [
            "fonts/NotoSansJP-Bold.ttf",                               # カスタム
            "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",              # Mac
            "/System/Library/Fonts/Arial.ttf",                        # Mac
            "/System/Library/Fonts/Helvetica.ttc",                    # Mac
            "C:/Windows/Fonts/msgothic.ttc",                         # Windows
            "C:/Windows/Fonts/arial.ttf",                            # Windows
            "C:/Windows/Fonts/calibri.ttf"                           # Windows
        ]
    
    def _load_font(self, font_size):
        """フォント読み込み（フォールバック機能付き）"""
        for font_path in self.font_paths:
            try:
                font = ImageFont.truetype(font_path, font_size)
                print(f"✅ フォント使用: {os.path.basename(font_path)}")
                return font
            except (IOError, OSError):
                continue
        
        # 全てのフォントが読み込めない場合
        font = ImageFont.load_default()
        print("⚠️ デフォルトフォントを使用（日本語表示に問題がある可能性があります）")
        return font
    
    def _calculate_text_position(self, draw, text, font):
        """テキストの中央配置位置を計算"""
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        text_x = (self.width - text_width) // 2
        text_y = (self.height - text_height) // 2
        
        print(f"📏 テキストサイズ: {text_width}x{text_height}")
        print(f"📍 テキスト位置: ({text_x}, {text_y})")
        
        return text_x, text_y
    
    def generate(self, title, output_file="ogp.png", **options):
        """
        OGP画像生成メイン関数
        
        Args:
            title (str): タイトルテキスト
            output_file (str): 出力ファイル名
            **options: カスタマイズオプション
                - background_color (str): 背景色
                - text_color (str): 文字色  
                - font_size (int): フォントサイズ
        """
        # オプション設定（デフォルト値で補完）
        background_color = options.get('background_color', self.default_background)
        text_color = options.get('text_color', self.default_text_color)
        font_size = options.get('font_size', self.default_font_size)
        
        print(f"🎨 OGP画像生成中: '{title}'")
        print(f"📐 サイズ: {self.width}x{self.height}")
        print(f"🎨 背景色: {background_color}, 文字色: {text_color}")
        
        # 画像作成
        image = Image.new("RGB", (self.width, self.height), background_color)
        draw = ImageDraw.Draw(image)
        
        # フォント読み込み
        font = self._load_font(font_size)
        
        # テキスト位置計算
        text_x, text_y = self._calculate_text_position(draw, title, font)
        
        # テキスト描画
        draw.text((text_x, text_y), title, font=font, fill=text_color)
        
        # 保存
        try:
            image.save(output_file)
            print(f"✅ 画像を保存しました: {output_file}")
            
            # ファイル情報表示
            if os.path.exists(output_file):
                file_size = os.path.getsize(output_file)
                print(f"📊 ファイルサイズ: {file_size:,} bytes")
                
        except Exception as e:
            print(f"❌ 保存に失敗しました: {e}")
            raise

# 便利関数
def generate_ogp(title, output_file="ogp.png", **options):
    """シンプルなOGP画像生成関数"""
    generator = OGPGenerator()
    return generator.generate(title, output_file, **options)

def interactive_mode():
    """インタラクティブモード"""
    print("🎨 OGP画像ジェネレーター")
    print("=" * 40)
    
    # タイトル入力
    title = input("📝 タイトルを入力してください: ").strip()
    if not title:
        print("❌ タイトルが入力されていません")
        return
    
    # 基本生成
    print("\n🚀 基本設定で生成中...")
    generate_ogp(title)
    
    # カスタマイズオプション
    print(f"\n🎨 カスタマイズしますか？ (y/n): ", end="")
    if input().lower() == 'y':
        print("\n⚙️ カスタム設定")
        print("-" * 20)
        
        options = {}
        
        # 背景色
        bg_color = input("🎨 背景色 (例: #ff5733, デフォルト: #1e1e1e): ").strip()
        if bg_color:
            options['background_color'] = bg_color
        
        # 文字色
        text_color = input("✏️ 文字色 (例: #ffffff, デフォルト: #ffffff): ").strip()
        if text_color:
            options['text_color'] = text_color
        
        # フォントサイズ
        font_size_input = input("📏 フォントサイズ (例: 80, デフォルト: 64): ").strip()
        if font_size_input.isdigit():
            options['font_size'] = int(font_size_input)
        
        # カスタムファイル名生成
        safe_title = title[:10].replace(' ', '_').replace('/', '_')
        custom_filename = f"ogp_custom_{safe_title}.png"
        
        print(f"\n🚀 カスタム設定で生成中...")
        generate_ogp(title, custom_filename, **options)

def batch_generate(titles, **options):
    """複数タイトルの一括生成"""
    print(f"📦 {len(titles)} 個のOGP画像を一括生成中...")
    
    results = []
    for i, title in enumerate(titles):
        filename = f"ogp_batch_{i+1:03d}_{title[:10].replace(' ', '_')}.png"
        try:
            generate_ogp(title, filename, **options)
            results.append((title, filename, True))
        except Exception as e:
            print(f"❌ '{title}' の生成に失敗: {e}")
            results.append((title, filename, False))
    
    # 結果サマリー
    successful = sum(1 for _, _, success in results if success)
    print(f"\n📊 一括生成完了: {successful}/{len(titles)} 成功")
    
    return results

if __name__ == "__main__":
    interactive_mode()