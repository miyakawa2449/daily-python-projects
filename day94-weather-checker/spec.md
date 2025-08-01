# 🌤️ day94-weather-checker 設計書

## 📋 **プロジェクト概要**

### 🎯 **アプリケーション名**
**天気予報Webアプリ - OpenWeatherMap API 統合システム**

### 📝 **プロジェクト説明**
OpenWeatherMap APIを活用して、日本全国の現在の天気と5日間予報をリアルタイムで表示するWebアプリケーションです。Flask、JavaScript非同期処理、レスポンシブデザインを組み合わせた実用的な天気情報ツールです。

### 🗂️ **ファイル構成**
```
day94-weather-checker/
├── app.py                      # Flask メインアプリケーション
├── .env                        # 環境変数（APIキー管理）
├── .gitignore                  # Git除外設定
├── templates/
│   └── index.html             # 天気表示メイン画面
├── static/
│   ├── css/
│   │   └── style.css          # 天気アプリデザイン
│   ├── js/
│   │   └── weather.js         # 非同期API通信・UI制御
│   └── icons/                 # 天気アイコン（オプション）
├── utils/
│   ├── weather_api.py         # OpenWeatherMap API処理
│   └── test_api.py            # API接続診断ツール
├── requirements.txt           # Python依存関係
├── spec.md                    # この設計書
└── README.md                  # プロジェクト説明
```

---

## 🎯 **学習目標**

### **主要技術習得**
- ✅ **API連携**: OpenWeatherMap REST API の完全活用
- ✅ **非同期処理**: JavaScript async/await・Promise.all
- ✅ **Flask API**: JSON レスポンス・エラーハンドリング
- ✅ **環境変数**: python-dotenv による安全な設定管理

### **実践的スキル**
- ✅ **外部サービス統合**: サードパーティAPI の効果的活用
- ✅ **レスポンシブUI**: CSS Grid・Flexbox による柔軟なレイアウト
- ✅ **エラーハンドリング**: 通信エラー・データ欠損への対処
- ✅ **セキュリティ**: APIキー管理・XSS対策

---

## 🎨 **機能要件**

### **🔧 基本機能（必須実装）**

#### **1. 現在天気表示**
- 気温・体感温度・湿度・気圧
- 天気説明（日本語）・天気アイコン
- 風速・風向・視程

#### **2. 5日間予報表示**
- 日付・曜日・予想気温
- 天気アイコン・天気説明
- グリッドレイアウトでの見やすい表示

#### **3. 地域選択機能**
- 日本全国10都市対応
- ドロップダウンによる直感的選択
- 選択時の自動データ更新

#### **4. データ更新機能**
- 手動更新ボタン
- 5分間隔自動更新
- ローディング状態表示

### **🌟 追加機能（チャレンジ要素）**

#### **5. レスポンシブデザイン**
- デスクトップ・タブレット・スマートフォン対応
- CSS Grid による動的レイアウト
- タッチデバイス最適化

#### **6. エラーハンドリング**
- API接続エラー時の適切な表示
- 無効な都市名への対処
- ネットワークエラー時の自動復旧

---

## 🛠️ **技術仕様**

### **バックエンド（Flask + OpenWeatherMap API）**

#### **主要エンドポイント**
```python
# Flask API エンドポイント
@app.route('/')
def index():
    """メイン画面表示"""
    return render_template('index.html')

@app.route('/api/weather/current')
def get_current_weather():
    """現在天気取得"""
    city = request.args.get('city')
    return jsonify(weather_data)

@app.route('/api/weather/forecast')  
def get_forecast():
    """5日間予報取得"""
    city = request.args.get('city')
    return jsonify(forecast_data)
```

#### **OpenWeatherMap API統合**
```python
# weather_api.py 主要処理
import requests
import os
from dotenv import load_dotenv

class WeatherAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.base_url = 'https://api.openweathermap.org/data/2.5'
    
    def get_current_weather(self, city):
        """現在天気取得"""
        url = f"{self.base_url}/weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ja'
        }
        response = requests.get(url, params=params)
        return response.json()
    
    def get_forecast(self, city):
        """5日間予報取得"""
        url = f"{self.base_url}/forecast"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ja'
        }
        response = requests.get(url, params=params)
        return response.json()
```

### **フロントエンド（HTML5 + CSS + JS）**

