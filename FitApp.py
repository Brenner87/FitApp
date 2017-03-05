#!/usr/local/bin/python3
import sqlite3, os, re

class DataHandler:
	def __init__(self):
		self.db_name='Products.db'
		try:
			self.db_con = sqlite3.connect(self.db_name)
			self.cursor = self.db_con.cursor()
		except Exception as er:
			print("Was not able to connet to DB: " + er)
		self.create_table()

	def create_table(self):
		create_query='CREATE TABLE IF NOT EXISTS products(name VARCHAR PRIMARY KEY, protein REAL, fat REAL, carbohydrate REAL, kcal REAL)'
		try:
			self.cursor.execute(create_query)
		except sqlite3.Error as er:
			print("Was not able to create table: "+er)
		else:
			self.db_con.commit()
			print ("DB is OK.")

	def insert_data(self ,values):
		insert_query='INSERT INTO products VALUES (?,?,?,?,?)'
		try:
			self.cursor.execute(insert_query, (values['name'], values['protein'], values['fat'], values['carbohydrate'], values['kcal'],))
		except sqlite3.IntegrityError as er:
			if re.search(r'UNIQUE constraint failed', str(er)): print("[ВНИМАНИЕ] Продукт "+values['name']+" уже существует")
			else: print(er)
		except Exception as er:	print(er)
		else:
			self.db_con.commit()
			print ("Продукт {0} успешно добавлен в базу".format(values['name']))

	def get_data(self, prod):
		query="SELECT * FROM products WHERE name='"+prod+"'"
		self.cursor.execute(query)
		self.data=self.cursor.fetchall()


	def output_product(self):
		print(self.data)
		if not self.data: print("Нет такого продукта: "+prod)
		else:
			print ('Имя: {0}, белки: {1}, жиры: {2}, углеводы: {3}, каллорийность: {4}'.format(*self.data))

	def input_data(self):
		pass


	def calculate(self, mass):
		print (self.data)
		self.output=[i*mass*0.01  for i in self.data[0] if isinstance(i,float)]
		self.output.insert(0,self.data[0][0])
		print (self.output)


#================================================================================================================================
#================================================================================================================================


#db_name='Products.db'
prod="Творог"
mass=300
#try:
#	db_con=sqlite3.connect(db_name)
#	cursor=db_con.cursor()
#except Exception as er:
#	print("Was not able to connet to DB: "+er)

my_handler=DataHandler()

#my_handler.insert_data({'name':'Творог', 'protein':17, 'fat':5, 'carbohydrate':0,'kcal':80})
my_handler.get_data(prod)
total=my_handler.calculate(mass)
my_handler.output_product()



