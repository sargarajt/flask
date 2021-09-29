from main import app,api
from main.emp_resource import Employee
from main import db

db.create_all()
api.add_resource(Employee, "/employee/<int:emp_id>")

if __name__ == "__main__":
    app.run(debug=True)