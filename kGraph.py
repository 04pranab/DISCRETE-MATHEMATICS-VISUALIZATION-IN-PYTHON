import DM.EdgeGenerater as EG
import DM.Digraph as DG
import itertools as IT

def draw_k(n):
    edges = EG.gen_edges(n)
    if len(edges) <= 1:
        return [(edges[0], edges[0])] if edges else []
    else:
        comb = IT.combinations(edges, 2)
        relation = [(a, b) for a, b in comb]
    return set(relation)

a = draw_k(7)
DG.draw_digraph(a)