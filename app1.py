
from flask import Flask, render_template, request, redirect
import model1

app = Flask(__name__)

@app.route("/")
def index():
    ## print the guestbook
    return render_template("index.html", entries=model1.get_entries())

@app.route("/add")
def addentry():
    ## add a guestbook entry
    return render_template("addentry.html")

@app.route("/admin")
def admin():
    ## add a guestbook entry
    return render_template("admin.html",  entries=model1.get_entries())

@app.route("/postentry", methods=["POST"])
def postentry():
    name = request.form["name"]
    message = request.form["message"]
    model1.add_entry(name, message)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def deleteentry():
    id = request.form["id"]
    model1.delete_entry(id)
    return redirect("/")

if __name__=="__main__":
    model1.init()
    app.run(debug=True)