#### **JavaScript 非同期API通信**
```javascript
// weather.js 主要処理
class WeatherApp {
    constructor() {
        this.selectedCity = '東京';
        this.updateInterval = null;
        this.init();
    }
    
    async init() {
        this.setupEventListeners();
        await this.updateWeatherData();
        this.startAutoUpdate();
    }
    
    // 並行データ取得
    async updateWeatherData() {
        try {
            this.showLoading();
            
            const [currentWeather, forecast] = await Promise.all([
                this.fetchCurrentWeather(this.selectedCity),
                this.fetchForecast(this.selectedCity)
            ]);
            
            this.displayCurrentWeather(currentWeather);
            this.displayForecast(forecast);
            
        } catch (error) {
            this.showError('天気データの取得に失敗しました');
        } finally {
            this.hideLoading();
        }
    }
    
    // API通信（現在天気）
    async fetchCurrentWeather(city) {
        const response = await fetch(`/api/weather/current?city=${encodeURIComponent(city)}`);
        if (!response.ok) throw new Error('API Error');
        return await response.json();
    }
    
    // UI更新（現在天気）
    displayCurrentWeather(data) {
        document.getElementById('city-name').textContent = data.city;
        document.getElementById('temperature').textContent = data.temperature;
        document.getElementById('description').textContent = data.description;
        // ... 他の要素更新
    }
}

// アプリケーション初期化
document.addEventListener('DOMContentLoaded', () => {
    new WeatherApp();
});
```

#### **レスポンシブCSS設計**
```css
/* style.css レスポンシブレイアウト */
.weather-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    display: grid;
    gap: 20px;
}

/* デスクトップレイアウト */
.weather-main {
    display: flex;
    gap: 20px;
}

.current-weather {
    flex: 1;
    background: linear-gradient(135deg, #74b9ff, #0984e3);
    border-radius: 15px;
    padding: 20px;
    color: white;
}

/* 5日間予報グリッド */
.forecast-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 15px;
}

/* モバイル対応 */
@media (max-width: 768px) {
    .weather-main {
        flex-direction: column;
    }
    
    .weather-details {
        grid-template-columns: repeat(2, 1fr);
    }
    
    .forecast-container {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* ローディングアニメーション */
.loading {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 3px solid #f3f3f3;
    border-top: 3px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
```

---

## 📱 **UI/UXデザイン要件**

### **レイアウト構成**

#### **ヘッダー部分**
```html
<!-- 都市選択・更新ボタン -->
<header class="weather-header">
    <h1>🌤️ 天気予報</h1>
    <div class="controls">
        <select id="city-select">
            <option value="東京">東京</option>
            <option value="大阪">大阪</option>
            <!-- 他都市 -->
        </select>
        <button id="refresh-btn">🔄 更新</button>
    </div>
</header>
```

#### **メイン表示エリア**
```html
<!-- 現在天気・詳細情報 -->
<main class="weather-main">
    <section class="current-weather">
        <div class="weather-overview">
            <h2 id="city-name">東京</h2>
            <div class="temperature-display">
                <span id="temperature">25</span>°C
            </div>
            <p id="description">晴れ</p>
        </div>
        
        <div class="weather-details">
            <div class="detail-item">
                <span class="label">体感温度</span>
                <span id="feels-like">27°C</span>
            </div>
            <!-- 他詳細情報 -->
        </div>
    </section>
</main>
```

#### **5日間予報エリア**
```html
<!-- 予報カード群 -->
<section class="forecast-section">
    <h3>📅 5日間予報</h3>
    <div class="forecast-container" id="forecast-container">
        <!-- JavaScript で動的生成 -->
    </div>
</section>
```

### **操作フロー**

#### **基本操作シーケンス**
```
1. ページ読み込み
   ↓
2. デフォルト都市（東京）の天気データ取得
   ↓
3. 現在天気・5日間予報の表示
   ↓
4. ユーザーによる都市変更
   ↓
5. 新しい都市のデータ取得・表示更新
   ↓
6. 5分間隔での自動更新開始
```

---

## ⚡ **技術実装のポイント**

### **🔒 セキュリティ対策**

#### **APIキー管理**
```bash
# .env ファイル（Git管理対象外）
OPENWEATHER_API_KEY=your_actual_api_key_here

# .gitignore 設定
.env
*.env
.DS_Store
__pycache__/
```

