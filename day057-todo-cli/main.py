import json
import os

# main.pyと同じディレクトリにtodo_data.jsonを保存
FILENAME = os.path.join(os.path.dirname(__file__), "todo_data.json")

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)

def main():
    tasks = load_tasks()
    while True:
        print("\nToDoリスト:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print("\n1: 追加 | 2: 削除 | 3: 終了")
        choice = input("選択してください: ")
        if choice == "1":
            task = input("追加するタスク: ")
            tasks.append(task)
        elif choice == "2":
            num = int(input("削除する番号: ")) - 1
            if 0 <= num < len(tasks):
                tasks.pop(num)
        elif choice == "3":
            break
        else:
            print("無効な入力です。")
        save_tasks(tasks)

if __name__ == "__main__":
    main()
