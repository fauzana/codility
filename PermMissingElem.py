def solution(A):
    n = len(A) + 1
    x = n * (n + 1) // 2
    for i in A:
        x -= i
    return x

print solution([2, 3, 1, 5])