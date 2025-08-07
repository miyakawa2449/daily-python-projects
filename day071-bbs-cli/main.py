from datetime import datetime

FILENAME = "bbs_log.txt"

def write_post(content):
    """投稿内容をファイルに保存"""
    with open(FILENAME, 'a', encoding='utf-8') as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {content}\n")

def show_posts():
    """投稿一覧を表示"""
    print("\n📝 現在の投稿ログ:")
    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if not lines:
                print("(まだ投稿はありません)")
            else:
                for i, line in enumerate(lines, 1):
                    print(f"{i}: {line.strip()}")
    except FileNotFoundError:
        print("(ログファイルがまだありません)")

def main():
    print("💬 CLI掲示板へようこそ")
    while True:
        print("\n1: 投稿する")
        print("2: 投稿一覧を見る")
        print("3: 終了")
        choice = input("番号を選んでください: ").strip()

        if choice == '1':
            content = input("投稿内容を入力してください: ").strip()
            if content:
                write_post(content)
                print("✅ 投稿を保存しました。")
            else:
                print("⚠️ 空の投稿は保存できません。")
        elif choice == '2':
            show_posts()
        elif choice == '3':
            print("👋 終了します。")
            break
        else:
            print("⚠️ 無効な選択です。")

if __name__ == "__main__":
    main()
