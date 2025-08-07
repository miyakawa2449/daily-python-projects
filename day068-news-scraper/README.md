# 🌐 ニュースタイトル取得アプリ (News Scraper)

Hacker Newsからリアルタイムでニュースタイトルを取得するWebスクレイピングアプリケーションです。基本版とCSV保存対応の拡張版の2種類を実装し、Webスクレイピングの基礎から実用的なデータ処理まで学習できます。

## 📝 アプリケーション概要

**主な機能**:
- **リアルタイムニュース取得**: Hacker Newsの最新ニュースを即座に取得
- **HTMLの自動解析**: BeautifulSoupによる高精度なタグ解析
- **URL補完機能**: 内部リンクの自動補完で完全なURL表示
- **エラーハンドリング**: 通信エラーやHTML構造変更への対応
- **CSV保存機能**: データの永続化と後処理対応（拡張版のみ）

**学習ポイント**:
- Webスクレイピングの基本技術
- HTMLの構造理解とデバッグ手法
- ライブラリの適切な選択と組み合わせ
- 段階的な機能実装アプローチ

## 📁 ファイル構成

```
day68-news-scraper/
├── main2.py          # シンプル版（基本機能のみ）
├── main.py           # 拡張版（CSV保存・統計機能付き）
├── debug.py          # デバッグ用（HTML構造調査）
└── README.md         # このファイル
```

### 🎯 **各ファイルの役割**

#### **main2.py（シンプル版）**
- **目的**: ニュースタイトルの即座確認
- **依存ライブラリ**: `requests`, `beautifulsoup4`
- **機能**: 基本的な取得・表示のみ
- **適用場面**: 学習用、プロトタイプ、軽量実行

#### **main.py（拡張版）**
- **目的**: 包括的なニュースデータ管理
- **依存ライブラリ**: `requests`, `beautifulsoup4`, `csv`, `datetime`
- **機能**: CSV保存、統計分析、タイムスタンプ記録
- **適用場面**: データ分析、定期実行、履歴管理

#### **debug.py（デバッグ版）**
- **目的**: HTML構造の詳細調査
- **機能**: タグ数調査、クラス要素検出、HTML抜粋表示
- **適用場面**: 問題発生時の原因調査

## 🚀 実行方法

### 📋 **必要なライブラリのインストール**

```bash
pip install requests beautifulsoup4
```

**標準ライブラリ**（追加インストール不要）:
- `csv`: CSVファイル保存用
- `datetime`: 時刻処理用

### 💻 **実行コマンド**

#### **基本版（軽量・高速）**
```bash
cd day68-news-scraper
python main2.py
```

#### **拡張版（多機能）**
```bash
python main.py
```

#### **デバッグ版（問題調査用）**
```bash
python debug.py
```

## 💡 使い方

### 🎮 **基本版（main2.py）の実行例**

```bash
python main2.py
```

**出力例**:
```
🌐 Hacker Newsにアクセス中: https://news.ycombinator.com/
📰 Hacker News タイトル一覧 (31件):
 1. Hidden interface controls are affecting usability
    🔗 https://interactions.acm.org/archive/view/july-august-2025/...
 2. July 5, 1687: When Newton Explained Why You Don't Float Away
    🔗 https://multiverseemployeehandbook.com/blog/...
 3. Serving 200M requests per day with a CGI-bin
    🔗 https://simonwillison.net/2025/Jul/5/cgi-bin-performance/
...（最大20件まで表示）
```

### 🎯 **拡張版（main.py）の実行例**

```bash
python main.py
```

**出力例**:
```
🌐 Hacker News 拡張版スクレイパー開始
📰 取得成功: 31件
============================================================
 1. Hidden interface controls are affecting usability
    🔗 https://interactions.acm.org/archive/view/july-august-2025/...
    📊 文字数: 45 | タイプ: external

 2. July 5, 1687: When Newton Explained Why You Don't Float Away
    🔗 https://multiverseemployeehandbook.com/blog/...
    📊 文字数: 54 | タイプ: external
...

💾 データを hackernews_20250706_143025.csv に保存しました

📊 統計情報:
  • 総件数: 31件
  • 外部リンク: 28件
  • 内部リンク: 3件
  • 平均タイトル長: 42.3文字
  • 最長タイトル: Game publishers respond to Stop Killing Games... (89文字)
  • 最短タイトル: X-Clacks-Overhead (17文字)
```

