import sqlite3

# создаем соединение с базой
conn = sqlite3.connect("chinook_sqlite.sqlite")
# создаем курсор - специальный объект который делает запросы и получает их результаты
cursor = conn.cursor()

# код
cursor.execute("SELECT Name FROM artists ORDER BY Name LIMIT 3")
results = cursor.fetchall()
results2 = cursor.fetchall()

cursor.execute("insert into artists values (Null, 'A Aagrh!')")
conn.commit()

cursor.execute('SELECT Name FROM artists ORDER BY Name LIMIT ?', ('2',))
cursor.execute('SELECT Name FROM artists ORDER BY Name LIMIT :limit', {"limit": 3})

new_artists = {
    ('A Aargh!,',),
    ('A Aargh-2!,',),
    ('A Aargh-3!,',),
}

cursor.executemany("insert into artists values (Null, ?);", new_artists)

results3 = cursor.fetchall()
print(results3)

print(results)
print(results2)
# закрываем соединение
conn.close()

try:
    cursor.execute(sql_statement)
    result = cursor.fetchall()
except sqlite3.DatabaseError as err:
    print("Error:", err)
else:
    conn.commit()
finally:
    conn.close()
