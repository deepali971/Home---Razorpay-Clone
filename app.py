from flask import Flask, request, jsonify, render_template, session, redirect, url_for, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'A1b2C3d4E5f6G7h8I9j0!@#$%^&*()'  # Example of a random secret key

@app.route('/', methods=['GET'])
def home():
    return render_template('features.html')  # Redirect to features page instead of index

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contact_submissions (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        conn.commit()
        conn.close()
        return jsonify({"message": "Contact form submitted successfully!"}), 200
    return render_template('contact.html')

@app.route('/features', methods=['GET'])
def features():
    return render_template('features.html')

@app.route('/pricing', methods=['GET'])
def pricing():
    return render_template('pricing.html')

@app.route('/checkout', methods=['GET'])
def checkout():
    if not session.get('logged_in'):
        print("User not logged in, redirecting to login.")  # Debugging output
        return redirect(url_for('login'))  # Redirect to login if not logged in
    print("User is logged in, rendering checkout.")  # Debugging output
    return render_template('checkout.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user and check_password_hash(user[0], password):  # Check hashed password
            session['logged_in'] = True
            print("User logged in, session set.")  # Debugging output
            return redirect(url_for('checkout'))  # Redirect to checkout after login
        return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('app.db')
        cursor = conn.cursor()
        hashed_password = generate_password_hash(password)
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()
        print(f"User signed up: {username}")  # Debugging output
        return redirect(url_for('login'))  # Redirect to login after signup
    return render_template('signup.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # Remove the user from the session
    return redirect(url_for('home'))

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
