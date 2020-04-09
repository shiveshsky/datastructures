class Solution:
    def countElements(self, arr) -> int:
        set_arr = set(arr)
        count = 0
        for i in set_arr:
            if i+1 in set_arr:
                count+=1
        return count