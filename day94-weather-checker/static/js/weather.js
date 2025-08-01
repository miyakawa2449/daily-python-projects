// 現在の天気と予報データを管理
let currentWeatherData = null;
let forecastData = null;

// DOM要素の取得
const citySelect = document.getElementById('citySelect');
const updateBtn = document.getElementById('updateBtn');
const loadingCurrent = document.getElementById('loadingCurrent');
const loadingForecast = document.getElementById('loadingForecast');
const weatherCard = document.getElementById('weatherCard');
const forecastContainer = document.getElementById('forecastContainer');
const errorMessage = document.getElementById('errorMessage');

// ページ読み込み時に初期データを取得
document.addEventListener('DOMContentLoaded', function() {
    updateWeather();
    
    // 都市選択変更時の自動更新
    citySelect.addEventListener('change', updateWeather);
});

// 天気データを更新
async function updateWeather() {
    const selectedCity = citySelect.value;
    
    // ローディング表示
    showLoading();
    hideError();
    
    try {
        // 現在の天気と予報を並行取得
        const [currentWeather, forecast] = await Promise.all([
            fetchCurrentWeather(selectedCity),
            fetchForecast(selectedCity)
        ]);
        
        if (currentWeather && forecast) {
            displayCurrentWeather(currentWeather);
            displayForecast(forecast);
            hideLoading();
        } else {
            throw new Error('天気データの取得に失敗しました');
        }
        
    } catch (error) {
        console.error('天気更新エラー:', error);
        showError(error.message);
        hideLoading();
    }
}

// 現在の天気を取得
async function fetchCurrentWeather(city) {
    try {
        const response = await fetch(`/api/weather/current?city=${encodeURIComponent(city)}`);
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        return data;
        
    } catch (error) {
        console.error('現在天気取得エラー:', error);
        throw error;
    }
}

// 天気予報を取得
async function fetchForecast(city) {
    try {
        const response = await fetch(`/api/weather/forecast?city=${encodeURIComponent(city)}`);
        
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
        
        const data = await response.json();
        
        if (data.error) {
            throw new Error(data.error);
        }
        
        return data;
        
    } catch (error) {
        console.error('予報取得エラー:', error);
        throw error;
    }
}

// 現在の天気を表示
function displayCurrentWeather(data) {
    currentWeatherData = data;
    
    // 天気アイコン
    const weatherIcon = document.getElementById('weatherIcon');
    weatherIcon.src = `http://openweathermap.org/img/wn/${data.icon}@2x.png`;
    weatherIcon.alt = data.description;
    
    // 基本情報
    document.getElementById('cityName').textContent = data.city;
    document.getElementById('weatherDescription').textContent = data.description;
    document.getElementById('temperature').textContent = data.temperature;
    document.getElementById('feelsLike').textContent = data.feels_like;
    
    // 詳細情報
    document.getElementById('humidity').textContent = `${data.humidity}%`;
    document.getElementById('windSpeed').textContent = `${data.wind_speed} m/s`;
    document.getElementById('pressure').textContent = `${data.pressure} hPa`;
    document.getElementById('visibility').textContent = `${data.visibility} km`;
    document.getElementById('updateTime').textContent = data.datetime;
    
    // カード表示
    weatherCard.style.display = 'block';
}

// 5日間予報を表示
function displayForecast(data) {
    forecastData = data;
    
    forecastContainer.innerHTML = '';
    
    data.forEach(forecast => {
        const forecastCard = document.createElement('div');
        forecastCard.className = 'forecast-card';
        
        forecastCard.innerHTML = `
            <div class="forecast-date">${forecast.date}</div>
            <div class="forecast-day">${getDayName(forecast.day)}</div>
            <img class="forecast-icon" 
                 src="http://openweathermap.org/img/wn/${forecast.icon}@2x.png" 
                 alt="${forecast.description}">
            <div class="forecast-temp">${forecast.temperature}°C</div>
            <div class="forecast-desc">${forecast.description}</div>
        `;
        
        forecastContainer.appendChild(forecastCard);
    });
    
    forecastContainer.style.display = 'grid';
}

// 曜日の日本語変換
function getDayName(day) {
    const dayNames = {
        'Mon': '月',
        'Tue': '火', 
        'Wed': '水',
        'Thu': '木',
        'Fri': '金',
        'Sat': '土',
        'Sun': '日'
    };
    return dayNames[day] || day;
}

// ローディング表示
function showLoading() {
    loadingCurrent.style.display = 'block';
    loadingForecast.style.display = 'block';
    weatherCard.style.display = 'none';
    forecastContainer.style.display = 'none';
    
    // 更新ボタンを無効化
    updateBtn.disabled = true;
    updateBtn.textContent = '更新中...';
}

// ローディング非表示
function hideLoading() {
    loadingCurrent.style.display = 'none';
    loadingForecast.style.display = 'none';
    
    // 更新ボタンを有効化
    updateBtn.disabled = false;
    updateBtn.textContent = '🔄 更新';
}

// エラー表示
function showError(message) {
    document.getElementById('errorText').textContent = message;
    errorMessage.style.display = 'block';
    weatherCard.style.display = 'none';
    forecastContainer.style.display = 'none';
}

// エラー非表示
function hideError() {
    errorMessage.style.display = 'none';
}

// 自動更新（5分ごと）
setInterval(updateWeather, 5 * 60 * 1000);

// ページの可視性が変わった時の処理
document.addEventListener('visibilitychange', function() {
    if (!document.hidden) {
        // ページが再表示された時に更新
        updateWeather();
    }
});