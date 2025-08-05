from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv
import markdown

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    markdown_content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

@app.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:id>')
def post_detail(id):
    post = Post.query.get_or_404(id)
    html_content = markdown.markdown(post.markdown_content, extensions=['codehilite', 'fenced_code'])
    return render_template('post_detail.html', post=post, html_content=html_content)

@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        markdown_content = request.form['content']
        
        html_content = markdown.markdown(markdown_content, extensions=['codehilite', 'fenced_code'])
        
        post = Post(
            title=title,
            content=html_content,
            markdown_content=markdown_content
        )
        
        db.session.add(post)
        db.session.commit()
        
        flash('記事が作成されました！', 'success')
        return redirect(url_for('index'))
    
    return render_template('create_post.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    
    if request.method == 'POST':
        post.title = request.form['title']
        post.markdown_content = request.form['content']
        post.content = markdown.markdown(post.markdown_content, extensions=['codehilite', 'fenced_code'])
        post.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        flash('記事が更新されました！', 'success')
        return redirect(url_for('post_detail', id=post.id))
    
    return render_template('edit_post.html', post=post)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    
    flash('記事が削除されました。', 'info')
    return redirect(url_for('index'))

@app.route('/load_markdown', methods=['GET', 'POST'])
def load_markdown():
    if request.method == 'POST':
        file_path = request.form['file_path']
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            title = os.path.splitext(os.path.basename(file_path))[0]
            html_content = markdown.markdown(markdown_content, extensions=['codehilite', 'fenced_code'])
            
            post = Post(
                title=title,
                content=html_content,
                markdown_content=markdown_content
            )
            
            db.session.add(post)
            db.session.commit()
            
            flash(f'{file_path}から記事を読み込みました！', 'success')
            return redirect(url_for('index'))
            
        except FileNotFoundError:
            flash('ファイルが見つかりません。', 'error')
        except Exception as e:
            flash(f'エラーが発生しました: {str(e)}', 'error')
    
    return render_template('load_markdown.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)