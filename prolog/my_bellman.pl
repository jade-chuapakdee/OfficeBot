parent(john, jim).
parent(john, ann).
parent(jane, jim).
parent(jane, ann).

male(john).
female(jane).
%:-op(300, xfy, ->).
%:-op(300, xfx, /).

g(
	3,
	[a,b,c,d,e,f,g,h],
	[a->e/1, e->f/2, f->g/1, g->h/2,
	a->b/2, b->c/1, c->d/2, d->h/1]
 ).

 g(
	4,
	[a1,b,c,d,e,f,g],
	[a1->b/6, a1->c/5, a1->d/5,
         b->e/(-1),
         c->b/(-2), c->e/1,
         d->c/(-2), d->f/(-1),
         e->g/3,
         f->g/3]
 ).
g(6,
    [az,bz,cz,ez],

    [
	az->bz/4,
	az->cz/(-3),
	cz->az/(4),
	az->ez/7,
	bz->ez/2,
	bz->cz/(-2)
			]
).
  g(
	5,

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

g_vertices(Gid, Vertices) :-
	g(Gid, Vertices, _).

g_edges(Gid, Edges) :-
	g(Gid, _, Edges).

g_vertex(Gid, Vertex) :-
	g_vertices(Gid, Vertices),
	member(Vertex, Vertices).

%% Bellman-Ford

% bf(+Gid, +Start, +Stop, ?Cost, -Path) (+Cost does not make sense, though)
bf(Gid, Start, Stop, Cost, Path) :-
	g_vertex(Gid, Start),
	g_vertex(Gid, Stop),
	retractall(bf_shortest(Gid, _)),
	bf_set_shortest(Gid, nill->Start/0),
	g_edges(Gid, Edges),
	length(Edges, M),
	bf_loop(Gid, M),
	bf_path_summary(Gid, Start, Stop, Cost, Path),
	retractall(bf_shortest(Gid, _)),
	!.

bf_set_shortest(Gid, From->To/Cost) :-
	retract(bf_shortest(Gid, From->To/_)),
	asserta(bf_shortest(Gid, From->To/Cost)),
	!.
bf_set_shortest(Gid, From->To/Cost) :-
	asserta(bf_shortest(Gid, From->To/Cost)).

bf_visited(Gid, Vertex) :-
	bf_shortest(Gid, _->Vertex/_).

bf_loop(_, 0) :- !.
bf_loop(Gid, M) :-
	Mnext is M - 1,
	bf_explore(Gid),
	bf_loop(Gid, Mnext).

bf_explore(Gid) :-
	g_vertices(Gid, Vertices),
	bf_explore(Gid, Vertices).

bf_explore(_, []) :- !.
bf_explore(Gid, [Vertex|Rest]) :-
	bf_visited(Gid, Vertex),
	bf_update(Gid, Vertex),
	bf_explore(Gid, Rest),
	!.
bf_explore(Gid, [_|Rest]) :-
	bf_explore(Gid, Rest).

bf_update(Gid, Vertex) :-
	findall(Vertex->To/Cost,
	(
		g_edges(Gid, E),
		member(Vertex->To/Cost, E)
	), Adjacent),
	bf_update_path(Gid, Vertex, Adjacent).

bf_update_path(_, _, []) :- !.
bf_update_path(Gid, From, [From->To/Cost|Rest]) :-
	bf_shortest(Gid, _->To/TCost),
	bf_shortest(Gid, _->From/FCost),
	PCost is FCost + Cost,
	bf_update_record(Gid, From->To, TCost, PCost),
	bf_update_path(Gid, From, Rest),
	!.
bf_update_path(Gid, From, [From->To/Cost|Rest]) :-
	bf_shortest(Gid, _->From/FCost),
	PCost is FCost + Cost,
	bf_set_shortest(Gid, From->To/PCost),
	bf_update_path(Gid, From, Rest).

bf_update_record(_, _, OldCost, NewCost) :-
	OldCost =< NewCost,
	!.
bf_update_record(Gid, From->To, OldCost, NewCost) :-
	NewCost < OldCost,
	bf_set_shortest(Gid, From->To/NewCost).

bf_path_summary(Gid, Start, Stop, Cost, Path) :-
	bf_shortest(Gid, _->Stop/Cost),
	bf_assemble_path(Gid, Start, [Stop], Path).

bf_assemble_path(_, Start, [Start|RAcc], [Start|RAcc]) :- !.
bf_assemble_path(Gid, Start, Acc, Path) :-
	[To|_] = Acc,
	bf_shortest(Gid, From->To/_),
	bf_assemble_path(Gid, Start, [From|Acc], Path).