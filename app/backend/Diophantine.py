from math import gcd
from .Euclid import find_values

def solve_diophantine_equation(a: int, b: int, c: int) -> dict:
    answer = dict()
    answer["gcd"] = gcd(a, b)
    if c % answer["gcd"] != 0:
        answer["result"] = "Нет решений"
        return answer
    answer["table"] = find_values(a, b)
    k1, k2 = answer["table"][-1][2], answer["table"][-1][3]
    answer["k1"] = k1
    answer["k2"] = k2
    if c != 1:
        answer["multiplicated"] = True
        x0 = k1 * c
        y0 = k2 * c
    else:
        answer["multiplicated"] = False
    answer["part_solution"] = (x0, y0)
    answer["common_solution"] = {
        "x": (x0, b / answer["gcd"]),
        "y": (y0, a / answer["gcd"])
    }
    return answer