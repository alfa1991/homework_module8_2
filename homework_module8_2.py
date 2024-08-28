def personal_sum(numbers):
  """
  Подсчитывает сумму чисел в коллекции.

  Args:
    numbers: Коллекция чисел.

  Returns:
    Кортеж: (сумма чисел, количество некорректных данных).
  """

  result = 0
  incorrect_data = 0
  for num in numbers:
    try:
      result += num
    except TypeError:
      incorrect_data += 1
  return result, incorrect_data

def calculate_average(numbers):
  """
  Вычисляет среднее арифметическое коллекции чисел.

  Args:
    numbers: Коллекция чисел.

  Returns:
    Среднее арифметическое или None в случае ошибки.
  """

  try:
    total, incorrect = personal_sum(numbers)
    if incorrect > 0:
      print(f"Некорректный тип данных для подсчёта суммы - {incorrect} раз")
    if len(numbers) == 0:
      raise ZeroDivisionError
    return total / len(numbers)
  except TypeError:
    print("В numbers записан некорректный тип данных")
  except ZeroDivisionError:
    print("Деление на ноль")
  return None

print(f"Результат 1: {calculate_average('1, 2, 3')}")
print(f"Результат 2: {calculate_average([1, 'Строка', 3, 'Ещё Строка'])}")
print(f"Результат 3: {calculate_average(567)}")
print(f"Результат 4: {calculate_average([42, 15, 36, 13])}")