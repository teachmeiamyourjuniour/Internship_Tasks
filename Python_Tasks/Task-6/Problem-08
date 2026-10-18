#8.Tuples
# https://www.hackerrank.com/challenges/python-tuples/problem


if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))

    # Reproduce the pre-Python-3.8 64-bit tuple hash algorithm
    mask = (1 << 64) - 1

    x = 0x345678
    mult = 1000003
    length = len(t)

    for item in t:
        y = hash(item)

        x = ((x ^ y) * mult) & mask

        length -= 1
        mult += 82520 + length + length
        mult &= mask

    x = (x + 97531) & mask

    # Convert unsigned 64-bit result to signed 64-bit integer
    if x >= (1 << 63):
        x -= (1 << 64)

    if x == -1:
        x = -2

    print(x)
