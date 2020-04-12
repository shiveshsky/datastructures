class Node:
    val = None
    is_finished = False
    children = {}
    index = None


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a strings
    def solve(self, A, B):
        a_dict = A
        find_b = B

        dict_trie = None
        for word in a_dict:
            if dict_trie is None:
                dict_trie = self.make_trie(dict_trie, word)
            else:
                self.make_trie(dict_trie, word)
        ans = ""
        for word in B:
            ans += str(self.search_word(dict_trie, word, 1))
        return ans

    def make_trie(self, parent, val):
        if len(val) == 0:
            parent.is_finished = True
            return
        elif parent is None:
            node = Node()
            node.val = ""
            node.children = dict()
            self.make_trie(node, val)
            return node
        ch = val[0]
        rem = val[1:]
        child = parent.children.get(ch)
        if child is None:
            child = Node()
            child.val = ch
            child.children = dict()
            parent.children[ch] = child
        self.make_trie(child, rem)

    def search_word(self, parent, val, correction):
        if len(val) == 0 and correction == 0:
            return 1
        elif len(val)==0 and correction>0:
            return 0
        if parent is None:
            return 0
        ch = val[0]
        rem = val[1:]
        if correction >0:
            for key in parent.children.keys():
                correction -= 1
                found = self.search_word(parent.children.get(key), rem, correction)
                if found:
                    return 1
            correction += 1
        elif correction==0:
            if parent.children.get(ch) is not None:
                return self.search_word(parent.children.get(ch), rem, correction)
        return 0



if __name__ == '__main__':
    print(Solution().solve([ "tripti", "shukla", "shukta", "akshay", "dixit", "naithani", "godani", "kushagra", "makhan", "modiji", "yogiji", "kohli" ], [ "tripta", "shukta", "shukla", "shukka", "dickshit", "dikit", "kitti", "kohla", "modija", "nathani", "maithani", "akshat", "akshara", "tript" ]))
    # print(Solution().solve(["hello", "hills"], ["hello", "hells", "pella"]))
    # print(Solution().solve(["data", "circle", "cricket"], ["date", "circel", "crikket", "data", "circl"]))