import random
import string

def generate_password(length=12):
    # 使用する文字のセット
    chars = string.ascii_letters + string.digits + string.punctuation
    
    # パスワードをランダムに生成
    password = ''.join(random.choices(chars, k=length))
    
    return password

def main():
    try:
        length = int(input("生成するパスワードの文字数を入力してください: "))
        if length <= 0:
            print("文字数は1以上にしてください。")
            return
        
        password = generate_password(length)
        print(f"生成されたパスワード: {password}")
        
    except ValueError:
        print("数字を入力してください。")

if __name__ == "__main__":
    main()
