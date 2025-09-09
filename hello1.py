from flask import Flask
app = Flask(__name__)
@app.route('/') 
def firstApp():
    return "Hello World"
app.run(debug=True)