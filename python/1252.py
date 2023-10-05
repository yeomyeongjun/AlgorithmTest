
a = input(); b = input()
c = []
for j in range(max(len(a), len(b)) + 1):
    c.append(0)

print(c)

i = -1
for j in range(min(len(a), len(b)) + 1):
    c[i] += int(a[i]) + int(b[i])

    if c[i] >= 2:
        print("true")
        c[i] = 0
        c[i - 1] += 1

    print(i)

    print(c)
    i -= 1

