:- dynamic(add_to_visited/2).
:- dynamic(branch_from/2).
:- dynamic(linking/2).
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
	heuristic_value(Source,Destination,Cost),
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

	a_star_recursive(NextVertex,Destination,RestFrontier,[Head|Tail]),
	branch_from(Head,Parent),
	%append to pathlist if not in pathlist
	(Head = Parent ->
		append([],[Head|Tail],Path)
		;
		append([Parent],[Head|Tail],Path), !
		).



add_to_frontier([],_,_,_,Frontier,Frontier).

add_to_frontier([Head|Tail],CurrentVertex,AccumulatedCost,Destination,Frontier,UpdatedFrontier):-

	% get g(n) of the current neighbor node from the source
	heuristic_value(CurrentVertex,Destination,CurrentHeuristic),
	NeighborAccumulatedCost is AccumulatedCost - CurrentHeuristic + 1,

	% get h(n) of the current neighbor node 
	heuristic_value(Head,Destination,HeadHeuristic),
 
	% check if the current neighbor is in the visited list
	(add_to_visited(Head,HeadFn)->

		Visited_AccumulatedCost is HeadFn - HeadHeuristic,

		% check if the current neighbor's g(n) < g(n) in the visited list or not
		(NeighborAccumulatedCost < Visited_AccumulatedCost ->

			%remove that neighbor from the visited list
			retract(add_to_visited(Head,HeadFn)),
			branch_from(Head,H_Parent),
			retract(branch_from(Head,H_Parent))
			;
			true
			)
		;
		true

	),

	% check if the current neighbor is in Frontier
	(delete_from_heap(Frontier,Another_Head_Fn,Head,DeletedHeap) ->

			FrontierAccumulatedCost is Another_Head_Fn - HeadHeuristic,

			% check if the current neighbor's g(n) < g(n) in Frontier
			(NeighborAccumulatedCost < FrontierAccumulatedCost ->
				branch_from(Head,Another_H_Parent),
				retract(branch_from(Head,Another_H_Parent))
				;
				true
				)

		;
		merge_heaps(heap(nil,0),Frontier,DeletedHeap)
		),


	% add to Frontier if the above conditions weren't satistied
	(add_to_visited(Head,HeadFn) ->
		merge_heaps(heap(nil,0),DeletedHeap,RestFrontier)
		;
		(delete_from_heap(DeletedHeap,Another_Head_Fn,Head,_) ->
			merge_heaps(heap(nil,0),DeletedHeap,RestFrontier)
			;
			CurrentNeigbor_TotalCost is NeighborAccumulatedCost + HeadHeuristic,
			add_to_heap(DeletedHeap,CurrentNeigbor_TotalCost,Head,RestFrontier),
			assertz(branch_from(Head,CurrentVertex))
			)
		),

	add_to_frontier(Tail,CurrentVertex,AccumulatedCost,Destination,RestFrontier,UpdatedFrontier).


heuristic_value(Vertex,Destination,Heuristic):-
	get_XY(Vertex,X1,Y1),
	get_XY(Destination,X2,Y2),
	abs(X2-X1,DX),
	abs(Y2-Y1,DY),
	Heuristic is (DX + DY) * 1.

all_neighbors(Vertex,Neighbors):-
	findall(Neighbor,linking(Vertex,Neighbor),Neighbors).
    

get_XY((X,Y), X,Y).


linking((0,0),(1, 0)).
linking((1,0),(1, 1)).
linking((1,0),(0, 0)).
linking((3,0),(3, 1)).
linking((3,0),(4, 0)).
linking((4,0),(4, 1)).
linking((4,0),(3, 0)).
linking((4,0),(5, 0)).
linking((5,0),(5, 1)).
linking((5,0),(4, 0)).
linking((5,0),(6, 0)).
linking((6,0),(5, 0)).
linking((6,0),(7, 0)).
linking((7,0),(7, 1)).
linking((7,0),(6, 0)).
linking((7,0),(8, 0)).
linking((8,0),(8, 1)).
linking((8,0),(7, 0)).
linking((8,0),(9, 0)).
linking((9,0),(8, 0)).

