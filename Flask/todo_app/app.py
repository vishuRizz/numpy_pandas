from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)

items = [
    {"id": 1, "name": "name 1", "description": "des 1"},
    {"id": 2, "name": "name 2", "description": "des 2"},
    {"id": 3, "name": "name 3", "description": "des 3"},
]
CORS(app, resources={r"/*": {"origins": "*"}})
@app.route("/")
def home():
    return f'welcome to the main todo list page' 

@app.route("/todo", methods=["GET"])
def todo():
    return items

@app.route("/todo/<id>",methods=["GET"])
def todo_id(id):
    for item in items:
        if item["id"] == int(id):
            return item

@app.route("/todo", methods=["POST"])
def new_todo():
    new_item = {
        "id" : items[-1]["id"] + 1 if items else 1 ,
        "name" : request.json["name"],
        "description" : request.json["description"] 
    }
    items.append(new_item)
    return items

if __name__=="__main__":
    app.run(debug=True)