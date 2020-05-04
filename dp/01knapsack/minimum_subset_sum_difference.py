import math


class MinSubsetSumDiff:
    def min_subset(self, arr, findsum):
        dp = [[0 for _ in range(0, findsum+1)] for i in range(0, len(arr)+1)]

        for i in range(0, len(arr)+1):
            dp[i][0] = True
        for j in range(1, findsum+1):
            dp[0][j] = False

        for i in range(1, len(arr)+1):
            for j in range(1, findsum+1):
                if arr[i-1]<=j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1]

    def solve(self, arr):
        # it will be from 0 to sum(arr)
        range_of_possible_subsets = sum(arr)
        dp_arr = self.min_subset(arr, range_of_possible_subsets)
        '''
                if subset sum is s1 and s2 then we need to minimize 
                s1-s2
                and you know that s1 + s2 = sumarr
                so s1 -(sumarr-s1)
                we have to minimize sumarr - 2s1 
        '''
        # possible_sums = [i for i in range(0, len(dp_arr)) if dp_arr[i]]
        minsubsetddff = math.inf
        for i in range(0, len(dp_arr)//2):
            if dp_arr[i] == True:
                minsubsetddff = min(minsubsetddff, range_of_possible_subsets- 2*i)
        return minsubsetddff


if __name__ == '__main__':
    print(MinSubsetSumDiff().solve([1, 6, 11, 5]))
