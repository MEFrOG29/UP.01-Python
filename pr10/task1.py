def factorial(n):
  try:
    if n < 0:
      raise ValueError
    elif n == 0 | n == 1:
      return 1
    else:
      return n * factorial(n-1)
  except TypeError:
    return "Ошибка типа данных"
  except ValueError:
    return "Ошибка значения"

if __name__ == '__main__':
  print(factorial(5))
