"""
Навмисно поганий код для погіршення Maintainability та Reliability
"""

# 1. Надмірна складність (погіршує Maintainability)
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

# 8. Залежність від реалізації (погіршує Maintainability)
def bad_dependency():
    import sys
    if sys.version_info[0] == 3 and sys.version_info[1] == 8:
        return "Python 3.8"
    else:
        return "Other version"

# 9. Погана обробка None (погіршує Reliability)
def get_length(items):
    return len(items)  # Може викликати TypeError при items=None

# 10. Занадто багато параметрів (погіршує Maintainability)
def overcomplicated_function(a, b, c, d, e, f, g, h, i, j):
    return a + b - c * d / e + f - g * h / i + j

# 11. Неочевидні імена змінних (погіршує Maintainability)
def calculate(x1, x2):
    y1 = x1 * 2.5
    y2 = x2 / 1.5
    z = y1 + y2
    return z * 0.17  # Що таке 0.17? Магічне число (S109)

# 12. Невикористані змінні (погіршує Maintainability)
def unused_vars():
    temp = 42  # S1481
    return 100

# 13. Порожні блоки (погіршує Maintainability)
try:
    pass  # S118
except:
    pass

# 14. Занадто глибокі вкладення (погіршує Maintainability)
def deep_nesting(x):
    if x > 0:
        for i in range(x):
            if i % 2 == 0:
                while True:
                    if i > 10:
                        break
    return x

# 15. Небезпечні типи змінних (погіршує Reliability)
def mutable_default_arg(items=[]):  # S5704
    items.append(1)
    return items