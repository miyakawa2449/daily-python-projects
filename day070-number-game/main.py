import random

def number_game():
    answer = random.randint(1, 100)
    tries = 0

    print("🔢 数当てゲームへようこそ！")
    print("1から100の中から正解を当ててください。")

    while True:
        try:
            guess = int(input("あなたの予想: "))
            tries += 1

            if guess < answer:
                print("もっと大きい数です。")
            elif guess > answer:
                print("もっと小さい数です。")
            else:
                print(f"🎉 正解！{tries} 回で当てました！")
                break

        except ValueError:
            print("⚠️ 数字を入力してください。")

if __name__ == "__main__":
    number_game()
