import heapq

import math


class Node:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):

        adg = [list() for _ in range(A)]
        for row in B:
            adg[row[0]].append(Node(row[1], row[2]))
            adg[row[1]].append(Node(row[0], row[2]))
        return list(map(lambda x: -1 if x == math.inf else x, self.dijkastra(adg, C, A)))

    def dijkastra(self, adg, source, vertices):
        dist = [math.inf] * vertices
        priorityqueue = []
        heapq.heapify(priorityqueue)
        heapq.heappush(priorityqueue, Node(source, 0))
        visited = set()
        dist[source] = 0
        while len(priorityqueue) > 0:
            ele = heapq.heappop(priorityqueue).node
            visited.add(ele)
            self.explore_neighbors(ele, adg, visited, dist, priorityqueue)
        return dist

    def explore_neighbors(self, ele, adg, visited, distance, priorityqueue):

        for child in adg[ele]:
            if child.node not in visited:
                edge_distance = child.cost
                new_distance = distance[ele] + edge_distance

                if new_distance < distance[child.node]:
                    distance[child.node] = new_distance
                heapq.heappush(priorityqueue, Node(child.node, distance[child.node]))


# from queue import PriorityQueue
# from collections import defaultdict
# class Solution:
#     # @param A : integer
#     # @param B : list of list of integers
#     # @param C : integer
#     # @return a list of integers
#     def solve(self, A, B, C):
#         graph = defaultdict(list)
#         vis = [False]*A
#         dist = [float('inf')]*A
#         pq = PriorityQueue()
#         dist[C] = 0
#         for i in range(len(B)):
#             #Adding node and weight
#             graph[B[i][0]].append((B[i][1], B[i][2]))
#             graph[B[i][1]].append((B[i][0], B[i][2]))
#         pq.put((0, C))
#
#         while not pq.empty():
#             #Get the top item
#             w, v = pq.get()
#
#             #Check if node is already visited
#             if vis[v] == True:
#                 continue
#             #If not mark it visited
#             vis[v] = True
#             for i in range(len(graph[v])):
#                 node, weight = graph[v][i]
#                 if dist[v]+weight < dist[node]:
#                     dist[node] = dist[v]+weight
#                     pq.put((dist[node], node))
#
#
#         for d in range(A):
#             if dist[d] == float('inf'):
#                 dist[d] = -1
#
#         return dist

if __name__ == '__main__':
    print(Solution().solve(6, [
        [0, 4, 9],
        [3, 4, 6],
        [1, 2, 1],
        [2, 5, 1],
        [2, 4, 5],
        [0, 3, 7],
        [0, 1, 1],
        [4, 5, 7],
        [0, 5, 1]
    ], 2))
