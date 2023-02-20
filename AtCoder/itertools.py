#重複あり順列
list(itertools.product(range(n), repeat=n))

#重複なし順列
list(itertools.permutations(range(n), n))

#重複あり組み合わせ
lsit(itertools.combinations_with_replacement(range(n), n))

#重複なし組み合わせ
list(itertools.combinations(range(n), n))
