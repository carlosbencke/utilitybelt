from flask import Flask
import text_manipulation

app = Flask(__name__)

@app.route("/")
def hello():
   # form to input 
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
