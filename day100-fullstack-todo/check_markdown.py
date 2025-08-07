from app import create_app, db
from models import Todo
from routes.todo import markdown_to_html

app = create_app()

with app.app_context():
    todo = Todo.query.get(2)
    if todo:
        print("=== Original Description ===")
        print(todo.description)
        print("\n=== Generated HTML ===")
        html = markdown_to_html(todo.description)
        print(html)
        print("\n=== Current HTML in DB ===")
        print(todo.description_html)