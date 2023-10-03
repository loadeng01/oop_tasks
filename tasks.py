# TASK 1

# 1)Создайте класс MathUtils с staticmethod под названием multiply,
# который принимает два аргумента и возвращает их произведение.


# class MathUtils:
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#
# multi = MathUtils.multiply(4, 5)
# print(multi)


# 2)Создайте класс DateUtils с classmethod под названием is_valid_date, который принимает строку в формате даты
# (например, "2023-07-18") и проверяет, является ли эта дата действительной. Метод должен возвращать True,
# если дата действительна, и False в противном случае.

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






#
# 3)Создайте класс StringUtils с staticmethod под названием is_palindrome, который принимает строку и проверяет,
# является ли она палиндромом (читается одинаково слева направо и справа налево). Метод должен возвращать True,
# если строка является палиндромом, и False в противном случае.






#
# 4)Создайте класс Shape с staticmethod под названием get_circle_area, который принимает радиус и возвращает площадь круга.
# Площадь круга вычисляется по формуле πr^2, где π примерно равно 3.14159.
#
# 5)Создайте класс FileUtils с classmethod под названием get_file_extension,
# который принимает имя файла в виде строки и возвращает его расширение.
# Если файл не имеет расширения, метод должен возвращать пустую строку.
# Например, для файла "document.txt" метод должен вернуть ".txt".
