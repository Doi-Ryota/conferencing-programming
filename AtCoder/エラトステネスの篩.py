# -*- coding:utf-8 -*-


def get_sieve_of_eratosthenes(n):
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


data = get_sieve_of_eratosthenes(100)