#### **入力値検証**
```python
# app.py セキュリティ対策
from flask import request, jsonify, escape

@app.route('/api/weather/current')
def get_current_weather():
    city = request.args.get('city', '').strip()
    
    # 入力値検証
    if not city:
        return jsonify({'error': '都市名が必要です'}), 400
    
    # サニタイズ
    city = escape(city)
    
    # 許可都市リスト検証
    if city not in ALLOWED_CITIES:
        return jsonify({'error': '対応していない都市です'}), 400
```

### **📁 ファイル管理**

#### **環境設定ファイル**
```python
# requirements.txt
Flask==2.3.3
requests==2.31.0
python-dotenv==1.0.0

# app.py 環境変数読み込み
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')
```

#### **設定の外部化**
```python
# config.py（推奨）
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')
    OPENWEATHER_BASE_URL = 'https://api.openweathermap.org/data/2.5'
    
    # 対応都市定義
    JAPANESE_CITIES = {
        '東京': 'Tokyo,JP',
        '大阪': 'Osaka,JP',
        '名古屋': 'Nagoya,JP',
        '福岡': 'Fukuoka,JP',
        '札幌': 'Sapporo,JP',
        '仙台': 'Sendai,JP',
        '広島': 'Hiroshima,JP',
        '京都': 'Kyoto,JP',
        '神戸': 'Kobe,JP',
        '横浜': 'Yokohama,JP'
    }
```

### **🎨 パフォーマンス最適化**

#### **効率的なAPI呼び出し**
```javascript
// 並行処理による高速化
const fetchWeatherData = async (city) => {
    try {
        // Promise.all で並行実行
        const [currentResponse, forecastResponse] = await Promise.all([
            fetch(`/api/weather/current?city=${encodeURIComponent(city)}`),
            fetch(`/api/weather/forecast?city=${encodeURIComponent(city)}`)
        ]);
        
        // レスポンス検証
        if (!currentResponse.ok || !forecastResponse.ok) {
            throw new Error('API request failed');
        }
        
        // 並行データ解析
        const [currentData, forecastData] = await Promise.all([
            currentResponse.json(),
            forecastResponse.json()
        ]);
        
        return { currentData, forecastData };
        
    } catch (error) {
        throw new Error(`天気データ取得エラー: ${error.message}`);
    }
};
```

#### **メモリ効率的なDOM操作**
```javascript
// 効率的な要素更新
const updateWeatherDisplay = (weatherData) => {
    // DocumentFragment による効率的更新
    const fragment = document.createDocumentFragment();
    
    // 要素の一括更新
    const updates = {
        'city-name': weatherData.city,
        'temperature': `${weatherData.temperature}°C`,
        'description': weatherData.description,
        'humidity': `${weatherData.humidity}%`,
        'pressure': `${weatherData.pressure}hPa`
    };
    
    // バッチ更新でリフロー最小化
    Object.entries(updates).forEach(([id, value]) => {
        const element = document.getElementById(id);
        if (element) element.textContent = value;
    });
};
```

---

## 🧪 **開発・テスト手順**

### **Phase 1: 環境構築・基本設定**

#### **Step 1: プロジェクト初期化**
```bash
# ディレクトリ作成
mkdir day94-weather-checker
cd day94-weather-checker

# Git初期化
git init

# Python仮想環境作成（推奨）
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係インストール
pip install Flask requests python-dotenv
pip freeze > requirements.txt
```

#### **Step 2: APIキー取得・設定**
```bash
# OpenWeatherMap アカウント作成
# 1. https://openweathermap.org/ でサインアップ
# 2. API Keys タブでキーを確認
# 3. .env ファイル作成

echo "OPENWEATHER_API_KEY=your_api_key_here" > .env
echo ".env" >> .gitignore
```

#### **Step 3: 基本ファイル作成**
```bash
# ディレクトリ構造作成
mkdir -p templates static/css static/js utils

# 基本ファイル作成
touch app.py
touch templates/index.html
touch static/css/style.css
touch static/js/weather.js
touch utils/weather_api.py
touch utils/test_api.py
```

### **Phase 2: API接続・データ取得**

