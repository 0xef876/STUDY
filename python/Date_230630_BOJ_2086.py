def square(A, n):
    if n == 1:
        return A
    else:
        temp = square(A, n//2)
        ret = multi_matrix(temp, temp)
        if n % 2:
            return multi_matrix(ret, A)
        else:
            return ret


def multi_matrix(A, B):
    C = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= 1000000000
    return C


a, b = map(int, input().split())

A = [[1, 1], [1, 0]]

sum_a = square(A, a + 1)[0][1]
sum_b = square(A, b + 2)[0][1]
print((sum_b - sum_a + 1000000000) % 1000000000)
