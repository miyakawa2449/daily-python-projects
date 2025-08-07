# app.py
from flask import Flask, render_template, request, jsonify, send_file, redirect, url_for
import os
from werkzeug.utils import secure_filename
import uuid
from PIL import Image
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB max file size

# アップロードディレクトリの設定
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ディレクトリが存在しない場合は作成
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'ファイルが選択されていません'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'ファイルが選択されていません'}), 400
    
    if file and allowed_file(file.filename):
        # ユニークなファイル名を生成
        original_filename = secure_filename(file.filename)
        file_extension = original_filename.rsplit('.', 1)[1].lower()
        unique_filename = f"{str(uuid.uuid4())}.{file_extension}"
        
        # ファイルを保存
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)
        
        return jsonify({
            'success': True,
            'filename': unique_filename,
            'original_name': original_filename,
            'url': f'/static/uploads/{unique_filename}'
        })
    
    return jsonify({'error': '対応していないファイル形式です'}), 400

@app.route('/edit', methods=['POST'])
def edit_image():
    try:
        data = request.get_json()
        filename = data.get('filename')
        operation = data.get('operation')
        
        if not filename or not operation:
            return jsonify({'error': 'パラメータが不足しています'}), 400
        
        # 元画像のパス
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if not os.path.exists(original_path):
            return jsonify({'error': 'ファイルが見つかりません'}), 404
        
        # 画像を開く
        with Image.open(original_path) as img:
            # 操作に応じて処理
            if operation == 'rotate_right':
                edited_img = img.rotate(-90, expand=True)
            elif operation == 'rotate_left':
                edited_img = img.rotate(90, expand=True)
            elif operation == 'reset':
                edited_img = img.copy()
            else:
                return jsonify({'error': '不正な操作です'}), 400
            
            # 編集済み画像を保存
            edited_filename = f"edited_{filename}"
            edited_path = os.path.join(app.config['UPLOAD_FOLDER'], edited_filename)
            
            # 元の形式を保持して保存
            if img.format:
                edited_img.save(edited_path, format=img.format, quality=95)
            else:
                # 形式が不明な場合はJPEGで保存
                edited_img.save(edited_path, format='JPEG', quality=95)
            
            return jsonify({
                'success': True,
                'edited_filename': edited_filename,
                'edited_url': f'/static/uploads/{edited_filename}',
                'width': edited_img.width,
                'height': edited_img.height
            })
            
    except Exception as e:
        print(f"編集エラー: {e}")
        return jsonify({'error': '画像の編集に失敗しました'}), 500

@app.route('/reset', methods=['POST'])
def reset_image():
    try:
        data = request.get_json()
        original_filename = data.get('original_filename')
        
        if not original_filename:
            return jsonify({'error': 'ファイル名が指定されていません'}), 400
        
        original_path = os.path.join(app.config['UPLOAD_FOLDER'], original_filename)
        if not os.path.exists(original_path):
            return jsonify({'error': '元ファイルが見つかりません'}), 404
        
        return jsonify({
            'success': True,
            'reset_url': f'/static/uploads/{original_filename}',
            'filename': original_filename
        })
        
    except Exception as e:
        print(f"リセットエラー: {e}")
        return jsonify({'error': 'リセットに失敗しました'}), 500

if __name__ == '__main__':
    app.run(debug=True)