from math import sqrt

import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок


def fidelity():
    return pow(10, -2)


def higher_end():
    return 2


def lower_end():
    return 1


def frequency():
    return 50


def our_function(x):
    return 2 * pow(x, 2) + 3 * pow(5 - x, 4 / 3)


def get_index_of_min_value_by_list(n_list: list) -> int:
    min_index = 0
    i = 0
    for value in n_list:
        if value < n_list[min_index]:
            min_index = i
        i += 1

    return min_index


def get_min_x_value_with_method_of_bisections(lower_value=lower_end(), higher_value=higher_end(), fidelity=fidelity()):
    x_list = np.linspace(lower_value, higher_value, 4)
    y_list = [our_function(x) for x in x_list]
    lower_index = get_index_of_min_value_by_list(list(y_list))

    if lower_index == 0 or lower_index == 3:
        raise ValueError("Invalid range")

    if x_list[lower_index + 1] - x_list[lower_index - 1] < fidelity:
        if y_list[lower_index - 1] < y_list[lower_index + 1]:
            x_needed = x_list[lower_index - 1]
        else:
            x_needed = x_list[lower_index + 1]
        return x_needed

    return get_min_x_value_with_method_of_bisections(x_list[lower_index - 1], x_list[lower_index + 1])


def get_n_fibonacci_number(n: int):
    return pow((1 + sqrt(5)) / 2, n + 1) - pow((1 - sqrt(5)) / 2, n + 1) / sqrt(5)


def get_min_x_value_with_method_of_fibonacci(lower_value=lower_end(), higher_value=higher_end(), fidelity=fidelity()):
    k = (higher_value - lower_value) / fidelity
    j = 0
    while get_n_fibonacci_number(j) <= k:
        j += 1
    b = (higher_value - lower_value) / get_n_fibonacci_number(1)
    x = {1: lower_value + b * get_n_fibonacci_number(j - 2)}



def main():
    x_list = np.linspace(lower_end() - 1, higher_end() + 1, frequency())
    y_list = [our_function(x) for x in x_list]
    data = {'x': x_list, 'y': y_list}
    min_x = get_min_x_value_with_method_of_bisections()
    min_y = our_function(min_x)

    df = DataFrame(data, columns=['x', 'y'])
    plt.plot(x_list, y_list, 'r', [min_x], [min_y], 'gs')
    plt.show()


if __name__ == '__main__':
    main()
