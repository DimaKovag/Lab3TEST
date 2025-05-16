"""
Приклад якісного коду, що відповідає стандартам SonarQube
"""

import logging
from typing import List, Optional
from dataclasses import dataclass
import math

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class Circle:
    """Клас для роботи з колом"""
    radius: float

    @property
    def area(self) -> float:
        """Площа круга"""
        return math.pi * self.radius ** 2

    @property
    def circumference(self) -> float:
        """Довжина кола"""
        return 2 * math.pi * self.radius

def safe_divide(dividend: float, divisor: float) -> Optional[float]:
    """Безпечне ділення з обробкою помилок"""
    try:
        return dividend / divisor
    except ZeroDivisionError:
        logger.warning("Attempted division by zero")
        return None
    except TypeError as e:
        logger.error(f"Type error in division: {e}")
        return None

def calculate_statistics(numbers: List[float]) -> dict:
    """Обчислення базової статистики"""
    if not numbers:
        return {}

    stats = {
        'mean': sum(numbers) / len(numbers),
        'max': max(numbers),
        'min': min(numbers),
    }
    return stats

def process_data(data: List[str]) -> List[int]:
    """Обробка даних з валідацією вхідних значень"""
    result = []
    for item in data:
        try:
            processed = int(item.strip())
            if processed > 0:  # Додаткова валідація
                result.append(processed)
        except (ValueError, AttributeError) as e:
            logger.warning(f"Invalid data item: {item}, error: {e}")
    return result

class DataProcessor:
    """Клас для обробки даних зі збереженням стану"""
    
    def __init__(self, initial_data: List[float] = None):
        self.data = initial_data if initial_data else []

    def add_data(self, value: float) -> None:
        """Додавання нового значення"""
        if isinstance(value, (int, float)):
            self.data.append(float(value))

    def get_stats(self) -> dict:
        """Отримання статистики"""
        return calculate_statistics(self.data)

def main() -> None:
    """Основна логіка програми"""
    try:
        # Приклад використання
        circle = Circle(radius=5.0)
        print(f"Area: {circle.area:.2f}")
        print(f"Circumference: {circle.circumference:.2f}")

        result = safe_divide(10, 2)
        print(f"Division result: {result}")

        data = ["10", "20", "abc", "30", "-5"]
        processed = process_data(data)
        print(f"Processed data: {processed}")

        processor = DataProcessor([1.5, 2.5, 3.5])
        processor.add_data(4.5)
        print(f"Statistics: {processor.get_stats()}")

    except Exception as e:
        logger.exception(f"Unexpected error: {e}")
        raise

if __name__ == "__main__":
    main()