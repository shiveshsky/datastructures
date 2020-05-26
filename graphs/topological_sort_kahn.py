import heapq


class Solution:
    def solve(self, A, B):
        adg = [list() for i in range(A + 1)]
        for row in B:
            adg[row[0]].append(row[1])
        return self.topological_sort(A, adg)

    def topological_sort(self, A, adg):
        indegree = [0] * (A + 1)

        for i in range(len(adg)):
            for j in adg[i]:
                indegree[j] += 1
        queue = []
        heapq.heapify(queue)
        for i in range(1, A + 1):
            if indegree[i] == 0:
                heapq.heappush(queue, i)

        cnt = 0

        top_order = []
        while queue:

            # Extract front of queue (or perform dequeue)
            # and add it to topological order
            u = heapq.heappop(queue)
            top_order.append(u)

            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in adg[u]:
                indegree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if indegree[i] == 0:
                    heapq.heappush(queue, i)

            cnt += 1
        if cnt != A:
            return []
        return top_order


if __name__ == '__main__':
    print(Solution().solve(8, [[1, 4], [1, 2], [4, 2], [4, 3], [3, 2], [5, 2], [3, 5], [8, 2], [8, 6]]))
