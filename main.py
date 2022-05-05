import heapq


def main():
	graph = {
		"a": { "w": 14, "x": 7, "y": 9 },
		"b": { "w": 9, "z": 6 },
		"w": { "a": 14, "b": 9, "y": 2 },
		"x": { "a": 7, "y": 10, "z": 15 },
		"y": { "a": 9, "w": 2, "x": 10, "z": 11 },
		"z": { "b": 6, "x": 15, "y": 11 }
	}

	print(dijkstra(graph, "a", "a")) # (0, ["a"])
	print(dijkstra(graph, "a", "b")) # (20, ["a", "y", "w", "b"])


def dijkstra(graph, start, end):
	distances = { key: float("inf") for key in graph.keys() }
	distances[start] = 0

	visited = set()
	predecessors = {}

	node = start

	while node != end:
		visited.add(node)

		for neighbor in graph[node].keys():
			if neighbor not in visited:
				tentative_distance = distances[node] + graph[node][neighbor]
				recorded_distance = distances[neighbor]

				if tentative_distance < recorded_distance:
					distances[neighbor] = tentative_distance
					predecessors[neighbor] = node

		node = get_closest_node(graph, visited, distances)

	return distances[node], get_path(end, predecessors)


def get_closest_node(graph, visited, distances):
	unvisited = []

	for k in graph:
		if k not in visited:
			unvisited.append((distances[k], k))

	heapq.heapify(unvisited)

	_, closest_node = heapq.heappop(unvisited)

	return closest_node


def get_path(end, predecessors):
	path = []

	while True:
		path.append(end)

		if end not in predecessors:
			return list(reversed(path))

		end = predecessors[end]


if __name__ == "__main__":
	main()
