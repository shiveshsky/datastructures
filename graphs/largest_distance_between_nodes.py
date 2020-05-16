import heapq


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        children = {}
        root = None
        for i, x in enumerate(A):
            if x == -1:
                root = i
            else:
                if x in children:
                    children[x] += [i]
                else:
                    children[x] = [i]

        largest_dist = 0

        for k, v in self.dfs(root, children, 0, {}).items():
            largest_dist = max(self.largest_dist_from_paths(v), largest_dist)

        return largest_dist

    def largest_dist_from_paths(self, paths):
        paths += [0, 0]
        a, b = heapq.heappop(paths), heapq.heappop(paths)
        return -1 * (a + b)

    def dfs(self, root, children, path_len, paths):
        paths[root] = [0]

        if root not in children: return paths

        for child in children[root]:
            paths = self.dfs(child, children, path_len + 1, paths)
            heapq.heappush(paths[root], min(paths[child]) - 1)

        return paths


if __name__ == '__main__':
    print(Solution().solve([-1, 0, 0]))
