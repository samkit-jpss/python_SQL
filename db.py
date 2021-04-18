from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask('database')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data.sqlite'
db=SQLAlchemy(app)

class DataBase(db.Model):
	emp_name=db.Column(db.Text)
	emp_id=db.Column(db.Integer,primary_key=True)
	emp_role=db.Column(db.Text)

	def __init__(self,name,id,role):
		self.emp_name=name
		self.emp_id=id
		self.emp_role=role

db.create_all()

#Create Operation
"""
obj=DataBase("Samkit",10,"Software Engineer")
db.session.add(obj)
db.session.commit()

obj2=DataBase("Michael",5,"Content Creator")
db.session.add(obj2)
db.session.commit()

obj3=DataBase("John",31,"Salseman")
db.session.add(obj3)
db.session.commit()

"""
#Read Operation

r1=DataBase.query.all()
print(r1[0].emp_name)

#Filter Operation

f=DataBase.query.filter_by(emp_role="HR")
print(f.all()[0].emp_name)

#Update Operation

up =DataBase.query.get(1)
up.emp_id=10
db.session.add(up)
db.session.commit()	

#Delete Operation

dele=DataBase.query.get(2)
db.session.delete(dele)
db.session.commit()