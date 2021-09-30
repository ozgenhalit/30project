from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World From Flask."

@app.route('/second')
def second():
    return "This is the second line"

@app.route('/third/subthird')
def third():
    return "This is the third line of our website"

@app.route("/forth/<string:id>")
def forth(id):
    return f"Id of this page is {id}"

if __name__ == '__main__' :
    app.run(debug=True)