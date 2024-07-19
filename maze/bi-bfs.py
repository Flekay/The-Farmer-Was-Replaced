def maze_bi_bfs(maze,root):
    parents1 = {}
    parents2 = {}
    explored1 = {root}
    explored2 = {maze["Treasure"]}
    q1 = [root]
    q2 = [maze["Treasure"]]

    q1_idx = 0
    q2_idx = 0

    q1append = q1.append
    q2append = q2.append

    explored1add = explored1.add
    explored2add = explored2.add

    while True:
        from_start = q1[q1_idx]
        q1_idx += 1

        from_end = q2[q2_idx]
        q2_idx += 1


        if from_start in explored2:
            from_end = from_start
            break
        if from_end in explored1:
            from_start = from_end
            break

        for dir in maze[from_start]:
            neighbor = maze[from_start][dir]
            if neighbor not in explored1:
                explored1add(neighbor)
                parents1[neighbor] = dir,from_start
                q1append(neighbor)


        for dir in maze[from_end]:
            neighbor = maze[from_end][dir]
            if neighbor not in explored2:
                explored2add(neighbor)
                parents2[neighbor] = dir,from_end
                q2append(neighbor)


    p1 = []
    p1append = p1.append
    current = from_start
    while current in parents1:
        dir,parent = parents1[current]
        p1append(dir)
        current = parent

    p2 = []
    p2append = p2.append
    current = from_end
    while current in parents2:
        dir,parent = parents2[current]
        p2append(opposite(dir))
        current = parent

    return p1,p2
