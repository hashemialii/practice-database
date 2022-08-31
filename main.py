import sqlite3


db = sqlite3.connect('employee.sqlite')

# search ==> sqlite python crate table

# create_query = 'CREATE TABLE IF NOT EXISTS people (' \
#                'id INTEGER PRIMARY KEY, ' \
#                'name TEXT NOT NULL, ' \
#                'phone TEXT, ' \
#                'department TEXT DEFAULT UNKNOWN)'


create_query = 'CREATE TABLE IF NOT EXISTS salary (' \
               'id INTEGER, ' \
               'amount INTEGER NOT NULL, ' \
               'date TIMESTAMP)'

# search ==> sqlite python run commend
db.execute(create_query)

# search ==> sqlite insert
db.execute('INSERT INTO people (id, name, phone, department) '
           'VALUES (1001, "Ali Hashemi", "09121234567", "IT")')


# after do sth in your database u should commit and close your db
db.commit()
db.close()

