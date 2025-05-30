from flask import Flask, render_template, request, jsonify, send_from_directory
import random
import string

app = Flask(__name__)

# Fonction pour générer un mot de passe
def generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude_ambiguous):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    ambiguous = "il1Lo0O"

    char_pool = ""
    if use_upper:
        char_pool += upper
    if use_lower:
        char_pool += lower
    if use_digits:
        char_pool += digits
    if use_symbols:
        char_pool += symbols

    if exclude_ambiguous:
        char_pool = ''.join([c for c in char_pool if c not in ambiguous])

    if not char_pool:
        return ""

    return ''.join(random.choice(char_pool) for _ in range(length))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    password = generate_password(
        length=data.get('length', 12),
        use_upper=data.get('use_upper', True),
        use_lower=data.get('use_lower', True),
        use_digits=data.get('use_digits', True),
        use_symbols=data.get('use_symbols', True),
        exclude_ambiguous=data.get('exclude_ambiguous', False)
    )
    return jsonify({"password": password})

@app.route('/ads.txt')
def serve_ads():
    return send_from_directory('.', 'ads.txt')

if __name__ == '__main__':
    app.run(debug=True)
