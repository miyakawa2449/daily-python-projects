# simple_server.py

import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "public"  # サーバーで公開したいディレクトリ

# カレントディレクトリを指定のディレクトリに変更
os.chdir(DIRECTORY)

# ハンドラの作成（SimpleHTTPRequestHandlerは自動的にファイルを提供してくれる）
Handler = http.server.SimpleHTTPRequestHandler

# サーバーの起動
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"✅ サーバー起動中: http://localhost:{PORT}/")
    print(f"📂 公開ディレクトリ: {os.path.abspath(DIRECTORY)}")
    httpd.serve_forever()
