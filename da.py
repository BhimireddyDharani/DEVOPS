from flask import Flask, render_template, request

app = Flask(__name__)
users = {}  # In-memory user store

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    action = request.form['action']
    username = request.form['username']
    password = request.form['password']

    if action == 'register':
        if username in users:
            return "Username already exists! Please try logging in."
        users[username] = password
        return f"Registration successful for {username}! Now go back and login."

    elif action == 'login':
        if username in users and users[username] == password:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            return "Invalid username or password."

if __name__ == '__main__':
    app.run(debug=True)
