class Fraction:
    """
Ваша задача - реализовать перегрузĸи операторов
арифметичесĸих действий c дробями в ĸлассе Fraction.
Реализовать задачу в PyQT5.
    """

    def __init__(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return f'Fraction -> {self.__x} / {self.__y}'

    def get_fraction(self) -> tuple:
        return self.__x, self.__y

# Переопределяем функции
    def __add__(self, other):
        """
        Возвращает суму дробей по формуле:
        Fraction (x,y)
        x = x1 + x2
        y = y1 or y2 - если они одинаковы, если нет, ищем общий знаменатель

        :param other: Fraction
        :return: Fraction
        """
        x1, y1 = self.get_fraction()
        x2, y2 = other.get_fraction()

        x = x1 + x2
    # Условие поиска общего знаменателя
        if y1 == y2:
            y = y1
            return Fraction(x, y)

        if y1 != y2:
            n = y1 * y2
            while y1 != 0 and y2 != 0:
                if y1 > y2:
                    y1 %= y2
                else:
                    y2 %= y1
            m = n // (y1 + y2)

        return Fraction(x, m)


    def __sub__(self, other):
        """
        Возвращает результат вычитания дробей по формуле:
        Fraction (x,y)
        x = x1 - x2
        y = y1 or y2 - если они одинаковы, если нет, ищем одбщий знаменатель

        :param other: Fraction
        :return: Fraction
        """
        x1, y1 = self.get_fraction()
        x2, y2 = other.get_fraction()

        x = x1 - x2
        # Условие поиска общего знаменателя
        if y1 == y2:
            y = y1
            return Fraction(x, y)

        if y1 != y2:
            n = y1 * y2
            while y1 != 0 and y2 != 0:
                if y1 > y2:
                    y1 %= y2
                else:
                    y2 %= y1
            m = n // (y1 + y2)

        return Fraction(x, m)


    def __mul__(self, other):
        """
        Возвращает результат умножени дробей по формуле:
        Fraction (x,y)
        x = x1 * x2
        y = y1 * y2

        :param other: Fraction
        :return: Fraction
        """
        x1, y1 = self.get_fraction()
        x2, y2 = other.get_fraction()

        x = x1 * x2
        y = y1 * y2

        return Fraction(x, y)

    def __truediv__(self, other):
        """
        Возвращает результат деления дробей по формуле:
        Fraction (x,y)
        x = x1 * x2
        y = y1 * y2

        :param other: Fraction
        :return: Fraction
        """

        x1, y1 = self.get_fraction()
        x2, y2 = other.get_fraction()

        x = x1 * y2
        y = y1 * x2

        return Fraction(x, y)
