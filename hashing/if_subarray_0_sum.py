class Solution:
    def solve(self, A):
        my_map = {}
        running_sum = 0
        for i in A:
            running_sum += i
            if my_map.get(running_sum) is not None or running_sum == 0:
                return 1
            else:
                my_map[running_sum]=running_sum

        return -1


print(Solution().solve([5, 17, -22, 11]))