#### **Step 4: API接続テスト**
```python
# utils/test_api.py
import os
import requests
from dotenv import load_dotenv

def test_api_connection():
    load_dotenv()
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    if not api_key:
        print("❌ APIキーが見つかりません")
        return False
    
    # 基本接続テスト
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': 'Tokyo,JP',
        'appid': api_key,
        'units': 'metric',
        'lang': 'ja'
    }
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            print(f"✅ API接続成功！東京の気温: {temp}°C")
            return True
        else:
            print(f"❌ API エラー: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 接続エラー: {e}")
        return False

if __name__ == "__main__":
    test_api_connection()
```

#### **Step 5: WeatherAPI クラス実装**
```python
# utils/weather_api.py
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

class WeatherAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.base_url = 'https://api.openweathermap.org/data/2.5'
        
        if not self.api_key:
            raise ValueError("OPENWEATHER_API_KEY が設定されていません")
    
    def get_current_weather(self, city):
        """現在の天気情報を取得"""
        url = f"{self.base_url}/weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ja'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        # データ整形
        return {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'wind_speed': data.get('wind', {}).get('speed', 0),
            'wind_direction': data.get('wind', {}).get('deg', 0),
            'visibility': data.get('visibility', 0) / 1000,  # km変換
            'datetime': datetime.now().strftime('%Y年%m月%d日 %H:%M')
        }
    
    def get_forecast(self, city):
        """5日間天気予報を取得"""
        url = f"{self.base_url}/forecast"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ja'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        forecasts = []
        
        # 1日1つの予報を抽出（正午のデータを使用）
        for item in data['list'][::8]:  # 3時間間隔なので8個おき
            date_obj = datetime.fromtimestamp(item['dt'])
            forecasts.append({
                'date': date_obj.strftime('%m/%d'),
                'day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'][date_obj.weekday()],
                'temperature': round(item['main']['temp']),
                'description': item['weather'][0]['description'],
                'icon': item['weather'][0]['icon']
            })
        
        return forecasts[:5]  # 5日分
```

### **Phase 3: Flask API実装**

