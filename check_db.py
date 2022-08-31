import sqlite3


db = sqlite3.connect('employee.sqlite')

# Retrieve Data:
people_query = db.execute('SELECT * FROM people')
id_name = db.execute('SELECT id, name FROM people')

salary_query = db.execute('SELECT * FROM salary')

print(people_query)

for item in people_query:
    print(item)
    # tuple

# better to use keys (it does not search in db)
for item in id_name:
    print(item)

print('=' * 40)

for item in salary_query:
    print(item)

