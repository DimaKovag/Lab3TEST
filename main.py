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


def process_data(data):
    result = []
    for i in range(len(data)):
        if data[i] % 2 == 0:
            for j in range(len(data)):
                if data[j] > 5:
                    for k in range(len(data)):
                        if data[k] < 10:
                            result.append(data[i] + data[j] * data[k])
    return result

# 2. Дублювання коду (погіршує Maintainability)
def calculate_area1(radius):
    return 3.14 * radius * radius

def calculate_area2(r):
    return 3.14 * r * r  # Той самий код з іншими назвами

# 3. Необроблені винятки (погіршує Reliability)
def divide_numbers(a, b):
    return a / b  # Може викликати ZeroDivisionError

# 4. Недосяжний код (погіршує Reliability)
def check_value(x):
    if x > 100:
        return "Big"
    elif x > 50:
        return "Medium"
    elif x > 0:
        return "Small"
    else:
        return "Negative"
    print("This never executes")  # S2583

# 5. Занадто довгі методи (погіршує Maintainability)
def long_complicated_method():
    # 50+ рядків дублюючогося коду
    x = 0
    for i in range(100):
        x += i
        if i % 2 == 0:
            x -= 1
        elif i % 3 == 0:
            x += 2
        else:
            x *= 1.5
    # ... ще 40+ рядків аналогічного коду ...
    return x

# 6. Порушення принципів SOLID (погіршує Maintainability)
class GodObject:
    def __init__(self):
        self.data = []
    
    def process_data(self):
        # ... 50+ рядків коду ...
        pass
    
    def save_to_file(self):
        # ... 30+ рядків коду ...
        pass
    
    def validate_input(self):
        # ... 20+ рядків коду ...
        pass

# 7. Нестабільні тести (погіршує Reliability)
def test_random_behavior():
    import random
    assert random.randint(0, 100) > 50  # S2699