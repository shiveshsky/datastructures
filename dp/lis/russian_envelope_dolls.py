class Envelops:
    def __init__(self, x, y):
        self.height = x
        self.width = y

    def __lt__(self, other):
        if self.height < other.height:
            return True
        # if height is same width sould be in decreasing order
        # beacause we do lis on the width and if smaller is before it will come
        # in increasing subsequence
        elif self.height == other.height:
            return other.width < self.width
        return False


class Solution:
    def maxEnvelopes(self, envelopes):
        envel_objs = [Envelops(envel[0], envel[1]) for envel in envelopes]
        envel_objs.sort()

        lis = [1]*(len(envelopes))

        for i in range(0, len(envelopes)):
            for j in range(i-1, -1, -1):
                if envel_objs[j].width < envel_objs[i].width:
                    lis[i] = max(lis[i], lis[j]+1)

        return max(lis)


if __name__ == '__main__':
    print(Solution().maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]))
