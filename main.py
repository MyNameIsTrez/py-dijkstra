import heapq


def main():
	showcase_cyclic()
	showcase_acyclic()


def showcase_cyclic():
	cyclic_graph = {
		"a": { "w": 14, "x": 7, "y": 9 },
		"b": { "w": 9, "z": 6 },
		"w": { "a": 14, "b": 9, "y": 2 },
		"x": { "a": 7, "y": 10, "z": 15 },
		"y": { "a": 9, "w": 2, "x": 10, "z": 11 },
		"z": { "b": 6, "x": 15, "y": 11 }
	}

	dijkstra = Dijkstra(cyclic_graph)

	print(dijkstra.run("a", "a")) # ['a']
	print(dijkstra.run("a", "b")) # ['a', 'y', 'w', 'b']


def showcase_acyclic():
	acyclic_graph = {
		"a": { "b": 1, "c": 2 },
		"b": { "d": 3 },
		"c": { "d": 4 },
		"d": { "e": 5 },
		"e": {}
	}

	dijkstra = Dijkstra(acyclic_graph)

	print(dijkstra.run("a", "a")) # ['a']
	print(dijkstra.run("a", "e")) # ['a', 'b', 'd', 'e']


class Dijkstra:
	def __init__(self, graph):
		self.graph = graph


	def run(self, start, end):
		distances = { key: float("inf") for key in self.graph.keys() }
		distances[start] = 0

		unvisited = { key for key in self.graph.keys() }

		parents = {}

		node = start

		while node != end:
			unvisited.remove(node)

			for neighbor in self.graph[node].keys():
				if neighbor in unvisited:
					tentative_distance = distances[node] + self.graph[node][neighbor]
					recorded_distance = distances[neighbor]

					if tentative_distance < recorded_distance:
						distances[neighbor] = tentative_distance
						parents[neighbor] = node

			node = self.get_closest_node(unvisited, distances)

		return self.get_path(end, parents)


	def get_closest_node(self, unvisited, distances):
		unvisited_min_heap = [(distances[node], node) for node in unvisited]

		# Great explanation of heapify: https://stackoverflow.com/a/61446534/13279557
		heapq.heapify(unvisited_min_heap)

		_, closest_node = heapq.heappop(unvisited_min_heap)

		return closest_node


	def get_path(self, end, parents):
		path = []

		while True:
			path.append(end)

			if end not in parents:
				return list(reversed(path))

			end = parents[end]


if __name__ == "__main__":
	main()
