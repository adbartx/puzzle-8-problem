import heapq
state = (6,8,0,3,4,7,1,2,5)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def get_neighbors(state):
    indx = state.index(0)
    row = indx // 3
    col = indx % 3

    moves = {
        "up": (row - 1, col),
        "down": (row + 1, col),
        "left": (row, col - 1),
        "right": (row, col + 1),
    }
    valid_moves = {}
    for direc, (r, c) in moves.items():
        if 0 <= r <=2 and 0 <= c <=2:
            new_indx = r * 3 + c
            new_state = list(state)
            new_state[indx], new_state[new_indx] = new_state[new_indx], new_state[indx]
            valid_moves[direc] = tuple(new_state)
    return valid_moves

def is_goal(state):
    return state == goal

def Mdist (state):
    total = 0
    for i, tile in enumerate(state):
        if tile == 0:
            continue
        curent_row = i // 3
        curent_col = i % 3

        goal_index = tile-1
        goal_row = goal_index // 3
        goal_col = goal_index % 3

        total += abs(curent_row - goal_row) + abs(curent_col - goal_col)
    return total

def a_star(start):
    fronta = []
    pocitadlo = 0
    heapq.heappush(fronta, (0, 0, pocitadlo, start, []))
    visited = set()
    while fronta:
        f,g, _, state, path = heapq.heappop(fronta)
        if state in visited:
            continue
        visited.add(state)
        if is_goal(state):
            return path
        for direc, new_state in get_neighbors(state).items():
            if new_state not in visited:
                pocitadlo += 1
                new_g = g+1
                new_h = Mdist(new_state)
                new_f = new_g + new_h
                heapq.heappush(fronta, (new_f, new_g, pocitadlo, new_state, path + [direc]))
    return None


print(a_star(state))




