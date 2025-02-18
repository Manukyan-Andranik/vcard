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

@app.route("/")
def home():
    return "Hello fromn Granat Digital Agency"

@app.route("/employees/<string:pos>")
def employee_id(pos):
    employee = find_employee_by_position(pos)
    if employee:
        return render_template("index.html", employee=employee)
    else:
        return "Employee not found", 404

if __name__ == "__main__":
    app.run(debug=True)
