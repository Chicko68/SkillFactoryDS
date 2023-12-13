"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def optimized_predict(number: int = 1) -> int:
    """Угадывание числа методом половинного деления
    Сначала устанавливаем начальное число посередине интервала угадывания,
    затем, если число не угадано, делим начальный интервал поиска пополам,
    а число устанавливаем в центре нового интервала поиска. И так интервал поиска
    итерационно сужается до тех пор, пока число не будет угадано.
       Функция принимает загаданное число и возвращает число попыток.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    # Задаём интервал, в пределах которого было загадано число
    lower_bound = 1
    upper_bound = 100

    # predict = np.random.randint(lower_bound, upper_bound + 1)    # Первое предположение
    predict = lower_bound + (upper_bound - lower_bound) // 2    # Первое предположение
    count = 1

    while number != predict:
        count += 1

        if number > predict:
            lower_bound = predict
            if upper_bound - lower_bound == 1:  # Если загадано последнее число интервала
                upper_bound += 1

        elif number < predict:
            upper_bound = predict

        predict = lower_bound + (upper_bound - lower_bound) // 2

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10))  # загадали список чисел
    print(random_array)

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(optimized_predict)