### 🔍 **生成されるCSVファイルの構造**

```csv
title,url,type,length,timestamp
"Hidden interface controls are affecting usability","https://interactions.acm.org/...",external,45,"2025-07-06T14:30:25.123456"
"July 5, 1687: When Newton Explained Why You Don't Float Away","https://multiverseemployeehandbook.com/...",external,54,"2025-07-06T14:30:25.123457"
```

## 📖 学んだことや今後の改善案（学習ログ）

### 🔧 主要な学習ポイント

#### 1️⃣ **ライブラリの役割分担と連携**

**完璧な4つのライブラリ連携を実感**:

##### 🌐 **requests** - HTTP通信の魔法使い
```python
response = requests.get("https://news.ycombinator.com/", headers=headers, timeout=10)
response.raise_for_status()
```

**役割**:
- **Webページへのアクセス**: HTTP GETリクエスト送信
- **User-Agent設定**: ボット対策回避のためのブラウザ偽装
- **タイムアウト制御**: 10秒でタイムアウト設定
- **エラーチェック**: HTTPステータスコードによる異常検出

**学習成果**: 
- もしrequestsが無ければ数百行の低レベルソケット通信実装が必要
- HTTPプロトコルの詳細を意識せずに高度な通信が可能

##### 🏷️ **BeautifulSoup** - HTMLタグ整理の職人
```python
soup = BeautifulSoup(response.text, "html.parser")
title_elements = soup.find_all(class_="title")
link = title_elem.find("a")
title = link.get_text(strip=True)
href = link.get('href', '')
```

**役割**:
- **HTML解析**: 文字列HTMLを操作可能な構造に変換
- **要素検索**: クラス名やタグ名による柔軟な検索
- **テキスト抽出**: タグ内のテキスト取得と前後空白除去
- **属性取得**: href属性などの取得

**学習成果**:
- 正規表現による無理やりなHTML解析と比べて圧倒的に安全・確実
- HTML構造の変化にも柔軟に対応可能

##### 📊 **csv** - データ保存の秘書
```python
filename = f"hackernews_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
writer = csv.DictWriter(f, fieldnames=['title', 'url', 'type', 'length', 'timestamp'])
writer.writeheader()
writer.writerows(news_data)
```

**役割**:
- **構造化データ保存**: 辞書形式のデータを自動的にCSV形式に変換
- **ヘッダー管理**: 列名の自動設定
- **エスケープ処理**: カンマや改行を含むデータの安全な保存
- **文字化け防止**: UTF-8エンコーディングによる日本語対応

##### 📅 **datetime** - 時間管理のスペシャリスト
```python
'timestamp': datetime.now().isoformat()
filename = f"hackernews_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
```

**役割**:
- **現在時刻取得**: 高精度な現在時刻の取得
- **ISO形式変換**: 標準的な日時文字列への変換
- **ファイル名用フォーマット**: 年月日時分秒形式での文字列生成
- **一意性確保**: 同じファイル名の重複防止

#### 2️⃣ **Webスクレイピングの本質的理解**

##### 🎯 **問題発生→デバッグ→解決のプロセス**

**実際に体験した流れ**:
```
1. 初期実装: class="titlelink"でタイトル取得を試行
   ↓
2. 問題発生: 0件取得（取得失敗）
   ↓
3. デバッグ実行: debug.pyで実際のHTML構造調査
   ↓
4. 原因発見: class="title"が正しいセレクター（61個発見）
   ↓
5. 修正実装: 正しいセレクターに変更
   ↓
6. 成功: 31件のニュース取得成功
```

**重要な学習**:
- **仮定より調査**: 想像でコードを書くより実際のHTML確認が重要
- **段階的デバッグ**: 問題を細分化して一つずつ検証
- **柔軟な対応**: サイト構造の変更に対する適応能力

##### 🔍 **HTML構造理解の重要性**

**想定していた構造 vs 実際の構造**:
```html
<!-- 想定（間違い） -->
<a class="titlelink">ニュースタイトル</a>

<!-- 実際（正解） -->
<td class="title">
    <a href="...">ニュースタイトル</a>
</td>
```