#### **Step 6: Flask アプリケーション作成**
```python
# app.py
from flask import Flask, render_template, jsonify, request
from utils.weather_api import WeatherAPI
import logging

app = Flask(__name__)

# ログ設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# WeatherAPI インスタンス
weather_api = WeatherAPI()

# 対応都市マッピング
JAPANESE_CITIES = {
    '東京': 'Tokyo,JP',
    '大阪': 'Osaka,JP',
    '名古屋': 'Nagoya,JP',
    '福岡': 'Fukuoka,JP',
    '札幌': 'Sapporo,JP',
    '仙台': 'Sendai,JP',
    '広島': 'Hiroshima,JP',
    '京都': 'Kyoto,JP',
    '神戸': 'Kobe,JP',
    '横浜': 'Yokohama,JP'
}

@app.route('/')
def index():
    """メイン画面"""
    return render_template('index.html')

@app.route('/api/weather/current')
def get_current_weather():
    """現在の天気API"""
    city = request.args.get('city', '東京')
    
    # 日本語都市名を英語に変換
    english_city = JAPANESE_CITIES.get(city, city)
    
    try:
        weather_data = weather_api.get_current_weather(english_city)
        logger.info(f"現在天気取得成功: {city}")
        return jsonify(weather_data)
    
    except requests.exceptions.RequestException as e:
        logger.error(f"API エラー: {e}")
        return jsonify({'error': 'API接続エラー'}), 500
    
    except Exception as e:
        logger.error(f"予期しないエラー: {e}")
        return jsonify({'error': 'サーバーエラー'}), 500

@app.route('/api/weather/forecast')
def get_forecast():
    """5日間予報API"""
    city = request.args.get('city', '東京')
    
    # 日本語都市名を英語に変換
    english_city = JAPANESE_CITIES.get(city, city)
    
    try:
        forecast_data = weather_api.get_forecast(english_city)
        logger.info(f"予報取得成功: {city}")
        return jsonify(forecast_data)
    
    except requests.exceptions.RequestException as e:
        logger.error(f"API エラー: {e}")
        return jsonify({'error': 'API接続エラー'}), 500
    
    except Exception as e:
        logger.error(f"予期しないエラー: {e}")
        return jsonify({'error': 'サーバーエラー'}), 500

@app.route('/favicon.ico')
def favicon():
    """ファビコン要求対応"""
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### **Phase 4: フロントエンド実装**

#### **Step 7: HTML テンプレート作成**
```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🌤️ 天気予報アプリ</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="weather-container">
        <!-- ヘッダー -->
        <header class="weather-header">
            <h1>🌤️ 天気予報</h1>
            <div class="controls">
                <select id="city-select">
                    <option value="東京">東京</option>
                    <option value="大阪">大阪</option>
                    <option value="名古屋">名古屋</option>
                    <option value="福岡">福岡</option>
                    <option value="札幌">札幌</option>
                    <option value="仙台">仙台</option>
                    <option value="広島">広島</option>
                    <option value="京都">京都</option>
                    <option value="神戸">神戸</option>
                    <option value="横浜">横浜</option>
                </select>
                <button id="refresh-btn">🔄 更新</button>
            </div>
        </header>

        <!-- ローディング表示 -->
        <div id="loading" class="loading-container" style="display: none;">
            <div class="loading"></div>
            <p>天気データを取得中...</p>
        </div>

        <!-- エラー表示 -->
        <div id="error-message" class="error-container" style="display: none;">
            <p id="error-text"></p>
            <button onclick="location.reload()">再試行</button>
        </div>

        <!-- メイン天気表示 -->
        <main class="weather-main" id="weather-content">
            <!-- 現在の天気 -->
            <section class="current-weather">
                <div class="weather-overview">
                    <h2 id="city-name">読み込み中...</h2>
                    <div class="temperature-display">
                        <span id="temperature">--</span>°C
                    </div>
                    <p id="description">--</p>
                    <p class="update-time">最終更新: <span id="last-update">--</span></p>
                </div>
                
                <div class="weather-details">
                    <div class="detail-item">
                        <span class="label">体感温度</span>
                        <span id="feels-like">--°C</span>
                    </div>
                    <div class="detail-item">
                        <span class="label">湿度</span>
                        <span id="humidity">--%</span>
                    </div>
                    <div class="detail-item">
                        <span class="label">気圧</span>
                        <span id="pressure">--hPa</span>
                    </div>
                    <div class="detail-item">
                        <span class="label">風速</span>
                        <span id="wind-speed">--m/s</span>
                    </div>
                    <div class="detail-item">
                        <span class="label">視程</span>
                        <span id="visibility">--km</span>
                    </div>
                </div>
            </section>
        </main>

        <!-- 5日間予報 -->
        <section class="forecast-section">
            <h3>📅 5日間予報</h3>
            <div class="forecast-container" id="forecast-container">
                <!-- JavaScript で動的生成 -->
            </div>
        </section>
    </div>

    <script src="{{ url_for('static', filename='js/weather.js') }}"></script>
</body>
</html>
```

#### **Step 8: JavaScript アプリケーション作成**
```javascript
// static/js/weather.js
class WeatherApp {
    constructor() {
        this.selectedCity = '東京';
        this.updateInterval = null;
        this.lastUpdateTime = null;
        
        // DOM要素参照
        this.elements = {
            citySelect: document.getElementById('city-select'),
            refreshBtn: document.getElementById('refresh-btn'),
            loading: document.getElementById('loading'),
            errorMessage: document.getElementById('error-message'),
            weatherContent: document.getElementById('weather-content'),
            forecastContainer: document.getElementById('forecast-container')
        };
        
        this.init();
    }
    
    async init() {
        console.log('🌤️ 天気アプリ初期化中...');
        this.setupEventListeners();
        await this.updateWeatherData();
        this.startAutoUpdate();
    }
    
    setupEventListeners() {
        // 都市選択変更
        this.elements.citySelect.addEventListener('change', async (e) => {
            this.selectedCity = e.target.value;
            await this.updateWeatherData();
        });
        
        // 更新ボタン
        this.elements.refreshBtn.addEventListener('click', async () => {
            await this.updateWeatherData();
        });
        
        // ページ可視性変更（タブ切り替え時の自動更新）
        document.addEventListener('visibilitychange', () => {
            if (!document.hidden && this.shouldUpdate()) {
                this.updateWeatherData();
            }
        });
    }
    
    shouldUpdate() {
        if (!this.lastUpdateTime) return true;
        const fiveMinutes = 5 * 60 * 1000;
        return Date.now() - this.lastUpdateTime > fiveMinutes;
    }
    
