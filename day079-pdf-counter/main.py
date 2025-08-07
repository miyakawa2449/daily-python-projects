import os
from PyPDF2 import PdfReader

def count_pages_pypdf2(filepath):
    try:
        reader = PdfReader(filepath)
        num_pages = len(reader.pages)
        print(f"📄 {os.path.basename(filepath)}: {num_pages}ページ")
        return num_pages
    except Exception as e:
        print(f"❌ エラー発生（{filepath}）: {e}")
        return None

if __name__ == "__main__":
    path = input("📁 PDFファイルのパスを入力してください: ").strip()
    count_pages_pypdf2(path)
