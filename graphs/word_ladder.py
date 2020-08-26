import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if not wordList:
            return 0

        hashmap = collections.defaultdict(list)
        queue = collections.deque()
        seen = set()

        n = len(beginWord)
        for word in wordList:
            for i in range(n):
                key = word[:i] + "*" + word[i + 1:]
                hashmap[key].append(word)

        queue.append((beginWord, 1))
        seen.add(beginWord)

        while queue:
            word, length = queue.popleft()
            for i in range(n):
                intermediate_word = word[:i] + "*" + word[i + 1:]
                for possible_word in hashmap[intermediate_word]:
                    if possible_word == endWord:
                        return length + 1
                    elif possible_word not in seen:
                        seen.add(possible_word)
                        queue.append((possible_word, length + 1))

        return 0


if __name__ == '__main__':
    print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
