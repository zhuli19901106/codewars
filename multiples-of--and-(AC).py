def count(n, k):
    return (n / k) * (n / k + 1) / 2 * k
    
def solution(number):
    n = number - 1
    return count(n, 3) + count(n, 5) - count(n, 15)
    