class Solution:
    def hash_func(self, word):
        hash_dict = {
            'a': 2,
            'b': 3,
            'c': 5,
            'd': 7,
            'e': 11,
            'f': 13,
            'g': 17,
            'h': 19,
            'i': 23,
            'j': 29,
            'k': 31,
            'l': 37,
            'm': 41,
            'n': 43,
            'o': 47,
            'p': 53,
            'q': 59,
            'r': 61,
            's': 67,
            't': 71,
            'u': 73,
            'v': 79,
            'w': 83,
            'x': 89,
            'y': 97,
            'z': 101,
        }
        ans = 1
        for ch in word:
            ans *= hash_dict[ch]
        return ans

    def anagrams(self, A):
        my_dic = dict()
        for i, word in enumerate(A):
            hashed_word = self.hash_func(word)
            if my_dic.get(hashed_word):
                my_dic[hashed_word].append(i+1)
            else:
                my_dic[hashed_word] = [i+1]
        ans = []
        for vals in my_dic.values():
            ans.append(vals)
        return ans
print(Solution().anagrams(["cat", "dog", "god", "tca"]))

