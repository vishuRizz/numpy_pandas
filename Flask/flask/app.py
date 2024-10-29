from flask import Flask, render_template, request

app = Flask(__name__) # giving flask the entry point to this flask application

@app.route("/")
def welcome():
    return "welcome to my first flask appssssssss"

@app.route("/hehe")
def hehe():
    return render_template('index.html')

@app.route("/post", methods=["POST", "GET"])
def postData():
    if request.method == 'POST':
        name = request.form['name']
        return f'hello bro {name}'
    return render_template('form.html')  
    
if __name__ == "__main__":
    app.run(debug=True)
    
