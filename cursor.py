import sqlite3
import datetime


db = sqlite3.connect('employee.sqlite')

# using generator in db (cursor is generator, does not directly connect to db)
cursor = db.cursor()


# new_amount = 30000
# salary_id = input('Please enter a new ID: ')
# cursor.executescript('UPDATE salary SET amount={} WHERE id={}'.format(new_amount, salary_id))

# WARNING: SQL Injection:
# input == 1001, drop table salary
# when use "executescript", It can execute multiple commands simultaneously but "execute" just one command,
# so we should use 'execute':


# new_amount = 30000
# salary_id = input('Please enter a new ID: ')
# cursor.execute('UPDATE salary SET amount={} WHERE id={}'.format(new_amount, salary_id))


# Warning: should not use stream formatting when getting information from the user
# Replacement Field:
new_amount = 30000
salary_id = input('Please enter a new ID: ')
cursor.execute('UPDATE salary SET amount=? WHERE id=?', (new_amount, salary_id))


# after do sth in your database u should commit and close your db
db.commit()
cursor.close()
db.close()

