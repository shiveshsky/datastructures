class Solution:
    def solve(self, A):
        party_combo = [0]*(A+1)
        party_combo[1] = 1
        party_combo[0] = 1
        for i in range(2, A + 1):
            # TODO here i-1 is number of ways he can choose partner from i-1 members
            # and then he forms pairs partycombo(i-2)
            party_combo[i] = party_combo[i - 1] % 10003 + ((i - 1) * party_combo[i - 2]) % 10003
        return party_combo[-1] % 10003


if __name__ == '__main__':
    print(Solution().solve(100000))
