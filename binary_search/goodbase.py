class Solve:
    def sum_good_base(self, digits, base):
        sum = 0
        # using sum of gp
        for i in range(0, digits):
            sum += base ** i
        return sum

    def goodbasesolve(self, A):
        A = int(A)
        for i in range(64, 1, -1):
            digits = i
            l = 2
            h = A - 1
            while l <= h:
                mid = (l + h) // 2
                sum_base = self.sum_good_base(digits, mid)
                if sum_base < A:
                    l = mid + 1
                elif sum_base > A:
                    h = mid - 1
                elif sum_base == A:
                    return str(mid)
        return str(A - 1)
