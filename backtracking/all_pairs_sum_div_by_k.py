class Solution:
    def count_pairs_with_sum_div_k(self, A, B):
        remainders = [0]*B
        for i in A:
            remainders[i%B]+=1
        # sum = remainders[0] * (remainders[0] - 1) / 2;
        sum=0
        i = 1
        while (i <= B // 2 and i != (B - i)):
            sum += remainders[i] * remainders[B- i]
            i += 1
        if (B % 2 == 0):
            sum += (remainders[B // 2] * (remainders[B // 2] - 1) // 2);
        return sum
