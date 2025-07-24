import os
from dotenv import load_dotenv
from openai import OpenAI

# .envファイルからAPIキーを読み込む
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    """ChatGPTにプロンプトを送信して応答を取得"""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "あなたは親切なAIアシスタントです。"},
                {"role": "user", "content": prompt}
            ]
        )
        message = response.choices[0].message.content
        return message.strip()
    except Exception as e:
        return f"❌ エラーが発生しました: {e}"

def main():
    print("🤖 ChatGPT APIチャットボット（終了するには 'exit'）")
    while True:
        user_input = input("🧑 あなた: ")
        if user_input.lower() in ['exit', 'quit']:
            print("👋 終了します。")
            break
        reply = chat_with_gpt(user_input)
        print(f"🤖 GPT: {reply}\n")

if __name__ == "__main__":
    main()
