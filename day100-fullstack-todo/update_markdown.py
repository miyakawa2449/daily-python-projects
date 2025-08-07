from app import create_app, db
from models import Todo
from routes.todo import markdown_to_html

app = create_app()

with app.app_context():
    todos = Todo.query.all()
    for todo in todos:
        if todo.description:
            todo.description_html = markdown_to_html(todo.description)
            print(f"Updated Todo #{todo.id}: {todo.title}")
    
    db.session.commit()
    print("すべてのToDoのMarkdownを更新しました。")