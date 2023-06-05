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


p = int(input())
q = int(input())
n = p * q
e = calculate_e_num(p, q)
d = find_d_num(e, p, q)
print(f"Public key: n={n}, e={e}")
print(f"Private key: d={d}")