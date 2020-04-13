def calcula_pi(n):
    count = 0
    nsqrt = 0
    while (count != n):
        count +=1
        nsqrt = nsqrt + 6/(count**2)
    pi = nsqrt**0.5
    return pi
