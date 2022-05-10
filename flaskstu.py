from flask import Flask, jsonify
app=Flask(__name__)
students={
    "21pw41":["Akshith","SS"],
    "21pw18":["Pranav","SS"],
    "21pw36":["Bala","SS"]
   }
@app.route("/")
def getstudents():
     return students
@app.route("/21pw41")
def get():
    return jsonify(students["21pw41"])
@app.route("/21pw18")
def get1():
    return jsonify(students["21pw18"])
@app.route("/21pw36")
def get2():
    return jsonify(students["21pw36"])
app.run()
