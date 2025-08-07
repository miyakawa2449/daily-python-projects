import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class WeatherAPI:
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY')
        self.base_url = "http://api.openweathermap.org/data/2.5"
        
        if not self.api_key:
            raise ValueError("OpenWeatherMap APIキーが設定されていません")
    
    def get_current_weather(self, city="Tokyo,JP"):
        """現在の天気を取得"""
        url = f"{self.base_url}/weather"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',  # 摂氏
            'lang': 'ja'        # 日本語
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"API呼び出しエラー: {e}")
            return None
    
    def get_forecast(self, city="Tokyo,JP"):
        """5日間の天気予報を取得"""
        url = f"{self.base_url}/forecast"
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'ja'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"予報取得エラー: {e}")
            return None
    
    def format_weather_data(self, data):
        """天気データを整形"""
        if not data:
            return None
            
        return {
            'city': data['name'],
            'country': data['sys']['country'],
            'temperature': round(data['main']['temp']),
            'feels_like': round(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'wind_speed': data['wind']['speed'],
            'wind_direction': data['wind'].get('deg', 0),
            'visibility': data.get('visibility', 0) / 1000,  # km変換
            'datetime': datetime.now().strftime('%Y年%m月%d日 %H:%M')
        }
    
    def format_forecast_data(self, data):
        """予報データを整形"""
        if not data:
            return None
            
        forecasts = []
        for item in data['list'][:5]:  # 5日分
            forecasts.append({
                'date': datetime.fromtimestamp(item['dt']).strftime('%m/%d'),
                'day': datetime.fromtimestamp(item['dt']).strftime('%a'),
                'temperature': round(item['main']['temp']),
                'description': item['weather'][0]['description'],
                'icon': item['weather'][0]['icon']
            })
        
        return forecasts

# 日本の主要都市リスト
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