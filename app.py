from flask import Flask, render_template, redirect
import json

app = Flask(__name__)

# Load data from JSON
def find_employee_by_position(position):
    try:
        with open("data/employees.json", "r") as file:
            employees_data = json.load(file)
        return employees_data["employees"][0][position]
    except Exception as e:
        return f"{position} Employee not found: Reason {e}", 404

def granat_data():
    with open("data/employees.json", "r") as file:
        employees_data = json.load(file)
    return employees_data["granat"]

@app.route("/")
def home():
    granat_d = granat_data()
    return render_template("content.html", data=granat_d)

@app.route("/<string:pos>")
def employee_id(pos):
    if not pos in ["ceo", "pm", "smm", "it"]:
        return redirect("/")
    employee = find_employee_by_position(pos)
    if employee:
        employee["name"] = f"{employee['first_name']} {employee['last_name']}"
        return render_template("index.html", employee=employee)
    else:
        return "Employee not found", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
