import queue

def get_neighbours(m, n, x):
    i = x / m
    j = x % m

    neigh_list1 = [x - m - 1, x - m, x - m + 1,
                  x - 1, x + 1,
                  x + m - 1, x + m, x + m + 1]
    neigh_mask1 = [i > 0 and j > 0, i > 0, i > 0 and j < m - 1,
                  j > 0, j < m - 1,
                  i < n - 1 and j > 0, i < n - 1, i < n - 1 and j < m - 1]

    neigh_list2 = [x - m,
                   x - 1, x + 1,
                   x + m]
    neigh_mask2 = [i > 0,
                   j > 0, j < m - 1,
                   i < n - 1]

    neigh_list = neigh_list1
    neigh_mask = neigh_mask1
    neighs = []
    for i in range(len(neigh_list)):
        if neigh_mask[i]:
            neighs.append(neigh_list[i])
    return neighs

# 0. INITIALIZATION
values = [0, 0, 0, 0, 0, 0,
		  1, 2, 1, 2, 0, 0,
		  0, 1, 2, 0, 0, 0,
		  1, 0, 1, 0, 0, 3,
		  0, 0, 0, 0, 0, 3]
m = 6
n = 5
visited = set()
current = []
q = queue.Queue()
for i in range(m*n):
    q.put(i)
figures_list = []
is_compound = True
is_compound = False

# 1. ITERATING LIST OF NOT VISITED CELLS TO CHECK IF THERE IS A FIGURE
while not q.empty():
    x = q.get()
    if x in visited or values[x] == 0:
        continue
    visited.add(x)

    # 2. START OF FIGURE SEARCH
    figure = [x]
    col = values[x]
    frontier = queue.Queue()
    neighs = get_neighbours(m, n, x)

    for ngh in neighs:
        if ngh in visited or values[ngh] == 0:
            continue
        if values[ngh] != col and not is_compound:
            continue
        frontier.put(ngh)

    while not frontier.empty():
        cell = frontier.get()
        if cell in visited or values[cell] == 0:
            continue
        if values[cell] != col and not is_compound:
            continue
        figure.append(cell)
        visited.add(cell)

        # 3. NEXT FIGURE'S CELL IS FOUND
        new_neighs = get_neighbours(m, n, cell)
        for ngh in new_neighs:
            if ngh in visited:
                continue
            if values[ngh] != col and not is_compound:
                continue
            frontier.put(ngh)

    figures_list.append((col, figure))

print(figures_list)