import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def create_task():
    task = input("タスク内容を入力してください: ").strip()
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print("✅ タスクを追加しました。")

def read_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📂 タスクはありません。")
    else:
        print("📋 タスク一覧:")
        for idx, t in enumerate(tasks, 1):
            status = "✔️" if t['done'] else "❌"
            print(f"{idx}. [{status}] {t['task']}")

def update_task():
    read_tasks()
    tasks = load_tasks()
    try:
        num = int(input("完了にするタスク番号: "))
        tasks[num-1]['done'] = True
        save_tasks(tasks)
        print("🔄 タスクを更新しました。")
    except (ValueError, IndexError):
        print("⚠️ 無効な番号です。")

def delete_task():
    read_tasks()
    tasks = load_tasks()
    try:
        num = int(input("削除するタスク番号: "))
        removed = tasks.pop(num-1)
        save_tasks(tasks)
        print(f"🗑️ タスクを削除しました: {removed['task']}")
    except (ValueError, IndexError):
        print("⚠️ 無効な番号です。")

def main():
    while True:
        print("\n1: タスク追加")
        print("2: タスク一覧")
        print("3: タスク完了に更新")
        print("4: タスク削除")
        print("5: 終了")
        choice = input("番号を選んでください: ").strip()

        if choice == '1':
            create_task()
        elif choice == '2':
            read_tasks()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("👋 終了します。")
            break
        else:
            print("⚠️ 無効な選択です。")

if __name__ == "__main__":
    main()
