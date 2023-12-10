

if __name__ == "__main__":
    a = 1214

    res = 0

    for _ in range(32):
        res = (res << 1) + (a & 1)
        a = a >> 1

    print(res)
