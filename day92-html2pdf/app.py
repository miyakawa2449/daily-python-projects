from flask import Flask, render_template, request, send_file
from weasyprint import HTML, CSS
import os
import io
from datetime import date

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        title = request.form.get("title")
        body = request.form.get("body")
        today = request.form.get("date") or date.today().isoformat()

        # HTMLテンプレートを使ってPDF用HTMLをレンダリング
        rendered = render_template("pdf_template.html", name=name, title=title, body=body, date=today)

        # 静的CSSファイルへの絶対パス
        css_path = os.path.join(app.root_path, 'static', 'style.css')

        # PDF出力をバッファに保存
        pdf_io = io.BytesIO()
        HTML(string=rendered, base_url=request.base_url).write_pdf(pdf_io, stylesheets=[CSS(filename=css_path)])
        pdf_io.seek(0)

        return send_file(pdf_io, as_attachment=True, download_name="report.pdf", mimetype='application/pdf')

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
