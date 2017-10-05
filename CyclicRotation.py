def solution(A, K):
    if len(A) == 0:
        return A
    K = K % len(A)
    return A[-K:] + A[:-K]

print(solution( [3, 8, 9, 7, 6], 3 ))
print(solution( [-1000, 5], 2 ))
# ([-9, 0], 2) the solution returned a wrong answer (got [0, -9] expected [-9, 0]).
#print(solution( [3, 8, 9, 7, 6], 3 ))
#print(solution( [3, 8, 9, 7, 6], 3 ))
#print(solution( [3, 8, 9, 7, 6], 3 ))
#print(solution( [3, 8, 9, 7, 6], 3 ))
#print(solution( [3, 8, 9, 7, 6], 3 ))
