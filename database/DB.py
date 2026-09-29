import sqlite3
#todo: дописать первого пользователя
connection = sqlite3.connect('bot.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
telegram_id INTEGER PRIMARY KEY,
name TEXT,
streak INTEGER DEFAULT 0,
longest_streak INTEGER DEFAULT 0,
last_report_date TEXT
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS reports (
id INTEGER PRIMARY KEY AUTOINCREMENT,
user_id INTEGER,
book_id INTEGER, 
pages INTEGER, 
date TEXT
)
''')


cursor.execute('''
CREATE TABLE IF NOT EXIST books (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
user_id INTEGER, 
title TEXT, 
author TEXT,
total_paged INTEGER,
current_page INTEGER DEFAULT 0
)
''')

connection.commit()
connection.close()