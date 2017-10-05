def solution(A):
    x = 0
    for i in A:
        x = x ^ i
    return x

print solution([9, 3, 9, 3, 9, 7, 9] )