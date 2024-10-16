def transitive_closure(graph):
    n = len(graph)
    closure = [[0 if i != j else 1 for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                closure[i][j] |= (closure[i][k] & closure[k][j])

    return closure


graph = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

tc = transitive_closure(graph)
for row in tc:
    print(row)