    async updateWeatherData() {
        try {
            this.showLoading();
            console.log(`📡 ${this.selectedCity}の天気データ取得中...`);
            
            // 並行データ取得
            const [currentWeather, forecast] = await Promise.all([
                this.fetchCurrentWeather(this.selectedCity),
                this.fetchForecast(this.selectedCity)
            ]);
            
            this.displayCurrentWeather(currentWeather);
            this.displayForecast(forecast);
            this.lastUpdateTime = Date.now();
            
            console.log('✅ 天気データ更新完了');
            
        } catch (error) {
            console.error('❌ 天気データ取得エラー:', error);
            this.showError(`天気データの取得に失敗しました: ${error.message}`);
        } finally {
            this.hideLoading();
        }
    }
    
    async fetchCurrentWeather(city) {
        const response = await fetch(`/api/weather/current?city=${encodeURIComponent(city)}`);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        return await response.json();
    }
    
    async fetchForecast(city) {
        const response = await fetch(`/api/weather/forecast?city=${encodeURIComponent(city)}`);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        return await response.json();
    }
    
    displayCurrentWeather(data) {
        if (data.error) {
            throw new Error(data.error);
        }
        
        // 基本情報更新
        document.getElementById('city-name').textContent = data.city;
        document.getElementById('temperature').textContent = data.temperature;
        document.getElementById('description').textContent = data.description;
        document.getElementById('last-update').textContent = data.datetime;
        
        // 詳細情報更新
        document.getElementById('feels-like').textContent = `${data.feels_like}°C`;
        document.getElementById('humidity').textContent = `${data.humidity}%`;
        document.getElementById('pressure').textContent = `${data.pressure}hPa`;
        document.getElementById('wind-speed').textContent = `${data.wind_speed}m/s`;
        document.getElementById('visibility').textContent = `${data.visibility}km`;
        
        // 表示切り替え
        this.elements.weatherContent.style.display = 'block';
    }
    
    displayForecast(forecasts) {
        if (forecasts.error) {
            throw new Error(forecasts.error);
        }
        
        this.elements.forecastContainer.innerHTML = '';
        
        forecasts.forEach(forecast => {
            const forecastCard = document.createElement('div');
            forecastCard.className = 'forecast-card';
            forecastCard.innerHTML = `
                <div class="forecast-date">${forecast.date}</div>
                <div class="forecast-day">${forecast.day}</div>
                <div class="forecast-icon">🌤️</div>
                <div class="forecast-temp">${forecast.temperature}°C</div>
                <div class="forecast-desc">${forecast.description}</div>
            `;
            this.elements.forecastContainer.appendChild(forecastCard);
        });
    }
    
    showLoading() {
        this.elements.loading.style.display = 'block';
        this.elements.errorMessage.style.display = 'none';
        this.elements.weatherContent.style.display = 'none';
        
        // ボタンを無効化
        this.elements.refreshBtn.disabled = true;
        this.elements.citySelect.disabled = true;
    }
    
    hideLoading() {
        this.elements.loading.style.display = 'none';
        
        // ボタンを有効化
        this.elements.refreshBtn.disabled = false;
        this.elements.citySelect.disabled = false;
    }
    
    showError(message) {
        this.elements.errorMessage.style.display = 'block';
        this.elements.weatherContent.style.display = 'none';
        document.getElementById('error-text').textContent = message;
    }
    
    startAutoUpdate() {
        // 5分間隔で自動更新
        this.updateInterval = setInterval(() => {
            console.log('🔄 自動更新実行');
            this.updateWeatherData();
        }, 5 * 60 * 1000); // 5分
        
        console.log('⏰ 自動更新開始（5分間隔）');
    }
    
    stopAutoUpdate() {
        if (this.updateInterval) {
            clearInterval(this.updateInterval);
            this.updateInterval = null;
            console.log('⏹️ 自動更新停止');
        }
    }
}

// アプリケーション初期化
document.addEventListener('DOMContentLoaded', () => {
    console.log('🚀 DOMロード完了 - アプリ起動');
    window.weatherApp = new WeatherApp();
});

// ページ離脱時の清理
window.addEventListener('beforeunload', () => {
    if (window.weatherApp) {
        window.weatherApp.stopAutoUpdate();
    }
});
```

### **Phase 5: CSS スタイリング**

#### **Step 9: レスポンシブデザイン実装**
```css
/* static/css/style.css */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #87CEEB 0%, #98FB98 50%, #F0E68C 100%);
    min-height: 100vh;
    padding: 20px;
}

