from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load data from JSON
def find_employee_by_position(position):
    try:
        with open("data/employees.json", "r") as file:
            employees_data = json.load(file)
        return employees_data["employees"][0][position]
    except Exception as e:
        print(e)
        return None

def granat_data():
    with open("data/employees.json", "r") as file:
        employees_data = json.load(file)
    return employees_data["granat"]

@app.route("/")
def home():
    return "Hello fromn Granat Digital Agency"

@app.route("/granat")
def granat():
    granat_d = granat_data()
    print(granat_d)
    return render_template("content.html", data=granat_d)

@app.route("/employees/<string:pos>")
def employee_id(pos):
    employee = find_employee_by_position(pos)
    if employee:
        employee["name"] = f"{employee['first_name']} {employee['last_name']}"
        return render_template("index.html", employee=employee)
    else:
        return "Employee not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
