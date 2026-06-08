from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Smart Bus Sync"

if __name__ == '__main__':
    app.run(debug=True)
