from main import db

class Employee_Model(db.Model):
    emp_id=db.Column(db.Integer, primary_key=True)
    emp_name=db.Column(db.String,nullable=False)
    emp_email=db.Column(db.String(25),unique=True,nullable=False)
    emp_age=db.Column(db.Integer,nullable=False)
    emp_salary=db.Column(db.Integer,nullable=False)
