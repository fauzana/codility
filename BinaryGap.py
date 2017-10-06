def solution(N):
    splitN = str(int(bin(N)[2:])).split('1')
    maxN = 0
    for j in range(0, (len(splitN)-1)):
        l = len(splitN[j])
        if maxN < l: maxN = l
    return maxN

print(solution(6))
print(solution(9))
print(solution(529))
print(solution(20))
print(solution(15))
