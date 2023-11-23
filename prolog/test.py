from pyswip import Prolog

prolog = Prolog()
prolog.consult('my_bellman.pl')


edges = ['a1','a2','a3','a4','a5',
    'b1','b2','b3','b4','b5',
    'c1','c2','c3','c4','c5']

source = 'a1' #input("Source: ")
destination = None #input("Destination: ")
edges_no_source = edges.remove(source)


edges = [
    "c2",
    "c3",
    "c4",
    "c5",
]

for e in edges:
    result = list(prolog.query(f'bf(5, a1, {e}, Cost, Path)'))
    print(result[0]['Path'])

# query = f'bf(5, {source}, {destination}, Cost, Path)'

# result = list(prolog.query(f'{query}'))
# print(result)