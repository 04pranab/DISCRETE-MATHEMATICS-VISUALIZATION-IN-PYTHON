import random

def generate_random_relation(A=[1, 2, 3, 4, 5]):
    n = len(A)
    relations = set()
    num_relations = random.randint(0,n**2-1)
    
    for _ in range(num_relations):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        relations.add((A[i], A[j]))

    return relations


"""A = [1, 2, 3, 4, 5]

random_R = generate_random_relation(A)
print("Random Relation R:",end=" ")
print(random_R)"""