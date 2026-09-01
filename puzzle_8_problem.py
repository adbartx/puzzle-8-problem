import heapq
state = (6,8,0,3,4,7,1,2,5)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def get_neighbors(state):
    index = state.index(0)
    row = index // 3
    col = index % 3

    moves = {
        "up": (row - 1, col),
        "down": (row + 1, col),
        "left": (row, col - 1),
        "right": (row, col + 1),
    }
    valid_moves = {}
    for direction, (r, c) in moves.items():
        if 0 <= r <=2 and 0 <= c <=2:
            new_index = r * 3 + c
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            valid_moves[direction] = tuple(new_state)
    return valid_moves

def is_goal(state):
    return state == goal

def manhattan_distance(state):
    total = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        current_row = i // 3
        current_col = i % 3

        goal_index = tile-1
        goal_row = goal_index // 3
        goal_col = goal_index % 3

        total += abs(current_row - goal_row) + abs(current_col - goal_col)
    return total

def a_star(start):
    frontier = []
    counter = 0
    heapq.heappush(frontier, (0, 0, counter, start, []))
    visited = set()
    while frontier:
        f,g, _, state, path = heapq.heappop(frontier)
        if state in visited:
            continue
        visited.add(state)
        if is_goal(state):
            return path
        for direction, new_state in get_neighbors(state).items():
            if new_state not in visited:
                counter += 1
                new_g = g+1
                new_h = manhattan_distance(new_state)
                new_f = new_g + new_h
                heapq.heappush(frontier, (new_f, new_g, counter, new_state, path + [direction]))
    return None


print(a_star(state))




