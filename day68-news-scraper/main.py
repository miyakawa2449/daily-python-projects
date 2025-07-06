import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def enhanced_hackernews_scraper():
    """拡張版 Hacker News スクレイパー"""
    
    print("🌐 Hacker News 拡張版スクレイパー開始")
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    response = requests.get("https://news.ycombinator.com/", headers=headers, timeout=10)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, "html.parser")
    title_elements = soup.find_all(class_="title")
    
    news_data = []
    
    for title_elem in title_elements:
        link = title_elem.find("a")
        if link and link.get_text(strip=True):
            title = link.get_text(strip=True)
            href = link.get('href', '')
            
            # URL正規化
            if href.startswith('http'):
                full_url = href
                url_type = "external"
            else:
                full_url = f"https://news.ycombinator.com/{href}"
                url_type = "internal"
            
            # データ構造化
            news_item = {
                'title': title,
                'url': full_url,
                'type': url_type,
                'length': len(title),
                'timestamp': datetime.now().isoformat()
            }
            news_data.append(news_item)
    
    # 結果表示
    print(f"📰 取得成功: {len(news_data)}件")
    print("=" * 60)
    
    for i, item in enumerate(news_data[:15], 1):
        print(f"{i:2d}. {item['title']}")
        print(f"    🔗 {item['url']}")
        print(f"    📊 文字数: {item['length']} | タイプ: {item['type']}")
        print()
    
    # CSV保存
    save_to_csv(news_data)
    
    # 統計情報
    show_statistics(news_data)
    
    return news_data

def save_to_csv(news_data):
    """ニュースデータをCSVに保存"""
    filename = f"hackernews_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['title', 'url', 'type', 'length', 'timestamp']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(news_data)
    
    print(f"💾 データを {filename} に保存しました")

def show_statistics(news_data):
    """統計情報を表示"""
    if not news_data:
        return
    
    external_count = sum(1 for item in news_data if item['type'] == 'external')
    internal_count = len(news_data) - external_count
    avg_length = sum(item['length'] for item in news_data) / len(news_data)
    
    print("📊 統計情報:")
    print(f"  • 総件数: {len(news_data)}件")
    print(f"  • 外部リンク: {external_count}件")
    print(f"  • 内部リンク: {internal_count}件")
    print(f"  • 平均タイトル長: {avg_length:.1f}文字")
    
    # 最長・最短タイトル
    longest = max(news_data, key=lambda x: x['length'])
    shortest = min(news_data, key=lambda x: x['length'])
    
    print(f"  • 最長タイトル: {longest['title'][:50]}... ({longest['length']}文字)")
    print(f"  • 最短タイトル: {shortest['title']} ({shortest['length']}文字)")

if __name__ == "__main__":
    enhanced_hackernews_scraper()
