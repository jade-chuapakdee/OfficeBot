% Predicate to query 
% ex. bellman_ford(1, a1, c2, Cost, Path) return the shortest path from a1 to c2 of graph 1

bellman_ford(ID, Source, Destination, Cost, Path) :-
	vertex(ID, Source),
	vertex(ID, Destination),
	retractall(shortest(ID, _)),
	set_shortest(ID, null->Source/0),
	edges(ID, Edges),
	length(Edges, M),
	loop(ID, M),
	summarize_path(ID, Source, Destination, Cost, Path),
	retractall(shortest(ID, _)),
	!.

visited(ID, Vertex) :-
	shortest(ID, _->Vertex/_).

loop(_, 0) :- !.
loop(ID, M) :-
	M_NEXT is M - 1,
	search_vertex(ID),
	loop(ID, M_NEXT).

search_vertex(ID) :-
	vertices(ID, Vertices),
	search_vertex(ID, Vertices).

search_vertex(_, []) :- !.
search_vertex(ID, [Vertex|Tail]) :-
	visited(ID, Vertex),
	update(ID, Vertex),
	search_vertex(ID, Tail),
	!.
search_vertex(ID, [_|Tail]) :-
	search_vertex(ID, Tail).

set_shortest(ID, From->To/Cost) :-
	retract(shortest(ID, From->To/_)),
	asserta(shortest(ID, From->To/Cost)),
	!.
set_shortest(ID, From->To/Cost) :-
	asserta(shortest(ID, From->To/Cost)).

update(ID, Vertex) :-
	findall(Vertex->To/Cost,
	(
		edges(ID, E),
		member(Vertex->To/Cost, E)
	), Adjacent),
	update_path(ID, Vertex, Adjacent).

update_path(_, _, []) :- !.
update_path(ID, From, [From->To/Cost|Tail]) :-
	shortest(ID, _->To/T_COST),
	shortest(ID, _->From/F_COST),
	P_COST is F_COST + Cost,
	replace_record(ID, From->To, T_COST, P_COST),
	update_path(ID, From, Tail),
	!.
update_path(ID, From, [From->To/Cost|Tail]) :-
	shortest(ID, _->From/F_COST),
	P_COST is F_COST + Cost,
	set_shortest(ID, From->To/P_COST),
	update_path(ID, From, Tail).

replace_record(_, _, Old_cost, New_cost) :-
	Old_cost =< New_cost,
	!.
replace_record(ID, From->To, Old_cost, New_cost) :-
	New_cost < Old_cost,
	set_shortest(ID, From->To/New_cost).

summarize_path(ID, Source, Destination, Cost, Path) :-
	shortest(ID, _->Destination/Cost),
	join_path(ID, Source, [Destination], Path).

join_path(_, Source, [Source|RAcc], [Source|RAcc]) :- !.
join_path(ID, Source, Acc, Path) :-
	[To|_] = Acc,
	shortest(ID, From->To/_),
	join_path(ID, Source, [From|Acc], Path).


graph(
	1,
	[a1,a2,a3,a4,a5,
    b1,b2,b3,b4,b5,
    c1,c2,c3,c4,c5],
	[   
	a1->a2/2,
	a1->a3/4,
	a2->a4/(-1),
	a3->a4/3,
	a4->a2/3,
	a4->a5/2,
	a5->a3/(-1),
	a5->b1/1,
	a5->b2/(-2),
	b1->a5/1,
	b1->b3/3,
	b2->b1/3,
	b2->b3/5,
	b3->b4/(-4),
	b4->b5/2,
	b4->c1/1,
	b5->b4/1,
	b5->c2/4,
	c1->b5/2,
	c1->c2/1,
	c2->c3/(-2),
	c2->c4/3,
	c3->b4/2,
	c3->c5/1,
	c4->c1/1,
	c4->c5/2,
	c5->a1/5
			]
 ).


% Set up the graph
vertices(ID, Vertices) :-
	graph(ID, Vertices, _).

edges(ID, Edges) :-
	graph(ID, _, Edges).

vertex(ID, Vertex) :-
	vertices(ID, Vertices),
	member(Vertex, Vertices).