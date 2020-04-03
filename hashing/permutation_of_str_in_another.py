from collections import Counter
#
#
# class Solution:
#     def solve(self, A, B):
#         b_cnt = Counter(B)
#         a_cnt = Counter(A[0:len(B)])
#         ans = 0
#
#         for i in range(0, len(A)):
#             a_cnt = Counter(A[i:i+len(B)])
#             if a_cnt == b_cnt:
#                 ans+=1
#
#
#         return ans
# TODO THE BELOW SOLUTION IS CORRECT :) ABOVE ONE IS ALSO CORRECT BUT REMEMBER THE BELOW ONE.
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str):
        if not s or not p or len(s) < len(p):
            return []

        # Another one of those problems that use a sliding
        # window approach. If you don't know what it is, then
        # that's fine, you can look it up now or after
        # going through this solution.

        # Lets treat the letters that we need as our capacity
        # to absorb letters from the string 's'
        # if p = "aab", letterCapacity = { "a": 2, "b": 1 }
        letterCapacity = Counter(p)

        # Lets also keep our current demand in a separate variable
        # so we don't have to sum up remaining letter capacities
        # throughout the program.
        demand = len(p)

        # This is where the result goes.
        result = []

        for charIdx, char in enumerate(s):

            # Lets move a window equal to the length
            # of 'p'.

            # Lets check to see if a character fell out of
            # the window. If it did, lets adjust our demand
            # and letterCapacity accordingly.
            if charIdx >= len(p):
                droppedChar = s[charIdx - len(p)]
                if droppedChar in letterCapacity:
                    letterCapacity[droppedChar] += 1

                    # This suggests that the letterCapacity
                    # could possibly drop below 0. That happens
                    # when you have multiple copies of the
                    # dropped character in your window, more than
                    # you needed (in 'p'). As you will see, we
                    # decrement the letterCapacity when such
                    # duplicates occur, even if the letterCapacity
                    # goes below 0. This makes the code easy to reason
                    # about.
                    if letterCapacity[droppedChar] > 0:
                        demand += 1

            # Deal with the new character.
            if char in letterCapacity:
                letterCapacity[char] -= 1
                if letterCapacity[char] >= 0:   
                    demand -= 1
                    if demand == 0:
                        result.append(charIdx - len(p) + 1)

        return result

print(Solution().findAnagrams('abcbacabc', 'abc'))

