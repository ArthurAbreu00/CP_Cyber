from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Vulnerabilidade proposital: reflected XSS
        username = request.form.get('username', '')
        # Passamos o username para o template. No template usamos |safe para simular vulnerabilidade.
        return render_template('login_result.html', username=username)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
