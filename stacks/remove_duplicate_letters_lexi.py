from collections import Counter


class Solution:
    def solve(self, A):
        cnt = Counter(A)
        length = len(A)
        visited = set()
        stk = []
        for char in A:
            if len(stk)==0:
                stk.append(char)
                visited.add(char)
                cnt[char] -= 1
            else:
                if char not in visited and stk[-1] <= char:
                    stk.append(char)
                    visited.add(char)
                    cnt[char] -= 1
                else:
                    while len(stk) > 0 and stk[-1] > char:
                        if cnt[stk[-1]] > 0 and char not in visited:
                            popper = stk.pop()
                            visited.remove(popper)
                        else:
                            break
                    if char not in visited:
                        stk.append(char)
                        visited.add(char)
                    cnt[char] -= 1
        return "".join(stk)


print(Solution().solve("nsutwcgpgpxonqbzsvpmjksjminhitsfenbhowixva"))

'''
Given a string A consisting of lowercase English alphabets. Find and return lexicographically smallest string B after removing duplicate letters from A so that every letter appears once and only once.
'''