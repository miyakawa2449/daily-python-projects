import pandas as pd
import os
from datetime import datetime

FILENAME = "household.csv"

# CSVファイルが存在しない場合は、ヘッダー付きで新規作成
if not os.path.exists(FILENAME):
    df_init = pd.DataFrame(columns=["日付", "項目", "金額"])
    df_init.to_csv(FILENAME, index=False)

def add_record():
    date_str = input("日付を入力（YYYY-MM-DD、省略で今日）: ").strip()
    if not date_str:
        date_str = datetime.today().strftime("%Y-%m-%d")

    item = input("項目を入力: ").strip()
    try:
        amount = int(input("金額を入力（整数）: ").strip())
    except ValueError:
        print("❌ 数字で入力してください")
        return

    new_data = pd.DataFrame([[date_str, item, amount]], columns=["日付", "項目", "金額"])
    new_data.to_csv(FILENAME, mode='a', header=False, index=False)
    print("✅ データを追加しました。")

def show_summary():
    df = pd.read_csv(FILENAME)
    print("\n📋 全データ:")
    print(df)

    print("\n💰 合計金額:", df["金額"].sum(), "円")

    print("\n📊 項目別の合計:")
    print(df.groupby("項目")["金額"].sum())

if __name__ == "__main__":
    while True:
        print("\n=== シンプル家計簿 ===")
        print("1. データを追加")
        print("2. 集計を表示")
        print("3. 終了")

        choice = input("番号を選んでください: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            print("👋 終了します。")
            break
        else:
            print("❌ 無効な入力です。")
