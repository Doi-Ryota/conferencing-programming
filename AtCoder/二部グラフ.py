n = I()
d = defaultdict(list)
for i in range(n-1):
    a,b = MI()
    d[a].append(b)
    d[b].append(a)
a = [set(),set()]
a[0].add(1)
kan = {1}
deq = deque()
deq.append(1)
while len(deq) != 0:
    p = deq.popleft()
    for i in d[p]:
        if p in a[0]:
            a[1].add(i)
        else:
            a[0].add(i)
        if i not in kan:
            deq.append(i)
            kan.add(i)
