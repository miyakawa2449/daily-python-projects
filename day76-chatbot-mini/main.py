import random

def respond(user_input):
    """ルールベースの簡易応答"""
    user_input = user_input.lower()
    if "こんにちは" in user_input:
        greetings = [
            "こんにちは！ご機嫌いかがですか？",
            "こんにちは！今日は良い天気ですね！",
            "こんにちは！お元気ですか？"
        ]
        return random.choice(greetings)
    elif "元気" in user_input:
        return "それは良かったです！"
    elif "さようなら" in user_input or "バイバイ" in user_input:
        return "さようなら！また話しましょう！"
    elif any(word in user_input for word in ["天気", "晴れ", "雨"]):
        return "今日の天気については詳しくないのですが、お出かけの予定はありますか？"
    else:
        return "すみません、よくわかりません。"

def main():
    print("ミニチャットボットへようこそ！(終了するには 'exit')")
    while True:
        user_input = input("あなた: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("チャットを終了します。")
            break
        reply = respond(user_input)
        print(f"Bot: {reply}")

if __name__ == "__main__":
    main()
