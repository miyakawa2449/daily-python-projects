# utils/test_api.py - APIキーのテスト用
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_api_key():
    """APIキーの有効性をテスト"""
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    print(f"🔍 APIキー確認: {api_key[:8]}...{api_key[-4:] if api_key and len(api_key) > 12 else 'キーが短すぎます'}")
    
    if not api_key or api_key == 'your_actual_api_key_here':
        print("❌ APIキーが設定されていません！")
        print("   .envファイルで OPENWEATHER_API_KEY を設定してください")
        return False
    
    # 実際にAPIを呼び出してテスト
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': 'Tokyo,JP',
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(url, params=params)
        print(f"📡 API レスポンス: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API接続成功！東京の気温: {data['main']['temp']}°C")
            return True
        elif response.status_code == 401:
            print("❌ APIキーが無効です！")
            print("   OpenWeatherMapで正しいAPIキーを確認してください")
            return False
        else:
            print(f"❌ API エラー: {response.status_code} - {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 接続エラー: {e}")
        return False

if __name__ == "__main__":
    test_api_key()