**学習成果**:
- **2段階アプローチ**: 親要素→子要素の順で確実に取得
- **デバッグファースト**: 先にHTML構造を調査してからコード実装
- **複数パターン対応**: 複数の取得方法を用意して堅牢性向上

##### 🛡️ **User-Agentによるアクセス制御回避**

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers)
```

**学習内容**:
- **ボット対策の存在**: 多くのサイトが自動アクセスを制限
- **ブラウザ偽装の必要性**: 正常なブラウザアクセスのように見せる技術
- **倫理的配慮**: 過度なアクセスを避ける責任ある利用

#### 3️⃣ **段階的機能実装の価値**

##### 📈 **機能拡張の流れ**

```python
# Stage 1: 最小構成（main2.py）
import requests
from bs4 import BeautifulSoup
# 目的: 基本機能の確実な実装

# Stage 2: 保存機能追加
import csv
# 目的: データの永続化

# Stage 3: 時刻記録追加  
from datetime import datetime
# 目的: 履歴管理とファイル名一意化

# Stage 4: 統計分析追加
show_statistics()
# 目的: データの傾向分析
```

**学習価値**:
- **段階的開発**: 小さく始めて確実に拡張
- **目的別設計**: 用途に応じた適切なライブラリ選択
- **保守性向上**: 機能ごとに分離された明確な設計

#### 4️⃣ **エラーハンドリングの実践**

##### 🚨 **2段階のエラー処理**

```python
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # HTTPエラーチェック
    
    soup = BeautifulSoup(response.text, "html.parser")
    # データ処理...
    
except requests.exceptions.RequestException as e:
    print(f"🚨 リクエストエラー: {e}")
    print("💡 インターネット接続やURLを確認してください")
except Exception as e:
    print(f"❓ 予期しないエラー: {e}")
```

**学習内容**:
- **具体的エラー処理**: RequestExceptionによる通信エラーの特定
- **一般的エラー処理**: 予期しない問題への対応
- **ユーザーフレンドリー**: 分かりやすいエラーメッセージと対処法提示

##### 🔧 **防御的プログラミング**

```python
if link and link.get_text(strip=True):  # 空チェック
    headlines.append(link)

href = link.get('href', '')  # デフォルト値設定

if href.startswith('http'):  # URL形式判定
    full_url = href
else:
    full_url = f"https://news.ycombinator.com/{href}"
```

**学習成果**:
- **NULL安全**: 存在しない要素への対処
- **データ検証**: 期待する形式かの事前チェック
- **フォールバック処理**: 異常データへの代替処理

#### 5️⃣ **ライブラリ選択の柔軟性**

##### 🎯 **目的別ライブラリ選択**

**シンプル版（main2.py）の選択**:
```python
import requests
from bs4 import BeautifulSoup
# csv, datetime を削除
```

**メリット**:
- **高速起動**: インポート時間の短縮
- **軽量実行**: メモリ使用量の削減
- **理解しやすさ**: 複雑さの排除
- **プロトタイプ向け**: 機能検証の迅速化

**拡張版（main.py）の選択**:
```python
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
# 全機能搭載
```

**メリット**:
- **永続化**: データの保存と後処理
- **分析機能**: 統計情報の提供
- **履歴管理**: いつ取得したかの記録
- **本格運用**: 実用的な機能の網羅

##### 💡 **「必要な分だけ使う」の美学**

```python
# 車輪の再発明をしない
requests → HTTP通信の標準実装を利用
BeautifulSoup → HTML解析の信頼性ある実装を利用
csv → CSV形式の正確な実装を利用
datetime → 時刻処理の国際標準実装を利用

# しかし、不要なものは使わない
用途に応じてライブラリを選択的に利用
```

### 🚀 今後の改善・発展アイデア

#### 📈 **機能拡張案**

##### 1️⃣ **複数サイト対応**
```python
sites = [
    {"name": "Hacker News", "url": "https://news.ycombinator.com/", "method": scrape_hackernews},
    {"name": "Product Hunt", "url": "https://www.producthunt.com/", "method": scrape_producthunt},
    {"name": "Reddit", "url": "https://www.reddit.com/r/programming/", "method": scrape_reddit},
]

def multi_site_scraper():
    all_news = []
    for site in sites:
        news = site['method'](site['url'])
        all_news.extend(news)
    return all_news
