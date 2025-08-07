import requests

def debug_exchange_rate(base="USD", target="JPY"):
    url = f"https://api.exchangerate.host/latest?base={base}&symbols={target}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        # 🔍 APIレスポンスの中身を確認
        print("=== APIレスポンス全体 ===")
        print(data)
        print("\n=== データの型 ===")
        print(type(data))
        print("\n=== 利用可能なキー ===")
        if isinstance(data, dict):
            print(list(data.keys()))
        
    except requests.exceptions.RequestException as e:
        print(f"API通信エラー: {e}")
    except Exception as e:
        print(f"予期しないエラー: {e}")

if __name__ == "__main__":
    print("為替レート取得アプリ（デバッグ版）")
    debug_exchange_rate("USD", "JPY")