from app import create_app, db
from models import User, Todo

app = create_app()

with app.app_context():
    db.create_all()
    print("データベーステーブルを作成しました。")

if __name__ == '__main__':
    app.run(debug=True, port=5000)