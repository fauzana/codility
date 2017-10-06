def solution(N, A):
    counters = [0] * N
    counterMax = 0
    currentMax = 0
    
    for i in A:
        if 1 <= i <= N:
            if counterMax > counters[i-1]:
                counters[i - 1] = counterMax
            counters[i-1] += 1
            if currentMax < counters[i - 1]:
                currentMax = counters[i - 1]
        else:
            counterMax = currentMax
    
    for i in range(0, N):
        if counters[i] < counterMax:
            counters[i] = counterMax

    return counters

print solution(5, [3, 4, 4, 6, 1, 4, 4])
