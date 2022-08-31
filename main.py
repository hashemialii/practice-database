import sqlite3
import datetime


db = sqlite3.connect('employee.sqlite')


# search ==> sqlite python Create table

# Create table
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

# Create Record
# db.execute('INSERT INTO people (id, name, phone, department) '
#            'VALUES(1001, "Ali Hashemi", "09121234567", "IT")')

# Create Record
# db.execute('INSERT INTO people VALUES(1002, "Peyman Haghighi", "09124569988", "SUPPORT")')

today = datetime.date.today()
db.execute('INSERT INTO salary VALUES(1001, 15000, "{}")'.format(today))
db.execute('INSERT INTO salary VALUES(1002, 17500, "{}")'.format(today))
db.execute('INSERT INTO salary VALUES(1003, 18000, "{}")'.format(today))


# Delete Data
# db.execute('DELETE FROM salary WHERE id=1001')
# db.execute('DELETE FROM salary WHERE id=1002')
# db.execute('DELETE FROM salary WHERE id=1003')

# update Data
# db.execute('UPDATE salary SET amount=25000 WHERE id=1002')

# after do sth in your database u should commit and close your db
db.commit()
db.close()

