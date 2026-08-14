import sqlite3
import hashlib
import os

PASSWORD = "admin123"          # Hard-coded credential
API_KEY = "sk_test_123456789"  # Hard-coded API key

username = input("Username: ")
command = input("Command: ")

# SQL Injection vulnerability
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
query = "SELECT * FROM users WHERE username = '" + username + "'"
cursor.execute(query)

# Weak cryptography (MD5)
password_hash = hashlib.md5(PASSWORD.encode()).hexdigest()
print(password_hash)

# Unsafe command execution
os.system(command)

conn.close()