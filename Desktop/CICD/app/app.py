from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "CI/CD"

if __name__ == '__main__':
    app.run(debug=True)  # Must be indented inside the if-block