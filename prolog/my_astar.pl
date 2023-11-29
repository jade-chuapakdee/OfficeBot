:- dynamic(add_to_visited/2).
:- dynamic(branch_from/2).
:- dynamic(connected_block/2).
:- dynamic(obstacle/1).
 


my_astar(Source, Destination, Path):-
	% check if either the source or the destination is the obstacle or not
    \+ obstacle(Source),
    \+ obstacle(Destination),

	% delete all related details before
	retractall(add_to_visited(_,_)),
    retractall(branch_from(_,_)),

	% create the starting point of the pathfinding
	assertz(branch_from(Source,Source)),
	get_heuristic(Source,Destination,Cost),
	assertz(add_to_visited(Source,Cost)),
	a_star_recursive(Source,Destination,heap(nil,0),Path).


a_star_recursive(Vertex,Destination,_,Path):-
	Vertex == Destination,
	append([],[Destination],Path),
	!.

a_star_recursive(Vertex,Destination,Frontier,Path):-

	% add the current accumulated cost to the visited list	
	add_to_visited(Vertex,AccumulatedCost),

	% get all neighbors of the current node
	all_neighbors(Vertex,NeighborList),

	% add all neighbors to the frontier 
	add_to_frontier(NeighborList,Vertex,AccumulatedCost,Destination,Frontier,UpdatedFrontier),

	% get the least-cost neighbor as f(n) = g(n) + h(n), from the heap(priority queue)
	get_from_heap(UpdatedFrontier,Fn,NextVertex,RestFrontier),

	% add that neighbor to the visited list
	assertz(add_to_visited(NextVertex,Fn)),

	a_star_recursive(NextVertex,Destination,RestFrontier,[H|T]),
	branch_from(H,Parent),
	%append to pathlist if not in pathlist
	(H = Parent ->
		append([],[H|T],Path)
		;
		append([Parent],[H|T],Path), !
		).



add_to_frontier([],_,_,_,Frontier,Frontier).

add_to_frontier([H|T],CurrentVertex,AccumulatedCost,Destination,Frontier,UpdatedFrontier):-
	% get g(n) of the current neighbor node from the source
	get_heuristic(CurrentVertex,Destination,CurrentHeuristic),
	NeighborAccumulatedCost is AccumulatedCost - CurrentHeuristic + 1,

	% get Heuristic of the current neighbor node 
	get_heuristic(H,Destination,HeadHeuristic),
 
	% Check current neighbor node if is in visited list
	(add_to_visited(H,HeadFn)->

		Visited_AccumulatedCost is HeadFn - HeadHeuristic,
		%check if current neighbor node g cost < already in visited list node g cost
		(NeighborAccumulatedCost < Visited_AccumulatedCost ->
			%remove the node from the visited list
			retract(add_to_visited(H,HeadFn)),
			branch_from(H,H_From),
			retract(branch_from(H,H_From))
			;
			true
			)
		;
		true

	),

	%Check current neighbor node if is in Frontier
	(delete_from_heap(Frontier,Another_Head_Fn,H,DeletedHeap) ->
			FrontierAccumulatedCost is Another_Head_Fn - HeadHeuristic,
			%check if current neighbor node g cost < already in frontier node g cost
			(NeighborAccumulatedCost < FrontierAccumulatedCost ->
				branch_from(H,Another_H_From),
				retract(branch_from(H,Another_H_From))
				;
				true
				)

		;
		merge_heaps(heap(nil,0),Frontier,DeletedHeap)
		),


	% add to Frontier if the above conditions weren't satistied
	(add_to_visited(H,HeadFn) ->
		merge_heaps(heap(nil,0),DeletedHeap,RestFrontier)
		;
		(delete_from_heap(DeletedHeap,Another_Head_Fn,H,_) ->
			merge_heaps(heap(nil,0),DeletedHeap,RestFrontier)
			;
			CurrentNeigbor_TotalCost is NeighborAccumulatedCost + HeadHeuristic,
			add_to_heap(DeletedHeap,CurrentNeigbor_TotalCost,H,RestFrontier),
			assertz(branch_from(H,CurrentVertex))
			)
		),

	add_to_frontier(T,CurrentVertex,AccumulatedCost,Destination,RestFrontier,UpdatedFrontier).


get_heuristic(Vertex,Destination,Heuristic):-
	get_coordinate(Vertex,X1,Y1),
	get_coordinate(Destination,X2,Y2),
	abs(X2-X1,DX),
	abs(Y2-Y1,DY),
	Heuristic is (DX + DY) * 1.

all_neighbors(Vertex,Neighbors):-
	findall(Neighbor,connected_block(Vertex,Neighbor),Neighbors).
    

get_coordinate((X,Y), X,Y).


