import fitz  # PyMuPDF

doc = fitz.open("PyMuPDF.pdf")

for page_index in range(len(doc)):
    page = doc[page_index]
    images = page.get_images(full=True)
    
    for i, img in enumerate(images):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        output = f"page{page_index+1}_img{i+1}.png"
        if pix.n < 5:  # グレースケール or RGB
            pix.save(output)
        else:  # CMYK
            pix = fitz.Pixmap(fitz.csRGB, pix)
            pix.save(output)
        print(f"✅ 画像を抽出: {output}")
