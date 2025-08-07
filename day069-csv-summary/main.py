import pandas as pd

def summarize_csv(filename="sample.csv"):
    print(f"📂 読み込みファイル: {filename}")
    try:
        # CSV読み込み
        df = pd.read_csv(filename)
        print("\n✅ データの先頭5行:")
        print(df.head())

        print("\n📊 列ごとの基本統計量:")
        print(df.describe())

        # 例: 'Category' 列でグループ化して 'Amount' を合計
        if 'Category' in df.columns and 'Amount' in df.columns:
            grouped = df.groupby('Category')['Amount'].sum().reset_index()
            print("\n📈 カテゴリ別合計:")
            print(grouped)

            # 結果を保存
            grouped.to_csv("summary.csv", index=False)
            print("\n💾 summary.csv に保存しました！")

    except FileNotFoundError:
        print("❌ ファイルが見つかりませんでした。")
    except Exception as e:
        print(f"❓ 予期しないエラー: {e}")

if __name__ == "__main__":
    summarize_csv("sample.csv")
