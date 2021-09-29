from flask_restful import Resource,abort,reqparse,marshal_with,fields
from main.emp_model import Employee_Model
from main import db

emp_resource_field={
    "emp_id":fields.Integer,
    "emp_name": fields.String,
    "emp_age": fields.Integer,
    "emp_email": fields.String,
    "emp_salary": fields.Integer
}

emp_args=reqparse.RequestParser()
emp_args.add_argument("name",type=str,help="name is required",required=True)
emp_args.add_argument("email",type=str,help="email is required",required=True)
emp_args.add_argument("age",type=int,help="age is required",required=True)
emp_args.add_argument("salary",type=int,help="salary is required",required=True)

emp_put_args=reqparse.RequestParser()
emp_put_args.add_argument("name",type=str,required=False)
emp_put_args.add_argument("email",type=str,required=False)
emp_put_args.add_argument("age",type=int,required=False)
emp_put_args.add_argument("salary",type=int,required=False)




class Employee(Resource):
    @marshal_with(emp_resource_field)
    def get(self, emp_id):
        employee=Employee_Model.query.filter_by(emp_id=emp_id).first()
        if employee:
            return employee
        else:
            abort (404,message="Not found")

    @marshal_with(emp_resource_field)
    def post(self,emp_id):
        args=emp_args.parse_args()
        employee= Employee_Model.query.filter_by(emp_id=emp_id).first()
        if employee:
            abort(409,message="employee is already there in table")
        employee=Employee_Model()
        employee.emp_id=emp_id
        employee.emp_name=args["name"]
        employee.emp_email=args["email"]
        employee.emp_age=args["age"]
        employee.emp_salary=args["salary"]
        db.session.add(employee)
        db.session.commit()
        return employee

    @marshal_with(emp_resource_field)
    def put(self,emp_id):
        args = emp_put_args.parse_args()
        employee = Employee_Model.query.filter_by(emp_id=emp_id).first()
        if employee:
            employee.emp_name=args["name"]
            employee.emp_email=args["email"]
            employee.emp_age=args["age"]
            employee.emp_salary=args["salary"]
            db.session.add(employee)
            db.session.commit()
            return employee
        else:
            abort(404, message="Not available")

    @marshal_with(emp_resource_field)
    def delete(self, emp_id):
        employee = Employee_Model.query.filter_by(emp_id=emp_id).first()
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return employee
        else:
            abort(404, message="employee not available")
