import datetime
import sqlite3


db = sqlite3.connect('employee.sqlite')
cursor = db.cursor()

for item in cursor.execute('SELECT * FROM salary'):
    print(item)

print('=' * 40)

salary_records = cursor.execute('SELECT * FROM salary')
print(salary_records)
print(type(salary_records))

for item in salary_records:
    print(item)

print('=' * 40)

# Warning: cursor is a generator so when iteration on cursor, it can not rest and print (you should call again cursor)
for item in salary_records:
    print(item)

print('=' * 40)

# for read one record:
salary_records = cursor.execute('SELECT * FROM salary')
print(salary_records.fetchone())
print(salary_records.fetchone())
print(salary_records.fetchone())
print(salary_records.fetchone())

print('=' * 40)

# it is List of all records of salary:
salary_records = cursor.execute('SELECT * FROM salary')

print(salary_records.fetchall())

print('=' * 40)

cursor.execute('UPDATE salary SET amount=? WHERE id=?', (13000, 1003))
# would give you the number of results of a query:
print(cursor.rowcount)

salary_records = cursor.execute('SELECT * FROM salary')
print(cursor.rowcount)

print('=' * 40)

# would give you last record that changed
today = datetime.date.today()
cursor.execute('INSERT INTO salary VALUES(?, ?, ?)', (1004, 28000, today))
print(cursor.lastrowid)







