class Node:
    val = None
    is_finished = False
    children = {}
    index = None


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        xor_prefix = []
        if len(A)==1:
            return [1,1]
        for num in A:
            if len(xor_prefix) == 0:
                xor_prefix.append(num)
            else:
                xor_prefix.append(num ^ xor_prefix[-1])
        for i, num in enumerate(xor_prefix):
            xor_prefix[i] = bin(num)[2:].zfill(31)
        binary_trie = None
        for i, num in enumerate(xor_prefix):
            if binary_trie is None:
                binary_trie = self.make_trie(binary_trie, num, i)
            else:
                self.make_trie(binary_trie, num, i)
        max_possible = 0
        max_i = 0
        max_j = 0
        for i, num in enumerate(xor_prefix):
            max_num, index = self.search_max_trie(binary_trie, num, "")
            if (max_possible < (int(num, 2) ^ int(max_num, 2))):
                max_possible = max(max_possible, A[i] ^ int(max_num, 2))
                max_i = i
                max_j = index

        return [max_i+2, max_j+1]
    def make_trie(self, parent, val, index):

        if len(val) == 0:
            parent.is_finished = True
            parent.index = index
            return
        if parent is None:
            node = Node()
            node.val = ""
            node.children = dict()
            self.make_trie(node, val, index)
            return node
        else:
            ch = val[0]
            rem = val[1:]
            child = parent.children.get(ch)
            if child is None:
                child = Node()
                child.val = ch
                child.children = dict()
                parent.children[ch] = child
            self.make_trie(child, rem, index)

    def search_max_trie(self, parent, val, max_possible):
        if len(val) == 0:
            return max_possible, parent.index
        ch = val[0]
        rem = val[1:]
        selected = ""
        if ch == "1":
            selected += "0"
            child = parent.children.get("0")
        else:
            selected += "1"
            child = parent.children.get("1")
        if child is None:
            if selected == "0":
                max_possible += "1"
                return self.search_max_trie(parent.children.get("1"), rem, max_possible)
            else:
                max_possible += "0"
                return self.search_max_trie(parent.children.get("0"), rem, max_possible)
        else:
            max_possible += selected
            return self.search_max_trie(child, rem, max_possible)


class MaxXorSubarray:
    def solve(self, arr):
        bin_arr = []
        for i in arr:
            bin_arr.append('{:032b}'.format(i))
        trie = None
        trie = self.insert_to_trie(trie, '{:032b}'.format(0), 0)

        overall_max = -99999
        prefix_xor = '0000000000000000000000'
        m_i = -1
        m_j = -1
        for i, num in enumerate(arr):
            prefix_xor = '{:032b}'.format(int(prefix_xor, 2) ^ num)
            max_num, index = self.search_max_possible(trie, prefix_xor, "")
            if overall_max < int(max_num, 2) ^ int(prefix_xor, 2):
                overall_max = int(max_num, 2) ^ int(prefix_xor, 2)
                m_i = i
                m_j = index
            elif overall_max == int(max_num, 2) ^ int(prefix_xor, 2):
                if abs(i-index) < abs(m_i-m_j):
                    m_i = i
                    m_j = index
            self.insert_to_trie(trie, prefix_xor, i+1)
        return [m_j+1, m_i+1]

    def insert_to_trie(self, parent, val, index):
        if len(val)==0:
            parent.is_finished = True
            parent.index = index
            return
        if parent is None:
            node = Node()
            node.val = "0"
            node.children = dict()
            self.insert_to_trie(node, val, index)
            return node
        ch = val[0]
        rem = val[1:]
        child = parent.children.get(ch)
        if child is None:
            child = Node()
            child.val = ch
            child.children = dict()
            parent.children[ch] = child
        self.insert_to_trie(child, rem, index)

    def search_max_possible(self, parent, num, prefix):
        if len(num)==0:
            return prefix, parent.index
        ch = num[0]
        rem = num[1:]
        child = None
        if ch == "0":
            child = parent.children.get("1")
        elif ch == "1":
            child = parent.children.get("0")
        if child is None:
            prefix+=ch
            return self.search_max_possible(parent.children.get(ch), rem, prefix)
        else:
            prefix+=child.val
            return self.search_max_possible(child, rem, prefix)


if __name__ == "__main__":
    # print(Solution().solve([1, 4, 3]))  # 2 3
    # print(Solution().solve([33, 29, 18]))  # 1 2
    # print(Solution().solve([15, 25, 23]))  # 2 2
    # print(Solution().solve([8]))  # 1 1
    print(Solution().solve([33, 34, 14, 10, 16, 23, 31, 8, 32]))
    print(MaxXorSubarray().solve([1, 4, 3]))
    print(MaxXorSubarray().solve([33, 29, 18]))
    print(MaxXorSubarray().solve([15, 25, 23]))
    print(MaxXorSubarray().solve([8]))
    print(MaxXorSubarray().solve([33, 34, 14, 10, 16, 23, 31, 8, 32]))