linking((0,1),(1, 1)).
linking((1,1),(1, 0)).
linking((1,1),(1, 2)).
linking((1,1),(0, 1)).
linking((1,1),(2, 1)).
linking((2,1),(1, 1)).
linking((2,1),(3, 1)).
linking((3,1),(3, 0)).
linking((3,1),(3, 2)).
linking((3,1),(2, 1)).
linking((3,1),(4, 1)).
linking((4,1),(4, 0)).
linking((4,1),(4, 2)).
linking((4,1),(3, 1)).
linking((4,1),(5, 1)).
linking((5,1),(5, 0)).
linking((5,1),(5, 2)).
linking((5,1),(4, 1)).
linking((7,1),(7, 0)).
linking((7,1),(8, 1)).
linking((8,1),(8, 0)).
linking((8,1),(8, 2)).
linking((8,1),(7, 1)).
linking((8,1),(9, 1)).
linking((9,1),(8, 1)).

linking((0,2),(1, 2)).
linking((1,2),(1, 1)).
linking((1,2),(1, 3)).
linking((1,2),(0, 2)).
linking((3,2),(3, 1)).
linking((3,2),(3, 3)).
linking((4,2),(4, 1)).
linking((5,2),(5, 1)).
linking((5,2),(5, 3)).
linking((8,2),(8, 1)).
linking((8,2),(8, 3)).
linking((8,2),(9, 2)).
linking((9,2),(8, 2)).

linking((0,3),(1, 3)).
linking((1,3),(1, 2)).
linking((1,3),(1, 4)).
linking((1,3),(0, 3)).
linking((1,3),(2, 3)).
linking((2,3),(1, 3)).
linking((2,3),(3, 3)).
linking((3,3),(3, 2)).
linking((3,3),(3, 4)).
linking((3,3),(2, 3)).
linking((5,3),(5, 2)).
linking((5,3),(5, 4)).
linking((5,3),(6, 3)).
linking((6,3),(5, 3)).
linking((6,3),(7, 3)).
linking((7,3),(7, 4)).
linking((7,3),(6, 3)).
linking((7,3),(8, 3)).
linking((8,3),(8, 2)).
linking((8,3),(8, 4)).
linking((8,3),(7, 3)).
linking((8,3),(9, 3)).
linking((9,3),(8, 3)).

linking((0,4),(1, 4)).
linking((1,4),(1, 3)).
linking((1,4),(1, 5)).
linking((1,4),(0, 4)).
linking((3,4),(3, 3)).
linking((3,4),(3, 5)).
linking((3,4),(4, 4)).
linking((4,4),(4, 5)).
linking((4,4),(3, 4)).
linking((4,4),(5, 4)).
linking((5,4),(5, 3)).
linking((5,4),(5, 5)).
linking((5,4),(4, 4)).
linking((7,4),(7, 3)).
linking((7,4),(7, 5)).
linking((7,4),(8, 4)).
linking((8,4),(8, 3)).
linking((8,4),(8, 5)).
linking((8,4),(7, 4)).

linking((0,5),(1, 5)).
linking((1,5),(1, 4)).
linking((1,5),(0, 5)).
linking((3,5),(3, 4)).
linking((4,5),(4, 4)).
linking((5,5),(5, 4)).
linking((5,5),(6, 5)).
linking((6,5),(5, 5)).
linking((6,5),(7, 5)).
linking((7,5),(7, 4)).
linking((7,5),(6, 5)).
linking((7,5),(8, 5)).
linking((8,5),(8, 4)).
linking((8,5),(7, 5)).
linking((8,5),(9, 5)).
linking((9,5),(8, 5)).

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