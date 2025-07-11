import qrcode

def generate_qr(data, filename="qrcode.png"):
    """QRコードを生成して保存"""
    qr = qrcode.QRCode(
        version=1,  # サイズ（1〜40）
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 誤り訂正レベル
        box_size=10,  # 1ボックスのサイズ
        border=4  # 白い枠のサイズ
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QRコードを {filename} に保存しました！")

if __name__ == "__main__":
    text = input("QRコードにする文字列やURLを入力してください: ")
    generate_qr(text.strip())
