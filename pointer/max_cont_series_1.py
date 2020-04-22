from heapq import heapify, heappush, heappop


class Solution1:
    def maxone(self, A, B):
        window_l = 0
        window_r = 0
        max_window_size = 0
        zero_count = 0
        ans = []
        i=0
        while window_r<len(A):
            if zero_count<=B:
                if A[window_r] == 0:
                    zero_count+=1
                window_r+=1
            if zero_count>B:
                if A[window_l]==0:
                    zero_count-=1
                window_l+=1
            if window_r-window_l > max_window_size and zero_count<=B:
                max_window_size = window_r-window_l
                ans = [i for i in range(window_l, window_r)]
        return ans

class Solution2:
    def solve(self, A):
        A.sort()
        prefix_sum = [0]*(len(A))
        mod = 10 **9 + 7
        for i, val in enumerate(A):
            if i==0:
                prefix_sum[i]=val
            else:
                prefix_sum[i]=(prefix_sum[i-1]+val)%mod
        ans = 0
        for i in range(0, len(prefix_sum)):
            ans = prefix_sum[i]%mod + ans%mod
        return ans%mod


from collections import defaultdict


class Solution3:
    # @param A : integer
    # @param B : integer
    # @param C : list of list of integers
    # @param D : integer
    # @param E : list of list of integers
    # @return an integer
    def solve(self, A, B, C, D, E):
        shop_item = defaultdict(set)
        for row in C:
            shop_item[row[0]].add(row[1])
        item_shop = defaultdict(set)
        for row in C:
            item_shop[row[1]].add(row[0])
        items = set()
        for row in E:
            items.add(row[1])
        found = set()
        cnt = 0
        for item in items:
            if item not in found:
                if item in item_shop:
                    maxfound = -1
                    maxfounded = set()
                    for shop in item_shop[item]:
                        newlyfounded = set()
                        for newitem in shop_item[shop]:
                            if newitem in items and newitem not in found:
                                newlyfounded.add(newitem)
                        if maxfound < len(newlyfounded):
                            maxfound = len(newlyfounded)
                            maxfounded = newlyfounded
                    found = found.union(maxfounded)
                    cnt += 1

                else:
                    return -1
        return cnt


if __name__ == '__main__':
    print(Solution3().solve(12, 5, [[7,1],[2,3],[3,2],[8,4],[3,3],[8,2],[4,2],[8,5],[10,4],[2,4],[2,1],[7,4], [12,3],[4,4],[12,5],[2,2],[11,1],[4,5],[3,5],[10,5],[10,2],[5,3],[3,1],[1,1],[7,3]], 6, [[6,1],[5,4],[1,4],[3,4],[3,2],[4,4]]))
    # print(Solution3().solve(11,6,[[6,3],[2,6],[3,4],[1,5],[8,1],[8,5],[2,5],[10,2],[11,4],[10,4],[11,6],[1,4],[9,1],[10,3],[8,6],[9,2],[1,2],[6,2],[1,3],[11,5],[10,1],[6,6],[9,3],[6,1]], 4, [[3,1],[4,5],[3,2],[4,1], [2,2],[1,3]]))










# 1 1 0 1 1 0 0 1 1 1
# m = 1