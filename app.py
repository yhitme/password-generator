from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_lower, use_upper, use_digits, use_specials):
    characters = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        return "Veuillez sélectionner au moins un type de caractère."

    return ''.join(random.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        try:
            length = int(request.form.get("length", 12))
            if length < 1 or length > 250:
                password = "La longueur doit être entre 1 et 250."
            else:
                use_lower = request.form.get("lowercase") == "on"
                use_upper = request.form.get("uppercase") == "on"
                use_digits = request.form.get("digits") == "on"
                use_specials = request.form.get("special") == "on"

                password = generate_password(length, use_lower, use_upper, use_digits, use_specials)
        except ValueError:
            password = "Entrée invalide pour la longueur."

    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
