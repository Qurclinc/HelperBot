from typing import List

def header_PAE() -> str:
    return "+--------+--------+--------+--------+--------+\n" \
           "|   №    |   ai   |   xi   |   yi   |   qi   |\n" \
           "+--------+--------+--------+--------+--------+"


def find_values(a: int, b: int) -> List[List]:
    """
    Возвращает список строк вида [i, ai, xi, yi, qi]
    где qi — целочисленное частное (a_{i-1} // a_i) для i>=1, для 0-го элемента '-'
    """
    result = [[0, a, 1, 0, "-"], [1, b, 0, 1, a // b]]
    i = 2
    while True:
        _, a2, x2, y2, q2 = result[i - 2]
        _, a1, x1, y1, q1 = result[i - 1]
        ai = a2 - a1 * q1
        xi = x2 - x1 * q1
        yi = y2 - y1 * q1
        if ai == 0:
            break
        qi_next = a1 // ai if ai != 0 else "-"
        result.append([i, ai, xi, yi, qi_next])
        i += 1

    return result


def do_PAE(values: List[List]) -> str:
    """
    Формирует табличный вывод как строку.
    """
    lines = []
    lines.append(header_PAE())
    for line in values:
        idx, ai, xi, yi, qi = map(str, line)
        lines.append("|" +
                     f"{idx:^8}" + "|" +
                     f"{ai:^8}" + "|" +
                     f"{xi:^8}" + "|" +
                     f"{yi:^8}" + "|" +
                     f"{qi:^8}" + "|")
        lines.append("+--------+--------+--------+--------+--------+")
    return "\n".join(lines)


# ---------- ОАЕ ----------
def header_OAE() -> str:
    return "+--------+-------------------------+\n" \
           "|   №    |       Текущие числа    |\n" \
           "+--------+-------------------------+"


def do_OAE(nums: list) -> str:
    """
    Алгоритм ОАЕ (общий алгоритм Евклида).
    nums: список чисел
    Возвращает табличку шагов.
    """
    result = []
    step = 1
    lines = [header_OAE()]

    while len(nums) != 1:
        minimal = min([i for i in nums if i > 0])
        nums.remove(minimal)
        tmp = [minimal] + [el % minimal for el in nums if el % minimal != 0]
        result.append(tmp)
        lines.append("|" + f"{step:^8}" + "|" + f"{str(tmp):^25}" + "|")
        lines.append("+--------+-------------------------+")
        nums = tmp[:]
        step += 1

    return "\n".join(lines)
