import os
import uuid
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production'

# 設定
UPLOAD_FOLDER = 'uploads'
THUMBNAIL_FOLDER = 'thumbnails'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['THUMBNAIL_FOLDER'] = THUMBNAIL_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

def allowed_file(filename):
    """
    アップロード可能なファイル形式かチェックする関数
    
    Args:
        filename (str): チェック対象のファイル名
    
    Returns:
        bool: 許可されたファイル形式の場合True、それ以外はFalse
    
    Note:
        - ファイル名に拡張子が含まれているかをチェック
        - 拡張子を小文字に変換してALLOWED_EXTENSIONSと照合
        - 対応形式: png, jpg, jpeg, gif
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_thumbnail(image_path, thumbnail_path, size=(300, 300)):
    """
    アップロード画像からサムネイル画像を作成する関数
    
    Args:
        image_path (str): 元画像ファイルのパス
        thumbnail_path (str): サムネイル保存先パス
        size (tuple): サムネイルサイズ (幅, 高さ)、デフォルト(300, 300)
    
    Note:
        - Pillowライブラリを使用してリサイズ処理
        - LANCZOSリサンプリングで高品質な縮小
        - optimize=True, quality=85でファイルサイズ最適化
        - アスペクト比を維持してリサイズ
    
    Raises:
        Exception: 画像ファイルの読み込みや保存に失敗した場合
    """
    with Image.open(image_path) as image:
        image.thumbnail(size, Image.Resampling.LANCZOS)
        image.save(thumbnail_path, optimize=True, quality=85)

def get_image_info(filepath):
    """
    画像ファイルのメタデータ情報を取得する関数
    
    Args:
        filepath (str): 画像ファイルのフルパス
    
    Returns:
        dict: 画像情報を含む辞書
            - size (float): ファイルサイズ（KB単位、小数点以下2桁）
            - uploaded (str): ファイル更新日時（YYYY-MM-DD HH:MM:SS形式）
    
    Note:
        - os.stat()でファイルシステム情報を取得
        - st_sizeをKB単位に変換（1024で割る）
        - st_mtimeを日時文字列に変換
        - ギャラリー表示用のメタデータとして使用
    """
    stat = os.stat(filepath)
    return {
        'size': round(stat.st_size / 1024, 2),  # KB
        'uploaded': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
    }

@app.route('/')
def index():
    """
    メインページ（ギャラリー表示）のルートハンドラ
    
    機能:
        - アップロード済み画像の一覧を取得・表示
        - 画像メタデータ（ファイル名、サイズ、アップロード日時）を収集
        - 最新アップロード順でソート
    
    Returns:
        str: レンダリングされたHTMLテンプレート
    
    Note:
        - uploadsフォルダ内の画像ファイルをスキャン
        - allowed_file()で対応ファイルのみフィルタリング
        - get_image_info()でメタデータ取得
        - テンプレートにimagesリストを渡して表示
    """
    # アップロード済み画像一覧取得
    images = []
    if os.path.exists(UPLOAD_FOLDER):
        for filename in os.listdir(UPLOAD_FOLDER):
            if allowed_file(filename):
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                info = get_image_info(filepath)
                images.append({
                    'filename': filename,
                    'size': info['size'],
                    'uploaded': info['uploaded']
                })
    
    # 最新順にソート
    images.sort(key=lambda x: x['uploaded'], reverse=True)
    return render_template('index.html', images=images)

@app.route('/upload', methods=['POST'])
def upload_files():
    """
    画像ファイルアップロード処理のルートハンドラ
    
    機能:
        - 複数ファイルの同時アップロード対応
        - ファイル形式バリデーション
        - 安全なファイル名生成（重複回避）
        - サムネイル自動生成
        - エラーハンドリングとユーザーフィードバック
    
    Returns:
        Response: インデックスページへのリダイレクト
    
    Note:
        - request.files.getlist()で複数ファイル取得
        - secure_filename()でセキュアなファイル名に変換
        - UUID追加で重複ファイル名を回避
        - サムネイル作成失敗時は元ファイルは保持
        - flash()でアップロード結果をユーザーに通知
    """
    if 'files' not in request.files:
        flash('ファイルが選択されていません')
        return redirect(request.url)
    
    files = request.files.getlist('files')
    uploaded_count = 0
    
    for file in files:
        if file and file.filename != '' and allowed_file(file.filename):
            # 安全なファイル名生成
            original_filename = secure_filename(file.filename)
            name, ext = os.path.splitext(original_filename)
            unique_filename = f"{name}_{uuid.uuid4().hex[:8]}{ext}"
            
            # ファイル保存
            filepath = os.path.join(UPLOAD_FOLDER, unique_filename)
            file.save(filepath)
            
            # サムネイル作成
            thumbnail_path = os.path.join(THUMBNAIL_FOLDER, unique_filename)
            try:
                create_thumbnail(filepath, thumbnail_path)
                uploaded_count += 1
            except Exception as e:
                flash(f'サムネイル作成エラー: {unique_filename}')
                continue
    
    if uploaded_count > 0:
        flash(f'{uploaded_count}個のファイルをアップロードしました')
    else:
        flash('アップロードできるファイルがありませんでした')
    
    return redirect(url_for('index'))

@app.route('/image/<filename>')
def uploaded_file(filename):
    """
    アップロード済みオリジナル画像の配信ルートハンドラ
    
    Args:
        filename (str): 取得する画像ファイル名
    
    Returns:
        Response: 画像ファイルのレスポンス
    
    Note:
        - send_from_directory()で安全なファイル配信
        - モーダル表示での拡大画像表示に使用
        - 直接ファイルパスアクセスを防ぐセキュリティ機能
        - Content-Typeは自動設定される
    """
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/thumbnail/<filename>')
def thumbnail_file(filename):
    """
    サムネイル画像の配信ルートハンドラ
    
    Args:
        filename (str): 取得するサムネイルファイル名
    
    Returns:
        Response: サムネイル画像ファイルのレスポンス
    
    Note:
        - ギャラリーグリッド表示用の小サイズ画像を配信
        - オリジナル画像と同じファイル名でサムネイルフォルダから取得
        - 300x300px（最大）サイズでアスペクト比維持
        - ページ読み込み速度向上のため軽量化済み
    """
    return send_from_directory(THUMBNAIL_FOLDER, filename)

@app.route('/delete/<filename>', methods=['POST'])
def delete_file(filename):
    """
    画像ファイル削除処理のルートハンドラ
    
    Args:
        filename (str): 削除対象のファイル名
    
    Returns:
        Response: インデックスページへのリダイレクト
    
    機能:
        - オリジナル画像とサムネイルを同時削除
        - ファイル存在チェック後に安全に削除
        - エラー発生時の適切なエラーハンドリング
        - ユーザーへの削除結果フィードバック
    
    Note:
        - POSTメソッドのみ許可（意図しない削除を防止）
        - 両方のファイルが存在しない場合でもエラーにしない
        - 例外発生時はflash()でエラーメッセージ表示
        - 削除後は自動的にギャラリーページに戻る
    """
    try:
        # オリジナル削除
        original_path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(original_path):
            os.remove(original_path)
        
        # サムネイル削除
        thumbnail_path = os.path.join(THUMBNAIL_FOLDER, filename)
        if os.path.exists(thumbnail_path):
            os.remove(thumbnail_path)
        
        flash(f'{filename} を削除しました')
    except Exception as e:
        flash(f'削除エラー: {str(e)}')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    """
    アプリケーションのエントリーポイント
    
    起動時処理:
        - 必要ディレクトリの自動作成
        - 開発サーバーの起動
    
    設定:
        - debug=True: 開発モード（自動リロード、詳細エラー表示）
        - host='0.0.0.0': 全てのネットワークインターフェースでリッスン
        - port=5001: ポート5001で起動（5000はmacOS AirPlayと競合回避）
    
    Note:
        - exist_ok=Trueで既存フォルダがあってもエラーにしない
        - 本番環境では debug=False, host/port適切に設定
    """
    # フォルダ作成
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(THUMBNAIL_FOLDER, exist_ok=True)
    
    app.run(debug=True, host='0.0.0.0', port=5001)