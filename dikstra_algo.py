graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}
processes = []
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processes:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def dikstra(costs):
    ### while we have nodes to process
    ### grab the node that is closest to the start
    ### update costs for its neigbors
    ### if any of the nighbores' costs were updated , update the parents too
    ### mark this node processed

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processes.append(node)
        node = find_lowest_cost_node(costs)


if __name__ == "__main__":
    print(graph["start"].keys())
    infinity = float("inf")
    costs = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity
    dikstra(costs)
    print("done")
