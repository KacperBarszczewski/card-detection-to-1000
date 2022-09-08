from flask import Flask, jsonify, render_template

import CardDetector



app = Flask(__name__, static_url_path='/static')

CardDetector.run()

@app.route('/')
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)