.weather-container {
    max-width: 1200px;
    margin: 0 auto;
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    overflow: hidden;
}

/* ヘッダー */
.weather-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px 30px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.weather-header h1 {
    font-size: 2rem;
    font-weight: 600;
}

.controls {
    display: flex;
    gap: 15px;
    align-items: center;
}

#city-select {
    padding: 8px 12px;
    border: none;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.9);
    font-size: 1rem;
    cursor: pointer;
}

#refresh-btn {
    padding: 8px 16px;
    border: none;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.2);
    color: white;
    cursor: pointer;
    transition: all 0.3s ease;
}

#refresh-btn:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-2px);
}

#refresh-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

/* ローディング・エラー */
.loading-container, .error-container {
    text-align: center;
    padding: 40px;
}

.loading {
    display: inline-block;
    width: 40px;
    height: 40px;
    border: 4px solid #f3f3f3;
    border-top: 4px solid #3498db;
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 20px;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.error-container {
    color: #e74c3c;
    background: rgba(231, 76, 60, 0.1);
    margin: 20px;
    border-radius: 10px;
}

/* メイン天気表示 */
.weather-main {
    padding: 30px;
}

.current-weather {
    background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
    color: white;
    border-radius: 15px;
    padding: 30px;
    margin-bottom: 30px;
}

.weather-overview {
    text-align: center;
    margin-bottom: 30px;
}

.weather-overview h2 {
    font-size: 2rem;
    margin-bottom: 10px;
}

.temperature-display {
    font-size: 4rem;
    font-weight: 300;
    margin: 20px 0;
}

.weather-overview p {
    font-size: 1.2rem;
    text-transform: capitalize;
}

.update-time {
    font-size: 0.9rem;
    opacity: 0.8;
    margin-top: 10px;
}

/* 詳細情報グリッド */
.weather-details {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 20px;
}

.detail-item {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    padding: 15px;
    text-align: center;
    backdrop-filter: blur(10px);
}

.detail-item .label {
    display: block;
    font-size: 0.9rem;
    opacity: 0.8;
    margin-bottom: 5px;
}

.detail-item span:last-child {
    font-size: 1.2rem;
    font-weight: 600;
}

/* 5日間予報 */
.forecast-section {
    padding: 0 30px 30px;
}

.forecast-section h3 {
    font-size: 1.5rem;
    margin-bottom: 20px;
    color: #2c3e50;
}

.forecast-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 15px;
}

.forecast-card {
    background: white;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
}

.forecast-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.forecast-date {
    font-size: 1rem;
    font-weight: 600;
    color: #2c3e50;
    margin-bottom: 5px;
}

.forecast-day {
    font-size: 0.9rem;
    color: #7f8c8d;
    margin-bottom: 10px;
}

.forecast-icon {
    font-size: 2rem;
    margin: 10px 0;
}

.forecast-temp {
    font-size: 1.3rem;
    font-weight: 600;
    color: #e74c3c;
    margin: 10px 0;
}

.forecast-desc {
    font-size: 0.9rem;
    color: #7f8c8d;
    text-transform: capitalize;
}

