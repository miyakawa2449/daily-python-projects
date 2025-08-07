import requests

def get_exchange_rate(base="USD", target="JPY"):
    url = f"https://api.exchangerate.host/latest?base={base}&symbols={target}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # HTTPエラーを例外に
        
        data = response.json()
        rate = data["rates"][target]
        
        print(f"1 {base} = {rate} {target}")
        
    except requests.exceptions.RequestException as e:
        print(f"API通信エラー: {e}")
    except KeyError:
        print("APIレスポンスの解析に失敗しました。")

if __name__ == "__main__":
    print("為替レート取得アプリ")
    get_exchange_rate("USD", "JPY")
