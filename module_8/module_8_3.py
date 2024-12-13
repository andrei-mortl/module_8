class IncorrectVinNumber(Exception):
    """Класс ошибки vin-номера"""
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    """Класс ошибки номера автомобиля"""
    def __init__(self, message):
        self.message = message

class Car:
    """Класс автомобилей"""
    def __init__(self, model, __vin, __numbers):
        self.model = str(model)
        self.__vin = int(__vin)
        self.__is_valid_vin(self.__vin)
        self.__numbers = str(__numbers)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номера (не число)')
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectVinNumber('Некорректный тип данных для номеров')
        if not len(numbers) == 6:
            raise IncorrectVinNumber('Неверная длина номера')
        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
