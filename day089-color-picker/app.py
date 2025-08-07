from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update-color', methods=['POST'])
def update_color():
    color = request.json.get('color')
    return jsonify({'message': f'選択された色は {color} です。', 'color': color})

if __name__ == '__main__':
    app.run(debug=True)
