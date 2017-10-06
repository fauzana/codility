def solution(A, B, K):
    return (B - A) // K + 1 if A % K == 0 else (B - (A - A % K)) // K

print solution(6, 11, 2)
print solution(11, 345, 17)
print solution(0, 1, 11)
print solution(10, 10, 20)
