def is_reflexive(relation, set_elements):
    return all((a, a) in relation for a in set_elements)

def is_symmetric(relation):
    return all((b, a) in relation for (a, b) in relation)

def is_transitive(relation):
    return all((a, c) in relation for (a, b) in relation for (b, c) in relation if (a, c) not in relation)

def is_equivalence_relation(relation, set_elements):
    return is_reflexive(relation, set_elements) and is_symmetric(relation) and is_transitive(relation)

# Example usage
set_elements = {1, 2, 3}
relation = {(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (2, 3), (3, 2), ()}

is_equivalence = is_equivalence_relation(relation, set_elements)
print("Is the relation an equivalence relation?", is_equivalence)
