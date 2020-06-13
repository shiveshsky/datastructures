class Node:
    val = None
    freq = 0
    is_finished = False
    children = {}


class Solution:
    def prefix(self, A):
        trie = None
        for word in A:
            if trie is None:
                trie = self.make_trie(trie, word)
            else:
                self.make_trie(trie, word)
        search_prefix = []
        for word in A:
            prefix = self.search_prefix(trie, word, "")
            search_prefix.append(prefix)
        return search_prefix

    def make_trie(self, parent, word):
        if len(word)==0:
            parent.is_finished = True
            return
        if parent is None:
            node = Node()
            node.val = ""
            node.freq = 1
            node.children = dict()
            self.make_trie(node, word)
            return node
        ch = word[0]
        rem = word[1:]
        child = parent.children.get(ch)
        if child is None:
            child = Node()
            child.val = ch
            child.children = dict()
            parent.children[ch] = child
        child.freq += 1
        self.make_trie(child, rem)

    def search_prefix(self, parent, word, prefix):
        if len(word) == 0:
            return prefix
        ch = word[0]
        rem = word[1:]
        child = parent.children.get(ch)
        if child is not None:
            prefix += child.val
            if child.freq == 1:
                return prefix
            else:
                return self.search_prefix(child, rem, prefix)
        return prefix


if __name__ == '__main__':
    sol = Solution()
    print(sol.prefix(["zebra", "dog", "duck", "dove"]))
    print(sol.prefix(["id", "qscdxrjmow", "rxsjybldbe", "sarcbyne", "dyggxxp", "lorel", "nmpa"]))