```

##### 2️⃣ **フィルタリング機能**
```python
def filter_news_by_keywords(news_data, keywords):
    """キーワードに基づくニュースフィルタリング"""
    filtered = []
    for item in news_data:
        for keyword in keywords:
            if keyword.lower() in item['title'].lower():
                filtered.append(item)
                break
    return filtered

# 使用例
tech_news = filter_news_by_keywords(news_data, ['python', 'javascript', 'AI', 'machine learning'])
```

##### 3️⃣ **定期実行機能**
```python
import schedule
import time

def scheduled_scraping():
    """定期的なニュース取得とデータ蓄積"""
    print(f"📅 定期実行: {datetime.now()}")
    news_data = enhanced_hackernews_scraper()
    
    # 過去データとの比較
    compare_with_previous_data(news_data)

# 毎時実行の設定
schedule.every().hour.do(scheduled_scraping)

while True:
    schedule.run_pending()
    time.sleep(60)
```

##### 4️⃣ **データベース保存**
```python
import sqlite3

def save_to_database(news_data):
    """SQLiteデータベースへの保存"""
    conn = sqlite3.connect('news_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            type TEXT,
            length INTEGER,
            timestamp TEXT,
            UNIQUE(url)
        )
    ''')
    
    for item in news_data:
        cursor.execute('''
            INSERT OR IGNORE INTO news (title, url, type, length, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (item['title'], item['url'], item['type'], item['length'], item['timestamp']))
    
    conn.commit()
    conn.close()
```

##### 5️⃣ **Web UI対応**
```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/news')
def get_news():
    news_data = enhanced_hackernews_scraper()
    return jsonify(news_data)

@app.route('/api/news/search/<keyword>')
def search_news(keyword):
    news_data = enhanced_hackernews_scraper()
    filtered = filter_news_by_keywords(news_data, [keyword])
    return jsonify(filtered)

if __name__ == '__main__':
    app.run(debug=True)
```

#### 🎯 **技術的改善案**

##### 1️⃣ **並列処理による高速化**
```python
import concurrent.futures
import threading

def parallel_multi_site_scraping():
    """複数サイトの並列取得"""
    sites = [
        "https://news.ycombinator.com/",
        "https://www.reddit.com/r/programming/",
        "https://lobste.rs/",
    ]
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(fetch_hackernews_titles, site): site for site in sites}
        
        results = {}
        for future in concurrent.futures.as_completed(futures):
            site = futures[future]
            try:
                results[site] = future.result()
            except Exception as e:
                print(f"❌ {site} でエラー: {e}")
        
        return results
```

##### 2️⃣ **キャッシュ機能**
```python
import pickle
from datetime import datetime, timedelta

def cached_scraping(cache_duration_minutes=30):
    """キャッシュ機能付きスクレイピング"""
    cache_file = 'news_cache.pkl'
    
    try:
        with open(cache_file, 'rb') as f:
            cache_data = pickle.load(f)
            
        # キャッシュの有効性確認
        if datetime.now() - cache_data['timestamp'] < timedelta(minutes=cache_duration_minutes):
            print("📦 キャッシュからデータを取得")
            return cache_data['news_data']
    except FileNotFoundError:
        pass
    
    # 新しいデータを取得
    print("🌐 新しいデータを取得中...")
    news_data = enhanced_hackernews_scraper()
    
    # キャッシュに保存
    cache_data = {
        'news_data': news_data,
        'timestamp': datetime.now()
    }
    
    with open(cache_file, 'wb') as f:
        pickle.dump(cache_data, f)
    
    return news_data
```

##### 3️⃣ **設定ファイル対応**
```python
import json

def load_config():
    """設定ファイルからパラメータ読み込み"""
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

# config.json
{
    "sites": {
        "hackernews": {
            "url": "https://news.ycombinator.com/",
            "enabled": true,
            "max_items": 20
        },
        "reddit": {
            "url": "https://www.reddit.com/r/programming/",
            "enabled": false,
            "max_items": 15
        }
    },
    "output": {
        "format": "csv",
        "include_timestamp": true,
        "include_statistics": true
    },
    "scraping": {
        "timeout": 10,
        "retry_count": 3,
        "user_agent": "Mozilla/5.0 ..."
    }
}
```

#### 🛡️ **品質向上案**

##### 1️⃣ **テスト機能**
```python
import unittest
from unittest.mock import patch, Mock

