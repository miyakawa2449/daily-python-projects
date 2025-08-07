import fitz

doc = fitz.open("PyMuPDF.pdf")
page = doc[0]
text = page.get_text()
print("📄 抽出テキスト:\n", text)
