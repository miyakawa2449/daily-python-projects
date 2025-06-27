import re

def is_safe_expression(expr):
    # 数字、演算子、括弧、小数点のみ許可
    pattern = r'^[0-9+\-*/().\s]+$'
    return re.match(pattern, expr) is not None

def main():
    print("シンプル電卓アプリ（終了するには 'exit'）")
    while True:
        expr = input("式を入力してください: ")
        if expr.lower() in {"exit", "quit"}:
            print("終了します。")
            break
        if is_safe_expression(expr):
            try:
                result = eval(expr)
                print(f"答え: {result}")
            except ZeroDivisionError:
                print("ゼロで割ることはできません。")
            except Exception as e:
                print(f"エラーが発生しました: {e}")
        else:
            print("無効な文字が含まれています")

if __name__ == "__main__":
    main()
