from datetime import datetime

def stopwatch():
    print("⏱️ ストップウォッチ開始！ Enterキーでスタートします。")
    input()
    start_time = datetime.now()
    print(f"▶️ 計測開始: {start_time.strftime('%H:%M:%S')}")
    
    try:
        input("⏹️ 計測終了するには Enterキーを押してください...")
    except KeyboardInterrupt:
        print("\n⏹️ キーボード割り込みで終了しました。")

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    seconds = elapsed_time.total_seconds()

    print(f"⏹️ 計測終了: {end_time.strftime('%H:%M:%S')}")
    print(f"⌛ 経過時間: {seconds:.2f} 秒")

if __name__ == "__main__":
    stopwatch()
