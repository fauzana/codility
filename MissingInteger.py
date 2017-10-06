def solution(A):
    seen = [False] * len(A)
    for value in A:
        if 0 < value <= len(A):
            seen[value-1] = True
 
    for idx in xrange(len(seen)):
        if seen[idx] == False:
            return idx + 1
 
    return len(A) + 1

print solution([1, 3, 6, 4, 1, 2])
print solution([1, 2, 3])
print solution([-1, -3])