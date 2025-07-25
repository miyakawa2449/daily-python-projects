from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# メモリ上のToDoリスト（起動中のみ有効）
todos = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            todos.append(task)
        return redirect(url_for('index'))
    return render_template('index.html', todos=todos)

@app.route('/delete/<int:index>')
def delete_task(index):
    """指定されたインデックスのタスクを削除"""
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
