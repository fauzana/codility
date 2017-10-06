def solution(A):
    n = len(A)
    total = sum(A)
    
    runningTotal = A[0]
    total = total - A[0]
    
    diff = abs(total - runningTotal)
    
    for i in range(1, n-1):
        runningTotal = runningTotal + A[i]
        total = total - A[i]
        temp = abs(total - runningTotal)
        if temp < diff: diff = temp

    return diff

print solution([3, 1, 2, 4, 3])