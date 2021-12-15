import random
import string


def random_str(length: int) -> str: return ''.join(
    random.choices(string.ascii_letters + string.digits, k=length))


print(random_str(45))
