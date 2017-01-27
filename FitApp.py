#!/usr/local/bin/python3
import sqlite3, os

def create_db(db_name):
	cur_dir=os.getcwd()
	create_query='CREATE TABLE products(name VARCHAR PRIMARY KEY, protein REAL, fat REAL, carbohydrate REAL, kcal REAL)'
	try:
		con=sqlite3.connect(db_name)
		cur=con.cursor()
		cur.execute(create_query)
		con.commit()
	except Exception:
		print("Was not able to create DB file in "+cur_dir+"\\"+db_name)

def insert_data(db_name,values):
	insert_query='INSERT INTO products VALUES (?,?,?,?,?)'
	try:
		con=sqlite3.connect(db_name)
		cur=con.cursor()
		cur.execute(insert_query, (values['name'], values['protein'], values['fat'], values['carbohydrate'], values['kcal'],))
		con.commit()
	except sqlite3.Error as er:
		print ("er: "+str(er))
	
db_name='Products.db'

if not os.path.isfile(db_name): create_db(db_name)
insert_data(db_name,{'name':'Творог', 'protein':17, 'fat':5, 'carbohydrate':0,'kcal':80})