connected_block((0,0),(0, 1)).
connected_block((0,0),(1, 0)).
connected_block((1,0),(1, 1)).
connected_block((1,0),(0, 0)).
connected_block((3,0),(3, 1)).
connected_block((3,0),(4, 0)).
connected_block((4,0),(4, 1)).
connected_block((4,0),(3, 0)).
connected_block((4,0),(5, 0)).
connected_block((5,0),(5, 1)).
connected_block((5,0),(4, 0)).
connected_block((5,0),(6, 0)).
connected_block((6,0),(5, 0)).
connected_block((6,0),(7, 0)).
connected_block((7,0),(7, 1)).
connected_block((7,0),(6, 0)).
connected_block((7,0),(8, 0)).
connected_block((8,0),(8, 1)).
connected_block((8,0),(7, 0)).
connected_block((8,0),(9, 0)).
connected_block((9,0),(9, 1)).
connected_block((9,0),(8, 0)).
connected_block((0,1),(0, 0)).
connected_block((0,1),(0, 2)).
connected_block((0,1),(1, 1)).
connected_block((1,1),(1, 0)).
connected_block((1,1),(1, 2)).
connected_block((1,1),(0, 1)).
connected_block((1,1),(2, 1)).
connected_block((2,1),(1, 1)).
connected_block((2,1),(3, 1)).
connected_block((3,1),(3, 0)).
connected_block((3,1),(3, 2)).
connected_block((3,1),(2, 1)).
connected_block((3,1),(4, 1)).
connected_block((4,1),(4, 0)).
connected_block((4,1),(4, 2)).
connected_block((4,1),(3, 1)).
connected_block((4,1),(5, 1)).
connected_block((5,1),(5, 0)).
connected_block((5,1),(5, 2)).
connected_block((5,1),(4, 1)).
connected_block((7,1),(7, 0)).
connected_block((7,1),(8, 1)).
connected_block((8,1),(8, 0)).
connected_block((8,1),(8, 2)).
connected_block((8,1),(7, 1)).
connected_block((8,1),(9, 1)).
connected_block((9,1),(9, 0)).
connected_block((9,1),(9, 2)).
connected_block((9,1),(8, 1)).
connected_block((0,2),(0, 1)).
connected_block((0,2),(0, 3)).
connected_block((0,2),(1, 2)).
connected_block((1,2),(1, 1)).
connected_block((1,2),(1, 3)).
connected_block((1,2),(0, 2)).
connected_block((3,2),(3, 1)).
connected_block((3,2),(3, 3)).
connected_block((3,2),(4, 2)).
connected_block((4,2),(4, 1)).
connected_block((4,2),(3, 2)).
connected_block((4,2),(5, 2)).
connected_block((5,2),(5, 1)).
connected_block((5,2),(5, 3)).
connected_block((5,2),(4, 2)).
connected_block((8,2),(8, 1)).
connected_block((8,2),(8, 3)).
connected_block((8,2),(9, 2)).
connected_block((9,2),(9, 1)).
connected_block((9,2),(9, 3)).
connected_block((9,2),(8, 2)).
connected_block((0,3),(0, 2)).
connected_block((0,3),(0, 4)).
connected_block((0,3),(1, 3)).
connected_block((1,3),(1, 2)).
connected_block((1,3),(1, 4)).
connected_block((1,3),(0, 3)).
connected_block((1,3),(2, 3)).
connected_block((2,3),(1, 3)).
connected_block((2,3),(3, 3)).
connected_block((3,3),(3, 2)).
connected_block((3,3),(3, 4)).
connected_block((3,3),(2, 3)).
connected_block((5,3),(5, 2)).
connected_block((5,3),(5, 4)).
connected_block((5,3),(6, 3)).
connected_block((6,3),(5, 3)).
connected_block((6,3),(7, 3)).
connected_block((7,3),(7, 4)).
connected_block((7,3),(6, 3)).
connected_block((7,3),(8, 3)).
connected_block((8,3),(8, 2)).
connected_block((8,3),(8, 4)).
connected_block((8,3),(7, 3)).
connected_block((8,3),(9, 3)).
connected_block((9,3),(9, 2)).
connected_block((9,3),(8, 3)).
connected_block((0,4),(0, 3)).
connected_block((0,4),(0, 5)).
connected_block((0,4),(1, 4)).
connected_block((1,4),(1, 3)).
connected_block((1,4),(1, 5)).
connected_block((1,4),(0, 4)).
connected_block((3,4),(3, 3)).
connected_block((3,4),(3, 5)).
connected_block((3,4),(4, 4)).
connected_block((4,4),(4, 5)).
connected_block((4,4),(3, 4)).
connected_block((4,4),(5, 4)).
connected_block((5,4),(5, 3)).
connected_block((5,4),(5, 5)).
connected_block((5,4),(4, 4)).
connected_block((7,4),(7, 3)).
connected_block((7,4),(7, 5)).
connected_block((7,4),(8, 4)).
connected_block((8,4),(8, 3)).
connected_block((8,4),(8, 5)).
connected_block((8,4),(7, 4)).
connected_block((0,5),(0, 4)).
connected_block((0,5),(1, 5)).
connected_block((1,5),(1, 4)).
connected_block((1,5),(0, 5)).
connected_block((3,5),(3, 4)).
connected_block((3,5),(4, 5)).
connected_block((4,5),(4, 4)).
connected_block((4,5),(3, 5)).
connected_block((4,5),(5, 5)).
connected_block((5,5),(5, 4)).
connected_block((5,5),(4, 5)).
connected_block((5,5),(6, 5)).
connected_block((6,5),(5, 5)).
connected_block((6,5),(7, 5)).
connected_block((7,5),(7, 4)).
connected_block((7,5),(6, 5)).
connected_block((7,5),(8, 5)).
connected_block((8,5),(8, 4)).
connected_block((8,5),(7, 5)).
connected_block((8,5),(9, 5)).
connected_block((9,5),(8, 5)).
obstacle((2,0)).
obstacle((6,1)).
obstacle((2,2)).
obstacle((6,2)).
obstacle((7,2)).
obstacle((4,3)).
obstacle((2,4)).
obstacle((6,4)).
obstacle((9,4)).
obstacle((2,5)).