def solution(A):
    N = len(A)
    T = N * (N + 1) // 2
    detect = [False] * N

    for i in A:
        if 0 <= i > N:
            return 0
        if detect[i-1] == True:
            return 0
        T = T - i
        detect[i-1] = True
    return 1 if T == 0 else 0

print solution([4, 1, 3, 2])
print solution([4, 1, 3])
print solution([1, 4, 1])
