from math import gcd

def euler_phi(n: int) -> int:
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def is_prime(n: int) -> bool:
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Ввод данных
def find_reverse(a: int, m: int) -> str:
    # a, m = map(int, input().split())
    answer = []
    # Проверка взаимной простоты
    if gcd(a, m) != 1:
        return "Обратного элемента не существует"
    else:
        # Выбор теоремы
        if is_prime(m):
            exponent = m - 2
            theorem = "Ферма"
            answer += [f"Использована малая теорема Ферма: {a}^(-1) ≡ {a}^({m}-2) mod {m}"]
        else:
            phi_m = euler_phi(m)
            exponent = phi_m - 1
            theorem = "Эйлера"
            answer += [f"Использована теорема Эйлера: {a}^(-1) ≡ {a}^(φ({m})-1) mod {m}"]

        # Бинарный алгоритм
        binary_exp = bin(exponent)[2:]  # Полное бинарное представление
        result = 1
        base = a % m

        answer += [f"Вычисляем: {a}^({exponent}) mod {m}"]
        answer += [f"Бинарное представление: {binary_exp}"]

        # Формируем строки операций
        full_sequence = ""
        short_sequence = ""
        for bit in binary_exp:
            if bit == '1':
                full_sequence += f"SM{a}"
                short_sequence += f"SM{a}"
            else:
                full_sequence += "S"
                short_sequence += "S"

        # Удаляем первый бит из короткой последовательности
        short_sequence = short_sequence[2:] if len(short_sequence) > 2 else ""

        answer += [f"Полная последовательность: {full_sequence}"]
        answer += [f"С удаленным первым битом: {short_sequence}"]
        answer += ["\n"]

        # Вычисляем и выводим сравнения
        result = base
        answer += [f"{a} ≡ {result} (mod {m})"]

        for i, bit in enumerate(binary_exp[1:], 1):
            # S операция (возведение в квадрат)
            old_result = result
            result = (result * result) % m
            answer += [f"{old_result}^2 = {old_result ** 2} (mod {m}) ≡ {result} (mod {m})"]

            # M операция если бит = 1 (умножение на основание)
            if bit == '1':
                old_result = result
                result = (result * base) % m
                answer += [f"{old_result}×{a} = {old_result * a} (mod {m}) ≡ {result} (mod {m})"]

        answer += [f"\nРезультат: {a}^(-1) ≡ {result} (mod {m})"]
        return "\n".join(answer)