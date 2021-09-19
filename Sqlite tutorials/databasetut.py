import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

#Create a cursor
c = conn.cursor()

#Drop Table
c.execute("DROP TABLE customers")

# Create a Table

# c.execute("""CREATE TABLE customers (
# 	first_name text,
# 	last_name text,
# 	email text
# )""")

# many_customer = [
# 					('Wes', 'Brown', 'wes@brown.com'), 
# 					('Steph', 'Kuewa', 'steph@kuewa.com'),
# 					('Dan', 'Pas', 'dan@pas.com'),
# 				]

# Insert
# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customer)

# Query the database
# c.execute("SELECT * FROM customers WHERE last_name = 'Muppalaneni'")


# Read
# c.fetchone()
# c.fetchmany()
# c.fetchall()



# Update Records
# c.execute("""UPDATE customers SET first_name = 'John'
# 			WHERE rowid = 1
# 	""")


# Delete Records
# c.execute("DELETE from customers WHERE rowid = 5")


# Query by database order
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")

# Commit our command
conn.commit()

# Query by AND OR
#c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' AND/OR rowid = 3 ")

# Using LIMIT in QUERY
# c.execute("SELECT rowid, * FROM customers LIMIT 2")


#c.execute("SELECT rowid, * FROM customers LIMIT 2")
items = c.fetchall()
for item in items:
	print(item)

# Close the connection
conn.close()