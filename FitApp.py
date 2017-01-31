#!/usr/local/bin/python3
import sqlite3, os, re 
	
def create_table(db_con,cursor):
	create_query='CREATE TABLE IF NOT EXISTS products(name VARCHAR PRIMARY KEY, protein REAL, fat REAL, carbohydrate REAL, kcal REAL)'
	try:
		cursor.execute(create_query)
	except sqlite3.Error as er:
		print("Was not able to create table: "+er)
	else:
		db_con.commit()
		print ("DB is OK.")
	return "Done"

def insert_data(db_con,cursor,values):
	insert_query='INSERT INTO products VALUES (?,?,?,?,?)'
	try:
		cursor.execute(insert_query, (values['name'], values['protein'], values['fat'], values['carbohydrate'], values['kcal'],))		
	except sqlite3.IntegrityError as er:
		if re.search(r'UNIQUE constraint failed', str(er)): print("[ВНИМАНИЕ] Продукт "+values['name']+" уже существует")
		else: print(er) 
	except Exception as er:	print(er)
	else: 
		db_con.commit()
		print ("Продукт {0} успешно добавлен в базу".format(values['name']))
	return "Done"

def get_data(db_con,cursor,prod):
	query="SELECT * FROM products WHERE name='"+prod+"'"
	cursor.execute(query)
	output=cursor.fetchall()
	return output

def output_product(data):
	if not data: print("Нет такого продукта: "+prod)
	else:
		print ('Имя: {0}, белки: {1}, жиры: {2}, углеводы: {3}, каллорийность: {4}'.format(*data)) 
	return "Done"

def input_data():
	pass


def calculate(data,mass):
	print (data)
	output=[i*mass*0.01  for i in data[0] if isinstance(i,float)]
	output.insert(0,data[0][0])
	print (output)
	return output


#================================================================================================================================
#================================================================================================================================


db_name='Products.db'
prod="Творог"
mass=300
try:
	db_con=sqlite3.connect(db_name)
	cursor=db_con.cursor()
except Exception as er:
	print("Was not able to connet to DB: "+er)

create_table(db_con,cursor)
insert_data(db_con,cursor,{'name':'Творог', 'protein':17, 'fat':5, 'carbohydrate':0,'kcal':80})
#data=get_data(db_con,cursor,prod)
total=calculate(data,mass)
output_product(total)



