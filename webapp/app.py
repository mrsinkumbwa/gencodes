from flask import Flask, render_template
import random
import string

app = Flask(__name__)

def generate_password(length=250):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    generated_passwords = [generate_password(random.randint(250, 300)) for _ in range(5, 11)]
    return render_template('/index.html', passwords=generated_passwords)

if __name__ == '__main__':
    app.run(debug=True)

