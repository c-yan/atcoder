K = int(input())


def is_lunlun(i):
    result = -1
    n = [ord(c) - 48 for c in str(i)]
    for j in range(len(n) - 1):
        if abs(n[j] - n[j + 1]) <= 1:
            continue
        if n[j] < n[j + 1]:
            for k in range(j + 1, len(n)):
                n[k] = 0
            result = int(''.join(str(k) for k in n))
            result += 10 ** (len(n) - (j + 1))
        else:
            result = int(''.join(str(k) for k in n))
            result += 10 ** (len(n) - (j + 2))
        break
    return result


i = 1
while True:
    # print(i)
    t = is_lunlun(i)
    if t == -1:
        K -= 1
        if K == 0:
            print(i)
            exit()
        i += 1
    else:
        i = t
