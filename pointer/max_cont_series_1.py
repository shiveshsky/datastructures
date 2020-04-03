class Solution:
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


print(Solution().maxone([1,1,0,1,1,0,0,1,1,1], 1))









# 1 1 0 1 1 0 0 1 1 1
# m = 1