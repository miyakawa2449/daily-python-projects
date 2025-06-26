import time
import re

def parse_time_string(time_str):
    pattern = r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?"
    cleaned = time_str.strip().lower().replace(" ", "")
    match = re.fullmatch(pattern, cleaned)
    if not match:
        return None

    hours = int(match.group(1)) if match.group(1) else 0
    minutes = int(match.group(2)) if match.group(2) else 0
    seconds = int(match.group(3)) if match.group(3) else 0

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds if total_seconds > 0 else None


def countdown(seconds):
    try:
        for i in range(seconds, 0, -1):
            # カーソルを行の先頭に戻して上書き表示
            print(f"\r残り {i:02d} 秒", end="", flush=True)
            time.sleep(1)
        print("\r時間になりました！" + " " * 10)  # 余分な文字を消去
    except KeyboardInterrupt:
        print("\n\nタイマーをキャンセルしました。")

def main():
    try:
        user_input = input("時間を入力してください（例: 1h30m、2m、45s）: ")
        seconds = parse_time_string(user_input)
        if seconds is None:
            print("無効な形式です。例：1h30m、2m、45s など")
            return
        countdown(seconds)
    except ValueError:
        print("数字を入力してください。")

if __name__ == "__main__":
    main()
