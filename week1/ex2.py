def rsa_fun(p, q, en_text):
    n = p * q
    e = calculate_e_num(p, q)
    d = find_d_num(e, p, q)
    data_as_number = hash(en_text) % n
    t = data_as_number ** e % n
    r = t ** d % n
    return n, e, d, t, r


def gcd(first_num, second_num) -> int:
    if second_num == 0:
        return first_num
    else:
        return gcd(second_num, (first_num % second_num))

def calculate_e_num(p: int, q: int) -> int:
    for e in range(2, (p - 1) * (q - 1)):
        if gcd((q - 1) * (p - 1), e) == 1:
            return e

find_d_num = lambda e, p, q: pow(e, -1, (p - 1) * (q - 1))

print(rsa_fun(53, 59, 1858))