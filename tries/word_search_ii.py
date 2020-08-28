from typing import List


class Node:
    def __init__(self, char):
        self.words = None
        self.char = char
        self.child = dict()
        self.is_end = False


class Solution:
    def create_trie(self, word, root, prefix):
        if word == "":
            root.is_end = True
            root.words = prefix
            return
        if root is None:
            root = Node(" ")
            root.child = dict()
            self.create_trie(word, root, "")
            return root
        curr_chr = word[0]
        rem = word[1:]
        prefix += curr_chr
        if root.child.get(curr_chr, None) is None:
            tmp = Node(curr_chr)
            tmp.child = dict()
            root.child[curr_chr] = tmp
        self.create_trie(rem, root.child.get(curr_chr), prefix)

    def traverse_dfs(self, root, matr, res, i, j):
        if root.is_end:
            res.add(root.words)
        if i < 0 or j < 0:
            return
        if i >= len(matr) or j >= len(matr[0]):
            return
        if matr[i][j] == "_":
            return
        if root.child.get(matr[i][j], None):
            original = matr[i][j]
            matr[i][j] = "_"
            self.traverse_dfs(root.child.get(original), matr, res, i + 1, j)
            self.traverse_dfs(root.child.get(original), matr, res, i - 1, j)
            self.traverse_dfs(root.child.get(original), matr, res, i, j + 1)
            self.traverse_dfs(root.child.get(original), matr, res, i, j - 1)
            matr[i][j] = original

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = None
        for word in words:
            if root is None:
                root = self.create_trie(word, root, "")
            else:
                self.create_trie(word, root, "")
        ans = set()
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                # if root.child.get(board[i][j]):
                self.traverse_dfs(root, board, ans, i, j)
        return ans


if __name__ == '__main__':
    print(Solution().findWords([["a", "a"]], ["aa"]))
#   print(Solution().findWords([["a"]], ['a']))
#   print(Solution().findWords([['o','a','a','n'],
# ['e','t','a','e'],
# ['i','h','k','r'],
# ['i','f','l','v']], ["oath","pea","eat","rain", "oathf"]))
