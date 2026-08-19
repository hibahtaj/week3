from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('reg.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    roll = request.form.get('roll')
    year = request.form.get('year')

    return render_template('success.html', name=name, year=year)

if __name__ == '__main__':
    app.run(debug=True)