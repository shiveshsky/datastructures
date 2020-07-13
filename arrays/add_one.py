class Solution:
    def plusOne(self, digits):
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                ele = digits[i] + 1
                if ele == 10:
                    digits[i] = 0
                    carry += 1
                else:
                    digits[i] = ele
                    carry = 0
            else:
                if carry == 1:
                    ele = digits[i] + 1
                    if ele == 10:
                        digits[i] = 0
                        carry = 1
                    else:
                        digits[i] = ele
                        carry = 0
        if carry == 1:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    print(Solution().plusOne([9, 9]))
