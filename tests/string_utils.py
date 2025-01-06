# создание функции
def reverse_string(s):
    return s[::-1] # возвращает перевернутую строку

def is_palindrom(s):
    decorated = ''.join(c.lower() for c in s if c.isalnum())
    return decorated == decorated[::-1] # проверяет является ли строка палиндромом
