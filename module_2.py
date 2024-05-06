"""Функція discount_price"""


def discount_price(price, discount):
    """function discount_price"""
    def apply_discount():
        nonlocal price
        price *= (1 - discount)
    apply_discount()
    return price


# Приклад використання:
print(discount_price(50, 0.5))

def get_fullname(first_name, last_name, middle_name=""):
    if middle_name:
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"
print(get_fullname("Mykola","Mazo","/"))

def format_string(string: str, length: int) -> str:
    if len(string) >= length:
        return string
    else:
        spaces = (length - len(string)) // 2
        formatted_string = " " * spaces + string
        return formatted_string
print(format_string("wer",5))

def first(size, *args):
    return size + len(args)

def second(size, **kwargs):
    return size + len(kwargs)
print(first(30,1,1,1,1))
print(second(1))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def number_of_groups(n: int, k: int) -> int:
    numerator = factorial(n)
    denominator = factorial(n - k) * factorial(k)
    combinations = int(numerator / denominator)
    return combinations

print(factorial(5))
print(number_of_groups(4,2))