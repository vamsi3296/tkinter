import database

# Add a Record
# database.add_one("Laura", "Smith", "laura@smith.com")

# Delete a record
#database.delete_one('8')

stuff = [
	('Brenda', 'Smitherton', 'brenda@smitherton.com'),
	('Joshua', 'Smith', 'joshua@smith.com')
]

database.add_many(stuff)

# Show the data
database.show_all()

