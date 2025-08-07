import requests

def get_usd_jpy_rate():
    """USD → JPY の為替レートを取得（シンプル版）"""
    
    try:
        # 無料API使用
        url = "https://open.er-api.com/v6/latest/USD"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if data["result"] == "success":
            jpy_rate = data["rates"]["JPY"]
            print(f"💱 1 USD = {jpy_rate:.2f} JPY")
            
            # 計算例
            usd_amount = 100
            jpy_amount = usd_amount * jpy_rate
            print(f"💰 {usd_amount} USD = {jpy_amount:,.0f} JPY")
            
        else:
            print("❌ 為替レート取得に失敗しました")
            
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")

if __name__ == "__main__":
    print("USD → JPY 為替レート取得")
    get_usd_jpy_rate()