N = 0
all_node = []

def help(src, des, distance):
    if (distance < 0):
        distance = f'({str(distance)})'
    print(f'{src}->{des}/{distance},')

def help1(src, des, weight):
    global N
    if src not in all_node:
        all_node.append(src)
    if des not in all_node:
        all_node.append(des)
        
    print(f'graph.edge[{N}].src = {src}')
    print(f'graph.edge[{N}].dest = {des}')
    print(f'graph.edge[{N}].weight = {weight}')
    N += 1

def help2(src, des, weight):
    global N
    if src not in all_node:
        all_node.append(src)
    if des not in all_node:
        all_node.append(des)
        
    print(f'graph[{N}][0] = {src}')
    print(f'graph[{N}][1] = {des}')
    print(f'graph[{N}][2] = {weight}')
    N += 1



help2(1,2,2)
help2(1,3,4)
help2(2,4,-1)
help2(3,4,3)
help2(4,5,2)
help2(4,2,3)
help2(5,6,1)
help2(5,7,-2)
help2(5,3,-1)
help2(6,5,1)
help2(6,8,3)
help2(7,6,3)
help2(7,8,5)
help2(8,9,-4)
help2(9,10,2)
help2(9,11,1)
help2(10,12,4)
help2(10,9,1)
help2(11,10,2)
help2(11,12,1)
help2(12,13,-2)
help2(12,14,3)
help2(13,9,2)
help2(13,15,1)
help2(14,15,2)
help2(14,11,1)
help2(15,1,5)

# help2('a1','a3',4)
# help2('a2','a4',-1)
# help2('a3','a4',3)
# help2('a4','a2',3)
# help2('a4','a5',2)
# help2('a5','a3',-1)
# help2('a5','b1',1)
# help2('a5','b2',-2)
# help2('b1','a5',1)
# help2('b1','b3',3)
# help2('b2','b1',3)
# help2('b2','b3',5)
# help2('b3','b4',-4)
# help2('b4','b5',2)
# help2('b4','c1',1)
# help2('b5','b4',1)
# help2('b5','c2',4)
# help2('c1','b5',2)
# help2('c1','c2',1)
# help2('c2','c3',-2)
# help2('c2','c4',3)
# help2('c3','b4',2)
# help2('c3','c5',1)
# help2('c4','c1',1)
# help2('c4','c5',2)
# help2('c5','a1',5)