import math


class Solution:
    # @param A : list of integers
    # @return an integer
    def factorize(self, n):
        count = 0;
        ans = []
        # count the number of
        # times 2 divides
        while ((n % 2 > 0) == False):
            # equivalent to n = n / 2;
            n >>= 1;
            count += 1;

        # if 2 divides it
        if (count > 0):
            ans.append(2)
            # print(2, count);

        # check for all the possible
        # numbers that can divide it
        for i in range(3, int(math.sqrt(n)) + 1):
            count = 0;
            while (n % i == 0):
                count += 1;
                n = int(n / i);
            if (count > 0):
                ans.append(i)
                # print(i, count);
            i += 2;

        # if n at the end is a prime number.
        if (n > 2):
            ans.append(n)
            # print(n, 1);
        return ans

    def prime_sieve_factors(self, A):
        n = A//2 +1
        prime_sieve  = [0]*(n)
        pf = []
        for i in range(2, n):
            if prime_sieve[i]==0:
                if A%i==0:
                    pf.append(i)
                for j in range(i, n, i):
                    prime_sieve[j]=1
        if len(pf)>0:
            return pf
        else:
            return [A]

    def printPowerSet(self, listA):
        set_size = len(listA)
        # set_size of power set of a set
        # with set_size n is (2**n -1)
        pow_set_size = (int)(math.pow(2, set_size));
        counter = 0;
        j = 0;
        ans = []
        # Run from counter 000..0 to 111..1
        for counter in range(0, pow_set_size):
            subset = []
            for j in range(0, set_size):

                # Check if jth bit in the
                # counter is set If set then
                # print jth element from set
                if ((counter & (1 << j)) > 0):
                    subset.append(listA[j])
                    # print(listA[j], end="");
            ans.append(subset)
            # print("");
        return ans

    def xorSum(self, allsets):
        sum = 0
        for sub in allsets:
            tmp = 0
            for s in sub:
                tmp=tmp^s
            sum+=tmp
        return sum

    def solve(self, A):
        sum = 0
        for ele in A:
            prime_factors = self.factorize(ele)
            all_sets = self.printPowerSet(prime_factors)
            sum+=(self.xorSum(all_sets)%(10**9+7))
        return sum%(10**9+7)

print(Solution().printPowerSet([1,2,3,4]))
# print(Solution().solve([ 51, 98, 91, 73, 77, 81, 96, 82, 39 ]))
# print(Solution().prime_sieve_factors(1))