/* レスポンシブデザイン */
@media (max-width: 768px) {
    body {
        padding: 10px;
    }
    
    .weather-header {
        flex-direction: column;
        gap: 15px;
        text-align: center;
    }
    
    .weather-header h1 {
        font-size: 1.5rem;
    }
    
    .controls {
        width: 100%;
        justify-content: center;
    }
    
    .weather-main {
        padding: 20px;
    }
    
    .current-weather {
        padding: 20px;
    }
    
    .temperature-display {
        font-size: 3rem;
    }
    
    .weather-details {
        grid-template-columns: repeat(2, 1fr);
        gap: 15px;
    }
    
    .forecast-section {
        padding: 0 20px 20px;
    }
    
    .forecast-container {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 480px) {
    .weather-header h1 {
        font-size: 1.3rem;
    }
    
    .temperature-display {
        font-size: 2.5rem;
    }
    
    .weather-details {
        grid-template-columns: 1fr;
    }
    
    .forecast-container {
        grid-template-columns: 1fr;
    }
}

/* アニメーション */
.weather-main {
    animation: fadeIn 0.5s ease-in;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* スクロールバーカスタマイズ */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb {
    background: #888;
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: #555;
}
```

---

## 🎯 **学習チェックポイント**

### **技術理解度確認**

#### **API統合理解（必須）**
- [ ] **OpenWeatherMap API**: エンドポイント・パラメータの理解
- [ ] **認証方式**: APIキーによる認証の実装
- [ ] **レスポンス処理**: JSON データの解析・変換
- [ ] **エラーハンドリング**: HTTP ステータスコード・例外処理

#### **非同期JavaScript理解（重要）**
- [ ] **async/await**: 非同期関数の適切な使用
- [ ] **Promise.all**: 並行処理による最適化
- [ ] **fetch API**: HTTP リクエストの送信・受信
- [ ] **DOM操作**: 動的なコンテンツ更新

#### **Flask Web開発理解（重要）**
- [ ] **ルーティング**: URL と関数のマッピング
- [ ] **JSON API**: データのシリアライゼーション
- [ ] **テンプレート**: Jinja2 による動的HTML生成
- [ ] **静的ファイル**: CSS・JavaScript の配信

#### **環境管理理解（推奨）**
- [ ] **環境変数**: python-dotenv による設定管理
- [ ] **セキュリティ**: APIキーの安全な管理
- [ ] **Git管理**: .gitignore による機密情報保護

### **実装品質評価**

#### **コード品質**
- [ ] **可読性**: 適切な命名・コメント・構造化
- [ ] **保守性**: 機能分離・モジュール化
- [ ] **拡張性**: 新機能追加の容易さ
- [ ] **エラー処理**: 堅牢な例外・エラーハンドリング

#### **ユーザビリティ**
- [ ] **レスポンシブ**: 各デバイスでの適切な表示
- [ ] **操作性**: 直感的なインターフェース
- [ ] **フィードバック**: ローディング・エラー表示
- [ ] **パフォーマンス**: 快適な応答速度

---

## 🚀 **今日の成功基準**

### **🎯 最小成功ライン（MVP）**
1. **API接続** → ✅ OpenWeatherMap から正確な天気データ取得
2. **基本表示** → ✅ 現在天気・5日間予報の表示
3. **地域切り替え** → ✅ 10都市での動作確認
4. **エラー処理** → ✅ 接続エラー時の適切な表示

### **🌟 理想的な完成度**
1. **レスポンシブUI** → ✅ モバイル・デスクトップ最適化
2. **自動更新** → ✅ 定期的なデータ更新機能
3. **使いやすさ** → ✅ 直感的で快適な操作感
4. **実用性** → ✅ 日常的に使える完成度

---

## 🎊 **day94完了後の達成感**

### **🏆 習得した技術スキル**
- ✅ **外部API統合**: 実際のWebサービスとの連携
- ✅ **非同期処理**: 現代的なJavaScript開発手法
- ✅ **レスポンシブデザイン**: マルチデバイス対応
- ✅ **環境管理**: 安全な設定・認証情報管理

### **🌟 実用アプリ開発経験**
- ✅ **毎日使える**: 実際の天気確認ツールとして活用
- ✅ **データ精度**: 気象庁データと一致する正確な情報
- ✅ **完成度**: 企業レベルのWebアプリケーション品質

### **🚀 今後への展開力**
- 🌐 **他API統合**: ニュース・株価・地図など様々なサービス
- 📱 **モバイルアプリ**: PWA・React Native への応用
- 🔄 **リアルタイム**: WebSocket・Server-Sent Events の活用
- 🏢 **業務システム**: 企業向けダッシュボード・監視ツール

**day94は、API統合Webアプリ開発の完全なマスターと、実用的なツール作成能力の獲得という、大きな成長を達成しました！** 🌤️✨

---

## 📚 **参考リソース**

### **公式ドキュメント**
- **OpenWeatherMap API**: https://openweathermap.org/api
- **Flask**: https://flask.palletsprojects.com/
- **MDN Web Docs**: https://developer.mozilla.org/

### **学習リソース**
- **JavaScript非同期処理**: Promise・async/await の詳細
- **CSS Grid**: モダンレイアウト手法
- **REST API設計**: HTTP メソッド・ステータスコード

### **発展学習**
- **WebSocket**: リアルタイム通信
- **PWA**: Progressive Web Apps
- **TypeScript**: 型安全なJavaScript開発

---

これで、初心者プログラマーが段階的に理解しながら天気予報Webアプリを開発できる完全な設計書が完成しました！🌤️🚀