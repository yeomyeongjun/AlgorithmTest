A = input()

B = []
for i in range(26):
    B.append(-1)

for i in range(len(A)):
    if B[ord(A[i]) - 97] == -1:
        B[ord(A[i]) - 97] = i

for i in range(len(B)):
    print(B[i], end = ' ')