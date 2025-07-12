from PIL import Image

def resize_image(input_path, output_path, width, height):
    """画像を指定サイズにリサイズして保存"""
    with Image.open(input_path) as img:
        resized_img = img.resize((width, height))
        resized_img.save(output_path)
        print(f"✅ {output_path} に保存しました！")

if __name__ == "__main__":
    input_file = input("変換する画像ファイル名を入力してください: ").strip()
    width = int(input("幅(px)を入力してください: "))
    height = int(input("高さ(px)を入力してください: "))
    output_file = input("保存するファイル名を入力してください: ").strip()

    resize_image(input_file, output_file, width, height)
