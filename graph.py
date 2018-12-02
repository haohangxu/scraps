def find_components(graph):
    n = len(graph[0])
    
    friend_groups = 0
    groupings = [0] * n
                
        
    for i in range(0, n):
        if groupings[i] == 0:
            friend_groups += 1
            groupings[i] = friend_groups
            
        for j in range(i, n):
            if graph[i][j]:
                groupings[j] = friend_groups

    return friend_groups

    
graph = [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]]
print(find_components(graph))

                
