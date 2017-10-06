def solution(X, A):
    isJump = [False] * X
    path = X
    
    for i in xrange(len(A)):
        if isJump[A[i] - 1] == False:
            isJump[A[i] - 1] = True
            path -= 1
            if path == 0:
                return i
    return -1

print solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
print solution(2, [2, 2, 2, 2, 2])
