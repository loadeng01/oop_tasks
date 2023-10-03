# TASK 1

class MathUtils:
    @staticmethod
    def multiply(a, b):
        return a * b

multi = MathUtils.multiply(4, 5)
print(multi)



# TASK 2

class DateUtils:
    @classmethod
    def is_valid_date(cls, date: str):
        from datetime import datetime
        current = datetime.now().strftime(f'%Y-%m-%d')

        if current == date:
            return True
        return False

date = DateUtils.is_valid_date("2023-07-18")
print(date)



# TASK 3

class StringUtils:
    @staticmethod
    def is_palindrome(word: str):
        word = word.lower()
        if word == word[::-1]:
            return True
        return False

print(StringUtils.is_palindrome('Nolon'))



#TASK 4

class Shape:
    @staticmethod
    def get_circle_area(radius):
        from math import pi
        return (radius**2) * pi

print(Shape.get_circle_area(4))



# TASK 5

class FileUtils:
    @classmethod
    def get_file_extension(cls, file_name: str):
        try:
            dot = file_name.index('.')
        except ValueError:
            return ''
        else:
            return file_name[dot:]

print(FileUtils.get_file_extension('data.html'))

