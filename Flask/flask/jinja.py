from flask import Flask, render_template, request
app = Flask("__main__")

@app.route("/")
def home():
    return f'this is the home page of jinja flask app'

@app.route("/user/<id>")
def user(id):
    return render_template('user.html', id=id)


if __name__ == "__main__":
    app.run(debug=True)