import random

def main():
    omikuji_list = [
        "大吉: 今日は最高の一日になるでしょう！",
        "中吉: 良いことがありそうです。",
        "小吉: 小さな幸運が訪れます。",
        "末吉: 期待しすぎず、流れに任せましょう。",
        "凶: 気を引き締めて慎重に行動してください。",
        "大凶: 無理をせず、今日は休むのが吉です。"
    ]
    
    print("おみくじアプリ🎴")
    while True:
        user_input = input("おみくじを引きますか？（y/n）: ").lower()
        
        if user_input == "y":
            result = random.choice(omikuji_list)
            print(f"結果: {result}\n")
        elif user_input == "n":
            print("また引いてください！")
            break
        else:
            print("y か n を入力してください。")

if __name__ == "__main__":
    main()
