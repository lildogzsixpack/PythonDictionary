from flask import Flask, render_template, request
import json
import config

app = Flask(__name__)
app.secret_key = config.flask_key

data = json.load(open("data.json"))


@app.route('/motivation', methods=['GET'])
def motivation():
    return '<center><iframe width="560" height="315" src="https://www.youtube.com/embed/3ugZUq9nm4Y" frameborder="0" allowfullscreen></iframe></center>'


@app.route("/")
@app.route("/home")
@app.route("/index")
def hello():
    return render_template("home.html", data=list(data.keys()))


@app.route('/get_word', methods=['POST', 'GET'])
def get_word():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        word = request.form['search'].lower()
        if word in data:
            result = data[word]
        else:
            result = "Cannot find word. Please try again"
            return render_template("home.html", result=str(result))
        return render_template("home.html", result=result, data=json.dumps(data))


if __name__ == "__main__":
    app.run(host=config.host, port=config.port, debug=config.debug)
