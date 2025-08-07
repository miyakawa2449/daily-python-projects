import requests
from bs4 import BeautifulSoup

def fetch_hackernews_titles(url="https://news.ycombinator.com/"):
    print(f"🌐 Hacker Newsにアクセス中: {url}")
    
    try:
        # User-Agentを設定（一部サイトでブロック回避）
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # 修正: class="title"の要素を取得
        title_elements = soup.find_all(class_="title")
        
        headlines = []
        for title_elem in title_elements:
            # title要素内のaタグ（リンク）を探す
            link = title_elem.find("a")
            if link and link.get_text(strip=True):  # 空でないテキストを持つリンク
                headlines.append(link)
        
        print(f"📰 Hacker News タイトル一覧 ({len(headlines)}件):")
        
        if headlines:
            for i, headline in enumerate(headlines[:20], 1):  # 最初の20件
                title = headline.get_text(strip=True)
                href = headline.get('href', '')
                
                print(f"{i:2d}. {title}")
                
                # URLの表示
                if href:
                    if href.startswith('http'):
                        print(f"    🔗 {href}")
                    else:
                        print(f"    🔗 https://news.ycombinator.com/{href}")
                
        else:
            print("❌ ニュースタイトルが見つかりませんでした")
            print("🔍 HTMLの構造を再確認してください")
            
    except requests.exceptions.RequestException as e:
        print(f"🚨 リクエストエラー: {e}")
        print("💡 インターネット接続やURLを確認してください")
    except Exception as e:
        print(f"❓ 予期しないエラー: {e}")

if __name__ == "__main__":
    fetch_hackernews_titles()