class TestNewsScraper(unittest.TestCase):
    
    @patch('requests.get')
    def test_successful_scraping(self, mock_get):
        """正常なスクレイピングのテスト"""
        # モックレスポンス設定
        mock_response = Mock()
        mock_response.text = '<td class="title"><a href="test.html">Test Title</a></td>'
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        # テスト実行
        result = fetch_hackernews_titles()
        
        # 結果検証
        self.assertGreater(len(result), 0)
        self.assertEqual(result[0]['title'], 'Test Title')
    
    @patch('requests.get')
    def test_network_error_handling(self, mock_get):
        """ネットワークエラーのテスト"""
        mock_get.side_effect = requests.exceptions.RequestException("Network Error")
        
        with self.assertRaises(requests.exceptions.RequestException):
            fetch_hackernews_titles()

if __name__ == '__main__':
    unittest.main()
```

##### 2️⃣ **ログ機能**
```python
import logging

def setup_logging():
    """ログ設定"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('news_scraper.log'),
            logging.StreamHandler()
        ]
    )

def enhanced_scraper_with_logging():
    """ログ機能付きスクレイパー"""
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("🌐 スクレイピング開始")
        news_data = enhanced_hackernews_scraper()
        logger.info(f"✅ {len(news_data)}件のニュースを取得成功")
        return news_data
    except Exception as e:
        logger.error(f"❌ スクレイピング失敗: {e}")
        raise
```

### 💡 **重要な学習成果**

#### 🎯 **技術的理解の深化**

##### 📚 **ライブラリエコシステムの真価**
- **requests**: HTTP通信の複雑さを完全に隠蔽
- **BeautifulSoup**: HTML解析の安全性と柔軟性を提供
- **csv**: データ保存の標準的な実装
- **datetime**: 時刻処理の国際標準対応

**実感**: 「**ライブラリさまさま**」- 4つのライブラリが完璧に連携して高機能アプリを実現

##### 🔧 **問題解決プロセスの体系化**
1. **仮説実装**: 想定される方法で初期実装
2. **問題発生**: 期待する結果が得られない
3. **デバッグ調査**: 実際の状況を詳細に調査
4. **原因特定**: 仮定と現実の差異を発見
5. **修正実装**: 正確な情報に基づく再実装
6. **成功確認**: 期待する結果の獲得

**価値**: 今後あらゆる開発で活用できる普遍的なプロセス

##### 🎨 **設計思想の学習**
- **段階的開発**: 小さく始めて確実に拡張
- **目的別実装**: 用途に応じた適切な機能選択
- **保守性重視**: 理解しやすく変更しやすい設計
- **ユーザビリティ**: 分かりやすいメッセージと適切な処理

#### 🚀 **実用的価値**

##### ✅ **即座に活用可能**
- **情報収集ツール**: 日常的なニュース取得に使用可能
- **学習素材**: Webスクレイピングの教材として活用
- **拡張基盤**: より高度なデータ収集システムの基礎

##### 📈 **発展可能性**
- **ビジネス応用**: 競合分析、市場調査、トレンド分析
- **研究用途**: データサイエンス、自然言語処理の素材
- **自動化基盤**: 定期実行、アラート機能、レポート生成

## 🎉 総評

Day 68のWebスクレイピングプロジェクトは、**実用的なアプリケーション開発**と**基礎技術の深い理解**を同時に達成できた非常に価値の高い学習体験でした。

### ✅ **特に価値があった学習内容**

1. **ライブラリ連携の美しさ**: 4つのライブラリが完璧に連携する設計の理解
2. **問題解決プロセス**: デバッグファーストアプローチの実践的体験
3. **段階的開発**: 機能を段階的に追加する現実的な開発手法
4. **実用性と学習性**: 即座に使えるツールでありながら教育的価値も高い

### 🎯 **今後への展開**

このプロジェクトで習得した技術は、**あらゆるWeb関連開発**において基盤技術として活用できます。特に**データ収集**、**API連携**、**情報分析**といった分野において、今回の経験が直接的に活かされるでしょう。

**Webスクレイピングの基礎から実用まで**を網羅的に学習できた、
