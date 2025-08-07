import os
import secrets
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from PIL import Image
import markdown2
import bleach
from app import db
from models import Todo
from forms import TodoForm

todo_bp = Blueprint('todo', __name__)

ALLOWED_TAGS = [
    'p', 'br', 'strong', 'em', 'u', 'i', 'b', 'code', 'pre',
    'blockquote', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'a', 'img', 'hr', 'table', 'thead', 'tbody', 'tr', 'th', 'td',
    'input', 'del', 's'
]
ALLOWED_ATTRIBUTES = {
    'a': ['href', 'title'],
    'img': ['src', 'alt', 'title'],
    'input': ['type', 'checked', 'disabled']
}

def save_image(form_image):
    if not form_image:
        return None
    
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = random_hex + f_ext
    image_path = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'], image_fn)
    
    img = Image.open(form_image)
    if img.height > 800 or img.width > 800:
        output_size = (800, 800)
        img.thumbnail(output_size)
    img.save(image_path)
    
    return image_fn

def markdown_to_html(text):
    if not text:
        return ''
    
    # インデントされた見出しを修正（Markdownの見出しは行頭になければならない）
    import re
    # 行頭のスペースを削除（見出しとリストアイテムのみ）
    lines = text.split('\n')
    cleaned_lines = []
    for line in lines:
        # 見出し（#で始まる）の場合、先頭のスペースを削除
        if re.match(r'^\s*#+\s', line):
            line = line.lstrip()
        cleaned_lines.append(line)
    
    cleaned_text = '\n'.join(cleaned_lines)
    
    html = markdown2.markdown(cleaned_text, extras=[
        'fenced-code-blocks', 
        'tables', 
        'break-on-newline',
        'header-ids',
        'strike',
        'task_list',
        'code-friendly'
    ])
    clean_html = bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES, strip=True)
    return clean_html

@todo_bp.route('/')
@login_required
def index():
    todos = Todo.query.filter_by(user_id=current_user.id).order_by(Todo.created_at.desc()).all()
    return render_template('todo/index.html', todos=todos)

@todo_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = TodoForm()
    if form.validate_on_submit():
        todo = Todo(
            user_id=current_user.id,
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            due_date=form.due_date.data
        )
        
        if form.description.data:
            todo.description_html = markdown_to_html(form.description.data)
        
        if form.image.data:
            image_file = save_image(form.image.data)
            todo.image_path = image_file
        
        db.session.add(todo)
        db.session.commit()
        flash('ToDoを作成しました。', 'success')
        return redirect(url_for('todo.index'))
    
    return render_template('todo/form.html', form=form, title='新規作成')

@todo_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    todo = Todo.query.get_or_404(id)
    if todo.user_id != current_user.id:
        flash('このToDoを編集する権限がありません。', 'danger')
        return redirect(url_for('todo.index'))
    
    form = TodoForm()
    if form.validate_on_submit():
        todo.title = form.title.data
        todo.description = form.description.data
        todo.priority = form.priority.data
        todo.due_date = form.due_date.data
        
        if form.description.data:
            todo.description_html = markdown_to_html(form.description.data)
        
        if form.image.data:
            if todo.image_path:
                old_image = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'], todo.image_path)
                if os.path.exists(old_image):
                    os.remove(old_image)
            image_file = save_image(form.image.data)
            todo.image_path = image_file
        
        db.session.commit()
        flash('ToDoを更新しました。', 'success')
        return redirect(url_for('todo.index'))
    
    elif request.method == 'GET':
        form.title.data = todo.title
        form.description.data = todo.description
        form.priority.data = todo.priority
        form.due_date.data = todo.due_date
    
    return render_template('todo/form.html', form=form, title='編集', todo=todo)

@todo_bp.route('/toggle/<int:id>')
@login_required
def toggle(id):
    todo = Todo.query.get_or_404(id)
    if todo.user_id != current_user.id:
        flash('このToDoを変更する権限がありません。', 'danger')
        return redirect(url_for('todo.index'))
    
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('todo.index'))

@todo_bp.route('/delete/<int:id>')
@login_required
def delete(id):
    todo = Todo.query.get_or_404(id)
    if todo.user_id != current_user.id:
        flash('このToDoを削除する権限がありません。', 'danger')
        return redirect(url_for('todo.index'))
    
    if todo.image_path:
        image_path = os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'], todo.image_path)
        if os.path.exists(image_path):
            os.remove(image_path)
    
    db.session.delete(todo)
    db.session.commit()
    flash('ToDoを削除しました。', 'success')
    return redirect(url_for('todo.index'))

@todo_bp.route('/view/<int:id>')
@login_required
def view(id):
    todo = Todo.query.get_or_404(id)
    if todo.user_id != current_user.id:
        flash('このToDoを表示する権限がありません。', 'danger')
        return redirect(url_for('todo.index'))
    
    return render_template('todo/view.html', todo=todo)