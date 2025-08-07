from flask import Flask, render_template, request, jsonify
from utils.weather_api import WeatherAPI, JAPANESE_CITIES
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key')

# WeatherAPI インスタンス
weather_api = WeatherAPI()

@app.route('/')
def index():
    """メイン画面"""
    return render_template('index.html', cities=JAPANESE_CITIES)

@app.route('/api/weather/current')
def get_current_weather():
    """現在の天気API"""
    city = request.args.get('city', 'Tokyo,JP')
    
    # 日本語都市名の変換
    if city in JAPANESE_CITIES:
        city = JAPANESE_CITIES[city]
    
    # 天気データ取得
    raw_data = weather_api.get_current_weather(city)
    if not raw_data:
        return jsonify({'error': '天気データの取得に失敗しました'}), 500
    
    # データ整形
    weather_data = weather_api.format_weather_data(raw_data)
    return jsonify(weather_data)

@app.route('/api/weather/forecast')
def get_forecast():
    """天気予報API"""
    city = request.args.get('city', 'Tokyo,JP')
    
    # 日本語都市名の変換
    if city in JAPANESE_CITIES:
        city = JAPANESE_CITIES[city]
    
    # 予報データ取得
    raw_data = weather_api.get_forecast(city)
    if not raw_data:
        return jsonify({'error': '予報データの取得に失敗しました'}), 500
    
    # データ整形
    forecast_data = weather_api.format_forecast_data(raw_data)
    return jsonify(forecast_data)

# favicon対応
@app.route('/favicon.ico')
def favicon():
    return '', 204

# エラーハンドラーを簡素化（専用テンプレート不要）
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'ページが見つかりません'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'サーバーエラーが発生しました'}), 500

if __name__ == '__main__':
    app.run(debug=True)