from flask import Flask
app = Flask(__name__)
@app.route('/') 
def firstApp():
    return "Hello World"
    return "This id devops lab"
    return "HIII11"
    return "Feature 1 branch update"

app.run(debug=True)
