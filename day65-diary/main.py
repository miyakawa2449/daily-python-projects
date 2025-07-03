import os
from datetime import datetime

def get_diary_filename():
    today = datetime.now().strftime("%Y-%m-%d")
    return f"{today}.txt"

def write_diary(entry):
    filename = get_diary_filename()
    with open(filename, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%H:%M:%S")
        f.write(f"[{timestamp}] {entry}\n")

def read_diary():
    filename = get_diary_filename()
    if not os.path.exists(filename):
        print("今日の日記はまだありません。")
        return
    print(f"=== {filename} の内容 ===")
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read().strip())

def main():
    print("📔 日記アプリ（終了するには 'q'）")
    read_diary()
    while True:
        entry = input("日記に追加したいことを入力してください: ").strip()
        if entry.lower() in {"q", "quit", "exit"}:
            print("終了します。")
            break
        if entry:
            write_diary(entry)
            print("日記に追加しました！")
        else:
            print("何も入力されていません。")

if __name__ == "__main__":
    main()
