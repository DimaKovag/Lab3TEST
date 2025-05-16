"""
Приклад навмисно поганого коду для тестування SonarQube
"""

import os
import pickle
from flask import Flask
import subprocess
import sys
import re

app = Flask(__name__)

# 1. Проблема безпеки: Hardcoded credentials
DB_PASSWORD = "admin123"  # S2068
API_KEY = "1234-5678-9012"  # S2068

# 2. Невикористані імпорти/змінні
unused_var = 42  # S1481

# 3. Дублювання коду
def calc_sum(a, b):
    return a + b

def calculate_sum(x, y):  # S4144
    return x + y

# 4. Проблеми з безпекою: SQL-ін'єкція
def get_user(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"  # S3649
    # ... виконання запиту ...

# 5. Небезпечні операції
def run_command(cmd):
    return subprocess.call(cmd, shell=True)  # S2076

# 6. Погана обробка винятків
def divide(a, b):
    try:
        return a / b  # S108
    except:
        pass  # S118

# 7. "Магічні числа"
def process_data():
    for i in range(0, 100, 7):  # S109
        print(i * 0.33)  # S109

# 8. Проблеми з продуктивністю
def find_duplicates(data):
    return [x for x in data if data.count(x) > 1]  # S4140

# 9. Небезпечна серіалізація
def load_config():
    with open("config.pickle", "rb") as f:
        return pickle.load(f)  # S5796

# 10. Поганий стиль коду
class MyClass:  # S101
    def __init__(SELF):  # S001
        SELF.value = 0  # S001
    
    def getVAL(self):  # S001
        return self.value * 2.5  # S001

# 11. Регулярні вирази з проблемами
def validate_phone(phone):
    return re.match(r"\d+", phone)  # S5852

# 12. Проблеми з потокобезпекою
shared_counter = 0

def increment_counter():
    global shared_counter
    shared_counter += 1

# 13. Потенційні XSS (для веб-додатків)
@app.route("/hello/<name>")
def hello(name):
    return f"<h1>Hello {name}!</h1>"  # S5131

# 14. Занадто довга функція
def long_function():  # S138
    # ... 50+ рядків коду ...
    pass

# 15. Пусті блоки коду
if __name__ == "__main__":
    pass  # S118

# 16. Недостатня інкапсуляція
class BadEncapsulation:
    def __init__(self):
        self.secret = "password"  # S1068

# 17. Проблеми з ресурсами
def read_file():
    f = open("data.txt")  # S2092
    data = f.read()
    # забули закрити файл
    return data

# 18. Погане ім'я змінної
a = 10  # S001

# 19. Невикористаний код
def unused_function():  # S1144
    return 42

# 20. Проблеми зі складністю
def complex_function(x):  # S1541
    if x > 0:
        if x < 10:
            if x % 2 == 0:
                return True
    return False