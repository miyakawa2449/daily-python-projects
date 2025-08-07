import random

def main():
    choices = ["rock", "paper", "scissors"]  # グー、パー、チョキ

    print("じゃんけんゲーム（rock/paper/scissors）終了するには 'exit'")

    while True:
        user_choice = input("あなたの手を入力してください: ").lower()
        if user_choice in {"exit", "quit"}:
            print("ゲームを終了します。")
            break
        if user_choice not in choices:
            print("無効な手です。rock, paper, scissors から選んでください。")
            continue

        computer_choice = random.choice(choices)
        print(f"コンピュータの手: {computer_choice}")

        if user_choice == computer_choice:
            print("あいこです！")
        elif (
            (user_choice == "rock" and computer_choice == "scissors")
            or (user_choice == "scissors" and computer_choice == "paper")
            or (user_choice == "paper" and computer_choice == "rock")
        ):
            print("あなたの勝ち！")
        else:
            print("あなたの負け！")

if __name__ == "__main__":
    main()
