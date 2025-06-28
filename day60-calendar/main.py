import calendar

def format_japanese_calendar(year, month):
    """日本語でカレンダーを生成"""
    # 月名の日本語対応
    month_names = {
        1: "1月", 2: "2月", 3: "3月", 4: "4月", 5: "5月", 6: "6月",
        7: "7月", 8: "8月", 9: "9月", 10: "10月", 11: "11月", 12: "12月"
    }
    
    # 曜日の日本語対応
    day_names = ["日", "月", "火", "水", "木", "金", "土"]
    
    # 基本カレンダーデータを取得（日曜日始まりに統一）
    cal = calendar.Calendar(firstweekday=6)  # 6 = 日曜日始まり
    month_calendar = cal.monthdays2calendar(year, month)
    
    # ヘッダー作成
    header = f"{year}年{month_names[month]}"
    day_header = "  ".join(f"{day:>1}" for day in day_names)  # 曜日も2文字幅に統一
    
    # 日付部分を生成
    lines = []
    for week in month_calendar:
        week_str = "  ".join(f"{day[0]:2}" if day[0] != 0 else "  " for day in week)
        lines.append(week_str)
    
    # 結果を組み立て
    result = f"{header:^24}\n{day_header}\n" + "\n".join(lines)
    return result

def main():
    print("カレンダー表示アプリ 📅")
    try:
        year = int(input("年を入力してください（例: 2024）: "))
        month = int(input("月を入力してください（1〜12）: "))
        if month < 1 or month > 12:
            print("1〜12 の月を入力してください。")
            return

        # 英語カレンダー生成
        cal = calendar.TextCalendar(firstweekday=6)  # 日曜日始まり
        month_str = cal.formatmonth(year, month, w=3, l=1)
        print("\n📅 English Calendar:")
        print(month_str)
        
        # 日本語カレンダー生成
        japanese_calendar = format_japanese_calendar(year, month)
        print("\n🗾 日本語カレンダー:")
        print(japanese_calendar)

    except ValueError:
        print("数字を入力してください。")

if __name__ == "__main__":
    main()
