import requests
import os
from dotenv import load_dotenv

load_dotenv() # .envファイルから環境変数を読み込む

def translate_text(text, target_lang="EN"):
    """DeepL APIを使ってテキストを翻訳"""
    api_key = os.getenv("DEEPL_API_KEY")
    if not api_key:
        print("❌ 環境変数 DEEPL_API_KEY が設定されていません")
        return

    url = "https://api-free.deepl.com/v2/translate"
    params = {
        "auth_key": api_key,
        "text": text,
        "target_lang": target_lang
    }

    try:
        response = requests.post(url, data=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        translated_text = data["translations"][0]["text"]
        return translated_text
    except requests.exceptions.RequestException as e:
        print(f"🚨 API通信エラー: {e}")
    except Exception as e:
        print(f"❓ 予期しないエラー: {e}")

def main():
    print("🌐 翻訳アプリ (終了するには 'exit')")
    while True:
        text = input("翻訳するテキストを入力してください: ").strip()
        if text.lower() in {"exit", "quit"}:
            print("👋 終了します。")
            break
        translated = translate_text(text, target_lang="EN")
        if translated:
            print(f"✅ 翻訳結果: {translated}")

if __name__ == "__main__":
    main()
