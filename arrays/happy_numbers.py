class Solution:
    def isHappy(self, n: int) -> bool:
        sum_so_far = set()
        sum = n
        while sum != 1:
            str_dig = str(sum)
            tmp_sum = 0
            for i in str_dig:
                tmp_sum+=int(i)**2
            if tmp_sum not in sum_so_far:
                sum_so_far.add(tmp_sum)
                sum = tmp_sum
            else:
                return False
        return True

if __name__ == '__main__':
    print(Solution().isHappy(5))
