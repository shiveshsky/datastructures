class Node:
    val = None
    is_finished = False
    children = {}


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        binary_trie = None
        max_len = 0
        binary_nums = []
        for num in A:
            binary = bin(num)[2:]
            binary_nums.append(binary)
            max_len = max(max_len, len(binary))
        for i, nums in enumerate(binary_nums):
            binary_nums[i] = nums.zfill(max_len)
        for num in binary_nums:
            if binary_trie is None:
                binary_trie = self.make_trie(binary_trie, num)
            else:
                self.make_trie(binary_trie, num)
        max_possible = 0
        for i, num in enumerate(binary_nums):
            max_num = self.search_max_trie(binary_trie, num, "")
            max_possible = max(max_possible, A[i]^int(max_num, 2))
        return max_possible

    def make_trie(self, parent, val):
        if len(val) == 0:
            parent.is_finished = True
            return
        if parent is None:
            node = Node()
            node.val = ""
            node.children = dict()
            self.make_trie(node, val)
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
            self.make_trie(child, rem)

    def search_max_trie(self, parent, val, max_possible):
        if len(val)==0:
            return max_possible
        ch = val[0]
        rem = val[1:]
        selected = ""
        if ch == "1":
            selected+="0"
            child = parent.children.get("0")
        else:
            selected += "1"
            child = parent.children.get("1")
        if child is None:
            if selected=="0":
                max_possible += "1"
                return self.search_max_trie(parent.children.get("1"), rem, max_possible)
            else:
                max_possible += "0"
                return self.search_max_trie(parent.children.get("0"), rem, max_possible)
        else:
            max_possible+=selected
            return self.search_max_trie(child, rem, max_possible)


class Max2numXor:
    def solve(self, arr):
        bin_arr = []
        for i in arr:
            bin_arr.append('{:032b}'.format(i))
        trie = None
        trie = self.insert_to_trie(trie, '{:032b}'.format(0))
        overall_max = 0
        for num in bin_arr:
            max_num = self.search_max_possible(trie, num, "")
            overall_max = max(int(max_num, 2) ^ int(num, 2), overall_max)
            self.insert_to_trie(trie, num)
        return overall_max

    def insert_to_trie(self, parent, val):
        if len(val)==0:
            parent.is_finished = True
            return
        if parent is None:
            node = Node()
            node.val = 0
            node.children = dict()
            self.insert_to_trie(node, val)
            return node
        ch = val[0]
        rem = val[1:]
        child = parent.children.get(ch)
        if child is None:
            child = Node()
            child.val = ch
            child.children = dict()
            parent.children[ch] = child
        self.insert_to_trie(child, rem)

    def search_max_possible(self, parent, num, prefix):
        if len(num)==0:
            return prefix
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



if __name__ == '__main__':
    print(Solution().solve([1,2,3,4,5]))
    print(Max2numXor().solve([1,2,3,4,5]))