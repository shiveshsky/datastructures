class Solution:
    def keypad_combo(self, keypressed, kmap, alreadypressed, ans):
        if keypressed == "":
            ans.append(alreadypressed)
            return
        # for k in range(len(keypressed)):
        for v in kmap[keypressed[0]]:
            alreadypressed += v
            self.keypad_combo(keypressed[1:], kmap, alreadypressed, ans)
            alreadypressed = alreadypressed[0:-1]


# Solution().
# keypad_combo("234",{'1':'1', '0':'0',
# '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno',
# '7':'pqrs', '8':'tuv', '9':'wxyz'}, "", ans)
