import requests

def get_exchange_rate(base="USD", target="JPY"):
    """無料APIを使用した為替レート取得"""
    
    # 🆓 無料API 1: Open Exchange Rates API (制限あり)
    url = f"https://open.er-api.com/v6/latest/{base}"
    
    try:
        print(f"🌐 APIにリクエスト中...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # APIレスポンスの構造確認
        if data.get("result") == "success":
            rates = data.get("rates", {})
            if target in rates:
                rate = rates[target]
                print(f"💱 1 {base} = {rate:.4f} {target}")
                return rate
            else:
                print(f"❌ {target} の為替レートが見つかりません")
                print(f"利用可能な通貨: {list(rates.keys())[:10]}...")  # 最初の10個を表示
        else:
            print(f"❌ API呼び出しが失敗: {data}")
            
    except requests.exceptions.RequestException as e:
        print(f"🚨 API通信エラー: {e}")
    except KeyError as e:
        print(f"🔑 データ構造エラー: {e}")
    except Exception as e:
        print(f"❓ 予期しないエラー: {e}")

def get_exchange_rate_alternative(base="USD", target="JPY"):
    """代替無料API"""
    
    # 🆓 無料API 2: Currency API (GitHub)
    base_lower = base.lower()
    target_lower = target.lower()
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{base_lower}/{target_lower}.json"
    
    try:
        print(f"🌐 代替APIにリクエスト中...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if target_lower in data:
            rate = data[target_lower]
            print(f"💱 1 {base} = {rate:.4f} {target}")
            return rate
        else:
            print(f"❌ レート情報が見つかりません: {data}")
            
    except requests.exceptions.RequestException as e:
        print(f"🚨 代替API通信エラー: {e}")
    except Exception as e:
        print(f"❓ 代替API予期しないエラー: {e}")

def get_multiple_rates():
    """複数の為替レートを取得"""
    pairs = [
        ("USD", "JPY"),
        ("EUR", "JPY"), 
        ("GBP", "JPY"),
        ("USD", "EUR")
    ]
    
    print("📊 複数の為替レート取得中...")
    for base, target in pairs:
        print(f"\n--- {base} → {target} ---")
        rate = get_exchange_rate(base, target)
        if rate is None:
            print("⚠️ 代替APIを試します...")
            get_exchange_rate_alternative(base, target)

if __name__ == "__main__":
    print("為替レート取得アプリ（修正版）")
    print("=" * 40)
    
    # 基本的な取得
    get_exchange_rate("USD", "JPY")
    
    print("\n" + "=" * 40)
    
    # 複数通貨の取得
    get_multiple_rates()