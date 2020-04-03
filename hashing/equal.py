class Solution:
    def equal(self, arr):
        sum_dict = {}
        result = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                current_sum = arr[i] + arr[j]
                if current_sum in sum_dict:
                    a, b, c, d = sum_dict[current_sum] + (i, j)
                    # print(a, b, c, d)
                    if a < b and c < d and a < c and b != c and b != d:
                        result.append([a, b, c, d])
                else:
                    sum_dict[current_sum] = (i, j)

        # print(result)
        if len(result) == 0:
            return []
        else:
            return min(result)

print(Solution().equal([1, 1, 1, 1, 1])) # 0 1 2 3

