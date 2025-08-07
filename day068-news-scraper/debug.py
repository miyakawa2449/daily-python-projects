import requests
from bs4 import BeautifulSoup

def debug_news_scraper(url="https://news.ycombinator.com/"):
    print(f"🌐 ニュースページにアクセス中: {url}")
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        print(f"✅ HTTPステータス: {response.status_code}")
        print(f"📊 レスポンスサイズ: {len(response.text)} 文字")
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # === デバッグ: 実際のHTML構造を確認 ===
        print("\n🔍 HTML構造の調査:")
        
        # h1, h2, h3 タグを確認
        for tag in ["h1", "h2", "h3"]:
            elements = soup.find_all(tag)
            print(f"{tag}タグ: {len(elements)}個")
            if elements:
                print(f"  最初の{tag}: {elements[0].get_text(strip=True)[:50]}...")
        
        # aタグ（リンク）を確認（ニュースタイトルはリンクの場合が多い）
        links = soup.find_all("a")
        print(f"aタグ: {len(links)}個")
        
        # class属性で一般的なニュースクラスを探す
        common_classes = ["title", "headline", "news", "story", "titlelink"]
        for class_name in common_classes:
            elements = soup.find_all(class_=class_name)
            if elements:
                print(f"class='{class_name}': {len(elements)}個")
                for i, elem in enumerate(elements[:3]):  # 最初の3つを表示
                    text = elem.get_text(strip=True)
                    print(f"  {i+1}. {text[:100]}...")
        
        # HTMLの一部を出力（最初の1000文字）
        print(f"\n📄 HTML一部抜粋:")
        print(response.text[:1000])
        print("...")
        
    except requests.exceptions.RequestException as e:
        print(f"🚨 リクエストエラー: {e}")
    except Exception as e:
        print(f"❓ 予期しないエラー: {e}")

if __name__ == "__main__":
    debug_news_scraper()