# 8-Puzzle Solver

A solver for the classic 8-puzzle (sliding tile) problem, written in Python using the
A* search algorithm with the Manhattan distance heuristic.

The 8-puzzle is a 3x3 grid holding tiles numbered 1 to 8 and one empty space. Tiles
adjacent to the empty space can slide into it. The goal is to reach the ordered
configuration in as few moves as possible.

```
start state          goal state
 6  8  _             1  2  3
 3  4  7      ->     4  5  6
 1  2  5             7  8  _
```

## Running it

Requires Python 3. There are no external dependencies — it uses only the standard
library `heapq` module.

```bash
python3 puzzle_8_problem.py
```

The script prints the sequence of moves that solves the puzzle, where each move
describes the direction the empty space travels:

```
['left', 'left', 'down', 'down', 'right', 'up', 'right', 'up', 'left', 'left',
 'down', 'down', 'right', 'up', 'left', 'down', 'right', 'right', 'up', 'up',
 'left', 'down', 'down', 'right']
```

For the default start state this is a 24-move solution, found in well under a second.

## How it works

The puzzle is represented as a flat 9-element tuple, where `0` stands for the empty
space. Tuples are used rather than lists because they are hashable, which allows
visited states to be stored in a set for constant-time lookup.

The search is a standard A*:

- **`get_neighbors(state)`** returns every state reachable in one move, by finding the
  empty space, converting its flat index to row and column coordinates, and swapping it
  with each in-bounds orthogonal neighbour.
- **`manhattan_distance(state)`** is the heuristic. For each tile it sums the vertical
  and horizontal distance from the tile's current position to its goal position. The
  empty space is excluded from the sum.
- **`a_star(start)`** expands states from a priority queue ordered by `f = g + h`, where
  `g` is the number of moves made so far and `h` is the Manhattan distance. A counter is
  pushed into each queue entry as a tie-breaker, so that entries with equal `f` and `g`
  never cause the heap to compare the state tuples themselves.

Because Manhattan distance never overestimates the true number of remaining moves, the
heuristic is admissible, and A* is therefore guaranteed to return an optimal
(shortest) solution.

## Notes and limitations

- The start state is hardcoded at the top of the file. To solve a different puzzle,
  edit the `state` tuple.
- Solvability is not checked. Half of all 8-puzzle configurations cannot reach the goal;
  for one of those the search explores every reachable state and then returns `None`.

## License

Released under the MIT License. See [LICENSE](LICENSE) for the full text.
