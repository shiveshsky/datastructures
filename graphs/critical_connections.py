from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if not connections: return None
        graph = defaultdict(list)
        distances = {}
        visited = set([0])
        critical_connections = list()

        def dfs(node, parent, distance):
            cur_distance = distance
            distances[node] = distance
            lowest_reach = distance

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    lowest = dfs(neighbor, node, distance + 1)
                    if lowest > cur_distance:
                        critical_connections.append((node, neighbor))

                    lowest_reach = min(lowest_reach, lowest)

                elif neighbor != parent:
                    lowest_reach = min(lowest_reach, distances[neighbor])

            return lowest_reach

        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        dfs(0, None, 1)
        return critical_connections


if __name__ == '__main__':
    print(Solution().criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]]))
