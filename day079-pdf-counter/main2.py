import os
import fitz  # PyMuPDF

def count_pages_fitz(filepath):
    try:
        doc = fitz.open(filepath)
        num_pages = doc.page_count
        print(f"📄 {os.path.basename(filepath)}: {num_pages}ページ")
        return num_pages
    except Exception as e:
        print(f"❌ エラー発生（{filepath}）: {e}")
        return None

if __name__ == "__main__":
    path = input("📁 PDFファイルのパスを入力してください: ").strip()
    count_pages_fitz(path)
