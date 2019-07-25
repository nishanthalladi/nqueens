import sys
import time
from collections import deque as dq
import random


def goal_test(state):
    return state.count(-1) == 0


def get_next_unassigned_var(state):
    # return state.index(-1)
    x = random.randint(0, len(state)-1)
    while state[x] != -1:
        x = random.randint(0, len(state)-1)
    return x


def diagonal_free(state, var, tent):
    for index, val_to_test in enumerate(state):
        dist = abs(var-index)
        if val_to_test == -1:
            continue
        if tent == val_to_test + dist or tent == val_to_test - dist:
            return False
    return True


def get_sorted_values(state, var):
    vars_ = []
    for i in range(len(state)):
        if diagonal_free(state, var, i) and i not in state:
            vars_.append(i)
    # for i in range(get_next_unassigned_var(state), len(state)):
    #     if diagonal_free(state, var, i) and i not in state:
    #         vars_.append(i)
    # for i in range(get_next_unassigned_var(state)):
    #     if diagonal_free(state, var, i) and i not in state:
    #         vars_.append(i)
    return vars_


def csp(state):
    if goal_test(state):
        return state
    var = get_next_unassigned_var(state)
    for val in get_sorted_values(state, var):
        new_list = state.copy()
        new_list[var] = val
        result = csp(new_list)
        if result is not None:
            return result
    return None


def bfs(state):
    fringe = dq()
    fringe.append(state)
    while fringe:
        curr = fringe.popleft()
        if goal_test(curr):
            return curr
        var = get_next_unassigned_var(curr)
        for val in get_sorted_values(curr, var):
            new_list = curr.copy()
            new_list[var] = val
            fringe.append(new_list)


def dfs(state):
    fringe = [state]
    while fringe:
        curr = fringe.pop()
        if goal_test(curr):
            return curr
        var = get_next_unassigned_var(curr)
        for val in get_sorted_values(curr, var):
            new_list = curr.copy()
            new_list[var] = val
            fringe.append(new_list)


def iterative(state):
    n = len(state)
    if n % 2 == 0:
        if (n - 2) % 6 == 0:
            for row in range(1, n // 2 + 1):
                state[row - 1] = (2 * row + n // 2 - 3) % n + 1
            for row in range(n // 2 + 1, n + 1):
                state[row - 1] = n - (2 * (n - row + 1) + n // 2 - 3) % n

        else:
            for row in range(1, n // 2 + 1):
                state[row - 1] = 2 * row
            for row in range(n // 2 + 1, n + 1):
                state[row - 1] = 2 * row - n - 1
    else:
        state[n - 1] = n - 1
        n = n - 1
        for row in range(1, n // 2 + 1):
            state[row - 1] = 2 * row
        for row in range(n // 2 + 1, n + 1):
            state[row - 1] = 2 * row - n - 1
    for i in range(n):
        state[i] = state[i] - 1
    return state


def initial_state(n):
    return [-1 for i in range(n)]


def test_code():
    print(csp(initial_state(int(sys.argv[1]))))
    solve_time = 0
    size = 8
    while solve_time < 2:
        start = time.perf_counter()
        state = csp(initial_state(size))
        end = time.perf_counter()
        size += 1
        solve_time = end - start
    print("For size %s, the time was %s." % (size, solve_time))


sys.setrecursionlimit(50000)
# max_val = 100
# for count in range(8, max_val + 1):
#     t = time.process_time()
#     sol = csp(initial_state(count))
#     t = time.process_time() - t
#     print(count, t)

# t = time.process_time()
# sol = iterative(initial_state(10000000))
# t = time.process_time() - t
# print(t)

test_code()
