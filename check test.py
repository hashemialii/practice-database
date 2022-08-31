import sqlite3

db = sqlite3.connect('employee.sqlite')

people_query = db.execute('SELECT * FROM people')

print(people_query)

for item in people_query:
    print(item)



