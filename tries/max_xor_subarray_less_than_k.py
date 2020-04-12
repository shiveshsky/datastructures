class TrieNode:
    def __init__(self):
        self.c = 0
        self.left = None
        self.right = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = 0

    def insert(self, val):
        ptr = self.root
        val = '{:032b}'.format(val)  # 32 bit value
        for x in val:
            if x == '1':
                if not ptr.right:
                    ptr.right = TrieNode()
                ptr = ptr.right
            else:
                if not ptr.left:
                    ptr.left = TrieNode()
                ptr = ptr.left
            ptr.c += 1

    def query(self, pref, k):
        ptr = self.root
        pref = '{:032b}'.format(pref)
        k = '{:032b}'.format(k)
        for x in range(32):
            if pref[x] == '1':
                if k[x] == '1':
                    if ptr.right:
                        self.ans += ptr.right.c
                    if ptr.left:
                        ptr = ptr.left
                    else:
                        break
                else:
                    if ptr.right:
                        ptr = ptr.right
                    else:
                        break
            else:
                if k[x] == '1':
                    if ptr.left:
                        self.ans += ptr.left.c
                    if ptr.right:
                        ptr = ptr.right
                    else:
                        break
                else:
                    if ptr.left:
                        ptr = ptr.left
                    else:
                        break


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, K):
        t = Trie()
        t.insert(0)
        pref = 0
        for x in A:
            pref ^= x
            t.query(pref, K)
            t.insert(pref)
        return t.ans % (10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution().solve([8, 3, 10, 2, 6, 7, 6, 9, 3], 3))